"
Medium Problem

Description

Table: Signups

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
user_id is the column of unique values for this table.
Each row contains information about the signup time for the user with ID user_id.
 

Table: Confirmations

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
| action         | ENUM     |
+----------------+----------+
(user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
user_id is a foreign key (reference column) to the Signups table.
action is an ENUM (category) of the type ('confirmed', 'timeout')
Each row of this table indicates that the user with ID user_id requested a confirmation message at time_stamp and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').
 

The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

Write a solution to find the confirmation rate of each user.

Return the result table in any order.
"

# Successful Solution - 1055ms

select S.user_id, IFNULL(ROUND(COUNT(CASE WHEN C.action='confirmed' THEN 1 END)/ COUNT(C.user_id), 2), 0) as confirmation_rate
from Signups S
left join Confirmations C
on S.user_id = C.user_id
group by S.user_id
order by confirmation_rate asc;


# More Efficient Solution - 550ms

SELECT s.user_id, 
    CASE WHEN c.user_id IS NULL THEN 0.00 
        ELSE ROUND(SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(*),2) END 
        AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON c.user_id = s.user_id
GROUP BY s.user_id;
