


# Successful Solution V1 - 2682ms

select P.project_id, Round(avg(E.experience_years), 2) as average_years
from Project P
left join Employee E
on P.employee_id = E.employee_id
group by project_id;

"
NOTES:
  - including the 'AS' keyword when adding alias' makes the runtime faster
  For this example the runtime 2682 => 832ms by adding 'as' for the table alias'

"