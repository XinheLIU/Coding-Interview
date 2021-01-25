SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email) > 1
/*
# Write your MySQL query statement below
SELECT Email from 
(
    SELECT Email, Count(Email) as cnt from Person group by Email
) as t
where cnt > 1
*/