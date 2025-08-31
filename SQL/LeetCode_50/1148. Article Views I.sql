# Write your MySQL query statement below

#imp points
-- here we are comapring values from 2 cols so indexing might not be super useful(non sargability). indexing work well when we comapre the col to constnat or rnage (sargability)  more about this in SARGable.md file notes
-- In this sum we can use both group by and distinct and both are okay not much difference most of the time sql optimsers does it thing and figure it out to process both queries efficently but in pratice group by is used when we are using aggregation next if not use distinct.

SELECT 
    DISTINCT author_id as id
FROM 
    Views
WHERE 
    author_id = viewer_id
-- GROUP BY
--     id
ORDER BY
    id

