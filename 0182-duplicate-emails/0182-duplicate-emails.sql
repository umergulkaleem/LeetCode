# Write your MySQL query statement below
SELECT email
FROM person
GROUP BY email
having COUNT(*)>1;