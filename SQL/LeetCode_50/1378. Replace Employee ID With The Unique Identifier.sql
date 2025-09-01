# Write your MySQL query statement below
-- we can slove this using left join because question clearly says if unquie_id not there then replace it with null that means include all the rows from table1(lefttable) - Employees

-- SELECT 
--      eu.unique_id as unique_id,e.name as name
-- FROM 
--     Employees AS e
-- LEFT JOIN 
--     EmployeeUNI AS eu
-- ON 
--     e.id = eu.id

#optimzation talks 
-- so employees(id) is already idnex(pk)and indexing both col in emplUNi would help join operation (covering index) 
# slighter cleaner version (with using)
SELECT 
     eu.unique_id as unique_id,e.name as name
FROM 
    Employees AS e
LEFT JOIN 
    EmployeeUNI AS eu
USING (id)