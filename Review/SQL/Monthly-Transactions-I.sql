"
Medium Problem

Description

Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
 

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order.

The query result format is in the following example.

 
"


# Successful Solution - 1267ms

select DATE_FORMAT(trans_date, '%Y-%m') as month, country, count(*) as trans_count, count(CASE WHEN state = 'approved' THEN 1 END) as approved_count, COALESCE(SUM(amount), 0) as trans_total_amount, COALESCE(SUM(CASE WHEN state = 'approved' THEN amount END), 0) as approved_total_amount
from Transactions
group by month, country;

# More Efficient Solution - 467ms
SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    COUNT(IF(state = 'approved', 1, NULL)) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM
    Transactions
GROUP BY
    month,
    country


"
NOTES:
  - EXTRACT(col_name, format) => EXTRACT(trans_date, '%Y-%m') => '2018-01'
  - MONTH(col_name) => returns the month => 1
  - YEAR(col_name)
  etc
"