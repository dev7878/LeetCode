# Write your MySQL query statement below
-- select e1.name from Employee e1
-- join Employee e2 on e1.managerId
-- group By e1.managerId 
-- having count(*) >=5;

SELECT e1.name from Employee e1 
join Employee e2 on e2.managerId = e1.id 
GROUP BY e2.managerId
HAVING COUNT(*) >= 5
