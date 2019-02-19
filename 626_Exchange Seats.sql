# Write your MySQL query statement below
SELECT * FROM
(SELECT id-1 AS id, student FROM seat
 WHERE id%2=0
 UNION
 SELECT id+1 AS id, student FROM seat
 WHERE id%2=1 AND id<(SELECT COUNT(id) FROM seat)
 UNION
 SELECT id AS id, student FROM seat
 WHERE id%2=1 AND id=(SELECT COUNT(id) FROM seat)
 ) AS new_seat
 ORDER BY id