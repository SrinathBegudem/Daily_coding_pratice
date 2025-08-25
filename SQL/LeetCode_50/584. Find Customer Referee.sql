# Write your MySQL query statement below\
# In production i will create an index first
-- CREATE INDEX
--     indx_customer_referee 
-- ON  
--     Customer (referee_id);

SELECT 
    name
FROM 
    Customer
where 
    referee_id != 2 OR referee_id IS NULL;


