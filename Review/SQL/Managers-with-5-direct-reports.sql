"
Medium Problem

Description:
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

Return the result table in any order.

"

# Successful Solution - 646ms
select F.name from employee F inner join (
    select count(*) as counted, managerId
    from employee
    where managerId is not Null
    group by managerId
) as M on F.id = M.managerId
where M.counted >= 5;

# More Efficient Solution - 290ms

select name from employee
where id in (select managerId from employee group by managerId
having count(managerId)>=5)