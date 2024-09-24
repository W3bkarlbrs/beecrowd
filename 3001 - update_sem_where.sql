select 
name, 
CASE
        WHEN type = 'A' THEN 20.0
        WHEN type = 'B' THEN 70.0
        WHEN type = 'C' THEN 530.5
        ELSE 0
    END AS price
from products
order by price asc, id desc;