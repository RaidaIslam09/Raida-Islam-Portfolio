-- ================================================
-- SQL Portfolio: CTEs (Common Table Expressions)
-- Author: Raida Tasnim Islam
-- ================================================

-- CTE 1: Department averages — readable version
WITH dept_avg AS (
    SELECT department,
           AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
)
SELECT department,
       avg_salary
FROM dept_avg
WHERE avg_salary > 80000
ORDER BY avg_salary DESC;

-- CTE 2: Employees above their department average
-- The "Big Fish in Small Ponds" query
WITH dept_avg AS (
    SELECT department,
           AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
)
SELECT e.name,
       e.department,
       e.salary,
       ROUND(da.avg_salary, 2) AS dept_avg
FROM employees e
INNER JOIN dept_avg da
    ON e.department = da.department
WHERE e.salary > da.avg_salary
ORDER BY e.salary DESC;

-- CTE 3: Multi-step analysis
-- Above average earners in high cost departments
WITH
dept_avg AS (
    SELECT department,
           AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
),
high_cost_depts AS (
    SELECT department
    FROM employees
    GROUP BY department
    HAVING SUM(salary) > 200000
)
SELECT e.name,
       e.department,
       e.salary,
       ROUND(da.avg_salary, 2) AS dept_avg
FROM employees e
INNER JOIN dept_avg da
    ON e.department = da.department
INNER JOIN high_cost_depts hcd
    ON e.department = hcd.department
WHERE e.salary > da.avg_salary
ORDER BY e.salary DESC;