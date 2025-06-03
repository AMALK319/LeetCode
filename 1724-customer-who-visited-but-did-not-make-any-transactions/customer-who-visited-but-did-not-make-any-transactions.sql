-- Write your PostgreSQL query statement below
select distinct(v.customer_id), count(v.visit_id) as count_no_trans
from visits v where v.visit_id not in (select visit_id from transactions)
group by v.customer_id;