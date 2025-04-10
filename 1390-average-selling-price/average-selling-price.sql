# Write your MySQL query statement below

SELECT p.product_id, IFNULL(ROUND(SUM(p.price*us.units)/ SUM(us.units),2),0) as average_price 
FROM Prices as p 
LEFT JOIN UnitsSold as us 
ON p.product_id = us.product_id and us.purchase_date >= p.start_date and us.purchase_date <= p.end_date
GROUP BY p.product_id


