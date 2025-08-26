# Write your MySQL query statement below
# let me create a covering index for this question name is already pk which is clustered index so it will be automatically included in the non clustered composite idnex of area and population
-- CREATE INDEX 
--     indx_world_area_population
-- ON
--     WORLD (area, population) 
# the above is wrong read notes https://github.com/SrinathBegudem/Daily_coding_pratice/blob/main/SQL/Notes/When_to_use_which_indexing(OR%20vs%20AND).md
# we should use single non cluster indexing for or operator and let sql decide the index merging or you can use union operation write two independ quieres and single index will work with the respective query optimised this unquie give no duplicates and more optimised is unionall + dustinct but requires external taking care of duplicates.
# so create multiple single non clusterin indexing 
-- CREATE INDEX idx_area ON World(area);
-- CREATE INDEX idx_population ON World(population);

SELECT 
    name, population, area
FROM
    World 
WHERE 
    area >= 3000000 
    OR population >= 25000000
#or use union 
-- SELECT name, population, area
-- FROM World
-- WHERE area >= 3000000
-- UNION
-- SELECT name, population, area
-- FROM World
-- WHERE population >= 25000000;