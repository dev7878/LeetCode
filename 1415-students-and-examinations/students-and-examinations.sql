# Write your MySQL query statement below

select s.student_id ,s.student_name, su.subject_name, count(e.student_id) as attended_exams from Students as s
cross join Subjects su 
left join Examinations e  on s.student_id = e.student_id and su.subject_name = e.subject_name
group by s.student_id, s.student_name, su.subject_name
order by s.student_id,  su.subject_name;


-- select
--     ST.student_id
--     ,ST.student_name
--     ,SU.subject_name
--     ,count(E.student_id) attended_exams
-- from Students ST
-- cross join Subjects SU
-- left join Examinations E on ST.student_id = E.student_id and SU.subject_name = E.subject_name
-- group by ST.student_id, ST.student_name, SU.subject_name
-- order by ST.student_id, SU.subject_name