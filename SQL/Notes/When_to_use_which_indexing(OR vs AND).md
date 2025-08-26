# 📘 MySQL Indexing Guide

A complete guide to understanding **when and how to use indexes in MySQL**. Covers single, composite, covering indexes, index merge, OR vs UNION, and rules for ordering.

---

## 🔹 1. Why Indexes Matter

* Index = data structure (usually a **B+Tree**) that speeds up lookups.
* Without indexes: MySQL does **full table scan** → O(n).
* With indexes: MySQL can **jump directly** to relevant rows → O(log n).

**Tradeoff:**

* ✅ Faster SELECT queries.
* ❌ Slower INSERT/UPDATE/DELETE (because indexes must be updated).
* ❌ More disk space.

---

## 🔹 2. Types of Indexes

### 2.1 Single-Column Index

* Index on one column.
* Best for queries filtering on **one column**.

```sql
CREATE INDEX idx_area ON World(area);
CREATE INDEX idx_population ON World(population);
```

👉 Example:

```sql
SELECT name, population, area
FROM World
WHERE area >= 3000000;
```

Uses `idx_area` for fast range scan.

---

### 2.2 Composite (Multi-Column) Index

* Index on multiple columns.
* MySQL uses **leftmost prefix rule**.

👉 If index = `(A, B, C)`:

* Works for `A`
* Works for `A, B`
* Works for `A, B, C`
* ❌ Does **not** work for `B`, `C`, or `B, C` (because `A` is skipped).

```sql
CREATE INDEX idx_continent_area_pop
ON World (continent, area, population);
```

Query:

```sql
SELECT name
FROM World
WHERE continent = 'Asia' AND area >= 3000000
ORDER BY population DESC;
```

✔️ Index is useful for filtering and ordering.

---

### 2.3 Covering Index

* An index that contains **all the columns needed** for the query.
* MySQL can answer query **entirely from index**, no table lookup.

```sql
CREATE INDEX idx_area_population_name
ON World (area, population, name);
```

Query:

```sql
SELECT name, population, area
FROM World
WHERE area >= 3000000;
```

✔️ Covered entirely by index.

⚠️ Downside: Larger index = more storage + slower writes.

---

### 2.4 Unique Index

* Ensures values are unique.
* MySQL automatically creates a unique index for **PRIMARY KEY**.

```sql
CREATE UNIQUE INDEX idx_email ON Users(email);
```

---

### 2.5 Fulltext Index

* For text searching (`MATCH ... AGAINST`).
* Only works on `CHAR`, `VARCHAR`, `TEXT`.

---

## 🔹 3. Ordering Rule of Thumb for Composite Indexes

👉 General order inside composite index:

1. Equality conditions (`=`)
2. Range conditions (`<, >, BETWEEN`)
3. ORDER BY / JOIN conditions

---

### Example

```sql
CREATE INDEX idx_state_city_salary
ON Employees(state, city, salary);
```

Query:

```sql
SELECT *
FROM Employees
WHERE state = 'CA' AND city = 'LA' AND salary > 80000
ORDER BY hire_date;
```

* `state` = equality ✅
* `city` = equality ✅
* `salary` = range ✅
* `hire_date` = ❌ cannot be used because it comes **after a range**.

So best order = `(state, city, salary)`.

---

### Explicit What Works / Doesn’t Work

Given index `(A, B, C)` = `(state, city, salary)`:

| Query Condition                                                            | Uses Index On            | Works? |
| -------------------------------------------------------------------------- | ------------------------ | ------ |
| `WHERE state = 'CA'`                                                       | A                        | ✅      |
| `WHERE state = 'CA' AND city = 'LA'`                                       | A, B                     | ✅      |
| `WHERE state = 'CA' AND salary > 80000`                                    | A (stops at range)       | ✅      |
| `WHERE city = 'LA'`                                                        | B only                   | ❌      |
| `WHERE salary > 80000`                                                     | C only                   | ❌      |
| `WHERE city = 'LA' AND salary > 80000`                                     | B, C                     | ❌      |
| `WHERE state = 'CA' AND city = 'LA' AND salary > 80000`                    | A, B, C                  | ✅      |
| `WHERE state = 'CA' AND city = 'LA' ORDER BY salary`                       | A, B, C                  | ✅      |
| `WHERE state = 'CA' AND city = 'LA' AND salary > 80000 ORDER BY hire_date` | A, B, C (not hire\_date) | ❌      |

👉 Takeaway: After a **range condition**, MySQL stops using further index columns.

---

## 🔹 4. AND vs OR in Indexing

### 4.1 AND (good for composite)

```sql
SELECT name
FROM World
WHERE continent = 'Asia'
  AND population >= 25000000;
```

👉 Use:

```sql
CREATE INDEX idx_continent_population ON World(continent, population);
```

---

### 4.2 OR (tricky)

```sql
SELECT name, population, area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;
```

* Composite `(area, population)` isn’t efficient.
* MySQL either:

  * Uses **index merge** (union of single indexes).
  * Or falls back to **table scan**.

👉 Solution:

```sql
CREATE INDEX idx_area ON World(area);
CREATE INDEX idx_population ON World(population);
```

---

## 🔹 5. Index Merge in MySQL

### What is Index Merge?

* MySQL combines results from **multiple single-column indexes**.
* Works for `OR` and some `AND`.

👉 Example:

```sql
EXPLAIN
SELECT name, population, area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;
```

Plan:

```
type: index_merge
key: idx_area, idx_population
Extra: Using union(idx_area, idx_population); Using where
```

* MySQL scans `idx_area`.
* Scans `idx_population`.
* Unions results.

✅ Faster than table scan.
❌ Still needs table lookup for non-indexed columns.

---

## 🔹 6. UNION vs OR

### Why use UNION?

* Splitting `OR` lets each query use its index independently.
* Often faster than index merge.

```sql
SELECT name, population, area
FROM World
WHERE area >= 3000000
UNION
SELECT name, population, area
FROM World
WHERE population >= 25000000;
```

* First query → uses `idx_area`.
* Second query → uses `idx_population`.
* `UNION` automatically removes duplicates.

---

### UNION vs UNION ALL

* `UNION`: removes duplicates (safe, but extra cost).
* `UNION ALL`: faster, keeps duplicates.

👉 Example with UNION ALL + DISTINCT:

```sql
SELECT name, population, area
FROM (
  SELECT name, population, area
  FROM World
  WHERE area >= 3000000
  UNION ALL
  SELECT name, population, area
  FROM World
  WHERE population >= 25000000
) t
GROUP BY name, population, area;
```

---

## 🔹 7. Special Cases

### OR on the same column

```sql
WHERE status = 'A' OR status = 'B'
```

Better:

```sql
WHERE status IN ('A', 'B');
```

Single index on `status` works perfectly.

---

### Covering Index Example (Hot Query)

```sql
CREATE INDEX idx_orders ON Orders(customer_id, status, order_date);
```

Query:

```sql
SELECT customer_id, status, order_date
FROM Orders
WHERE customer_id = 123 AND status = 'Shipped';
```

✔️ Covered entirely by the index.

---

## 🔹 8. Interview-Style Summary

1. **Single-column index** → when filtering by one column.
2. **Composite index** → when multiple conditions with AND (use ordering rule: equality → range → sort/join).
3. **Covering index** → when query is repetitive & read-heavy.
4. **OR conditions** → prefer two single-column indexes (index merge) or rewrite as UNION.
5. **UNION vs UNION ALL**:

   * UNION → dedupes, safe but slower.
   * UNION ALL → faster, but risk of duplicates.
6. **Always confirm with `EXPLAIN`**:

   ```sql
   EXPLAIN SELECT ...;
   ```

   Check if index is used (type = `range`, `index_merge`) or if it falls back to full table scan.

---

✅ These notes now cover:

* All index types (single, composite, covering)
* Ordering rules (equality → range → sort/join)
* AND vs OR strategies
* Index merge explanation
* UNION vs UNION ALL
* Practical + interview insights
