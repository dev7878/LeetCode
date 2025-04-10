# Write your MySQL query statement below
SELECT c.id, c.movie, c.description, c.rating from Cinema as c
WHERE id % 2 = 1 AND c.description != 'boring'
ORDER BY c.rating DESC;

