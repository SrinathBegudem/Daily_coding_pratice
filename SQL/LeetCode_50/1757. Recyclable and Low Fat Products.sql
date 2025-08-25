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

# Optimised sol
-- How this works in MySQL InnoDB?
-- InnoDB has a special rule:

-- Every secondary index automatically stores the PRIMARY KEY (clustered key) at the leaf nodes.

-- In our case: product_id is the PK.

-- If you create:
-- CREATE INDEX idx_products_flags
-- ON Products (low_fats, recyclable);
-- At the leaf level, InnoDB actually stores:
-- (low_fats, recyclable, product_id)
-- because the PK (product_id) is appended automatically.

-- So for the query:

-- SELECT product_id 
-- FROM Products
-- WHERE low_fats='Y' AND recyclable='Y';
-- The index alone has everything it needs (low_fats, recyclable for filtering; product_id for output).

-- This is effectively a covering index for that query, even though you didn’t explicitly include product_id.
-- Why does InnoDB do this?
-- Because InnoDB’s clustered index = the table itself.

-- Secondary indexes need a way to find the full row → they store the PK at the leaf.

-- That side effect means many queries automatically become “index-only” when you select the PK.

-- Interview-soundbite answer:

-- In InnoDB, a secondary index on (low_fats, recyclable) is a covering index for this query because the primary key product_id is automatically stored in every secondary index leaf. In Postgres, however, you’d need to explicitly add product_id to the index to make it covering.

#indexing sol below (covering)
-- CREATE INDEX 
--     indx_all_cols_covering
-- ON
--     Products (low_fats, recyclable)

-- SELECT 
--     product_id 
-- FROM 
--     Products
-- where 
--     low_fats = 'Y' 
--     AND recyclable = 'Y'




