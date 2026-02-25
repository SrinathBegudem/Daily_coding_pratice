# How to decide joins based on the given question.
Keyword → JOIN mapping (memorize this)

1) left join
“did not get any”, “missing”, “no record”, “may not exist”
→ LEFT JOIN

2) Inner join
“only if exists in both”
→ INNER JOIN

# In join when to have a condition inside ON and when to have it on WHERE
- If it is during matching then include it in ON 
- If it is about which row to keep, then it goes inside the where cond
EX for lc 577 
Conditions:

bonus < 1000

OR bonus IS NULL

These are filtering conditions, not join conditions.

So they go in WHERE, not in ON.

Why?
Because they decide which rows to keep, not how to match rows.

-----------------------------------------------
# LC 1280 COUNT(Column) VS COUNT(*), NULL val and NON NULL VAL COUNT

COUNT(column) does NOT count NULLs

COUNT(*) counts rows, even if columns are NULL

That’s the whole rule.

Let’s see it with a tiny example

Imagine this table after a LEFT JOIN:

student_id	subject_name	e_subject
2	Physics	NULL
2	Physics	NULL

Two rows exist, but the column is NULL.

What happens with different COUNTs?
COUNT(e_subject)   → 0
COUNT(*)           → 2


Why?

COUNT(e_subject) counts non-NULL values only

COUNT(*) counts rows, no matter what’s inside

GROUP BY — interview notes (concise)
1. Does GROUP BY column order matter?

No.

GROUP BY a, b, c


is the same as

GROUP BY c, b, a

2. What does GROUP BY actually do?

It collapses rows into one row per unique combination of the grouped columns.

3. What columns can appear in SELECT when GROUP BY exists?

Only:

columns in GROUP BY

or aggregated columns (COUNT, SUM, AVG, etc.)

👉 Rule to remember

If a column is selected and not aggregated, it must be in GROUP BY.

4. Why do we include all printed columns in GROUP BY?

Because SQL needs one value per group.
If it’s not grouped or aggregated, SQL doesn’t know which value to pick.


------------------------------
# You can chain as many JOINs as you want. Each JOIN has its own ON condition, and the ON clause applies to the tables being joined at that step.

Basic pattern
FROM t1
JOIN t2 ON t2.t1_id = t1.id
JOIN t3 ON t3.t2_id = t2.id


So:

JOIN t2 ... ON ... explains how t2 matches with what you currently have (initially t1)

JOIN t3 ... ON ... explains how t3 matches with the result of (t1 JOIN t2)

You can also join t3 directly to t1 if that’s the relationship:

FROM t1
JOIN t2 ON t2.t1_id = t1.id
JOIN t3 ON t3.t1_id = t1.id

What happens internally? What is the order?
Logically (how SQL is defined)

SQL is evaluated roughly like this:

FROM

JOIN ... ON ... (left to right)

WHERE

GROUP BY

HAVING

SELECT

ORDER BY

LIMIT

So logically, yes: it’s like:

first build t1 JOIN t2

then join that result with t3

and so on

Physically (what the database actually does)

The optimizer is free to reorder joins for speed, especially for INNER JOINs. So the engine might execute:

t2 JOIN t3 first

then join that with t1
even if you wrote t1 JOIN t2 JOIN t3.

But it will still return the same result (for inner joins) because inner joins are associative/commutative under normal conditions.

Exception: with LEFT JOIN / RIGHT JOIN, join order matters more, and the optimizer has less freedom.

Quick rule for ON conditions

For each join, your ON condition should connect:

a key from the “new” table

to a key already in the current result

Example mindset:

“When I add t3, how does t3 relate to what I already have?”



------------------------------------------
# IN VS NOT IN VS EXISTS VS NOT EXISTS


We will use this data:

Customer

(1, A)

(2, B)

(3, C)

(4, D)

Orders

(10, cust_id = 1)

(11, cust_id = 2)

(12, cust_id = NULL)

1) IN with subquery

Query:

SELECT *
FROM Customer
WHERE id IN (
    SELECT cust_id
    FROM Orders
);

How it executes internally

Step 1: Run the subquery first (one time)

SELECT cust_id FROM Orders;


Result set becomes:

{1, 2, NULL}


Think of SQL storing this as a set/list.

Step 2: Now evaluate outer query row by row against that set

Customer id = 1 → 1 IN {1,2,NULL} → TRUE → keep

Customer id = 2 → 2 IN {1,2,NULL} → TRUE → keep

Customer id = 3 → 3 IN {1,2,NULL} → FALSE → drop

Customer id = 4 → 4 IN {1,2,NULL} → FALSE → drop

✅ Final output: Customers 1 and 2

Key point

IN is basically:

“Compute a list once, then check membership.”

2) EXISTS (correlated, row-by-row)

Query:

SELECT *
FROM Customer c
WHERE EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.cust_id = c.id
);

How it executes internally

Here, the inner query references c.id, so it depends on the outer row.

For each Customer row:

Customer id = 1
Inner becomes WHERE o.cust_id = 1
Finds at least one row → EXISTS = TRUE → keep

Customer id = 2
Inner becomes WHERE o.cust_id = 2
Finds at least one row → TRUE → keep

Customer id = 3
Inner becomes WHERE o.cust_id = 3
Finds none → FALSE → drop

Customer id = 4
Inner becomes WHERE o.cust_id = 4
Finds none → FALSE → drop

✅ Final output: Customers 1 and 2

Key point

EXISTS is:

“For each row, check if a matching row exists, stop at first match.”

3) NOT IN with subquery (danger zone)

Query:

SELECT *
FROM Customer
WHERE id NOT IN (
    SELECT cust_id
    FROM Orders
);

How it executes internally

Step 1: Subquery runs once
Result set:

{1, 2, NULL}


Step 2: Evaluate outer rows
Here is the crucial part:

Customer id = 3: 3 NOT IN {1,2,NULL}

You might think:

3 is not 1

3 is not 2
So include it.

But SQL must also check:

3 is not NULL → this comparison is UNKNOWN (because anything compared to NULL becomes UNKNOWN)

So the whole NOT IN becomes UNKNOWN.

In SQL:

TRUE passes

FALSE fails

UNKNOWN also fails (treated like FALSE in WHERE)

So:

id = 1 → 1 NOT IN {1,2,NULL} → FALSE → drop

id = 2 → FALSE → drop

id = 3 → UNKNOWN → drop

id = 4 → UNKNOWN → drop

❌ Final output: nothing

Key point (memorize)

If the subquery can return NULL, NOT IN can return an empty result even when logically it should not.

If you really want NOT IN, you must filter NULLs:

WHERE id NOT IN (
    SELECT cust_id
    FROM Orders
    WHERE cust_id IS NOT NULL
);


Then you get 3 and 4.

4) NOT EXISTS (safe and preferred)

Query:

SELECT *
FROM Customer c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.cust_id = c.id
);

How it executes internally

This is the negative version of EXISTS.

For each Customer row:

Customer id = 1
Subquery finds a matching order → EXISTS = TRUE
NOT EXISTS = FALSE → drop

Customer id = 2
Match exists → drop

Customer id = 3
No matching orders → EXISTS = FALSE
NOT EXISTS = TRUE → keep

Customer id = 4
No matching orders → keep

✅ Final output: Customers 3 and 4

Key point

NOT EXISTS is:

“For each row, keep it only if no matching row exists.”

Final summary (simple rules)

IN: subquery runs once → membership check → OK usually

EXISTS: correlated, runs per row → relationship check → very safe

NOT IN: dangerous if subquery can include NULL → avoid in interviews

NOT EXISTS: safest for “not matching” logic → preferred




----------------------------
# correlated subquery

This is an important concept. Many people “use” correlated subqueries without actually understanding them. I’ll explain it cleanly, with clear examples, patterns, and when to recognize them in interviews.

1. What is a correlated subquery (plain English)

A correlated subquery is a subquery that depends on the outer query.

It cannot run by itself.

It is re-evaluated once for each row of the outer query.

It cannot run independently

It is evaluated row by row

Typical keywords: EXISTS, NOT EXISTS, comparisons with aggregates

2. Simple definition (interview-ready)

A correlated subquery is a subquery that references columns from the outer query and is evaluated row by row.

If the inner query uses a column from the outer query, it is correlated.

3. Small concrete example
Tables

Customer

id	name
1	A
2	B
3	C

Orders

id	cust_id	amount
10	1	100
11	1	200
12	2	300
Correlated subquery example
SELECT *
FROM Customer c
WHERE EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.cust_id = c.id
);

Why this is correlated

The inner query uses:

c.id


which belongs to the outer query.

The subquery cannot run alone because c.id is unknown by itself.

4. How it executes (very important)

SQL conceptually does this:

FOR each row in Customer:
    substitute c.id into subquery
    run subquery
    if condition is true:
        keep row


So:

Customer 1 → inner query runs with cust_id = 1

Customer 2 → inner query runs with cust_id = 2

Customer 3 → inner query runs with cust_id = 3

5. Non-correlated vs correlated (side by side)
Non-correlated subquery
SELECT *
FROM Customer
WHERE id IN (
    SELECT cust_id
    FROM Orders
);


Subquery runs once

Result stored as a set

Outer query checks membership

Correlated subquery
SELECT *
FROM Customer c
WHERE EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.cust_id = c.id
);


Subquery runs per outer row

Uses outer query column

Row-by-row logic

6. Classic correlated subquery patterns (memorize these)
Pattern 1: EXISTS / NOT EXISTS (most common)

Use when:

Checking relationships

Checking presence or absence

Avoiding NULL issues

Example:

SELECT *
FROM Employee e
WHERE NOT EXISTS (
    SELECT 1
    FROM Employee m
    WHERE m.managerId = e.id
);


Meaning:

Employees who are not managers

Pattern 2: Comparison with aggregate (very common in interviews)

Example:

SELECT *
FROM Employee e
WHERE salary > (
    SELECT AVG(salary)
    FROM Employee
    WHERE department = e.department
);


Why correlated:

Inner query uses e.department

Avg salary is recomputed per department

Meaning:

Employees earning above their department average

Pattern 3: Top-N per group

Example:

SELECT *
FROM Orders o
WHERE amount = (
    SELECT MAX(amount)
    FROM Orders
    WHERE cust_id = o.cust_id
);


Meaning:

Highest order per customer

7. When to use correlated subqueries

Use them when:

The condition depends on the current row

You need row-level comparison

Grouping logic is complex

EXISTS / NOT EXISTS logic is clearer than JOINs

8. When NOT to use them

Avoid when:

The subquery does not depend on the outer row

A JOIN + GROUP BY is simpler

Performance is critical and dataset is huge

Note: Modern optimizers often rewrite correlated subqueries into joins internally, so correctness matters more than micro-optimizations in interviews.

9. Pattern recognition in interviews

If the question says:

“for each customer”

“per employee”

“per department”

“who have / who do not have”

“greater than average of their group”

You are probably looking at:
→ correlated subquery
→ often with EXISTS or aggregates

10. Interview one-liner answer

If asked:

What is a correlated subquery?

Answer:

A correlated subquery is a subquery that references the outer query and is evaluated once per outer row.

11. Key takeaway (remember this)

If the inner query uses outer table columns → correlated

Runs row by row

EXISTS and NOT EXISTS are the most common forms

Very common in interview SQL questions

If you want, next I can:

rewrite correlated queries as JOINs

show execution plans

---------------------------------------------------------------
IFNULL vs COALESCE — Interview Notes
What problem do they solve

Both are used to replace NULL with a default value so calculations don’t break and results stay meaningful.

IFNULL

Syntax

IFNULL(value, replacement)


Key points

Takes exactly 2 arguments

If value is NULL → returns replacement

If value is NOT NULL → returns value

Database-specific (MySQL, SQLite)

Simple and readable

Limited flexibility

Example

IFNULL(score, 0)

COALESCE

Syntax

COALESCE(v1, v2, v3, ...)


Key points

Takes 2 or more arguments

Returns the first non-NULL value

SQL standard (ANSI SQL)

Works across databases (MySQL, Postgres, SQL Server, Oracle)

More powerful and flexible

Preferred in interviews and production SQL

Example

COALESCE(score, bonus, 0)

Core Relationship (Very Important)

IFNULL is a special case of COALESCE

IFNULL(a, b)     ≈     COALESCE(a, b)


But:

COALESCE(a, b, c)   ❌ cannot be done with IFNULL

Common Use Case (Division / Aggregates)

Avoid NULL results:

COALESCE(confirmed / total, 0)


Works the same as:

IFNULL(confirmed / total, 0)

Interview Comparison Table (Mental)
Feature	IFNULL	COALESCE
Arguments	Exactly 2	2 or more
SQL Standard	❌ No	✅ Yes
Cross-DB	❌ Limited	✅ Yes
Flexibility	Low	High
Interview Preference	⚠️ Okay	✅ Best
When to use what

Use IFNULL when

Writing quick MySQL-only queries

You only need one fallback

LeetCode problems

Use COALESCE when

Writing interview SQL

Writing production SQL

Handling multiple fallbacks

Want database portability

One-line interview answer (memorize)

IFNULL and COALESCE behave the same with two arguments, but COALESCE is more general, SQL-standard, and preferred.


------------------------------------
# What is DATE_FORMAT?

DATE_FORMAT is a MySQL function used to convert a date or datetime into a string in the format you want.

Basic syntax:

DATE_FORMAT(date_column, 'format_string')


date_column → a DATE or DATETIME value

format_string → tells MySQL how to display that date

It does not change the data, it only changes how it is shown or grouped.

What are those % symbols?

The % symbols are called format specifiers.

Each one means:

“Replace this with a specific part of the date”

Think of them as placeholders.

Most important format specifiers (you should memorize these)
Specifier	Meaning	Example
%Y	4-digit year	2024
%y	2-digit year	24
%m	Month number (01–12)	03
%c	Month number (1–12)	3
%M	Full month name	March
%b	Short month name	Mar
%d	Day of month (01–31)	09
%H	Hour (00–23)	18
%i	Minutes	45
%s	Seconds	30
Examples (very important)
Year–Month (most common)
DATE_FORMAT(order_date, '%Y-%m')


Output:

2024-03


Used for:

monthly reports

grouping by month

Full readable date
DATE_FORMAT(order_date, '%M %d, %Y')


Output:

March 09, 2024

Month name only (⚠️ risky for grouping)
DATE_FORMAT(order_date, '%M')


Output:

March


This ignores year, so January 2023 and January 2024 get merged.

Why %Y-%m is so popular
DATE_FORMAT(date, '%Y-%m')


Because:

Keeps year and month together

Sorts correctly as a string

Looks clean

Perfect for grouping

Is DATE_FORMAT only for SELECT?

No. You can use it in:

SELECT

GROUP BY

ORDER BY

WHERE (careful, may hurt performance)

Example:

GROUP BY DATE_FORMAT(order_date, '%Y-%m')

Important interview warning

DATE_FORMAT returns a string, not a date.

So:

Good for grouping and display

Not ideal for date math

For date math, use:

YEAR()

MONTH()

DATE_ADD()

DATEDIFF()

Mental model (store this)

% symbols tell MySQL which part of the date to print.

One-line interview explanation

DATE_FORMAT converts a date into a formatted string using percent-based specifiers like %Y for year and %m for month.

If you want next:

difference between DATE_FORMAT and EXTRACT

grouping by week

rolling monthly windows
---------------------------------------------------------

# LC 550 COUNT(*) without group by gives one output , and with group by gives multiple rows 


1. COUNT(*) without GROUP BY
SELECT COUNT(*) FROM table;


This counts all rows in the table.

Output: one single number
Example: 100

2. COUNT(*) with GROUP BY
SELECT col, COUNT(*) 
FROM table
GROUP BY col;


Now SQL works group by group, not on the whole table.

What happens:

Rows are split into groups based on col

COUNT(*) counts rows inside each group

Output: multiple rows, one per group

Example table:

col
A
A
B
B
B
C

Query:

SELECT col, COUNT(*) 
FROM table
GROUP BY col;


Output:

col	COUNT(*)
A	2
B	3
C	1

So:

NOT a single number

One count per group

3. Important clarification (very common confusion)

❌ This does NOT count number of groups:

SELECT COUNT(*) FROM table GROUP BY col;


This returns multiple rows, not one.

4. If you want number of groups

Use COUNT(DISTINCT col):

SELECT COUNT(DISTINCT col) FROM table;


Example result:

3

5. Mental model (remember this)

COUNT(*) → counts rows

GROUP BY → splits data into groups

COUNT(*) + GROUP BY → counts rows per group

COUNT(DISTINCT col) → counts number of groups


--------------------------------------
# LC 619. Biggest Single Number
Core Rule (MOST IMPORTANT)

When you use GROUP BY, all aggregate functions run per group, not across all rows.

This applies to:

MAX

MIN

COUNT

SUM

AVG

How aggregation really works
Without GROUP BY
SELECT MAX(num) FROM table;


→ One result
→ Aggregate runs over all rows

With GROUP BY
SELECT MAX(num)
FROM table
GROUP BY category;


→ One result per category
→ Aggregate runs inside each group

Why your query returned multiple rows
SELECT MAX(num)
FROM MyNumbers
GROUP BY num
HAVING COUNT(*) = 1;


After GROUP BY num:

Each group has only one value

MAX(num) = num for that group

So result = all single numbers, not the biggest one.

Correct pattern for “aggregate of aggregates”

When you need:

“MAX / MIN / COUNT of values after grouping”

You must do it in two steps:

Step 1: Group & filter
SELECT num
FROM MyNumbers
GROUP BY num
HAVING COUNT(*) = 1;

Step 2: Aggregate again
SELECT MAX(num) FROM (result);

Clean template (memorize)
SELECT AGG(col)
FROM (
    SELECT col
    FROM table
    GROUP BY col
    HAVING condition
) t;

COUNT behaves the same way
SELECT COUNT(*)
FROM table
GROUP BY category;


→ Returns multiple rows, one per category
→ NOT a single count

To count number of groups:

SELECT COUNT(*) FROM (
    SELECT category
    FROM table
    GROUP BY category
) t;

One-line interview summary

GROUP BY defines the unit of aggregation. Aggregate functions always operate within each group, never across groups unless grouping is removed or nested.

Mental checklist

Want one row → no GROUP BY

Want per group result → use GROUP BY

Want overall aggregate after grouping → use subquery or CTE

Final takeaway

Your understanding is 100% correct now.
This is one of the most common SQL interview traps, and you just cleared it.
------------------------------------------------------------
# What DISTINCT actually does

DISTINCT removes duplicate rows from the result set, not from the table.

It only looks at the columns listed in SELECT.

Core rule (most important)

DISTINCT applies to all columns in the SELECT list together, not individually.

Valid usages
1. DISTINCT on one column
SELECT DISTINCT col1
FROM table;


✔ Allowed even if table has col2, col3, etc.
✔ SQL ignores other columns completely
✔ Result = unique values of col1

2. DISTINCT on multiple columns (combination)
SELECT DISTINCT col1, col2
FROM table;


✔ Removes duplicate pairs (col1, col2)
✔ Both columns together define uniqueness

3. DISTINCT with aggregate functions
SELECT COUNT(DISTINCT col1)
FROM table;


✔ Counts unique values of col1
✔ Very common in interviews

4. DISTINCT inside aggregates
SELECT SUM(DISTINCT salary)
FROM employees;


✔ Removes duplicate salaries before summing

What you CANNOT do
❌ DISTINCT on a single column inside SELECT list
SELECT col1, DISTINCT col2   -- ❌ INVALID SQL
FROM table;


❌ SQL syntax error
❌ DISTINCT cannot be applied to only one column in SELECT

❌ Expect DISTINCT to keep related column values
SELECT DISTINCT product_key
FROM Customer;


❌ You lose customer_id information
✔ Only product_key survives

DISTINCT does not preserve row relationships.

DISTINCT vs GROUP BY (key difference)
DISTINCT	GROUP BY
Removes duplicate rows	Groups rows
No aggregation required	Aggregation required
Simpler	More control
Cannot select extra columns	Can select aggregated columns

Example:

SELECT DISTINCT class
FROM Courses;


vs

SELECT class
FROM Courses
GROUP BY class;


✔ Both valid
✔ GROUP BY preferred when using aggregates or HAVING

Common pitfalls (very important)
Pitfall 1: DISTINCT ≠ unique by one column
SELECT DISTINCT customer_id, product_key


✔ Unique pairs, not unique customers

Pitfall 2: DISTINCT does NOT deduplicate rows partially
SELECT DISTINCT col1, col2


If col2 differs, rows stay.

Pitfall 3: DISTINCT after JOIN can explode rows

JOINs create duplicates → DISTINCT hides them
This can mask logic bugs in interviews.

Pitfall 4: DISTINCT does not control WHICH row is kept

If duplicates differ in other columns, SQL does not guarantee which row survives.

When to use DISTINCT

✔ Remove duplicate rows in final output
✔ Count unique values
✔ Deduplicate after JOIN (carefully)
✔ Simple uniqueness checks

When NOT to use DISTINCT

❌ To pick one row per group
❌ To get “first” or “latest” row
❌ To preserve related column values
❌ As a replacement for correct JOIN logic

Use:

GROUP BY

window functions (ROW_NUMBER)

subqueries / CTEs instead

One-line mental model (remember this)

DISTINCT only sees the columns you SELECT and removes duplicate rows from that result.

# doubt about distinct applied to whole row vs single col
DISTINCT keyword in SELECT = applies to entire row
DISTINCT inside COUNT/SUM/AVG = applies to that column only
❌ ILLEGAL (DISTINCT in SELECT list):

SELECT col1, DISTINCT col2   -- SYNTAX ERROR
FROM table;
Apply Code
This tries to apply DISTINCT as a modifier to individual columns in the SELECT clause.

✅ LEGAL (DISTINCT inside aggregate function):

SELECT 
    movie, 
    COUNT(DISTINCT tickets_sold)   -- ✅ PERFECTLY VALID
FROM table
GROUP BY movie;
Apply Code
Here, DISTINCT is inside COUNT() — it's a parameter to the aggregate function, not a SELECT modifier.

Key difference:

Context	Syntax	Valid?
SELECT clause	SELECT col1, DISTINCT col2	❌ Illegal
Inside aggregate	SELECT COUNT(DISTINCT col2)	✅ Legal
Think of it this way:

DISTINCT as a standalone keyword in SELECT applies to the entire row
DISTINCT inside an aggregate (COUNT, SUM, AVG) only affects that function's calculation
Your example is 100% legal because DISTINCT is inside the COUNT() function, not in the SELECT list itself! ✅


---------------------------------------------------------------
# LC 180 COnsective numbers, WINDOW FUNCITON LAG VS LEAD 

1) What is a “window function”?

A window function is like doing a calculation “next to each row” while looking at other rows too.

Big difference from GROUP BY:

GROUP BY collapses many rows into fewer rows (one row per group).

A window function does not collapse rows. You keep every original row, and you add extra computed columns.

So window functions are not “group by”, they are “group by style logic, but without losing rows”.

2) What window are we talking about in LAG()?

Window functions are defined by the OVER(...) clause:

LAG(num, 1) OVER (PARTITION BY ... ORDER BY ...)


PARTITION BY = splits data into separate groups (separate “mini tables”).

ORDER BY = defines the sequence inside each partition (so “previous” and “next” make sense).

If you don’t write PARTITION BY, it means:

treat the entire table result as one single partition (one big window).

So in your query, the “window” is all rows, not “similar nums”.

You said: “lag inside num is the window so similar number are the window”
That is not correct.

If you did PARTITION BY num, then same numbers would be in the same window. But we did not.

3) Why do we need ORDER BY id if id is already ordered?

Even if id is auto-increment, SQL does not promise rows come out in id order unless you explicitly specify an ORDER BY somewhere.

Table storage order is not guaranteed.

Query output order is not guaranteed.

Window functions need a clear definition of “previous row”, so you must specify the order inside the window.

Also important:

ORDER BY id inside OVER(...) is for the window calculation only.

It does not necessarily sort your final output. (Unless you add ORDER BY at the end of the query.)

4) What exactly does LAG do, step by step?

Take your example:

id:  1  2  3  4  5  6  7
num: 1  1  1  2  1  2  2


Your CTE:

WITH t AS (
  SELECT
    id,
    num,
    LAG(num, 1) OVER (ORDER BY id) AS prev1,
    LAG(num, 2) OVER (ORDER BY id) AS prev2
  FROM Logs
)


Internal mental model (what SQL is doing conceptually):

Build the partition (no PARTITION BY), so it is all rows.

Sort that partition by id (for computing LAG).

For each row:

prev1 = num from 1 row before in that sorted list

prev2 = num from 2 rows before in that sorted list

If there is no previous row, you get NULL.

So t looks like this:

id	num	prev1	prev2
1	1	NULL	NULL
2	1	1	NULL
3	1	1	1
4	2	1	1
5	1	2	1
6	2	1	2
7	2	2	1

Now the filter:

WHERE num = prev1 AND num = prev2


Only row id=3 matches (1 = 1 = 1). That’s how it detects “three in a row”.

Then DISTINCT makes sure you output 1 just once.

5) What is LEAD then?

LAG looks backward (previous rows).

LEAD looks forward (next rows).

Example:

LEAD(num, 1) OVER (ORDER BY id)  -- next row’s num


Same idea, just the other direction.

6) Why we did NOT use PARTITION BY num

Because the problem is about consecutive rows, not “same number anywhere”.

If you did:

LAG(num) OVER (PARTITION BY num ORDER BY id)


then for num=1, it would look at previous “1” even if there was a 2 in between. That would incorrectly treat non-consecutive rows as consecutive.
------------------------------
# LEFT JOIN WITH FIltering in ON condition vs LEFT JOIN + WHERE  LC 1164. Product Price at a Given Date

if you want all values from left table then you filter inside ON clause

IF you do left join after that filter it will act like inner join 

IMP NOTE :If you do a LEFT JOIN and then put a condition on the right table in the WHERE clause, you usually turn it into an INNER JOIN, because rows where the right side is NULL get filtered out.

Example:

FROM A
LEFT JOIN B ON A.id = B.id
WHERE B.flag = 1


This removes all rows where there was no match in B (because B.flag is NULL), so you lose left rows. That’s inner join behavior.

✅ Also correct

If you put that same condition in the ON clause, you keep all rows from the left table, and only restrict which right rows can match:

FROM A
LEFT JOIN B
  ON A.id = B.id AND B.flag = 1

The small detail

Your statement is true when the filter references columns from the right table (the nullable side).

If the WHERE filter references only the left table, it doesn’t change the join type.

Also, you can keep a right-table filter in WHERE and still preserve left rows if you explicitly allow NULLs, like:

WHERE B.flag = 1 OR B.flag IS NULL


So your two lines are correct as the standard rule of thumb.
---------------
# LC 1204. Last Person to Fit in the Bus SUM (col) OVER() VS SUM(col) OVER(...)
SUM(weight) OVER (...) can mean two different things depending on what’s inside OVER.

Case A: SUM(weight) OVER ()

This is the same total for every row (because there’s no order, so the window is the whole table).

Example:

SELECT person_name, weight,
       SUM(weight) OVER () AS total
FROM Queue;


If total weight of everyone is 1875, then every row shows 1875.

Case B: SUM(weight) OVER (ORDER BY turn)

This is a running sum (prefix sum). It changes row by row.

Using your example, first sort by turn:

turn	name	weight
1	Alice	250
2	Alex	350
3	John Cena	400
4	Marie	200
5	Bob	175
6	Winston	500

Now compute:

SUM(weight) OVER (ORDER BY turn) AS total_weight


Result becomes:

turn	name	weight	total_weight
1	Alice	250	250
2	Alex	350	600
3	John Cena	400	1000
4	Marie	200	1200
5	Bob	175	1375
6	Winston	500	1875

So it’s not the same for every row because the ORDER BY turn tells SQL: “for each row, sum everything from the start up to this row (in turn order).”

That’s why the solution works: pick the last row where total_weight <= 1000, which is John Cena.
-------------------------------
# SELF JOIN PRATICE 
LeetCode self-join practice list (best order, easy → hard)
Employee/manager (best for “self join mental model”)

181. Employees Earning More Than Their Managers 
LeetCode

1978. Employees Whose Manager Left the Company (the one you’re doing)

1731. The Number of Employees Which Report to Each Employee 
GitHub
+1

570. Managers with at Least 5 Direct Reports 
Stackademic

“Compare adjacent rows” (self-join alternative to LAG/LEAD)

197. Rising Temperature 
LeetCode

603. Consecutive Available Seats 
GitHub

180. Consecutive Numbers 
LeetCode

Duplicates / cleanup

196. Delete Duplicate Emails 
dwf.dev

(Also do 182. Duplicate Emails as a warmup. It’s usually GROUP BY, but it helps the “duplicate detection” mindset.)

Mixed joins but includes real self-join

1241. Number of Comments per Post 
dwf.dev
+1

1364. Number of Trusted Contacts of a Customer (joins Customers to Customers via email, that’s a real self-join) 
Walkccc
+1

Harder “same table overlaps itself”

1747. Leetflex Banned Accounts (classic interval-overlap self join) 
Leetcode

Optional hard brain-stretcher

569. Median Employee Salary (can be solved with self-join style logic, and it’s tricky)
--------------------------------------------------
# string functions concat, left, right, substring
CONCAT()

Use: join strings together.

Syntax: CONCAT(s1, s2, ...)

Examples:

CONCAT('A','lice') → Alice

CONCAT('Hi',' ','Bob') → Hi Bob

CONCAT('ID=', 7) → ID=7

Important notes:

If any argument is NULL, result becomes NULL:

CONCAT('A', NULL) → NULL

Used in SELECT, WHERE, ORDER BY, JOIN conditions (anywhere an expression is allowed).

UPPER()

Use: convert to uppercase.

Syntax: UPPER(str)

Examples:

UPPER('aLice') → ALICE

UPPER('bob') → BOB

Notes:

Non-letters unchanged (UPPER('a1!') → A1!)

If input is NULL → output NULL.

LOWER()

Use: convert to lowercase.

Syntax: LOWER(str)

Examples:

LOWER('aLice') → alice

LOWER('BOB') → bob

Notes:

If input is NULL → output NULL.

LEFT()

Use: take the first N characters (from the left).

Syntax: LEFT(str, N)

Examples:

LEFT('aLice', 1) → a

LEFT('aLice', 2) → aL

LEFT('aLice', 10) → aLice (if N > length, you get full string)

Notes:

If str is NULL → NULL.

RIGHT()

Use: take the last N characters (from the right).

Syntax: RIGHT(str, N)

Examples:

RIGHT('aLice', 1) → e

RIGHT('aLice', 2) → ce

RIGHT('aLice', 10) → aLice

Notes:

If str is NULL → NULL.

SUBSTRING() / SUBSTR()

Use: take a piece of the string starting at a position.

Syntax:

SUBSTRING(str, start) (from start to end)

SUBSTRING(str, start, len) (take len chars)

Important: indexing starts at 1.

Examples:

SUBSTRING('aLice', 2) → Lice

SUBSTRING('aLice', 2, 2) → Li

SUBSTRING('aLice', 1, 3) → aLi

Notes:

If start is past the end, you get empty string ''.

If str is NULL → NULL.

LENGTH()

Use: number of characters in a string.

Syntax: LENGTH(str)

Examples:

LENGTH('Bob') → 3

LENGTH('') → 0

Notes:

If str is NULL → NULL.

(In MySQL, LENGTH returns bytes; for normal ASCII letters it matches characters. For Unicode multi-byte text, there’s also CHAR_LENGTH.)

TRIM()

Use: remove spaces from the beginning and end.

Syntax:

TRIM(str)

TRIM(BOTH 'x' FROM str) (remove specific char from both ends)

Examples:

TRIM(' Bob ') → Bob

TRIM(' ') → '' (empty string)

TRIM(BOTH '-' FROM '--abc--') → abc

Notes:

TRIM removes from ends only, not the middle:

TRIM('a b') → a b

If str is NULL → NULL.

Where do these “go” in SQL?

They are expressions, so you can use them almost anywhere:

SELECT: format output columns
SELECT UPPER(name) FROM Users;

WHERE: filter ignoring case/spaces
WHERE TRIM(name) = 'Bob'

ORDER BY: sort by transformed value
ORDER BY LOWER(name)

JOIN ON: match on cleaned/standardized keys
ON TRIM(a.email) = TRIM(b.email)

GROUP BY: group by transformed value (careful)
GROUP BY LOWER(city)

-------------------------------------------------------
# STRING PATTERN MATCHING "LIKE" and NOT LIKE LC 1527
These are called string pattern matching operators in SQL. The main one is LIKE (and NOT LIKE). They are different from CONCAT/UPPER/LOWER/LEFT/RIGHT/SUBSTRING which are string transformation/extraction functions. LIKE is mainly for filtering.

LIKE

Meaning: “Does this text match this pattern?”

Where used: mostly in WHERE, also in CASE, JOIN ON, and even SELECT as a boolean flag.

Syntax

WHERE col LIKE 'pattern'

Wildcards in LIKE
% (percent)

Matches any number of characters, including zero characters.

Examples:

Starts with DIAB1
conditions LIKE 'DIAB1%'
Matches: DIAB100, DIAB1, DIAB123 ABC

Ends with son
name LIKE '%son'
Matches: Jackson, Anderson

Contains ice anywhere
name LIKE '%ice%'
Matches: Alice, Spice

_ (underscore)

Matches exactly one character.

Examples:

Exactly 3 characters, starts with A
code LIKE 'A__'
Matches: A12, Abc
Not: A1, A123

DIAB1 plus exactly 2 characters
conditions LIKE 'DIAB1__'
Matches: DIAB100? No (that’s 3 chars after 1). It would match DIAB1AA or DIAB112.

Important LIKE notes

LIKE is not full regex. It only knows % and _ (plus escaping).

NULL behavior: NULL LIKE 'A%' is NULL (treated as false in WHERE).

Case sensitivity: depends on your column collation in MySQL. Many LeetCode tables behave case-insensitive, but not always.

Performance: LIKE 'abc%' can often use an index. LIKE '%abc%' usually cannot (slower) because it must scan.

NOT LIKE

Meaning: “Does not match the pattern.”

Syntax

WHERE col NOT LIKE 'pattern'


Example:

Names that do not start with A
name NOT LIKE 'A%'

Same NULL rule: if col is NULL, col NOT LIKE 'A%' becomes NULL, so it will not pass the WHERE unless you handle it (like col IS NULL OR col NOT LIKE ...).

Escaping % and _ (when you want literal characters)

Sometimes the text itself contains % or _ and you want to match them literally.

MySQL supports ESCAPE:

WHERE col LIKE '%\%%' ESCAPE '\'


This matches strings that contain a literal %.

Similarly for _:

WHERE col LIKE '%\_%' ESCAPE '\'

Why the DIAB1 solution uses two LIKE patterns

Your column conditions has codes separated by spaces. You want a code that starts with DIAB1 and is a separate token.

So it can appear:

at the start: "DIAB100 MYOP" → conditions LIKE 'DIAB1%'

after a space: "ACNE DIAB100" → conditions LIKE '% DIAB1%'

That’s why:

WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%';


This avoids matching something like "XDIAB100" where DIAB1 is not a separate code.

When to use what

Starts with: LIKE 'abc%'

Ends with: LIKE '%abc'

Contains: LIKE '%abc%'

Fixed length patterns: use _ like LIKE 'A__'

Token in a space-separated list: often use patterns with spaces like '% word%' or REGEXP if allowed.

Related tools you’ll see
REGEXP (more powerful than LIKE)

MySQL also has regex matching. Useful for word boundaries.
Example: token begins with DIAB1 at start or after space:

WHERE conditions REGEXP '(^| )DIAB1'


(LeetCode often accepts LIKE solutions, so stick with LIKE unless needed.)

INSTR / LOCATE (find substring position)

INSTR(col, 'abc') returns position (0 if not found)

LOCATE('abc', col) similar

Good when you want “contains” without patterns, but LIKE '%abc%' is more common.

------------------------------------------------------
# 2nd, 3rd ,4th, nTH highest salary LC 176, LC 177 
1) DISTINCT + ORDER BY + LIMIT/OFFSET

This is the simplest and it generalizes perfectly to k-th distinct salary.

For k-th highest distinct salary:

SELECT (
  SELECT DISTINCT salary
  FROM Employee
  ORDER BY salary DESC
  LIMIT 1 OFFSET (k - 1)
) AS KthHighestSalary;


Example for 5th:

SELECT (
  SELECT DISTINCT salary
  FROM Employee
  ORDER BY salary DESC
  LIMIT 1 OFFSET 4
) AS FifthHighestSalary;


Why it’s good:

Very easy to change 2 → 3 → 4 → 5 by changing OFFSET.

Returns NULL automatically if it doesn’t exist (because scalar subquery returns NULL when no row).

Note: LIMIT/OFFSET is MySQL/Postgres friendly. Some DBs use different syntax (SQL Server uses OFFSET ... FETCH).

2) Window function with DENSE_RANK (most “universal interview” way)

This is the cleanest pattern when you want k-th distinct rank and it works across most modern SQL engines.

WITH t AS (
  SELECT
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM Employee
)
SELECT
  MAX(CASE WHEN rnk = k THEN salary END) AS KthHighestSalary
FROM t;


Example for 5th:

WITH t AS (
  SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM Employee
)
SELECT MAX(CASE WHEN rnk = 5 THEN salary END) AS FifthHighestSalary
FROM t;


Why it’s strong:

Handles duplicates correctly (distinct ranking).

Easy to extend to “top k”, ties, etc.

This is the pattern Meta interviewers usually like because it shows window function skill.

3) MAX with “salary < MAX(salary)” trick

This is great for only 2nd highest. It does not scale nicely to 3rd, 4th, 5th without nesting multiple times or writing more complex logic.

So not the best “universal” choice.

What I’d recommend you remember

If you’re on LeetCode MySQL: DISTINCT + LIMIT/OFFSET is quickest.

If you want the most reusable interview pattern: DENSE_RANK.

If you tell me whether you want “k-th highest salary” as a reusable function-style template (like LeetCode 177 does for Nth Highest Salary), I’ll write the exact reusable query for that.

-------------------
# ORDER, OFFSET, LIMIT (THIS IS THE CONCEPUTAL ORDER)
Conceptually, yes:

ORDER BY decides the row order

OFFSET skips the first N rows

LIMIT takes the next K rows

So you can think of it like: “sort, skip, take”.

Can we write OFFSET and LIMIT in either order?

Depends on the database syntax.

PostgreSQL (and many others)

You typically write:

ORDER BY salary DESC
OFFSET 4
LIMIT 1;


Meaning: skip 4 rows, then take 1.

MySQL

You can write either style:

Style A (LIMIT with offset):

ORDER BY salary DESC
LIMIT 4, 1;


This means: skip 4, take 1.

Style B (LIMIT then OFFSET):

ORDER BY salary DESC
LIMIT 1 OFFSET 4;


Same meaning.

Important note

If you don’t have ORDER BY, then LIMIT/OFFSET is not reliable because the “row order” is not guaranteed.

-------------
# GROUP_CONCAT LC 1484. Group Sold Products By The Date
GROUP_CONCAT() is an aggregate function just like COUNT/SUM/MIN/MAX, so it’s normally used with GROUP BY to produce one output string per group.

It takes all the values in that group (for that column) and joins them into one string.

It supports:

DISTINCT to remove duplicates

ORDER BY inside to sort the values before joining

SEPARATOR to choose what goes between items (comma, pipe, etc.)

Example (your problem):

GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',')


Two small extra notes:

You can use GROUP_CONCAT() without GROUP BY too, then it concatenates values for the whole table into one row.

If a group has no values, it returns NULL, and for very large groups it can truncate based on MySQL’s group_concat_max_len setting.

-----------------------------
# LIKE vs REGEXP
Regex means “regular expression”, a pattern language to match text. In SQL interviews, it is used mainly to validate strings (emails, phone, codes) or find tokens inside a messy text column.

In MySQL you’ll see it as:

col REGEXP 'pattern' (same as RLIKE)

and in MySQL 8+: REGEXP_LIKE, REGEXP_REPLACE, REGEXP_SUBSTR, REGEXP_INSTR

LIKE vs REGEXP

LIKE is simpler:

% = any length

_ = exactly one char

good for “starts with”, “contains”, “ends with”

REGEXP is stronger:

character sets, rules, exact counts, anchors, groups, alternation

good for validation like your email problem

The core regex pieces you must know
1) Anchors

These control where the match must happen.

^ start of string

$ end of string

Examples:

'^abc' matches strings starting with abc

'abc$' matches strings ending with abc

'^abc$' matches exactly abc and nothing else

Why this matters in SQL: REGEXP by default can match anywhere inside the string. Anchors force full validation.

2) Character classes

These match “one character from a set”.

[A-Za-z] any letter

[0-9] digit

[A-Za-z0-9] letter or digit

[._-] dot, underscore, dash (inside [] dot is literal)

Negation:

[^0-9] any character that is NOT a digit

Examples:

'^[A-Za-z]' first character must be a letter

'^[0-9]+$' string must be all digits

3) Quantifiers (how many times)

These apply to the thing right before them.

* = 0 or more

+ = 1 or more

? = 0 or 1

{n} = exactly n times

{n,} = at least n times

{n,m} = between n and m times

Examples:

'a*' matches '', a, aa, aaa…

'a+' matches a, aa… but not empty

'^[0-9]{5}$' exactly 5 digits (ZIP code style)

4) Dot and escaping

. means “any single character” (not a literal dot)
So if you want a literal dot, you must escape it:

\. means “actual dot character”

In SQL strings you often need to double escape:

In many MySQL contexts: 'leetcode\\.com' to mean leetcode\.com in regex

5) Grouping and OR

( ... ) groups things

| means OR

Examples:

^(cat|dog)$ matches exactly cat or dog

^([A-Za-z]+)[0-9]+$ letters then digits

MySQL regex “functions” you might see

These are useful beyond LeetCode too.

mail REGEXP 'pattern' returns true/false match

REGEXP_LIKE(mail, 'pattern') same idea (MySQL 8+)

REGEXP_SUBSTR(text, 'pattern') returns matched substring

REGEXP_INSTR(text, 'pattern') returns position

REGEXP_REPLACE(text, 'pattern', 'repl') replaces matches

LeetCode usually expects just REGEXP / RLIKE.

Your email problem pattern, explained

Pattern:
^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$

Read it left to right:

^ start

[A-Za-z] first char must be a letter

[A-Za-z0-9._-]* then 0+ allowed chars (letters, digits, dot, underscore, dash)

@leetcode\\.com must end with @leetcode.com (dot escaped)

$ end

So it rejects:

.shapo@leetcode.com because first char is not a letter

quarz#2020@leetcode.com because # not allowed

david69@gmail.com wrong domain

MySQL query:

SELECT user_id, name, mail
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$';

Interview patterns to memorize
1) Starts with letter

^[A-Za-z]

2) Only letters and digits

^[A-Za-z0-9]+$

3) Exactly k digits

^[0-9]{k}$ (example k=5: ^[0-9]{5}$)

4) Contains a token at start or after space

For DIAB1 idea:

(^| )DIAB1 means DIAB1 either at string start or after a space
(Works when regex engine supports it)

5) One of multiple allowed suffixes

\\.(com|org|net)$ (dot escaped)

Common mistakes

Forgetting ^ and $, then you accidentally match a substring.

Forgetting to escape . so it matches any character.

Using * when you needed + (allows empty).

Forgetting SQL escaping for backslashes (like \\.).

Assuming case sensitivity. In MySQL it depends on collation.

-----------------------------------
# 1412. Find the Quiet Students in All Exams
Yes, NOT IN is the risky one when the subquery might contain NULL. Because of SQL’s 3-valued logic, a single NULL in the list can make the whole predicate become “unknown”, and then your WHERE filters everything out.

Why NOT IN can break

If the subquery returns: (11, NULL)

Then:

5 NOT IN (11, NULL) is UNKNOWN, not TRUE

and WHERE UNKNOWN behaves like FALSE, so the row is removed

That’s why people say NOT IN + possible NULLs = danger.

Is IN also risky?

Less risky. IN with a NULL usually only becomes UNKNOWN when there’s no match, which acts like FALSE in WHERE. So it doesn’t create the “filter out everything” disaster the way NOT IN does.

Can you just always use EXISTS / NOT EXISTS?

You can do that for subqueries, and it’s a good default in interviews because it avoids the NULL landmine.

Use EXISTS when you mean “there is at least one related row”

Use NOT EXISTS when you mean “there is no related row”

They behave well even if the inner table has NULLs.

When IN/NOT IN is totally fine

If the subquery column is guaranteed NOT NULL (primary key, or declared NOT NULL), then NOT IN is safe.

Example: if manager_id is NOT NULL in the subquery result, then:

WHERE x NOT IN (SELECT manager_id FROM ...)


is safe.

If you still want NOT IN, the safe fix

Filter NULLs inside the subquery:

WHERE x NOT IN (
  SELECT y
  FROM t
  WHERE y IS NOT NULL
)

Interview guidance

For “exclude matches” problems: prefer NOT EXISTS

For “membership in a small list of literals”: IN (1,2,3) is fine

For “membership from a subquery”: IN is fine, NOT IN only if you’re sure no NULLs

If you show me the exact pattern you’re using (like student_id NOT IN (...)), I’ll tell you whether NULL is possible there and what the safest version is.

-----------------------------------
# Inner JOIN vs CROSSJOIN LC 613. Shortest Distance in a Line
# 1️⃣ JOIN Without Filter ≠ CROSS JOIN (Syntax Error)

-- ❌ This is a SYNTAX ERROR in most SQL databases
FROM Point p1
JOIN Point p2

-- ✅ For Cartesian product, you must explicitly use:
FROM Point p1
CROSS JOIN Point p2
Apply Code
Why? JOIN requires an ON condition. Without it, most databases throw an error.

2️⃣ JOIN with ON = INNER JOIN (By Default)
-- These are EXACTLY the same:

FROM Point p1
JOIN Point p2 ON p1.x < p2.x

FROM Point p1
INNER JOIN Point p2 ON p1.x < p2.x
Apply Code
JOIN = INNER JOIN (the word INNER is optional!)

3️⃣ CROSS JOIN + WHERE = JOIN with ON
These produce the same result:

Option A: CROSS JOIN + WHERE
FROM Point p1
CROSS JOIN Point p2
WHERE p1.x < p2.x
Apply Code
Option B: JOIN with ON
FROM Point p1
JOIN Point p2
    ON p1.x < p2.x
Apply Code
Both are functionally equivalent!

Visual Explanation:
CROSS JOIN (No Filter):
FROM Point p1
CROSS JOIN Point p2

Result: ALL combinations
p1.x | p2.x
 -1  | -1
 -1  |  0
 -1  |  2
  0  | -1
  0  |  0
  0  |  2
  2  | -1
  2  |  0
  2  |  2
Total: 9 rows (3 × 3)
CROSS JOIN + WHERE:
FROM Point p1
CROSS JOIN Point p2
WHERE p1.x < p2.x

Step 1: Create 9 rows (like above)
Step 2: Filter with WHERE
Result:
p1.x | p2.x
 -1  |  0   ✅
 -1  |  2   ✅
  0  |  2   ✅
Total: 3 rows
JOIN with ON (Same Result!):
FROM Point p1
JOIN Point p2
    ON p1.x < p2.x

Directly produces:
p1.x | p2.x
 -1  |  0   ✅
 -1  |  2   ✅
  0  |  2   ✅
Total: 3 rows
Summary:
Syntax	Meaning	Filter Applied
CROSS JOIN	All combinations	None (Cartesian product)
CROSS JOIN ... WHERE	All combinations → filter	After join
JOIN ... ON	INNER JOIN with condition	During join
INNER JOIN ... ON	Same as above (explicit)	During join
Key Takeaway:
✅ JOIN (without LEFT/RIGHT/FULL) = INNER JOIN
✅ JOIN ON condition ≈ CROSS JOIN WHERE condition (same result, slightly different execution)
❌ JOIN without ON = Syntax Error (not the same as CROSS JOIN)

Does this clear it up? 🎯





3Puic29G9Y

i am atalking functionally not code wise if we do join wihtout condition means its cross join


Leet
Thought for 4s







Yes, you're absolutely correct! 🎯

Functionally (Logical Behavior):
✅ JOIN without condition = CROSS JOIN
Functionally, if you could do a JOIN without any filtering:

It produces all combinations (Cartesian product)
This is exactly what CROSS JOIN does
Point p1 × Point p2 (all combinations)
↓
p1.x | p2.x
 -1  | -1
 -1  |  0
 -1  |  2
  0  | -1
  0  |  0
  0  |  2
  2  | -1
  2  |  0
  2  |  2
✅ JOIN with condition = INNER JOIN with filtering
When you add ON p1.x < p2.x:

Takes all combinations (Cartesian product)
Filters to keep only matching rows
This is INNER JOIN behavior
All combinations (9 rows)
    ↓ (filter: p1.x < p2.x)
p1.x | p2.x
 -1  |  0   ✅
 -1  |  2   ✅
  0  |  2   ✅
(3 rows)
Your Understanding is 100% Correct:
Functionally:

JOIN without filter → produces all combinations → behaves like CROSS JOIN
JOIN with filter → produces filtered combinations → behaves like INNER JOIN
The only difference:

SQL syntax requires you to write CROSS JOIN explicitly for the first case
You can't just write JOIN alone (it's a syntax error)
In Summary:
What You Said	Functionally Correct?
"JOIN without filter acts as CROSS JOIN"	✅ YES (conceptually)
"JOIN with filter acts as INNER JOIN"	✅ YES (that's exactly what it is!)

-----------------
# Schemas, Fact Tables, and Dimension Tables — Interview Notes

### What is a schema?

The structure of how tables are organized and connected in a data warehouse.

---

## Star Schema

* One main **fact table** in the center.
* Multiple **dimension tables**, each connected only to the fact table.
* Dimensions are **not normalized**.
* Simple, fast, and BI-friendly.

**Keys in star schema**

* Fact table: contains **foreign keys** to all dimensions, plus measures.
* Dimension tables: each has **one primary key** (surrogate key), no foreign keys.

---

## Snowflake Schema

* Extension of star schema.
* **Dimension tables are normalized** into multiple related tables.
* Reduces redundancy, but requires more joins.

**Keys**

* Dimension tables can have **foreign keys** to other dimension tables.

---

## Galaxy Schema (Fact Constellation)

* **Multiple fact tables**.
* Shared dimension tables across those facts.
* Used when modeling several business processes together.

---

## Fact Tables

Store **measurable data**.

Examples: revenue, quantity, clicks, orders.

Characteristics:

* Very large.
* Contain **foreign keys** to dimension tables.
* Contain **measures**.
* Logical primary key is often a **combination of foreign keys**.

Answer questions like:

* How much?
* How many?
* How often?

---

## Dimension Tables

Store **descriptive context**.

Examples: product details, customers, stores, calendar dates.

Characteristics:

* Each has a **primary key** (surrogate key).
* Contains descriptive attributes people use to filter, group, and report.
* In star schema, they normally **do not have foreign keys**.

Answer questions like:

* Who?
* What?
* Where?
* When?

---

## Quick identification rule

* Stores numbers to analyze → **Fact table**
* Describes something → **Dimension table**

---------------------------------------
# self join pratice 
📚 Learning Path
Week 1: Basics
LC 181 (Employees Earning More). ✅
LC 197 (Rising Temperature) ✅
LC 196 (Delete Duplicates) ✅
Week 2: Intermediate
LC 180 (Consecutive Numbers)
LC 570 (Managers with 5 Reports)
LC 1270 (Your Problem!)
Week 3: Advanced
LC 612 (Shortest Distance)
LC 1747 (Interval Overlap)
LC 185 (Top Three Salaries)
Week 4: Expert
LC 601 (Human Traffic)
LC 262 (Trips and Users)
LC 1225 (Contiguous Dates)

# left join mastery 

# LEFT JOIN Deep Dive

## Behavior, pitfalls, and interview patterns

---

## 1. Core idea

A LEFT JOIN keeps **all rows from the table on the left**, and fills the right side with NULL when there is no match.

```sql
A LEFT JOIN B
```

Meaning:

* every row from **A** stays
* rows from **B** only appear when matched
* if no match, columns from **B** become NULL

---

## 2. Example: simple LEFT JOIN

Tables:

**customers**

| id | name |
| -: | ---- |
|  1 | Ana  |
|  2 | Ben  |
|  3 | Cara |

**orders**

| id | customer_id | amount |
| -: | ----------: | -----: |
| 10 |           1 |     50 |
| 11 |           1 |     30 |
| 12 |           2 |     20 |

Query:

```sql
SELECT c.id, c.name, o.amount
FROM customers c
LEFT JOIN orders o
  ON c.id = o.customer_id;
```

Result:

| id | name |                             amount |
| -: | ---- | ---------------------------------: |
|  1 | Ana  |                                 50 |
|  1 | Ana  |                                 30 |
|  2 | Ben  |                                 20 |
|  3 | Cara | NULL   ← no orders, but still kept |

Key takeaway:

> LEFT JOIN preserves the left table. Missing matches become NULL.

---

## 3. Chains of LEFT JOINs

```sql
FROM A
LEFT JOIN B ON ...
LEFT JOIN C ON ...
```

Important idea:

> Every LEFT JOIN preserves **all rows from the result so far**.

So A stays, even if B has no match.
B stays, even if C has no match.

Example:

```sql
FROM directors d
LEFT JOIN movies m ON m.director_id = d.director_id
LEFT JOIN sales s  ON s.movie_id = m.movie_id
```

Outcome:

* All directors remain
* Directors with no movies get NULL movie values
* Directors whose movies have no sales get NULL sales values

This is why we can find:

> directors who never had sales
> by checking `s.sale_id IS NULL`

---

## 4. The dangerous trap: WHERE clause

A LEFT JOIN can secretly turn into an INNER JOIN if you filter the right table incorrectly.

Bad:

```sql
WHERE s.sale_id IS NOT NULL
```

Now rows with NULL disappear.
You just lost the benefit of LEFT JOIN.

Correct when checking absence:

```sql
WHERE s.sale_id IS NULL
```

Rule to remember:

> Conditions on the right table belong in the JOIN clause if you still want left rows preserved.
> Conditions in WHERE remove rows after the join.

---

## 5. LEFT JOIN followed by INNER JOIN

Order matters.

Example:

```sql
FROM directors d
LEFT JOIN movies m ON m.director_id = d.director_id
INNER JOIN sales s ON s.movie_id = m.movie_id
```

Here, the INNER JOIN happens **after** the LEFT JOIN.

What happens?

* Any director whose movies have no sales disappears
* Because INNER JOIN requires matches

Result behaves like:

> show directors who have at least one sale.

Rule:

> Once you INNER JOIN, rows without matches are gone forever.

---

## 6. INNER JOIN followed by LEFT JOIN

Example:

```sql
FROM movies m
INNER JOIN sales s ON s.movie_id = m.movie_id
LEFT JOIN directors d ON d.director_id = m.director_id
```

Now:

* only movies that have sales are kept
* directors who never had sales vanish before the LEFT JOIN even runs

This is a common interview trick.

Rule:

> If you start from the fact table with INNER JOIN,
> you will never see “never purchased” or “never sold” cases.

Always start from the dimension table when the question says:

* never ordered
* never sold
* zero activity
* no transactions

---

## 7. LEFT JOIN checklist for interviews

When you see a question, ask:

1. Am I supposed to keep rows even when there is no match?
   If yes, LEFT JOIN.
2. Am I filtering NULLs the right way?
3. Did I accidentally collapse my LEFT JOIN by using the wrong WHERE clause?
4. Did I start from the right table?
5. Is there any INNER JOIN later that removes rows?

---

## 8. LEFT JOIN plus NULL logic pattern

The classic pattern:

> Find X that has never done Y

Example:

```sql
SELECT d.director_id
FROM directors d
LEFT JOIN movies m ON m.director_id = d.director_id
LEFT JOIN sales s  ON s.movie_id = m.movie_id
WHERE s.sale_id IS NULL;
```

Meaning:

* keep everyone
* detect those with no matching activity

This same pattern works for:

* users with no orders
* products never sold
* customers never logged in
* employees without projects

---

## 9. Alternative pattern: NOT EXISTS

Same logic, sometimes cleaner.

```sql
SELECT d.director_id
FROM directors d
WHERE NOT EXISTS (
    SELECT 1
    FROM movies m
    JOIN sales s ON s.movie_id = m.movie_id
    WHERE m.director_id = d.director_id
);
```

Both are correct.
Use whichever reads clearer in interviews.

---

## 10. Final quick rules

* LEFT JOIN keeps the left side.
* Chains of LEFT JOIN keep everything from the start.
* INNER JOIN anywhere removes rows permanently.
* WHERE on right table can silently break LEFT JOIN logic.
* Use NULL checks to detect “never happened” cases.
* Start from the dimension table for “never” questions.

Memorize this short phrase:

> LEFT JOIN finds missing things,
> INNER JOIN finds matching things.

# window function (IMP)
1. Aggregate Functions (SUM, AVG, COUNT, MIN, MAX)
With ORDER BY → Running/Cumulative
SUM(value) OVER (ORDER BY day)     -- Running sum
AVG(value) OVER (ORDER BY day)     -- Running average
COUNT(*) OVER (ORDER BY day)       -- Running count
MIN(value) OVER (ORDER BY day)     -- Running minimum
MAX(value) OVER (ORDER BY day)     -- Running maximum
Apply Code
Example:

day | value | SUM | AVG | COUNT | MIN | MAX
----|-------|-----|-----|-------|-----|----
1   | 10    | 10  | 10  | 1     | 10  | 10
2   | 20    | 30  | 15  | 2     | 10  | 20
3   | 5     | 35  | 11.7| 3     | 5   | 20
Without ORDER BY → Total (Same for all rows)
SUM(value) OVER ()  -- Total sum for all rows
Apply Code
Example:

day | value | SUM (no ORDER BY)
----|-------|------------------
1   | 10    | 35
2   | 20    | 35
3   | 5     | 35
2. ROW_NUMBER() - Sequential numbering
With ORDER BY → Ordered sequence
ROW_NUMBER() OVER (ORDER BY day)
Apply Code
✅ Assigns unique numbers based on order

Example:

day | value | ROW_NUMBER
----|-------|------------
1   | 10    | 1
2   | 20    | 2
3   | 5     | 3
Without ORDER BY → Random order
ROW_NUMBER() OVER ()
Apply Code
⚠️ Numbers rows but order is unpredictable

3. RANK() & DENSE_RANK() - Ranking with ties
With ORDER BY → Ranks based on values
RANK() OVER (ORDER BY score DESC)
DENSE_RANK() OVER (ORDER BY score DESC)
Apply Code
Example:

score | RANK | DENSE_RANK
------|------|------------
100   | 1    | 1
100   | 1    | 1    ← same rank
95    | 3    | 2    ← RANK skips 2, DENSE_RANK doesn't
90    | 4    | 3
Without ORDER BY → Meaningless (all get rank 1)
RANK() OVER ()  -- ❌ Not useful
Apply Code
4. LAG() & LEAD() - Access previous/next rows
Requires ORDER BY
LAG(value) OVER (ORDER BY day)      -- Previous row value
LAG(value, 2) OVER (ORDER BY day)   -- 2 rows before
LEAD(value) OVER (ORDER BY day)     -- Next row value
LEAD(value, 2) OVER (ORDER BY day)  -- 2 rows after
Apply Code
Example:

day | value | LAG(value) | LEAD(value)
----|-------|------------|------------
1   | 10    | NULL       | 20
2   | 20    | 10         | 5
3   | 5     | 20         | NULL
Without ORDER BY → Random/meaningless
⚠️ Cannot work properly without ORDER BY

5. FIRST_VALUE() & LAST_VALUE()
With ORDER BY → First/last in ordered set
FIRST_VALUE(value) OVER (ORDER BY day)
LAST_VALUE(value) OVER (ORDER BY day 
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
Apply Code
Example:

day | value | FIRST_VALUE | LAST_VALUE
----|-------|-------------|------------
1   | 10    | 10          | 5
2   | 20    | 10          | 5
3   | 5     | 10          | 5
⚠️ Note: LAST_VALUE needs frame specification to work correctly

Quick Summary Table:
Function	Needs ORDER BY?	With ORDER BY	Without ORDER BY
SUM/AVG/COUNT	No	Running total	Total sum
MIN/MAX	No	Running min/max	Overall min/max
ROW_NUMBER	No	Sequential by order	Random order
RANK/DENSE_RANK	Yes	Proper ranking	All rank 1
LAG/LEAD	Yes	Previous/next row	Meaningless
FIRST_VALUE/LAST_VALUE	Yes	First/last in order	Unpredictable
Pattern Recognition:
ORDER BY controls:

Direction → Which rows are included up to current row
Sequence → What "previous" and "next" mean
Range → Default frame is "UNBOUNDED PRECEDING to CURRENT ROW"
PARTITION BY controls:

Grouping → Resets calculation for each group
Example combining both:

SELECT 
    category,
    day,
    value,
    SUM(value) OVER (PARTITION BY category ORDER BY day) as running_sum,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY day) as row_num,
    LAG(value) OVER (PARTITION BY category ORDER BY day) as prev_value
FROM sales;
Apply Code
Practice challenge: Can you write a query that shows each day's value alongside:
# imp
🎯 ULTIMATE SQL PROBLEM-SOLVING CHEAT SHEET
1️⃣ UNDERSTANDING THE SUBJECT (Who/What is the focus?)
Phrase in Problem	Meaning	SQL Pattern
"For each student"	Focus on students	GROUP BY student_id or PARTITION BY student_id
"For each course"	Focus on courses	GROUP BY course_id
"Per department"	Focus on departments	GROUP BY department_id
"All students"	Return every student	Might need LEFT JOIN
Rule: The word after "for each" or "per" tells you what to group by.

2️⃣ WHEN TO USE DIFFERENT JOINS
INNER JOIN vs LEFT JOIN vs RIGHT JOIN
Phrase in Problem	Join Type	Why?
"Find all students even if they have no enrollments"	LEFT JOIN	Keep all from left table (students)
"Show only students who are enrolled"	INNER JOIN	Only matching records
"Include students without courses"	LEFT JOIN	NULL allowed for courses
"List every department, show employees if any"	LEFT JOIN	Keep all departments
"Find employees who have a manager"	INNER JOIN	Must have match
"Find employees including those without managers"	LEFT JOIN	NULL allowed for manager
🔍 JOIN Detection Keywords
INNER JOIN (Only matching records):

"Find students who enrolled"
"Get employees with a manager"
"Show only active users"
"List products that were sold"
LEFT JOIN (Keep all from main table):

"Find all students, show courses if any"
"List every employee, even if no department"
"Include users who haven't posted"
"Show departments whether or not they have employees"
RIGHT JOIN (Rare - usually rewrite as LEFT JOIN):

"Find all courses, show students if enrolled"
→ Better: "Find all students who enrolled in courses" with LEFT JOIN
📝 Join Selection Framework
Ask yourself:

Do I need ALL records from one table?

YES → Use LEFT/RIGHT JOIN (keep that table on LEFT/RIGHT)
NO → Use INNER JOIN
What if there's no match?

Want to keep the row → LEFT/RIGHT JOIN
Want to exclude the row → INNER JOIN
Example:

"Find all students and their grades. Include students who haven't taken any courses."

Main table: Students (we want ALL students)
Secondary table: Enrollments (may not exist)
Answer: Students LEFT JOIN Enrollments
3️⃣ WHEN TO USE GROUP BY
Phrase in Problem	Need GROUP BY?	Aggregate Function
"Total sales per product"	✅ YES	SUM(sales)
"Average grade for each student"	✅ YES	AVG(grade)
"Count how many courses each student took"	✅ YES	COUNT(course_id)
"Highest salary in each department"	✅ YES	MAX(salary)
"Find the student with the highest grade"	❌ NO	Use ORDER BY + LIMIT or window function
"List all students and their grades"	❌ NO	Simple SELECT
Rule: If you see "for each X, find [aggregate]" → GROUP BY X

GROUP BY vs Window Function
Scenario	Use GROUP BY	Use Window Function
"Total sales per product"	✅ GROUP BY product_id	❌
"Show each sale with total for that product"	❌	✅ SUM() OVER (PARTITION BY product_id)
"Top 3 students per class"	❌	✅ ROW_NUMBER() OVER (PARTITION BY class_id)
"Count of orders per customer"	✅ GROUP BY customer_id	❌
Key difference:

GROUP BY → Collapses rows (one result per group)
Window Function → Keeps all rows (adds calculated column)
4️⃣ AGGREGATION KEYWORDS
Phrase	Function	Example
"Total / Sum"	SUM()	Total revenue
"Average / Mean"	AVG()	Average grade
"Count / Number of"	COUNT()	Number of students
"Highest / Maximum"	MAX()	Highest salary
"Lowest / Minimum"	MIN()	Lowest price
"Most recent"	MAX(date) or ORDER BY date DESC LIMIT 1	Latest login
"Oldest"	MIN(date) or ORDER BY date ASC LIMIT 1	First order
5️⃣ FILTERING: WHERE vs HAVING
Use Case	Clause	When?
Filter before grouping	WHERE	On raw column values
Filter after grouping	HAVING	On aggregate results
Examples:

-- Filter students with grade > 80 BEFORE grouping
SELECT student_id, AVG(grade)
FROM Enrollments
WHERE grade > 80  -- ✅ WHERE (raw data)
GROUP BY student_id;

-- Filter students with average > 80 AFTER grouping
SELECT student_id, AVG(grade)
FROM Enrollments
GROUP BY student_id
HAVING AVG(grade) > 80;  -- ✅ HAVING (aggregated result)
Apply Code
Rule: If filtering involves SUM(), AVG(), COUNT() → use HAVING

6️⃣ RANKING & TOP N PROBLEMS
Phrase in Problem	SQL Pattern
"Top 3 salaries per department"	ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) + WHERE rank <= 3
"Highest grade for each student"	ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY grade DESC) + WHERE rank = 1
"Second highest salary"	ORDER BY salary DESC LIMIT 1 OFFSET 1 or DENSE_RANK()
"Nth highest value"	Window function with rank = N
When to use each ranking function:

Function	Ties?	Gaps?	Use When
ROW_NUMBER()	No	No	Need unique rank (1,2,3,4...)
RANK()	Yes	Yes	OK with gaps (1,1,3,4...)
DENSE_RANK()	Yes	No	No gaps (1,1,2,3...)
7️⃣ SUBQUERY vs JOIN vs WINDOW FUNCTION
Scenario	Best Approach	Example
"Students whose grade > class average"	Subquery in WHERE	WHERE grade > (SELECT AVG(grade)...)
"Add average grade alongside each record"	Window Function	AVG(grade) OVER (PARTITION BY class_id)
"Combine data from 2 tables"	JOIN	Students JOIN Enrollments
"Top N per group"	Window Function	ROW_NUMBER() OVER (PARTITION BY...)
8️⃣ COMMON TRICK PATTERNS
Pattern 1: "In case of a tie"
Phrase: "If multiple X have the same Y, choose the one with smallest/largest Z"

Solution: Add secondary sorting

ROW_NUMBER() OVER (
    PARTITION BY student_id 
    ORDER BY grade DESC, course_id ASC  -- Secondary sort
)
Apply Code
Pattern 2: "All X even if no Y"
Phrase: "List all students, even if they haven't enrolled"

Solution: LEFT JOIN

SELECT s.student_id, e.course_id
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id;
Apply Code
Pattern 3: "For each X, find Y"
Phrase: "For each department, find the highest salary"

Solution: GROUP BY or Window Function

-- If only need one row per department
SELECT department_id, MAX(salary)
FROM Employees
GROUP BY department_id;

-- If need all employee rows with department max
SELECT 
    employee_id,
    salary,
    MAX(salary) OVER (PARTITION BY department_id) as dept_max
FROM Employees;
Apply Code
Pattern 4: "X who have/did Y"
Phrase: "Students who enrolled in course 101"

Solution: INNER JOIN or WHERE with subquery

-- Join
SELECT DISTINCT s.*
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.course_id = 101;

-- Subquery
SELECT *
FROM Students
WHERE student_id IN (
    SELECT student_id FROM Enrollments WHERE course_id = 101
);
Apply Code
Pattern 5: "X who never Y"
Phrase: "Students who never enrolled" / "Customers who never ordered"

Solution: LEFT JOIN + IS NULL or NOT EXISTS

-- LEFT JOIN
SELECT s.*
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

-- NOT EXISTS
SELECT *
FROM Students s
WHERE NOT EXISTS (
    SELECT 1 FROM Enrollments e WHERE e.student_id = s.student_id
);
Apply Code
Pattern 6: "Running/Cumulative"
Phrase: "Running total" / "Cumulative sum" / "Up to date"

Solution: Window function with ORDER BY

SUM(value) OVER (ORDER BY date) as running_total
Apply Code
Pattern 7: "Consecutive"
Phrase: "Find N consecutive days" / "Streak of X"

Solution: Use ROW_NUMBER() and date difference

SELECT 
    date,
    ROW_NUMBER() OVER (ORDER BY date) as rn,
    DATE_SUB(date, INTERVAL rn DAY) as group_id
FROM table_name;
-- Consecutive dates will have same group_id
Apply Code
9️⃣ DECISION TREE
Start: Read the problem
    ↓
Is there "for each" or "per"?
    YES → Identify what to GROUP BY or PARTITION BY
    NO → Continue
    ↓
Need ALL records from one table?
    YES → LEFT/RIGHT JOIN
    NO → INNER JOIN
    ↓
Need aggregate (sum/avg/count)?
    YES → Use aggregate function
        ↓
        Filtering aggregate result?
            YES → HAVING
            NO → Continue
    NO → Continue
    ↓
Need top N per group?
    YES → Window function with ranking
    NO → Continue
    ↓
Need to keep all rows but add calculation?
    YES → Window function
    NO → GROUP BY
🔟 COMPLETE EXAMPLE WALKTHROUGH
Problem:

"Find the top 2 highest-paid employees in each department. Include departments even if they have fewer than 2 employees."

Step-by-step breakdown:

Subject: "in each department" → PARTITION BY department_id
Goal: "top 2 highest-paid" → Ranking needed
Constraint: "even if fewer than 2" → Need all departments (LEFT JOIN)
Special: "top 2" → ROW_NUMBER() with filter <= 2
Solution:

SELECT 
    d.department_name,
    e.employee_name,
    e.salary,
    ROW_NUMBER() OVER (
        PARTITION BY d.department_id 
        ORDER BY e.salary DESC
    ) as rank
FROM Departments d
LEFT JOIN Employees e ON d.department_id = e.department_id
WHERE rank <= 2
ORDER BY d.department_name, rank;
Apply Code
📋 QUICK REFERENCE CHECKLIST
Before writing SQL, ask:

 What is the subject? (for each X → GROUP BY or PARTITION BY X)
 Need ALL records from a table? (YES → LEFT JOIN)
 Need aggregation? (sum/avg/count → aggregate function)
 Filtering before or after grouping? (before → WHERE, after → HAVING)
 Need ranking or top N? (YES → window function)
 Tie-breaker needed? (YES → secondary ORDER BY)
 Need running total? (YES → window function with ORDER BY)
🎯 ULTIMATE SQL PROBLEM-SOLVING CHEAT SHEET
1️⃣ UNDERSTANDING THE SUBJECT (Who/What is the focus?)
Phrase in Problem	Meaning	SQL Pattern
"For each student"	Focus on students	GROUP BY student_id or PARTITION BY student_id
"For each course"	Focus on courses	GROUP BY course_id
"Per department"	Focus on departments	GROUP BY department_id
"All students"	Return every student	Might need LEFT JOIN
Rule: The word after "for each" or "per" tells you what to group by.

2️⃣ WHEN TO USE DIFFERENT JOINS
INNER JOIN vs LEFT JOIN vs RIGHT JOIN
Phrase in Problem	Join Type	Why?
"Find all students even if they have no enrollments"	LEFT JOIN	Keep all from left table (students)
"Show only students who are enrolled"	INNER JOIN	Only matching records
"Include students without courses"	LEFT JOIN	NULL allowed for courses
"List every department, show employees if any"	LEFT JOIN	Keep all departments
"Find employees who have a manager"	INNER JOIN	Must have match
"Find employees including those without managers"	LEFT JOIN	NULL allowed for manager
🔍 JOIN Detection Keywords
INNER JOIN (Only matching records):

"Find students who enrolled"
"Get employees with a manager"
"Show only active users"
"List products that were sold"
LEFT JOIN (Keep all from main table):

"Find all students, show courses if any"
"List every employee, even if no department"
"Include users who haven't posted"
"Show departments whether or not they have employees"
RIGHT JOIN (Rare - usually rewrite as LEFT JOIN):

"Find all courses, show students if enrolled"
→ Better: "Find all students who enrolled in courses" with LEFT JOIN
📝 Join Selection Framework
Ask yourself:

Do I need ALL records from one table?

YES → Use LEFT/RIGHT JOIN (keep that table on LEFT/RIGHT)
NO → Use INNER JOIN
What if there's no match?

Want to keep the row → LEFT/RIGHT JOIN
Want to exclude the row → INNER JOIN
Example:

"Find all students and their grades. Include students who haven't taken any courses."

Main table: Students (we want ALL students)
Secondary table: Enrollments (may not exist)
Answer: Students LEFT JOIN Enrollments
3️⃣ WHEN TO USE GROUP BY
Phrase in Problem	Need GROUP BY?	Aggregate Function
"Total sales per product"	✅ YES	SUM(sales)
"Average grade for each student"	✅ YES	AVG(grade)
"Count how many courses each student took"	✅ YES	COUNT(course_id)
"Highest salary in each department"	✅ YES	MAX(salary)
"Find the student with the highest grade"	❌ NO	Use ORDER BY + LIMIT or window function
"List all students and their grades"	❌ NO	Simple SELECT
Rule: If you see "for each X, find [aggregate]" → GROUP BY X

GROUP BY vs Window Function
Scenario	Use GROUP BY	Use Window Function
"Total sales per product"	✅ GROUP BY product_id	❌
"Show each sale with total for that product"	❌	✅ SUM() OVER (PARTITION BY product_id)
"Top 3 students per class"	❌	✅ ROW_NUMBER() OVER (PARTITION BY class_id)
"Count of orders per customer"	✅ GROUP BY customer_id	❌
Key difference:

GROUP BY → Collapses rows (one result per group)
Window Function → Keeps all rows (adds calculated column)
4️⃣ AGGREGATION KEYWORDS
Phrase	Function	Example
"Total / Sum"	SUM()	Total revenue
"Average / Mean"	AVG()	Average grade
"Count / Number of"	COUNT()	Number of students
"Highest / Maximum"	MAX()	Highest salary
"Lowest / Minimum"	MIN()	Lowest price
"Most recent"	MAX(date) or ORDER BY date DESC LIMIT 1	Latest login
"Oldest"	MIN(date) or ORDER BY date ASC LIMIT 1	First order
5️⃣ FILTERING: WHERE vs HAVING
Use Case	Clause	When?
Filter before grouping	WHERE	On raw column values
Filter after grouping	HAVING	On aggregate results
Examples:

-- Filter students with grade > 80 BEFORE grouping
SELECT student_id, AVG(grade)
FROM Enrollments
WHERE grade > 80  -- ✅ WHERE (raw data)
GROUP BY student_id;

-- Filter students with average > 80 AFTER grouping
SELECT student_id, AVG(grade)
FROM Enrollments
GROUP BY student_id
HAVING AVG(grade) > 80;  -- ✅ HAVING (aggregated result)
Apply Code
Rule: If filtering involves SUM(), AVG(), COUNT() → use HAVING

6️⃣ RANKING & TOP N PROBLEMS
Phrase in Problem	SQL Pattern
"Top 3 salaries per department"	ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) + WHERE rank <= 3
"Highest grade for each student"	ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY grade DESC) + WHERE rank = 1
"Second highest salary"	ORDER BY salary DESC LIMIT 1 OFFSET 1 or DENSE_RANK()
"Nth highest value"	Window function with rank = N
When to use each ranking function:

Function	Ties?	Gaps?	Use When
ROW_NUMBER()	No	No	Need unique rank (1,2,3,4...)
RANK()	Yes	Yes	OK with gaps (1,1,3,4...)
DENSE_RANK()	Yes	No	No gaps (1,1,2,3...)
7️⃣ SUBQUERY vs JOIN vs WINDOW FUNCTION
Scenario	Best Approach	Example
"Students whose grade > class average"	Subquery in WHERE	WHERE grade > (SELECT AVG(grade)...)
"Add average grade alongside each record"	Window Function	AVG(grade) OVER (PARTITION BY class_id)
"Combine data from 2 tables"	JOIN	Students JOIN Enrollments
"Top N per group"	Window Function	ROW_NUMBER() OVER (PARTITION BY...)
8️⃣ COMMON TRICK PATTERNS
Pattern 1: "In case of a tie"
Phrase: "If multiple X have the same Y, choose the one with smallest/largest Z"

Solution: Add secondary sorting

ROW_NUMBER() OVER (
    PARTITION BY student_id 
    ORDER BY grade DESC, course_id ASC  -- Secondary sort
)
Apply Code
Pattern 2: "All X even if no Y"
Phrase: "List all students, even if they haven't enrolled"

Solution: LEFT JOIN

SELECT s.student_id, e.course_id
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id;
Apply Code
Pattern 3: "For each X, find Y"
Phrase: "For each department, find the highest salary"

Solution: GROUP BY or Window Function

-- If only need one row per department
SELECT department_id, MAX(salary)
FROM Employees
GROUP BY department_id;

-- If need all employee rows with department max
SELECT 
    employee_id,
    salary,
    MAX(salary) OVER (PARTITION BY department_id) as dept_max
FROM Employees;
Apply Code
Pattern 4: "X who have/did Y"
Phrase: "Students who enrolled in course 101"

Solution: INNER JOIN or WHERE with subquery

-- Join
SELECT DISTINCT s.*
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.course_id = 101;

-- Subquery
SELECT *
FROM Students
WHERE student_id IN (
    SELECT student_id FROM Enrollments WHERE course_id = 101
);
Apply Code
Pattern 5: "X who never Y"
Phrase: "Students who never enrolled" / "Customers who never ordered"

Solution: LEFT JOIN + IS NULL or NOT EXISTS

-- LEFT JOIN
SELECT s.*
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

-- NOT EXISTS
SELECT *
FROM Students s
WHERE NOT EXISTS (
    SELECT 1 FROM Enrollments e WHERE e.student_id = s.student_id
);
Apply Code
Pattern 6: "Running/Cumulative"
Phrase: "Running total" / "Cumulative sum" / "Up to date"

Solution: Window function with ORDER BY

SUM(value) OVER (ORDER BY date) as running_total
Apply Code
Pattern 7: "Consecutive"
Phrase: "Find N consecutive days" / "Streak of X"

Solution: Use ROW_NUMBER() and date difference

SELECT 
    date,
    ROW_NUMBER() OVER (ORDER BY date) as rn,
    DATE_SUB(date, INTERVAL rn DAY) as group_id
FROM table_name;
-- Consecutive dates will have same group_id
Apply Code
9️⃣ DECISION TREE
Start: Read the problem
    ↓
Is there "for each" or "per"?
    YES → Identify what to GROUP BY or PARTITION BY
    NO → Continue
    ↓
Need ALL records from one table?
    YES → LEFT/RIGHT JOIN
    NO → INNER JOIN
    ↓
Need aggregate (sum/avg/count)?
    YES → Use aggregate function
        ↓
        Filtering aggregate result?
            YES → HAVING
            NO → Continue
    NO → Continue
    ↓
Need top N per group?
    YES → Window function with ranking
    NO → Continue
    ↓
Need to keep all rows but add calculation?
    YES → Window function
    NO → GROUP BY
🔟 COMPLETE EXAMPLE WALKTHROUGH
Problem:

"Find the top 2 highest-paid employees in each department. Include departments even if they have fewer than 2 employees."

Step-by-step breakdown:

Subject: "in each department" → PARTITION BY department_id
Goal: "top 2 highest-paid" → Ranking needed
Constraint: "even if fewer than 2" → Need all departments (LEFT JOIN)
Special: "top 2" → ROW_NUMBER() with filter <= 2
Solution:

SELECT 
    d.department_name,
    e.employee_name,
    e.salary,
    ROW_NUMBER() OVER (
        PARTITION BY d.department_id 
        ORDER BY e.salary DESC
    ) as rank
FROM Departments d
LEFT JOIN Employees e ON d.department_id = e.department_id
WHERE rank <= 2
ORDER BY d.department_name, rank;
Apply Code
📋 QUICK REFERENCE CHECKLIST
Before writing SQL, ask:

 What is the subject? (for each X → GROUP BY or PARTITION BY X)
 Need ALL records from a table? (YES → LEFT JOIN)
 Need aggregation? (sum/avg/count → aggregate function)
 Filtering before or after grouping? (before → WHERE, after → HAVING)
 Need ranking or top N? (YES → window function)
 Tie-breaker needed? (YES → secondary ORDER BY)
 Need running total? (YES → window function with ORDER BY)


# manatory sums to solve
1407. Top Travellers
1693. Daily Leads and Partners (meta youtbue pattern)
1747. Leetflex Banned Accounts ( interval de morgan law start1 ≤ end2  AND  start2 ≤ end1 that is )
1607. Sellers With No Sales
1440. Evaluate Boolean Expression
534. Game Play Analysis III ( prefix sum to cal the sum till cur date)
1783. Grand Slam Titles
1212. Team Scores in Football Tournament
586. Customer Placing the Largest Number of Orders
1709. Biggest Window Between Visits
608. Tree Node
607. Sales Person
1890. The Latest Login in 2020 (postgre sql)
1699. Number of Calls Between Two Persons
181. Employees Earning More Than Their Managers (self join)
1264. Page Recommendations(bidirectional freindship
)
# window function With ORDER BY → Cumulative Sum (Row-by-Row)
SUM(value) OVER (ORDER BY day)
Apply Code
✅ Sums from first row to current row (prefix sum)
Without ORDER BY → Total Sum (All Rows)
SUM(value) OVER ()
Apply Code
❌ Sums entire partition/group (same value for all rows)



# COALESCE VS IFNULL VS NULLIF 
COALESCE

What it does: returns the first non-NULL value.

PostgreSQL: ✅ yes
MySQL: ✅ yes

Example:

SELECT COALESCE(NULL, 0);              -- 0
SELECT COALESCE(col, 'NA') FROM t;

IFNULL

What it does: if the first argument is NULL, return the second.

PostgreSQL: ❌ no
MySQL: ✅ yes

Example (MySQL only):

SELECT IFNULL(NULL, 0);                -- 0
SELECT IFNULL(col, 'NA') FROM t;

NULLIF

What it does: if a = b, return NULL, else return a.

PostgreSQL: ✅ yes
MySQL: ✅ yes

Example:

SELECT NULLIF(0, 0);                   -- NULL
SELECT clicks / NULLIF(impressions, 0) FROM t;  -- avoids divide-by-zero

Is it okay to always use COALESCE instead of IFNULL?

Yes, and it’s usually better.

Reasons:

Portable: works in Postgres, MySQL, SQL Server, BigQuery, Snowflake, etc.

More powerful: can take more than 2 arguments:

COALESCE(a, b, c, 0)


So even in MySQL, using COALESCE is totally fine and interview-safe.


# self join and left join with same table confusion 
Reading self-joins with +1 / −1

Pattern

t1 JOIN t2 
ON t2.value = t1.value - 1


Read it like this:

t1 is “current”

t2 is “previous”

Because:

t2 = t1 − 1 → t2 happens before t1.

If it’s dates:

t2.date = t1.date - INTERVAL '1 day'


Means:

“yesterday joins with today.”

Flip it:

t2 = t1 + 1


Now t2 is next, t1 is current.

The LEFT JOIN “anchor rule”

Use LEFT JOIN + NULL when the question sounds like:

“Find rows where something did NOT happen.”

Steps:

Choose the row you always want to keep.
That is your anchor (put it on the LEFT).

Join to the thing that might exist (RIGHT).

Write the condition relative to the left:

right = left ± interval


Filter:

WHERE right.col IS NULL


Meaning:

“We looked for that row. It wasn’t there.”

Examples:

Churn
No login next month
right = left + 1 month

Reactivation
No login previous month
right = left - 1 month

When NOT to use the NULL trick

Do not use NULL logic when the question is:

“compare today vs yesterday”

“higher salary than manager”

“price went up compared to last day”

“find the first login after signup”

Those are comparison problems, not “missing row” problems.

You use:

INNER self join

or window functions (LAG, LEAD)

Example idea:

“Return days hotter than yesterday”

Anchor = today
Join to yesterday
Compare temps
No NULL check needed.

Date helpers to remember

Snap to start of period:

DATE_TRUNC('month', login_date)


Move time:

date + INTERVAL '1 month'
date - INTERVAL '7 days'


Extract parts:

EXTRACT(month FROM login_date)

One-line memory shortcuts

t2 = t1 - 1
t2 is previous, t1 is current.

t2 = t1 + 1
t2 is next, t1 is current.

LEFT JOIN + NULL
Use only when you’re finding something that didn’t happen.




# POSTGRE SQL
PostgreSQL mainly works with these types:

DATE

TIME

TIMESTAMP

TIMESTAMP WITH TIME ZONE (timestamptz)

INTERVAL

1. Getting current date and time
CURRENT_DATE

Returns today’s date (no time).

SELECT CURRENT_DATE;


Output:

2026-01-08


Use when you only care about the date.

CURRENT_TIME

Returns current time with timezone.

SELECT CURRENT_TIME;

CURRENT_TIMESTAMP

Returns current date + time with timezone.

SELECT CURRENT_TIMESTAMP;


Equivalent to:

SELECT now();

now()

Most commonly used.

SELECT now();


Type: timestamptz

Use in logging, session tracking, freshness checks.

2. Creating dates and timestamps
MAKE_DATE(year, month, day)

Creates a real DATE from integers.

SELECT MAKE_DATE(2024, 11, 15);


Output:

2024-11-15


Use when you have separate year, month, day columns.

MAKE_TIMESTAMP(y, m, d, h, min, sec)

Creates a timestamp.

SELECT MAKE_TIMESTAMP(2024, 11, 15, 10, 30, 0);

TO_DATE(text, format)

Converts string → date.

SELECT TO_DATE('2024-11-15', 'YYYY-MM-DD');

TO_TIMESTAMP(text, format)

Converts string → timestamp.

SELECT TO_TIMESTAMP('2024-11-15 10:30', 'YYYY-MM-DD HH24:MI');

3. Formatting dates (very important)
TO_CHAR(date_or_ts, format)

Converts date/timestamp → string.

SELECT TO_CHAR(CURRENT_DATE, 'YYYY-MM');


Output:

2026-01


Common formats:

YYYY → year

MM → month

DD → day

HH24 → hour (24h)

MI → minutes

SS → seconds

Use for reporting, dashboards, grouping labels.

4. Extracting parts of a date
EXTRACT(field FROM date_or_ts)

Returns a number.

SELECT EXTRACT(YEAR FROM CURRENT_DATE);


Other fields:

YEAR

MONTH

DAY

HOUR

MINUTE

SECOND

EPOCH

DATE_PART(field, date)

Same as EXTRACT.

SELECT DATE_PART('month', CURRENT_DATE);

EPOCH (very important)

Seconds since 1970-01-01 UTC.

SELECT EXTRACT(EPOCH FROM now());


Used for:

duration math

performance timing

converting intervals to seconds

5. Truncating dates (grouping by time)
DATE_TRUNC(unit, timestamp)

Cuts smaller parts.

SELECT DATE_TRUNC('month', now());


Examples:

DATE_TRUNC('day', ts)
DATE_TRUNC('month', ts)
DATE_TRUNC('year', ts)


Use when grouping by month, day, year.

6. Date arithmetic
Adding intervals
SELECT CURRENT_DATE + INTERVAL '7 days';
SELECT now() + INTERVAL '2 hours';

Subtracting dates
SELECT CURRENT_DATE - DATE '2026-01-01';


Output:

7


Type: integer (days)

Subtracting timestamps
SELECT end_time - start_time;


Output:

3 days 04:12:10


Type: INTERVAL

7. Working with INTERVAL
Summing intervals
SELECT SUM(end_time - start_time)
FROM sessions;


Returns total interval.

Convert interval → days
SELECT EXTRACT(EPOCH FROM SUM(end_time - start_time)) / 86400
FROM sessions;


Why 86400?

1 day = 24 × 60 × 60 seconds

JUSTIFY_HOURS(interval)

Normalizes hours into days.

SELECT JUSTIFY_HOURS(INTERVAL '30 hours');


Output:

1 day 6 hours


Also:

JUSTIFY_DAYS

JUSTIFY_INTERVAL

Use after aggregations.

8. Comparing dates
WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'

WHERE ts BETWEEN '2026-01-01' AND '2026-01-31'

9. Time zone functions
Convert timezone
SELECT now() AT TIME ZONE 'UTC';

SELECT now() AT TIME ZONE 'America/New_York';

10. Window functions with dates
LEAD / LAG (time gaps)
SELECT
  user_id,
  event_time AS start_time,
  LEAD(event_time) OVER (
    PARTITION BY user_id
    ORDER BY event_time
  ) AS end_time
FROM events;


Used for:

session durations

state changes

uptime tracking

11. Common interview patterns
Find first date per user
SELECT user_id, MIN(order_date)
FROM orders
GROUP BY user_id;

Monthly aggregation
SELECT
  DATE_TRUNC('month', order_date) AS month,
  COUNT(*)
FROM orders
GROUP BY month;

Filter last 7 days
WHERE created_at >= now() - INTERVAL '7 days'

Final mental model (important)

DATE → calendar day

TIMESTAMP → date + time

INTERVAL → duration

EXTRACT / DATE_PART → pull numbers

DATE_TRUNC → group time

TO_CHAR → format output

EPOCH → seconds math

If you want, next I can give you:

a 1-page PostgreSQL date cheat sheet, or

Meta / Google interview date questions with patterns, or

Common date bugs interviewers expect you to catch


The rule you must memorize

If you use LEFT JOIN, any condition on the right table must go in the ON clause, not the WHERE clause.

This is one of the most important SQL rules for interviews.