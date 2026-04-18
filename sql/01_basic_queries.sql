-- ====================================================
-- SQL Portfolio : Basic Queries
-- Author : Raida Tasnim Islam
-- Dataset : Company Employee
-- ====================================================

-- Query 1 : View All employees
SELECT *
From employees;

-- Query 2 : View Specific Column
SELECT name, department, salary
From employees;

-- Query 3 : Filter by department
SELECT name, city , salary
From employees
WHERE department = 'Analytics';

-- Query 4 : High Earners above 80000
SELECT name, department, salary
FROM employees
WHERE salary > 80000
ORDER BY salary DESC;

-- Query 5: Average Salary by Department
SELECT department,
       AVG(salary) AS avg_salary,
       COUNT(*) AS employee_count,
       MAX(salary) AS highest_salary,
       MIN(salary) AS lowest_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;

-- Query 6: Dallas Employee only
SELECT name, department, salary
FROM employees
WHERE city = 'Dallas'
ORDER BY salary DESC;

-- Query 7: Employees with more 4 years
SELECT name, department, years, salary
FROM employees
WHERE years > 4
ORDER BY years DESC;






