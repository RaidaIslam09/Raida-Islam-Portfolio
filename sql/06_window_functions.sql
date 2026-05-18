-- =========================================
-- SQL Portfolio : Windows Functions
-- =========================================

-- WINDOWS 1 : RANK within each department
-- RANK employees by salary within their department

SELECT name,
       department,
       salary,
       RANK() OVER (
           PARTITION BY department
           ORDER BY salary DESC
       ) AS dept_rank
FROM employees
ORDER BY department, dept_rank;

-- WINDOWS 2 : ROW_NUMBER - unique, no ties
-- Gurantees exactly pne unique number per row

SELECT name,
       department,
       salary,
       ROW_NUMBER() OVER (
           PARTITION BY department
           ORDER BY salary DESC
       ) AS row_num
FROM employees
ORDER BY department, row_num;

-- WINDOW 3: Top earner per department only
-- CTE + ROW_NUMBER = exactly one person per dept
WITH ranked AS (
    SELECT name,
           department,
           salary,
           ROW_NUMBER() OVER (
               PARTITION BY department
               ORDER BY salary DESC
           ) AS row_num
    FROM employees
)
SELECT name,
       department,
       salary
FROM ranked
WHERE row_num = 1
ORDER BY salary DESC;

-- WINDOW 4: LAG — compare to previous row
-- Shows previous salary and the difference
SELECT name,
       department,
       salary,
       LAG(salary, 1) OVER (
           ORDER BY salary DESC
       ) AS prev_salary,
       salary - LAG(salary, 1) OVER (
           ORDER BY salary DESC
       ) AS salary_diff
FROM employees
ORDER BY salary DESC;

-- WINDOW 5: Department average alongside individual
-- Keeps every row while showing group calculation
SELECT name,
       department,
       salary,
       ROUND(AVG(salary) OVER (
           PARTITION BY department
       ), 2) AS dept_avg,
       salary - ROUND(AVG(salary) OVER (
           PARTITION BY department
       ), 2) AS diff_from_avg
FROM employees
ORDER BY department, salary DESC;