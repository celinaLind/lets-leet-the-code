


# Solution 1: Did Not produce correct results
# Runtime: 2228ms , Time Taken: 16min
select distinct V.customer_id, Count(*) as count_no_trans 
from Visits as V, Transactions as T
where V.visit_id != T.visit_id;


# Correct Solution
select customer_id,count(*) as count_no_trans
from Visits 
left join 
Transactions
on Visits.visit_id = Transactions.visit_id 
where Transactions.visit_id is null
group by Visits.customer_id