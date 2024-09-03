-- Write query to get number of graded assignments for each student:
-- Write query to get number of graded assignments for each student:
SELECT student_id, COUNT(*) AS graded_assignments
FROM assignments
WHERE state IS "GRADED"
GROUP BY student_id
ORDER BY student_id ASC;