-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(*) AS grade_A_count
FROM assignments
WHERE grade is "A"
GROUP BY teacher_id
ORDER BY COUNT(*) DESC
LIMIT 1;
