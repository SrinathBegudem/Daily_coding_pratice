# Write your MySQL query statement below
# Basic sol
# Time complexity = O(N) scan of table (N = No of rows) and space = O(1)
SELECT 
    product_id 
FROM 
    Products
where 
    low_fats = 'Y' 
    AND recyclable = 'Y'