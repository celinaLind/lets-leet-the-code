"
Easy Problem

Description:

Table: Prices

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
(product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the price of the product_id in the period from start_date to end_date.
For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.
 

Table: UnitsSold

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
This table may contain duplicate rows.
Each row of this table indicates the date, units, and product_id of each product sold. 
 

Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places. If a product does not have any sold units, its average selling price is assumed to be 0.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Prices table:
+------------+------------+------------+--------+
| product_id | start_date | end_date   | price  |
+------------+------------+------------+--------+
| 1          | 2019-02-17 | 2019-02-28 | 5      |
| 1          | 2019-03-01 | 2019-03-22 | 20     |
| 2          | 2019-02-01 | 2019-02-20 | 15     |
| 2          | 2019-02-21 | 2019-03-31 | 30     |
+------------+------------+------------+--------+
UnitsSold table:
+------------+---------------+-------+
| product_id | purchase_date | units |
+------------+---------------+-------+
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |
+------------+---------------+-------+
Output: 
+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1          | 6.96          |
| 2          | 16.96         |
+------------+---------------+
Explanation: 
Average selling price = Total Price of Product / Number of products sold.
Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96
"

# UnSuccessful 
# Did not take into account when no units were sold for any product ID

select P.product_id, SUM(P.price*U.units)/SUM(U.units) as average_price
from Prices P
inner join UnitsSold U
on P.product_id = U.product_id
where P.start_date <= U.purchase_date <= P.end_date
group by P.product_id
order by average_price;

# Successful V2 - 1255ms

select P.product_id, IFNULL(ROUND(SUM(P.price*U.units)/SUM(U.units), 2), 0) as average_price
from Prices P
left join UnitsSold U
on P.product_id = U.product_id
and U.purchase_date between P.start_date and P.end_date
group by P.product_id
order by average_price;

# More Efficient Solution - 614ms

select p.product_id ,ROUND(COALESCE(SUM(u.units * p.price), 0)  / COALESCE(SUM(u.units), 1), 2) AS average_price
from Prices p 
left join UnitsSold u on 
p.product_id = u.product_id
AND u.purchase_date BETWEEN p.start_date AND p.end_date
group by p.product_id 

"
NOTES:

  - COALESCE() => returns the first NON-null value
  for the above example if the sum of the units or total units sold were null then the fcn returns a zero to use for the function

"