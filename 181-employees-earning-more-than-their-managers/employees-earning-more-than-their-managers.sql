# Write your MySQL query statement below

select emp.name as Employee
from employee emp
join employee mng
on emp.managerId = mng.id
where emp.salary > mng.salary