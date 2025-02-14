select c.product_name,s.year,s.price from sales as s
join product as c on s.product_id=c.product_id; 