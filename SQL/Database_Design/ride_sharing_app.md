ER Diagram and Schema Design Notes
Ride Sharing App (Uber-like) Step-by-Step, With Intuition
0) Goal of Schema Design

Design tables so that:

data is correct and consistent (integrity)

inserts/updates/deletes are safe

queries you expect are easy and fast

the structure can evolve without breaking everything

1) The Interview Mindset

When they say “Design a database schema for X”, they want to see:

Core business event

Actors

Supporting entities

Relationships + cardinalities

Convert to relational tables (PK/FK)

Handle M:N using bridge tables

Add only essential attributes

(Optional) constraints + indexing + scaling notes

Keep it simple first. Add complexity only if asked.

2) Step 1: Find the Core Business Event

Ask: What is the main thing that happens?

For Ride-sharing:

The central event is Ride

Everything connects to Ride:

User requests a ride

Driver fulfills the ride

Payment is for that ride

Rating is for that ride

Rule of thumb:
Most systems have a central “fact/event” table:

Uber → Ride

Amazon → Order

Banking → Transaction

Instagram → Post

3) Step 2: Identify Actors

Ask: Who participates in that event?

Ride-sharing:

User (rider)

Driver

Actors typically exist independently of events:

User can exist without rides

Driver can exist without rides

So User and Driver are strong entities.

4) Step 3: Identify Supporting Entities

Ask: What objects support the event and exist independently?

Good baseline entities:

User

Driver

Vehicle

Ride

Payment

Rating

Important clarification: Destination/Location

Location is usually NOT a separate entity for basic design.
Instead, store it as attributes in Ride:

pickup_address / dropoff_address

pickup_lat / pickup_lng

drop_lat / drop_lng

Make Location a separate table only if asked about:

advanced GIS, saved places, geofencing, location history at high scale

Important clarification: Tip

Tip is usually part of Payment (attribute) not a standalone entity initially:

tip_amount inside Payment

Make Tip a separate entity only if:

multiple tips, adjustments, splits, audit trail requirements

5) Step 4: Pick Relationships + Cardinality

Now you define how entities relate.

Baseline relationships

User 1 → N Ride
One user can have many rides, each ride has one user.

Driver 1 → N Ride
One driver can complete many rides, each ride has one driver.

Driver 1 → N Vehicle
One driver may have multiple vehicles (or history of vehicles).

Ride 1 → 1 Payment (baseline)
Each ride has one payment record (simple version).

Ride 1 → 1 Rating (baseline)
Each ride can have a rating entry (optional if not rated yet).

6) Step 5: Convert Relationships into Tables (PK/FK)
The key FK intuition

In a 1:N relationship, the foreign key goes on the N side.

Why?
Because one row on the “1 side” cannot store many ids without breaking 1NF (no multi-valued cells).

Example: User → Ride (1:N)

Wrong idea:

Put ride_id in User (User would need a list of ride_ids)

Correct:

Put user_id in Ride (each ride points to its user)

7) Baseline Relational Schema (Interview-Ready)
User

user_id (PK)

name

phone

email

created_at

Driver

driver_id (PK)

name

license_number

phone

status (online/offline)

created_at

Vehicle

vehicle_id (PK)

driver_id (FK → Driver.driver_id) ✅ (because Driver 1 → N Vehicle)

plate_number (unique)

model

color

Ride ✅ central table

ride_id (PK)

user_id (FK → User.user_id) ✅ (User 1 → N Ride)

driver_id (FK → Driver.driver_id) ✅ (Driver 1 → N Ride)

pickup_address

dropoff_address

pickup_lat, pickup_lng

drop_lat, drop_lng

requested_at

start_time

end_time

status (requested/accepted/in_progress/completed/cancelled)

fare_amount

Payment

Baseline (simple 1:1):

payment_id (PK)

ride_id (FK → Ride.ride_id) ✅

amount

tip_amount

method (card/cash/wallet)

status (pending/success/failed/refunded)

paid_at

Rating

rating_id (PK)

ride_id (FK → Ride.ride_id)

rater_user_id (FK → User.user_id) (who gave rating)

rated_driver_id (FK → Driver.driver_id) (who received rating)

stars (1–5)

comment

created_at

8) When Do We Need a Separate Table?
Rule 1: M:N relationship → bridge table

If both sides can have many of each other, you cannot store FK in just one table.

Example: Student ↔ Course is M:N

One student takes many courses

One course has many students

So create:

Enrollment (Bridge table)

student_id (FK → Student)

course_id (FK → Course)

PRIMARY KEY (student_id, course_id) ✅ composite PK prevents duplicates

Each row means:

“This student enrolled in this course.”

9) Why Repeating FK Values is OK

You noticed: in Orders / Rides, customer_id repeats many times.

That’s expected and correct.

Bad redundancy is repeating large descriptive fields:

name, phone, address repeated in many rows

Good design is repeating small references:

ids (FKs) repeated to link tables

This is what normalization aims for.

10) Upgrade Scenarios (Common Interview Follow-ups)
A) Multiple payment attempts per ride

If payment can be retried (failed → retry), then:
Ride → Payment becomes 1:N

So FK stays on the many side (Payment):

Payment:

payment_id (PK)

ride_id (FK)

status, attempt_number, etc.

Ride does NOT store payment_id list.

B) Shared vehicles (many drivers share one vehicle)

If:

a driver can drive many vehicles

a vehicle can be driven by many drivers

Then Driver ↔ Vehicle becomes M:N
So create bridge:

DriverVehicle

driver_id (FK)

vehicle_id (FK)

start_time, end_time (optional history)

PRIMARY KEY (driver_id, vehicle_id, start_time) (if tracking history)

C) Driver rates User also

Option 1 (clean): single Ratings table with columns:

rater_type (user/driver)

rated_type (user/driver)

rater_id

rated_id

ride_id
This is flexible but needs constraints.

Option 2 (simpler in interviews): two tables

UserRatesDriver

DriverRatesUser
Very clear but duplicates structure.

11) Normalization Notes (What to Say Out Loud)

Normalize OLTP schemas to reduce duplication and update anomalies.

Use FK references to avoid repeating descriptive data.

Denormalize later only when performance demands it and data is mostly read-heavy (OLAP).

12) Quick PK/FK Decision Rules (Memorize This)
1:1

Put FK on the dependent entity
Example:
User → UserProfile
Profile depends on User → FK in UserProfile

1:N

Put FK on the N side
Example:
User 1 → N Ride → FK in Ride

M:N

Make a bridge table
Bridge has:

two FKs

usually composite PK

13) Minimal Attributes Strategy (Interview Safe)

Don’t add 30 columns.

Include:

IDs

timestamps

status

money values

essential locations

You can always say:

“Additional fields like coupons, surge pricing, cancellation reasons can be added later.”

14) What To Mention at the End (If Time)

Constraints: PK, FK, NOT NULL, UNIQUE, CHECK(stars between 1 and 5)

Indexes: Ride(user_id), Ride(driver_id), Payment(ride_id), Rating(ride_id)

Partitioning: Ride by date if huge

Audit/log tables: RideStatusLog if needed

Only say these after the base schema is done.

15) Final Interview Script (How to Speak While Designing)

“The core event is Ride.”

“Actors are User and Driver.”

“Supporting entities are Vehicle, Payment, Rating.”

“Relationships: User 1:N Ride, Driver 1:N Ride, Ride 1:1 Payment, Ride 1:1 Rating.”

“Place FKs on the many side, and create bridge tables for M:N.”

“Keep attributes minimal and extend later.”