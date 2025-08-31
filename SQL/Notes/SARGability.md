# SARGability in SQL - Complete Study Notes

## 🚀 **QUICK REFERENCE - KEY POINTS**

### **What is SARGability?**
- **SARGable** = **S**earch **ARG**ument **ABLE** 
- **Can the query optimizer efficiently use indexes for this condition?**
- **Goal**: Index Seek (fast - jumps directly to data using B-tree) vs Table/Index Scan (slow - reads all pages sequentially)

### **Golden Rule** 
**Keep columns "naked" in WHERE clauses - no functions, no operations, no expressions**

### **✅ SARGable (Index-Friendly)**
```sql
WHERE column = constant
WHERE column > 100
WHERE column BETWEEN 1 AND 100  
WHERE column IN ('A', 'B', 'C')
WHERE column IS NULL
WHERE column LIKE 'prefix%'
```

### **❌ Non-SARGable (Index-Unfriendly)**
```sql
WHERE FUNCTION(column) = value     -- Functions on columns
WHERE column + 10 > 100           -- Math operations on columns  
WHERE column LIKE '%suffix'       -- Leading wildcards
WHERE UPPER(column) = 'VALUE'     -- String functions
WHERE column1 = column2           -- Column-to-column comparisons*
```

### **🎯 Performance Impact**
- **SARGable**: Milliseconds (logarithmic search)
- **Non-SARGable**: Seconds/Minutes (linear scan)

### **🔧 Quick Fixes**
```sql
-- ❌ Bad → ✅ Good
WHERE YEAR(date) = 2024        → WHERE date >= '2024-01-01' AND date < '2025-01-01'
WHERE price * 1.1 > 110        → WHERE price > 100
WHERE UPPER(name) = 'JOHN'     → WHERE name = 'john' (store consistently)
```

---

## 📚 **DETAILED CONCEPTS WITH EXAMPLES**

### **1. Understanding SARGability Fundamentals**

**SARGability** determines whether the SQL query optimizer can use indexes effectively. When a condition is SARGable, the database can:
- Use **Index Seeks** (jumps directly to specific rows using index structure) instead of **Index/Table Scans** (reads through all pages sequentially)
- Dramatically reduce the number of rows examined
- Execute queries in logarithmic time instead of linear time

**Example Scenario:**
```sql
-- Table with 1 million records and index on employee_id
SELECT * FROM employees WHERE employee_id = 12345;
```
- **With SARGable condition**: Examines ~log₂(1,000,000) ≈ 20 rows
- **With Non-SARGable condition**: Examines all 1,000,000 rows

### **2. SARGable Conditions (Index-Friendly)**

#### **2.1 Direct Equality Comparisons**
```sql
-- ✅ Perfect for indexes
SELECT * FROM products WHERE product_id = 100;
SELECT * FROM customers WHERE status = 'active';
SELECT * FROM orders WHERE order_date = '2024-01-15';
```

#### **2.2 Range Conditions**
```sql
-- ✅ Excellent for B-tree indexes
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM orders WHERE quantity BETWEEN 10 AND 100;
SELECT * FROM sales WHERE sale_date >= '2024-01-01';
```

#### **2.3 IN and EXISTS Clauses**
```sql
-- ✅ Can use index for each value
SELECT * FROM products WHERE category_id IN (1, 2, 3, 5);
SELECT * FROM customers WHERE region IN ('North', 'South');
```

#### **2.4 IS NULL / IS NOT NULL**
```sql
-- ✅ Can use index (depends on database)
SELECT * FROM orders WHERE cancelled_date IS NULL;
SELECT * FROM customers WHERE email IS NOT NULL;
```

#### **2.5 Prefix LIKE Patterns**
```sql
-- ✅ Can use index for prefix searches
SELECT * FROM customers WHERE last_name LIKE 'Smith%';
SELECT * FROM products WHERE sku LIKE 'ABC%';
```

### **3. Non-SARGable Conditions (Index-Unfriendly)**

#### **3.1 Functions on Columns**
```sql
-- ❌ Non-SARGable - Forces table scan
SELECT * FROM employees WHERE YEAR(hire_date) = 2024;
SELECT * FROM customers WHERE UPPER(last_name) = 'SMITH';
SELECT * FROM orders WHERE MONTH(order_date) = 3;

-- Why it's bad:
-- Database must apply YEAR() to EVERY row's hire_date before comparison
-- Index on hire_date becomes useless
```

**Better Approach:**
```sql
-- ✅ SARGable alternative
SELECT * FROM employees 
WHERE hire_date >= '2024-01-01' 
  AND hire_date < '2025-01-01';
```

#### **3.2 Arithmetic Operations on Columns**
```sql
-- ❌ Non-SARGable
SELECT * FROM products WHERE price * 1.08 > 100;  -- Adding tax
SELECT * FROM employees WHERE salary + bonus > 75000;

-- Why it's bad:
-- Must calculate price * 1.08 for every row
-- Index on price cannot be used effectively
```

**Better Approach:**
```sql
-- ✅ SARGable - Move calculation to the right side
SELECT * FROM products WHERE price > 100 / 1.08;  -- price > 92.59
```

#### **3.3 Leading Wildcards in LIKE**
```sql
-- ❌ Non-SARGable - Cannot use index
SELECT * FROM customers WHERE last_name LIKE '%son';
SELECT * FROM products WHERE description LIKE '%widget%';

-- Why it's bad:
-- Index is ordered by prefix, can't search by suffix
-- Must check every row
```

**Better Approaches:**
```sql
-- ✅ Full-text search (for text searching)
SELECT * FROM products WHERE MATCH(description) AGAINST('widget');

-- ✅ Reverse index (for suffix searches, advanced technique)
-- Store reversed strings in separate column and search
```

#### **3.4 Complex Expressions**
```sql
-- ❌ Non-SARGable
SELECT * FROM orders 
WHERE DATEDIFF(day, order_date, GETDATE()) <= 30;

SELECT * FROM employees 
WHERE CONCAT(first_name, ' ', last_name) = 'John Smith';
```

**Better Approaches:**
```sql
-- ✅ SARGable alternatives
SELECT * FROM orders 
WHERE order_date >= DATEADD(day, -30, GETDATE());

-- Create computed column or separate full_name column
SELECT * FROM employees WHERE full_name = 'John Smith';
```

### **4. Column-to-Column Comparisons (Your LeetCode Example)**

**Your Query:**
```sql
SELECT DISTINCT author_id as id
FROM Views
WHERE author_id = viewer_id  -- Column = Column comparison
ORDER BY id;
```

#### **Why Column = Column is Less Optimal:**

**Index Limitation:**
- Indexes are optimized for **column = constant** comparisons
- **Column = column** requires examining relationships between two columns
- Cannot directly use a single-column index effectively

**What Happens:**
1. Database may use index on one column (author_id) 
2. For each matching row, check if viewer_id equals author_id
3. OR do a full table scan and compare both columns for every row

**Performance Characteristics:**
```sql
-- More efficient (if you had a constant)
WHERE author_id = 123  -- Can use index directly

-- Less efficient (column comparison)  
WHERE author_id = viewer_id  -- May need to scan more rows
```

**Optimization Strategies:**
1. **Composite Index**: `CREATE INDEX idx_author_viewer ON Views(author_id, viewer_id)`
2. **Covering Index**: Include all needed columns
3. **Materialized View**: Pre-compute results if query runs frequently

### **5. Testing SARGability**

#### **5.1 SQL Server**
```sql
-- Enable execution plan
SET STATISTICS IO ON;
SET SHOWPLAN_ALL ON;

SELECT * FROM employees WHERE employee_id = 12345;

-- Look for:
-- ✅ "Index Seek" = SARGable (database jumps directly to data)
-- ❌ "Index Scan" or "Table Scan" = Non-SARGable (database reads all pages)
```

#### **5.2 PostgreSQL** 
```sql
EXPLAIN (ANALYZE, BUFFERS) 
SELECT * FROM employees WHERE employee_id = 12345;

-- Look for:
-- ✅ "Index Scan using idx_employee_id" = SARGable (uses index to jump to data)
-- ❌ "Seq Scan on employees" = Non-SARGable (sequential scan of all rows)
```

#### **5.3 MySQL**
```sql
EXPLAIN FORMAT=JSON
SELECT * FROM employees WHERE employee_id = 12345;

-- Look for:
-- ✅ "access_type": "const" or "range" = SARGable (uses index efficiently)
-- ❌ "access_type": "ALL" = Non-SARGable (table scan - reads all rows)
```

### **6. Advanced SARGability Techniques**

#### **6.1 Functional Indexes**
```sql
-- PostgreSQL/Oracle: Make non-SARGable queries SARGable
CREATE INDEX idx_upper_last_name ON customers (UPPER(last_name));

-- Now this becomes SARGable:
SELECT * FROM customers WHERE UPPER(last_name) = 'SMITH';
```

#### **6.2 Computed Columns (SQL Server)**
```sql
-- Add computed column
ALTER TABLE employees ADD hire_year AS YEAR(hire_date);
CREATE INDEX idx_hire_year ON employees (hire_year);

-- Now this becomes SARGable:
SELECT * FROM employees WHERE hire_year = 2024;
```

#### **6.3 Covering Indexes**
```sql
-- Include all needed columns in index
CREATE INDEX idx_covering 
ON orders (customer_id, order_date) 
INCLUDE (order_amount, status);

-- Query can be satisfied entirely from index
SELECT order_date, order_amount, status 
FROM orders 
WHERE customer_id = 123 AND order_date >= '2024-01-01';
```

### **7. Real-World Performance Examples**

#### **Scenario 1: Date Range Queries**
```sql
-- ❌ Non-SARGable (2.3 seconds on 1M rows)
SELECT COUNT(*) FROM orders 
WHERE YEAR(order_date) = 2024;

-- ✅ SARGable (0.003 seconds on 1M rows)  
SELECT COUNT(*) FROM orders
WHERE order_date >= '2024-01-01' 
  AND order_date < '2025-01-01';
```

#### **Scenario 2: Case-Insensitive Search**
```sql
-- ❌ Non-SARGable (1.8 seconds)
SELECT * FROM customers 
WHERE UPPER(last_name) = 'JOHNSON';

-- ✅ SARGable with proper data storage (0.001 seconds)
SELECT * FROM customers 
WHERE last_name = 'johnson';  -- Store data in consistent case

-- ✅ Or use case-insensitive collation
SELECT * FROM customers 
WHERE last_name = 'Johnson' COLLATE SQL_Latin1_General_CP1_CI_AS;
```

### **8. Common Mistakes and Solutions**

#### **8.1 The Null Trap**
```sql
-- ❌ Problematic - May not use index efficiently
SELECT * FROM orders WHERE customer_id != 123;

-- ✅ Better - More explicit
SELECT * FROM orders 
WHERE customer_id IS NOT NULL 
  AND customer_id != 123;
```

#### **8.2 The OR Trap**
```sql  
-- ❌ May not use indexes well
SELECT * FROM products 
WHERE name = 'Widget' OR description = 'Widget';

-- ✅ Better with UNION (if indexes exist on both columns)
SELECT * FROM products WHERE name = 'Widget'
UNION
SELECT * FROM products WHERE description = 'Widget';
```

#### **8.3 The Function Trap**
```sql
-- ❌ Common mistake
SELECT * FROM employees WHERE DATEDIFF(year, hire_date, GETDATE()) > 5;

-- ✅ SARGable solution
SELECT * FROM employees WHERE hire_date < DATEADD(year, -5, GETDATE());
```

### **9. Best Practices Summary**

1. **Always keep columns "naked"** in WHERE clauses
2. **Move functions to the right side** of comparisons
3. **Use ranges instead of functions** for date/time queries
4. **Test with execution plans** - don't assume
5. **Consider functional indexes** for unavoidable functions
6. **Store data consistently** to avoid case conversions
7. **Use appropriate data types** - don't store dates as strings
8. **Be careful with NULLs** - they affect index usage
9. **Prefer specific conditions** over negations when possible
10. **Monitor query performance** in production

### **10. Sargability Checklist**

Before writing any WHERE clause, ask:

**✅ Is this SARGable?**
- [ ] Column is not wrapped in functions
- [ ] No arithmetic operations on columns  
- [ ] Using = , >, <, BETWEEN, IN, IS NULL
- [ ] LIKE patterns start with letters (no leading %)
- [ ] Comparing column to constants, not other columns*

**❌ Red Flags (Non-SARGable)**
- [ ] Functions: `WHERE UPPER(col) = 'X'`
- [ ] Math: `WHERE col * 2 > 10` 
- [ ] Wildcards: `WHERE col LIKE '%text'`
- [ ] Complex expressions: `WHERE col + 5 = other_col - 3`

**Remember**: When in doubt, check the execution plan!

---

## 📖 **Additional Resources**

- **SQL Server**: Query Execution Plans
- **PostgreSQL**: EXPLAIN ANALYZE documentation  
- **MySQL**: Query Optimization documentation
- **Oracle**: SQL Tuning Guide

**Key Takeaway**: SARGability is about making your queries "index-friendly" by keeping conditions simple and direct. The database can only use indexes effectively when it doesn't have to perform calculations on every row.