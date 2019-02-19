# Write your MySQL query statement below
SELECT p.FirstName, p.LastName, q.City, q.State
FROM Person as p
LEFT JOIN Address as q ON p.PersonId=q.PersonId; 