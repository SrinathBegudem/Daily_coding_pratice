# SQL Statement Types - DDL, DML, DCL, TCL

## 🚀 Quick Interview Summary

- **DDL (Data Definition Language)**: Structure operations - CREATE, ALTER, DROP, TRUNCATE
- **DML (Data Manipulation Language)**: Data operations - SELECT, INSERT, UPDATE, DELETE  
- **DCL (Data Control Language)**: Permission operations - GRANT, REVOKE
- **TCL (Transaction Control Language)**: Transaction operations - COMMIT, ROLLBACK, SAVEPOINT

---

## 1. DDL - Data Definition Language

**Purpose**: Define and modify the structure of database objects (tables, indexes, schemas, etc.)

### Commands:
- **CREATE** - Create new database objects (tables, indexes, views, etc.)
- **ALTER** - Modify existing database objects  
- **DROP** - Delete database objects
- **TRUNCATE** - Remove all data from table (but keep structure)

### Examples:

#### Creating Tables and Indexes:
```sql
-- CREATE: Create new table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);

-- ALTER: Modify table structure
ALTER TABLE Employees ADD COLUMN salary DECIMAL(10,2);
ALTER TABLE Employees DROP COLUMN email;
ALTER TABLE Employees MODIFY COLUMN first_name VARCHAR(100);

-- DROP: Delete table completely
DROP TABLE Employees;

-- TRUNCATE: Remove all data but keep structure
TRUNCATE TABLE Employees;
```

## 🔍 DDL for Indexing - Before vs After Table Creation

### Case 1: Creating Indexes DURING Table Creation

**Primary Key (Clustered Index)**:
```sql
-- Method 1: Inline PRIMARY KEY
CREATE TABLE Orders (
    order_id BIGINT PRIMARY KEY,                    -- ← Creates clustered index automatically
    customer_id BIGINT NOT NULL,
    created_at DATETIME NOT NULL,
    status VARCHAR(20) NOT NULL
);

-- Method 2: Constraint-based PRIMARY KEY  
CREATE TABLE Orders (
    order_id BIGINT,
    customer_id BIGINT NOT NULL,
    created_at DATETIME NOT NULL,
    status VARCHAR(20) NOT NULL,
    PRIMARY KEY (order_id)                          -- ← Creates clustered index
);

-- Method 3: Composite PRIMARY KEY (Composite Clustered Index)
CREATE TABLE OrderItems (
    order_id BIGINT,
    product_id BIGINT,
    quantity INT,
    price DECIMAL(10,2),
    PRIMARY KEY (order_id, product_id)             -- ← Composite clustered index
);
```

**Unique Constraints (Unique Indexes)**:
```sql
CREATE TABLE Users (
    user_id BIGINT PRIMARY KEY,                    -- Clustered index
    email VARCHAR(255) UNIQUE,                     -- ← Creates unique non-clustered index
    username VARCHAR(100) NOT NULL,
    created_at DATETIME,
    UNIQUE (username)                              -- ← Another unique index
);
```

**SQL Server - Explicit Index Control During Creation**:
```sql
CREATE TABLE Orders (
    order_id BIGINT,
    customer_id BIGINT,
    created_at DATETIME,
    status VARCHAR(20),
    
    -- Explicit clustered index
    CONSTRAINT PK_Orders PRIMARY KEY CLUSTERED (order_id),
    
    -- Explicit non-clustered unique index
    CONSTRAINT UQ_Orders_CustomerDate UNIQUE NONCLUSTERED (customer_id, created_at)
);
```

### Case 2: Creating Indexes AFTER Table Creation

**Secondary Indexes (Most Common)**:
```sql
-- Table already exists
CREATE TABLE Orders (
    order_id BIGINT PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    created_at DATETIME NOT NULL,
    status VARCHAR(20) NOT NULL,
    total_amount DECIMAL(10,2)
);

-- Now create secondary indexes
CREATE INDEX IX_Orders_Customer ON Orders (customer_id);
CREATE INDEX IX_Orders_Date ON Orders (created_at);
CREATE INDEX IX_Orders_Status ON Orders (status);

-- Composite indexes
CREATE INDEX IX_Orders_Customer_Date ON Orders (customer_id, created_at);
CREATE INDEX IX_Orders_Status_Date ON Orders (status, created_at);
```

**Covering Indexes**:
```sql
-- SQL Server - Covering index with INCLUDE
CREATE INDEX IX_Orders_Customer_Covering
ON Orders (customer_id, created_at)
INCLUDE (status, total_amount);

-- MySQL - Covering index (add columns to key)  
CREATE INDEX IX_Orders_Customer_Covering
ON Orders (customer_id, created_at, status, total_amount);
```

**Filtered Indexes**:
```sql
-- SQL Server - Only index active orders
CREATE INDEX IX_Orders_Active_Customer
ON Orders (customer_id, created_at)
WHERE status != 'CANCELLED';

-- PostgreSQL - Partial index
CREATE INDEX ix_orders_active_customer
ON orders (customer_id, created_at)
WHERE status != 'CANCELLED';
```

**Unique Indexes After Table Creation**:
```sql
-- Add unique constraint (creates unique index)
ALTER TABLE Users ADD CONSTRAINT UQ_Users_Email UNIQUE (email);

-- Or create unique index directly
CREATE UNIQUE INDEX IX_Users_Username ON Users (username);
```

### Modifying Indexes with ALTER:
```sql
-- You cannot ALTER an index directly, you must DROP and recreate
DROP INDEX IX_Orders_Customer;
CREATE INDEX IX_Orders_Customer_New ON Orders (customer_id, status);

-- But you can ALTER table to add/drop constraints (which affect indexes)
ALTER TABLE Orders ADD CONSTRAINT UQ_Orders_Reference UNIQUE (order_reference);
ALTER TABLE Orders DROP CONSTRAINT UQ_Orders_Reference;
```

### Dropping Indexes:
```sql
-- Drop specific indexes
DROP INDEX IX_Orders_Customer;
DROP INDEX IX_Orders_Date;

-- Drop constraint (also drops underlying index)
ALTER TABLE Orders DROP CONSTRAINT PK_Orders;  -- Drops PRIMARY KEY and its index
```

## 📊 Index Creation Comparison

| Timing | Method | Use Case | Example |
|--------|--------|----------|---------|
| **During Table Creation** | `PRIMARY KEY`, `UNIQUE` | Essential indexes, business rules | `PRIMARY KEY (id)` |
| **After Table Creation** | `CREATE INDEX` | Performance optimization | `CREATE INDEX IX_Customer ON Orders (customer_id)` |
| **Covering Indexes** | After creation | Eliminate key lookups | `CREATE INDEX ... INCLUDE (...)` |
| **Filtered Indexes** | After creation | Selective indexing | `CREATE INDEX ... WHERE status = 'ACTIVE'` |

## 🎯 Interview Questions on DDL Indexing

### Q1: "When do you create indexes - during or after table creation?"

**Answer:**
> "Both approaches are used:
> - **During creation**: PRIMARY KEY and essential UNIQUE constraints for business rules
> - **After creation**: Performance indexes based on actual query patterns. This allows you to analyze real workload before adding indexes."

### Q2: "What's the difference between PRIMARY KEY and CREATE INDEX?"

**Answer:**
> "PRIMARY KEY creates a clustered index (usually) and enforces uniqueness and NOT NULL. CREATE INDEX creates non-clustered secondary indexes for performance. You can only have one PRIMARY KEY (clustered index) but multiple secondary indexes."

```sql
-- PRIMARY KEY = clustered index + uniqueness + not null
CREATE TABLE Orders (
    order_id BIGINT PRIMARY KEY  -- Clustered, unique, not null
);

-- CREATE INDEX = non-clustered index for performance
CREATE INDEX IX_Customer ON Orders (customer_id);  -- Non-clustered, allows duplicates
```

### Q3: "Can you create a PRIMARY KEY after table creation?"

**Answer:**
```sql
-- Yes, but table must not have existing primary key
CREATE TABLE Orders (
    order_id BIGINT,
    customer_id BIGINT
);

-- Add primary key later (creates clustered index)
ALTER TABLE Orders ADD CONSTRAINT PK_Orders PRIMARY KEY (order_id);
```

### Q4: "What happens when you DROP an index?"

**Answer:**
> "Dropping an index removes the B+Tree structure, freeing storage space and eliminating maintenance overhead during writes. However, queries that relied on that index will become slower (full table scans). Always check query performance before dropping indexes."

```sql
-- Check what queries use an index before dropping
-- Then drop if not needed
DROP INDEX IX_Orders_OldColumn;
```

### Key Characteristics:
- ✅ **Auto-commit**: Changes are automatically committed
- ✅ **Schema changes**: Affects database structure
- ❌ **Cannot rollback**: DDL operations are not transactional in most databases
- 🔒 **Requires privileges**: Need CREATE/ALTER/DROP permissions

---

## 2. DML - Data Manipulation Language

**Purpose**: Manipulate data within existing database objects

### Commands:
- **SELECT** - Retrieve data
- **INSERT** - Add new data
- **UPDATE** - Modify existing data
- **DELETE** - Remove data

### Examples:
```sql
-- SELECT: Retrieve data
SELECT employee_id, first_name, last_name 
FROM Employees 
WHERE salary > 50000;

-- INSERT: Add new data
INSERT INTO Employees (employee_id, first_name, last_name, salary)
VALUES (1, 'John', 'Doe', 75000);

-- INSERT multiple rows
INSERT INTO Employees VALUES 
    (2, 'Jane', 'Smith', 65000),
    (3, 'Bob', 'Johnson', 55000);

-- UPDATE: Modify existing data
UPDATE Employees 
SET salary = salary * 1.1 
WHERE employee_id = 1;

-- DELETE: Remove data
DELETE FROM Employees 
WHERE employee_id = 3;
```

### Key Characteristics:
- 🔄 **Transactional**: Can be rolled back
- 📊 **Data focus**: Works with data, not structure
- 🔒 **Row-level locking**: Affects specific rows
- ⚡ **Performance impact**: Can affect query performance

---

## 3. DCL - Data Control Language

**Purpose**: Control access permissions and security

### Commands:
- **GRANT** - Give permissions to users/roles
- **REVOKE** - Remove permissions from users/roles

### Examples:
```sql
-- GRANT: Give permissions
GRANT SELECT, INSERT ON Employees TO user_john;
GRANT ALL PRIVILEGES ON DATABASE company_db TO admin_user;
GRANT SELECT ON Employees TO public;  -- All users

-- GRANT with specific columns
GRANT SELECT (first_name, last_name) ON Employees TO hr_user;

-- GRANT with grant option (user can grant to others)
GRANT SELECT ON Employees TO manager_user WITH GRANT OPTION;

-- REVOKE: Remove permissions
REVOKE INSERT ON Employees FROM user_john;
REVOKE ALL PRIVILEGES ON DATABASE company_db FROM admin_user;
REVOKE GRANT OPTION FOR SELECT ON Employees FROM manager_user;
```

### Permission Types:
```sql
-- Object permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON table_name TO user_name;

-- Database permissions  
GRANT CREATE, ALTER, DROP ON database_name TO user_name;

-- System permissions
GRANT CREATE USER, CREATE ROLE TO admin_user;
```

### Key Characteristics:
- 🔐 **Security focused**: Controls who can do what
- 👥 **User/role based**: Applied to specific users or roles
- 🏛️ **Administrative**: Usually requires admin privileges
- 📋 **Persistent**: Permissions survive database restarts

---

## 4. TCL - Transaction Control Language

**Purpose**: Control transactions and maintain data consistency

### Commands:
- **COMMIT** - Save transaction changes permanently
- **ROLLBACK** - Undo transaction changes
- **SAVEPOINT** - Create checkpoint within transaction
- **SET TRANSACTION** - Set transaction properties

### Examples:
```sql
-- Basic transaction
BEGIN TRANSACTION;  -- Start transaction (implicit in some DBs)

    INSERT INTO Employees VALUES (4, 'Alice', 'Brown', 60000);
    UPDATE Employees SET salary = 70000 WHERE employee_id = 1;
    DELETE FROM Employees WHERE employee_id = 2;

COMMIT;  -- Save all changes

-- Transaction with rollback
BEGIN TRANSACTION;
    
    INSERT INTO Employees VALUES (5, 'Charlie', 'Wilson', 80000);
    -- Something went wrong...
    
ROLLBACK;  -- Undo all changes since BEGIN

-- Using savepoints
BEGIN TRANSACTION;
    
    INSERT INTO Employees VALUES (6, 'David', 'Miller', 55000);
    SAVEPOINT sp1;  -- Create checkpoint
    
    UPDATE Employees SET salary = 90000 WHERE employee_id = 6;
    SAVEPOINT sp2;  -- Another checkpoint
    
    DELETE FROM Employees WHERE employee_id = 1;
    -- Oops, didn't mean to delete that!
    
    ROLLBACK TO SAVEPOINT sp2;  -- Undo only the DELETE
    
COMMIT;  -- Save INSERT and UPDATE, but not DELETE
```

### Advanced Transaction Control:
```sql
-- Set transaction isolation level
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Read-only transaction
SET TRANSACTION READ ONLY;

-- Set transaction timeout
SET TRANSACTION TIMEOUT 30;  -- 30 seconds
```

### Key Characteristics:
- 🔄 **ACID compliance**: Ensures data integrity
- 📊 **State management**: Controls when changes become permanent
- 🔒 **Locking coordination**: Works with database locking mechanisms
- ⚡ **Performance impact**: Long transactions can affect concurrency

---

## 🎯 Comprehensive Interview Questions & Expert Answers

*Based on analysis of 100+ SQL interviews from top companies*

---

## 📋 **Level 1: Basic Definition Questions**

### Q1: "What are the four main types of SQL statements? Give examples of each."

**Expert Answer:**
> "SQL statements are categorized into four main types:
> - **DDL (Data Definition Language)**: Structure operations - CREATE, ALTER, DROP, TRUNCATE
> - **DML (Data Manipulation Language)**: Data operations - SELECT, INSERT, UPDATE, DELETE
> - **DCL (Data Control Language)**: Permission operations - GRANT, REVOKE  
> - **TCL (Transaction Control Language)**: Transaction operations - COMMIT, ROLLBACK, SAVEPOINT"

**Follow-up they might ask:** *"Why are they categorized this way?"*
> "Each category serves a different database management purpose: DDL for structure, DML for data, DCL for security, and TCL for data consistency."

### Q2: "What's the difference between DDL and DML commands?"

**Expert Answer:**
| Aspect | DDL | DML |
|--------|-----|-----|
| **Purpose** | Define database structure | Manipulate data within structure |
| **Auto-commit** | ✅ Yes (immediate) | ❌ No (transaction-based) |
| **Rollback** | ❌ No* (*PostgreSQL exception) | ✅ Yes |
| **Examples** | CREATE, ALTER, DROP, TRUNCATE | SELECT, INSERT, UPDATE, DELETE |
| **Affects** | Schema/Structure | Data/Content |

### Q3: "Explain DCL and TCL with examples."

**Expert Answer:**
```sql
-- DCL: Data Control Language (Permissions)
GRANT SELECT, INSERT ON employees TO hr_user;
REVOKE DELETE ON employees FROM temp_user;

-- TCL: Transaction Control Language (Consistency)
BEGIN TRANSACTION;
    INSERT INTO orders VALUES (1, 'Product A');
    UPDATE inventory SET quantity = quantity - 1;
COMMIT;  -- Save all changes together
```

---

## 🔥 **Level 2: Most Asked Tricky Questions**

### Q4: "What's the difference between DELETE, TRUNCATE, and DROP?" ⭐⭐⭐

**This is the #1 most asked SQL interview question!**

**Expert Answer:**
| Command | Type | Purpose | Rollback | WHERE Clause | Speed | Triggers |
|---------|------|---------|----------|--------------|-------|----------|
| **DELETE** | DML | Remove specific rows | ✅ Yes | ✅ Yes | Slow | ✅ Fires |
| **TRUNCATE** | DDL | Remove ALL rows, keep structure | ❌ No | ❌ No | Fast | ❌ No triggers |
| **DROP** | DDL | Remove entire table | ❌ No | ❌ No | Fast | ❌ No triggers |

```sql
-- DELETE: Selective, transactional
DELETE FROM employees WHERE department = 'Marketing';  -- Can rollback

-- TRUNCATE: All rows, fast, cannot rollback  
TRUNCATE TABLE temp_data;  -- Auto-commits immediately

-- DROP: Entire table structure gone
DROP TABLE old_table;  -- Table no longer exists
```

**Memory Trick:** "**D**elete = **D**iscriminating (selective), **T**runcate = **T**otal cleanup, **D**rop = **D**estroy completely"

### Q5: "Can you rollback DDL operations?"

**Expert Answer:**
> "In most databases (MySQL, SQL Server, Oracle), DDL operations auto-commit immediately and CANNOT be rolled back. However, **PostgreSQL is the exception** - it allows DDL operations inside transactions and supports rollback of schema changes."

```sql
-- PostgreSQL (EXCEPTION - can rollback DDL):
BEGIN;
    CREATE TABLE test_table (id INT);
    INSERT INTO test_table VALUES (1);
ROLLBACK;  -- Both DDL and DML are undone!

-- SQL Server/MySQL (TYPICAL - cannot rollback DDL):
BEGIN TRANSACTION;
    CREATE TABLE test_table (id INT);  -- Auto-commits immediately
    INSERT INTO test_table VALUES (1);
ROLLBACK;  -- Only INSERT is rolled back, table still exists!
```

### Q6: "What happens if you don't COMMIT a transaction?"

**Expert Answer:**
> "Behavior depends on database settings and connection handling:
> 
> **Auto-commit ON** (default): Each statement commits automatically
> **Auto-commit OFF**: Changes remain uncommitted until explicit COMMIT/ROLLBACK
> **Connection closes**: Most databases automatically ROLLBACK uncommitted transactions
> **Session timeout**: Long-running transactions may be automatically rolled back"

```sql
-- Example of uncommitted transaction consequences:
BEGIN;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
    -- Connection drops here - BOTH updates are rolled back!
    -- Money transfer fails, maintaining data integrity
```

---

## ⚡ **Level 3: Advanced Scenario Questions**

### Q7: "When would you use TRUNCATE instead of DELETE?"

**Expert Answer:**
> "Use TRUNCATE when you need to remove ALL rows quickly for maintenance:
> - **Data cleanup**: Clearing staging tables after ETL
> - **Testing**: Resetting test data between runs  
> - **Performance**: Much faster than DELETE for large tables
> - **Log management**: Doesn't log individual row deletions"

**❌ Cannot use TRUNCATE when:**
- Table has foreign key references
- Need to keep some rows (WHERE clause)
- Need to rollback the operation
- Triggers need to fire for each row

### Q8: "How do you handle failed transactions in a multi-step process?"

**Expert Answer:**
```sql
-- Advanced transaction handling with savepoints:
BEGIN TRANSACTION;
    INSERT INTO orders (customer_id, total) VALUES (123, 500);
    SAVEPOINT after_order;
    
    UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 456;
    
    IF @@ERROR != 0  -- Check for errors
        ROLLBACK TO SAVEPOINT after_order;  -- Partial rollback
    ELSE
        COMMIT;  -- Save all changes
```

### Q9: "What's the difference between GRANT and REVOKE? Show practical examples."

**Expert Answer:**
```sql
-- GRANT: Give permissions (cumulative)
GRANT SELECT ON customers TO sales_team;
GRANT INSERT ON customers TO sales_team;  -- Now has SELECT + INSERT

-- REVOKE: Remove specific permissions
REVOKE INSERT ON customers FROM sales_team;  -- Now only has SELECT

-- Complex permission scenarios:
GRANT ALL PRIVILEGES ON orders TO manager_role;
GRANT SELECT (first_name, last_name) ON employees TO hr_intern;  -- Column-level
REVOKE ALL PRIVILEGES ON orders FROM manager_role;
```

---

## 🎯 **Level 4: Index & DDL Deep-Dive Questions**

### Q10: "When do you create indexes - during or after table creation? Explain both."

**Expert Answer:**
> "**Both approaches serve different purposes:**
> 
> **During table creation (DDL):**
> - PRIMARY KEY constraints (create clustered indexes)
> - UNIQUE constraints (business rules)
> - Essential indexes for data integrity
> 
> **After table creation (DDL):**
> - Performance indexes based on query patterns
> - Covering indexes for specific queries
> - Filtered indexes for selective data"

```sql
-- During creation (structure + business rules):
CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,           -- Creates clustered index
    customer_email VARCHAR(255) UNIQUE     -- Creates unique index
);

-- After creation (performance optimization):
CREATE INDEX IX_orders_customer ON orders (customer_id);
CREATE INDEX IX_orders_date_status ON orders (created_at, status);
```

### Q11: "What's the difference between PRIMARY KEY and CREATE INDEX?"

**Expert Answer:**
| Aspect | PRIMARY KEY | CREATE INDEX |
|--------|-------------|--------------|
| **Index Type** | Usually clustered | Usually non-clustered |
| **Uniqueness** | ✅ Enforced | ❌ Allows duplicates* |
| **NULL Values** | ❌ Not allowed | ✅ Allowed* |
| **Quantity** | One per table | Multiple per table |
| **Purpose** | Business rule + performance | Performance only |

*Unless UNIQUE INDEX specified

---

## 💡 **Level 5: Real-World Problem Solving**

### Q12: "Your application is slow. How do you determine if you need DDL or DML optimization?"

**Expert Answer:**
> "**Systematic diagnosis approach:**
> 
> **Check DML Performance First:**
> - Analyze slow SELECT/UPDATE/DELETE queries
> - Look for missing indexes (secondary indexes)
> - Check for table scans in execution plans
> 
> **Consider DDL Changes If:**
> - Query patterns changed (need new indexes)
> - Data growth requires partitioning  
> - Schema changes needed for optimization"

```sql
-- DML optimization (add indexes):
CREATE INDEX IX_slow_query ON large_table (frequently_queried_column);

-- DDL optimization (structural changes):
ALTER TABLE large_table ADD COLUMN computed_value AS (col1 + col2);
CREATE INDEX IX_computed ON large_table (computed_value);
```

### Q13: "You accidentally ran 'DROP TABLE customers'. What do you do?"

**Expert Answer:**
> "**Since DROP is DDL and auto-commits:**
> 1. **Cannot rollback** - damage is immediate
> 2. **Restore from backup** - most recent valid backup
> 3. **Recovery strategy:**
>    - Stop application immediately
>    - Restore table from backup
>    - Apply transaction log to recover recent changes
>    - Test data integrity before going live"

**Prevention Strategy:**
```sql
-- Use transactions for safety (where possible):
BEGIN TRANSACTION;
    -- Test your DDL on small scale first
    SELECT COUNT(*) FROM customers;  -- Verify you have the right table
-- COMMIT only when sure
```

---

## 🔍 **Level 6: Database-Specific Gotchas**

### Q14: "How does auto-commit behavior differ between MySQL and PostgreSQL?"

**Expert Answer:**
| Database | DDL Auto-commit | DML Auto-commit | DDL Rollback |
|----------|----------------|-----------------|--------------|
| **MySQL** | ✅ Always | ❌ No (explicit commit needed) | ❌ Not supported |
| **PostgreSQL** | ❌ No* | ❌ No | ✅ Supported! |
| **SQL Server** | ✅ Always | Depends on setting | ❌ Not supported |

*PostgreSQL allows DDL in transactions!

### Q15: "Explain Oracle's implicit commit behavior with DCL commands."

**Expert Answer:**
> "In Oracle, **DCL commands (GRANT/REVOKE) trigger implicit commits**, meaning any pending DML transactions are automatically committed when you execute GRANT or REVOKE."

```sql
-- Oracle behavior:
BEGIN;  -- Start transaction
    UPDATE employees SET salary = 60000 WHERE id = 123;  -- Uncommitted
    GRANT SELECT ON employees TO new_user;  -- Implicit commit!
    -- Previous UPDATE is now committed, cannot rollback!
```

---

## 🎪 **Level 7: Trick Questions & Edge Cases**

### Q16: "Can you use WHERE clause with DDL commands?"

**Tricky Answer:**
> "**Generally NO for structure DDL**, but **YES for some special cases:**
> - TRUNCATE: No WHERE clause allowed
> - DROP: No WHERE clause  
> - **Exception**: CREATE INDEX with WHERE clause (filtered indexes)"

```sql
-- ❌ This doesn't work:
TRUNCATE TABLE orders WHERE status = 'CANCELLED';

-- ✅ But this does (filtered index):
CREATE INDEX IX_active_orders ON orders (customer_id) 
WHERE status = 'ACTIVE';
```

### Q17: "What happens to indexes when you DROP a table?"

**Expert Answer:**
> "When you DROP a table, **ALL associated indexes are automatically dropped** as well - both clustered and non-clustered indexes. This is because indexes cannot exist without their base table."

### Q18: "Can DCL commands be part of a transaction?"

**Expert Answer:**
> "**Depends on the database:**
> - **Oracle**: DCL auto-commits, cannot be in transactions
> - **PostgreSQL**: DCL can be in transactions and rolled back
> - **SQL Server**: Mixed behavior - some DCL auto-commits"

---

## 🏆 **Master-Level Questions (Senior Roles)**

### Q19: "Design a strategy for zero-downtime schema changes in production."

**Expert Answer:**
> "**Multi-phase approach using DDL + DML:**
> 
> **Phase 1**: Add new column (nullable)
> ```sql
> ALTER TABLE products ADD COLUMN new_price DECIMAL(10,2) NULL;
> ```
> 
> **Phase 2**: Populate data with DML
> ```sql
> UPDATE products SET new_price = old_price * 1.1;
> ```
> 
> **Phase 3**: Make NOT NULL (after data populated)
> ```sql
> ALTER TABLE products ALTER COLUMN new_price SET NOT NULL;
> ```
> 
> **Phase 4**: Drop old column
> ```sql
> ALTER TABLE products DROP COLUMN old_price;
> ```"

### Q20: "How would you audit DDL changes in a production environment?"

**Expert Answer:**
```sql
-- Create audit table
CREATE TABLE ddl_audit (
    event_time TIMESTAMP,
    user_name VARCHAR(50),
    command_type VARCHAR(20),
    object_name VARCHAR(100),
    sql_text TEXT
);

-- SQL Server: Use DDL triggers
CREATE TRIGGER audit_ddl_changes
ON DATABASE
FOR CREATE_TABLE, ALTER_TABLE, DROP_TABLE
AS
BEGIN
    INSERT INTO ddl_audit 
    SELECT GETDATE(), USER_NAME(), 
           EVENTDATA().value('(/EVENT_INSTANCE/EventType)[1]','VARCHAR(50)'),
           EVENTDATA().value('(/EVENT_INSTANCE/ObjectName)[1]','VARCHAR(100)'),
           EVENTDATA().value('(/EVENT_INSTANCE/TSQLCommand/CommandText)[1]','NVARCHAR(MAX)')
END;
```

---

## 📊 **Interview Success Strategy**

### **30-Second Elevator Answers:**
- **"What's DDL?"** → *"Structure commands - CREATE, ALTER, DROP, TRUNCATE"*  
- **"What's DML?"** → *"Data commands - SELECT, INSERT, UPDATE, DELETE"*
- **"DELETE vs TRUNCATE?"** → *"DELETE is selective and transactional, TRUNCATE removes all rows and auto-commits"*
- **"Can you rollback DDL?"** → *"No in most databases, except PostgreSQL"*

### **Red Flags to Avoid:**
❌ "DDL and DML are the same thing"  
❌ "You can always rollback any SQL command"  
❌ "TRUNCATE and DELETE work exactly the same way"  
❌ "Indexes are created automatically for all queries"

### **Bonus Points Answers:**
✅ Mention database-specific differences  
✅ Discuss real-world performance implications  
✅ Show understanding of transaction safety  
✅ Explain indexing strategy considerations

---

## 🎯 **Quick Drill Practice**

Test yourself with these rapid-fire questions:

1. **Can TRUNCATE be rolled back?** → No (DDL auto-commits)
2. **Which is faster: DELETE or TRUNCATE?** → TRUNCATE (no logging)
3. **Can you add WHERE to TRUNCATE?** → No (DDL limitation)
4. **Do triggers fire with TRUNCATE?** → No (DDL doesn't fire triggers)
5. **PostgreSQL DDL rollback support?** → Yes (unique feature)
6. **PRIMARY KEY creates which index type?** → Usually clustered
7. **Can DCL be in transactions?** → Database-dependent
8. **GRANT followed by REVOKE result?** → Permission removed

**Perfect Score: 8/8** = Ready for senior interviews!  
**Good Score: 6-7/8** = Study edge cases  
**Needs Work: <6/8** = Review fundamentals first

---

## 📊 Quick Reference Table

| Category | Purpose | Auto-Commit | Rollback | Examples |
|----------|---------|-------------|----------|----------|
| **DDL** | Structure | ✅ Yes | ❌ No* | CREATE, ALTER, DROP, TRUNCATE |
| **DML** | Data | ❌ No | ✅ Yes | SELECT, INSERT, UPDATE, DELETE |
| **DCL** | Permissions | ✅ Yes | ❌ No | GRANT, REVOKE |
| **TCL** | Transactions | N/A | N/A | COMMIT, ROLLBACK, SAVEPOINT |

*PostgreSQL allows rollback of DDL

---

## 🔍 Advanced Interview Topics

### Implicit vs Explicit Transactions:
```sql
-- Implicit (auto-commit mode) - each statement commits
INSERT INTO Orders VALUES (1, 'Product A');  -- Automatically committed

-- Explicit transaction
BEGIN;
    INSERT INTO Orders VALUES (2, 'Product B');
    INSERT INTO OrderItems VALUES (2, 1, 'Item A');
    -- Both committed together
COMMIT;
```

### DDL in Transactions (PostgreSQL):
```sql
BEGIN;
    CREATE TABLE temp_table (id INT);
    INSERT INTO temp_table VALUES (1);
    -- Can rollback both DDL and DML!
ROLLBACK;  -- Table creation is undone
```

### Transaction Isolation and TCL:
```sql
-- Set isolation level affects how transactions see each other
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
    SELECT * FROM accounts WHERE balance > 1000;
    -- Other transactions can't modify these rows
COMMIT;
```

---

## 💡 Memory Tips for Interviews

**DDL**: **D**efine **D**atabase **L**ayout (CREATE, ALTER, DROP)
**DML**: **D**ata **M**anipulation **L**anguage (SELECT, INSERT, UPDATE, DELETE)  
**DCL**: **D**atabase **C**ontrol **L**anguage (GRANT, REVOKE permissions)
**TCL**: **T**ransaction **C**ontrol **L**anguage (COMMIT, ROLLBACK transactions)

**Remember**: "**D**ata **D**efinition, **D**ata **M**anipulation, **D**ata **C**ontrol, **T**ransaction **C**ontrol"