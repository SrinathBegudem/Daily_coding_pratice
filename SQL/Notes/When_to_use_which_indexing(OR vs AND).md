# 📘 MySQL Indexing Guide

# This concept is specially arised when i am solving LC 595
So, i solved intially with covering index(composite) and then realised that composite indexing usually doesnt go well with 'OR' operator we usually do single col indexing for mutiple cols and let sql decide the the merge indexing and to be more clear we can use union operator and write 2 diff queries this is for question 595. and more optimised is union all + distinct or group by (no de duplication and quicker) but you need to explicity take care of duplicates.

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

---

## 🔹 9. Ordering with Range + ORDER BY — Guarantees and Gotchas

### Do I need `ORDER BY` if the rows “naturally” come ordered?

* **Yes, always specify `ORDER BY`** when you need deterministic ordering. Without it, SQL does **not** guarantee the returned order—even if today it “looks” sorted due to the chosen index/plan. A future plan (or a different index) may return rows in a different order.

### Why `ORDER BY` can be satisfied by an index (no filesort)

* If your `WHERE` uses only **equalities** on the left columns of a composite index, and your `ORDER BY` uses the **next** column(s) of that same index (same direction), MySQL can read rows already in order.

**Index**

```sql
CREATE INDEX idx_state_city_hiredate ON Employees(state, city, hire_date);
```

**Query**

```sql
SELECT *
FROM Employees
WHERE state = 'CA' AND city = 'LA'
ORDER BY hire_date; -- ✅ No filesort
```

### What changes when there’s a **range** in `WHERE`

* Once MySQL hits a **range condition** (`>`, `<`, `BETWEEN`, `LIKE 'abc%'`) on a column **before** your `ORDER BY` columns in the index key, it begins a **range scan**. From that point, it can’t also keep rows ordered by **later** columns in the same index → **filesort** needed.

**Index (filter-first)**

```sql
CREATE INDEX idx_state_city_salary ON Employees(state, city, salary);
```

**Query**

```sql
SELECT *
FROM Employees
WHERE state='CA' AND city='LA' AND salary>80000
ORDER BY hire_date;  -- ❌ Filesort (range on salary precedes ORDER BY column)
```

### Two valid strategies when range ≠ ORDER BY

1. **Favor filtering (range-first)**

   * Index: `[equalities] → [range column]` (e.g., `(state, city, salary)`).
   * Pro: Fast to find matching rows if the range is selective.
   * Con: **Filesort** for `ORDER BY`.

2. **Favor ordering (order-first)**

   * Index: `[equalities] → [ORDER BY columns]` (e.g., `(state, city, hire_date)`), rely on **Index Condition Pushdown (ICP)** to filter the range.
   * Pro: ✅ **No filesort**; can be great with `LIMIT` (early exit).
   * Con: May scan more rows because the range column isn’t indexed in position.

**Order-first example + LIMIT**

```sql
CREATE INDEX idx_state_city_hiredate ON Employees(state, city, hire_date DESC);

SELECT *
FROM Employees
WHERE state='CA' AND city='LA' AND salary>80000
ORDER BY hire_date DESC
LIMIT 50;  -- ✅ No filesort, early-exit after 50 matches
```

### Best case: range on the **same** column as `ORDER BY`

If your range and `ORDER BY` are on the **same** column, you can avoid filesort:

```sql
CREATE INDEX idx_state_city_hiredate ON Employees(state, city, hire_date);

SELECT *
FROM Employees
WHERE state='CA' AND city='LA' AND hire_date>=DATE('2024-01-01')
ORDER BY hire_date;  -- ✅ No filesort (range and order share the same key)
```

### Quick checklist (interview-ready)

* List predicates as **equality vs range**; list `ORDER BY` columns.
* If **range and order are on the same column(s)** → index `[equalities] → [that column]` → ✅ no filesort.
* If **range is on a different column** than `ORDER BY`:

  * **Filter-first**: `[equalities] → [range]` → expect **filesort**.
  * **Order-first**: `[equalities] → [ORDER BY]` + **ICP** → no filesort, more scanning.
* For **top‑N** pages → prefer order-first + `LIMIT` for early exit.
* **Always** confirm with `EXPLAIN`:

  * `Using filesort` → sort happening.
  * `Using index condition` → ICP filtering.
  * Absence of `Using filesort` when ordered → index satisfies `ORDER BY`.
