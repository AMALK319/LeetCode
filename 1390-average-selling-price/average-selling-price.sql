/* Write your PL/SQL query statement below */
/* select p.product_id, ROUND(sum(units*price)/sum(units), 2) as average_price 
from prices p, unitsSold u
where p.product_id = u.product_id and purchase_date between start_date and end_date
group by p.product_id
union
select product_id, 0
from prices
where product_id not in (select product_id from UnitsSold); */

/* Solution using join */
select p.product_id, COALESCE(ROUND(sum(units*price)/sum(units), 2), 0) as average_price 
from prices p left join unitsSold u
on p.product_id = u.product_id and purchase_date between start_date and end_date
group by p.product_id;