/* Write your PL/SQL query statement below */

/* select name as Customers
from Customers
where id not in (select customerId from Orders) */

select name as Customers
from Customers c
left join Orders o
on c.id = o.customerId
where o.customerId is null