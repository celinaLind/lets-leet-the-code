


# Successful Solution => 2376ms

SELECT S.student_id, S.student_name, E.subject_name, COALESCE(EXAM.attended_exams, 0) as attended_exams
FROM Students S
CROSS JOIN Subjects E
LEFT JOIN (
  SELECT E.student_id, E.subject_name, COUNT(*) as attended_exams
  FROM Examinations E
  GROUP BY E.student_id, E.subject_name
) EXAM ON S.student_id = EXAM.student_id AND E.subject_name = EXAM.subject_name
ORDER BY S.student_id, E.subject_name;


# Faster Solution (more optimized) => 760ms
SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;