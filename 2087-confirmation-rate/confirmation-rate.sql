# Write your MySQL query statement below
SELECT SU.user_id, ROUND(
        IFNULL(SUM( CONF.action = 'confirmed') / COUNT(*), 0.00),
        2
    )  as confirmation_rate FROM Signups as SU 
left Join Confirmations CONF on SU.user_id = CONF.user_id 
GROUP BY SU.user_id; 
