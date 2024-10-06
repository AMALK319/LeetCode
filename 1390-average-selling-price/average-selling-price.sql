# Write your MySQL query statement below

/* select p.product_id, avg(price*units) as average_price
from prices p, unitsSold u
where p.product_id = u.product_id and purchase_date between start_date and end_date
group by product_id; */

select product_id, ROUND(sum(selling_price)/sum(units), 2) as average_price 
from (  select p.product_id, start_date, purchase_date, end_date, price*units  as selling_price, units
        from prices p, unitsSold u
        where p.product_id = u.product_id and purchase_date between start_date and end_date) as sold
group by product_id
union
select product_id, 0
from prices
where product_id not in (select product_id from UnitsSold);