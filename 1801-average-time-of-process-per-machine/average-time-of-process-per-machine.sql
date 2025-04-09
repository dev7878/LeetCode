# Write your MySQL query statement below

select a1.machine_id ,ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time from Activity a1, Activity a2
-- join Activity a2 on a1.process_id = a2.process_id
where  a1.activity_type='start' and a2.activity_type ='end' and a1.process_id = a2.process_id and a1.machine_id = a2.machine_id
group by a1.machine_id; 

