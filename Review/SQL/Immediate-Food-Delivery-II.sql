"
Medium Problem 

Description:
Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the column of unique values of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
 

If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

The result format is in the following example.
"

# Successful Solution - 1814ms

select round(count(CASE WHEN order_date = customer_pref_delivery_date THEN 1 END)/count(*) * 100, 2) as immediate_percentage
from Delivery
where (customer_id, order_date) in (
    select customer_id, MIN(order_date)
    from Delivery
    group by customer_id
);

# Faster Solution - 625ms
select round(avg(order_date = customer_pref_delivery_date)*100,2) as immediate_percentage
from Delivery
where (customer_id,order_date) in 
    (select customer_id, min(order_date) as first_order
    from Delivery
    group by customer_id)

# Faster Solution - 514ms
select round(((count(case when a = 'immediate' then 1 end ))/count(a))*100,2) as immediate_percentage from
(select customer_id,min(order_date),min(customer_pref_delivery_date), (case when min(order_date) = min(customer_pref_delivery_date) then 'immediate' else 'scheduled' end) as a
from Delivery
group by 1) b