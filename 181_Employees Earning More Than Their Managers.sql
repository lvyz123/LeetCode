# Write your MySQL query statement below
SELECT a.Name AS Employee FROM Employee as a
LEFT JOIN Employee as b ON a.ManagerId=b.Id
WHERE a.Salary>b.Salary