-- school_queries.sql

-- 1. CREATE TABLES
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL CHECK (grade >= 1 AND grade <= 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- 2. INSERT DATA
-- Insert students
INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

-- Insert grades (using IDs from the students table - note: IDs may vary)
-- Assuming student IDs are 1-9 in the order inserted above
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Science', 89),
(8, 'Math', 90),
(8, 'History', 77),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);

-- Additional grades from the first file content
INSERT INTO grades (student_id, subject, grade) VALUES
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'Math', 83),
(9, 'Math', 89);

-- 3. Find all grades for a specific student (Alice Johnson)
SELECT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson';

-- 4. Calculate the average grade per student
SELECT s.id, s.full_name, ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC;

-- 5. List all students born after 2004
SELECT id, full_name, birth_year
FROM students
WHERE birth_year > 2004
ORDER BY birth_year;

-- 6. Create a query that lists all subjects and their average grades
SELECT subject, ROUND(AVG(grade), 2) as average_grade
FROM grades
GROUP BY subject
ORDER BY average_grade DESC;

-- 7. Find the top 3 students with the highest average grades
SELECT s.id, s.full_name, ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC
LIMIT 3;

-- 8. Show all students who have scored below 80 in any subject
SELECT DISTINCT s.id, s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.id;

-- OPTIMIZATION: Create indexes for frequently queried columns
CREATE INDEX IF NOT EXISTS idx_students_full_name ON students(full_name);
CREATE INDEX IF NOT EXISTS idx_students_birth_year ON students(birth_year);
CREATE INDEX IF NOT EXISTS idx_grades_student_id ON grades(student_id);
CREATE INDEX IF NOT EXISTS idx_grades_subject ON grades(subject);
CREATE INDEX IF NOT EXISTS idx_grades_grade ON grades(grade);
CREATE INDEX IF NOT EXISTS idx_grades_student_subject ON grades(student_id, subject);