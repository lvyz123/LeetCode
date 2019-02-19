# Write your MySQL query statement below
SELECT w1.Id FROM Weather as w1, Weather as w2
WHERE w1.Temperature>w2.Temperature AND DATEDIFF(w1.RecordDate,w2.RecordDate)=1