Database Design – Complete Master Notes
Transactional Modeling vs Analytical Modeling
1️⃣ Two Major Database Workloads

There are two primary database workloads in real systems:

Transactional Workloads (OLTP)

Analytical Workloads (OLAP)

These lead to two major modeling approaches:

Transactional Modeling

Analytical Modeling

These are different design philosophies because they solve different problems.

2️⃣ Transactional Modeling

(OLTP – Online Transaction Processing)

Also Called:

OLTP design

Operational database modeling

Production database modeling

Backend database design

Entity-Relationship (ER) modeling

What It Is

This is the live backend production database.

It runs your application in real time.

Examples:

Uber ride booking system

Amazon order placement system

Banking transaction system

Instagram post/comment system

Payment processing system

This is the database your app directly connects to.

Purpose

Run day-to-day business operations.

Focus on:

Correctness

Data integrity

Fast inserts and updates

High concurrency

ACID guarantees

Characteristics

Many small transactions

Row-level lookups

Millisecond response time

Data constantly changing

Strict consistency

Schema Design Style

Highly normalized (usually 3NF)

ER modeling

Strong PK/FK relationships

Referential integrity

Avoid redundancy

Small focused tables

Modeling Approach

Steps:

Identify core entities

Define primary keys

Define relationships

Place foreign keys

Normalize

Example (Ride Sharing – Production OLTP)

Entities:

User

Driver

Vehicle

Ride

Payment

Rating

Ride table:

ride_id (PK)

user_id (FK)

driver_id (FK)

start_time

end_time

fare

status

This is transactional modeling.

3️⃣ Analytical Modeling

(OLAP – Online Analytical Processing)

Also Called:

OLAP design

Dimensional modeling

Data warehouse modeling

BI modeling

Reporting schema design

What It Is

This is used for:

Business intelligence

Dashboards

Reporting

Data science

Historical trend analysis

This database is separate from production.

Purpose

Analyze the business.

Focus on:

Aggregations

Trends

Historical analysis

Large data scans

Characteristics

Read-heavy

Large datasets

Aggregation queries (SUM, COUNT, AVG)

Historical data

Seconds/minutes latency acceptable

Schema Design Style

Denormalized

Fact tables

Dimension tables

Star schema

Snowflake schema

Modeling Approach

Steps:

Define fact table (core measurable event)

Define dimensions (context tables)

Choose grain carefully

Handle SCD (slowly changing dimensions)

Example (Ride Analytics – OLAP Warehouse)

Fact_Ride:

ride_id

driver_id

user_id

date_id

fare_amount

distance

Driver_Dim:

driver_id

city

rating_bucket

Date_Dim:

date_id

month

quarter

year

This is stored in:

Snowflake

Redshift

BigQuery

Databricks

This is analytical modeling.

4️⃣ Data Warehouse

A data warehouse:

Stores structured historical data

Optimized for analytical queries

Uses dimensional modeling

Separate from production system

Typical architecture:

Backend Production DB (OLTP)
→ ETL / Streaming pipeline
→ Data Warehouse (OLAP)
→ BI / Analytics tools

Example:

PostgreSQL
→ Spark / Airflow
→ Snowflake
→ Tableau

5️⃣ Why They Are Separate

OLTP database:

Busy handling live users

Cannot afford heavy aggregation queries

Designed for correctness

OLAP database:

Optimized for scanning billions of rows

Designed for aggregation

Can tolerate slower queries

Different workload → different schema design.

6️⃣ Clean Comparison Table
Feature	Transactional Modeling	Analytical Modeling
Workload	OLTP	OLAP
Alternative Name	Operational DB	Data Warehouse
Environment	Backend production	Analytics system
Goal	Run business	Analyze business
Data	Current/live	Historical
Design Style	Normalized	Denormalized
Modeling Type	ER Modeling	Dimensional Modeling
Schema Pattern	3NF	Star / Snowflake
Focus	Writes + integrity	Reads + aggregation
7️⃣ Interview Strategy

If interviewer asks:

“Design database for Uber backend.”

→ Transactional modeling
→ Normalized ER schema
→ PK/FK

If interviewer asks:

“Design warehouse for Uber analytics.”

→ Analytical modeling
→ Star schema
→ Fact + dimension

8️⃣ Final Mental Model

Transactional modeling = Production backend database design.
Analytical modeling = Data warehouse design for insights.

Both are essential.
They serve different workloads.

Now this version contains:

OLTP

OLAP

Transactional modeling

Analytical modeling

Operational DB

Production DB

Data warehouse

ER modeling

Dimensional modeling

Star schema

Snowflake schema

Everything in one place.