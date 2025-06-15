/* Write your PL/SQL query statement below */

select e2.employee_id, e2.name, count(e1.employee_id) as reports_count, round(AVG(e1.age)) as average_age
from employees e1
join employees e2
on e1.reports_to = e2.employee_id
group by e2.employee_id, e2.name
order by e2.employee_id








/* where e1.employee_id in (select distinct(reports_to)
                      from Employees)  */
