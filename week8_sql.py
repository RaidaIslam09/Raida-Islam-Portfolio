# ================================================
# Week 8 — SQL with Python and SQLite
# Author: Raida Tasnim Islam
# ================================================

import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")
cursor = conn.cursor()
print("Database connected.")

# --- Create employees table ---
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id          INTEGER PRIMARY KEY,
        name        TEXT,
        department  TEXT,
        city        TEXT,
        salary      INTEGER,
        years       INTEGER,
        dept_id     INTEGER
    )
""")

# --- Create departments table ---
cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        dept_id    INTEGER PRIMARY KEY,
        dept_name  TEXT,
        budget     INTEGER,
        location   TEXT
    )
""")
print("Tables created.")

# --- Insert employee data ---
employees = [
    (1,  "Raida Islam",    "Analytics", "Dallas",  85000, 3, 10),
    (2,  "James Smith",    "Marketing", "Austin",  72000, 5, 20),
    (3,  "Priya Patel",    "Analytics", "Raleigh", 91000, 7, 10),
    (4,  "Carlos Garcia",  "Sales",     "Dallas",  68000, 2, 30),
    (5,  "Emma Wilson",    "Marketing", "Austin",  88000, 4, 20),
    (6,  "David Chen",     "Analytics", "Dallas",  79000, 6, 10),
    (7,  "Sofia Martinez", "Sales",     "Raleigh", 74000, 3, 30),
    (8,  "Marcus Johnson", "Marketing", "Dallas",  93000, 8, 20),
    (9,  "Aisha Brown",    "Analytics", "Austin",  96000, 5, 10),
    (10, "Tom Davis",      "Sales",     "Austin",  71000, 1, 30)
]

cursor.executemany("""
    INSERT OR IGNORE INTO employees
    VALUES (?,?,?,?,?,?,?)
""", employees)

# --- Insert department data ---
departments = [
    (10, "Analytics", 500000, "Dallas"),
    (20, "Marketing", 350000, "Austin"),
    (30, "Sales",     200000, "Raleigh"),
    (40, "Finance",   450000, "Dallas"),
    (50, "IT",        300000, "Austin")
]

cursor.executemany("""
    INSERT OR IGNORE INTO departments
    VALUES (?,?,?,?)
""", departments)

conn.commit()
print("Data inserted.")

# ================================================
# JOIN QUERIES
# ================================================

# --- INNER JOIN ---
print("\n" + "="*50)
print("INNER JOIN — Employees with Department Info")
print("="*50)
df_inner = pd.read_sql_query("""
    SELECT e.name,
           e.salary,
           e.city,
           d.dept_name,
           d.budget
    FROM employees e
    INNER JOIN departments d
        ON e.dept_id = d.dept_id
    ORDER BY e.salary DESC
""", conn)
print(df_inner)

# --- LEFT JOIN ---
print("\n" + "="*50)
print("LEFT JOIN — All Employees Including Unassigned")
print("="*50)
df_left = pd.read_sql_query("""
    SELECT e.name,
           e.salary,
           d.dept_name
    FROM employees e
    LEFT JOIN departments d
        ON e.dept_id = d.dept_id
    ORDER BY e.salary DESC
""", conn)
print(df_left)

# --- RIGHT JOIN simulation ---
print("\n" + "="*50)
print("ALL DEPARTMENTS — Including Empty Ones")
print("="*50)
df_right = pd.read_sql_query("""
    SELECT e.name,
           d.dept_name,
           d.budget,
           d.location
    FROM departments d
    LEFT JOIN employees e
        ON d.dept_id = e.dept_id
    ORDER BY d.dept_name
""", conn)
print(df_right)

# --- WHERE example ---
print("\n" + "="*50)
print("WHERE — Dallas employees average salary by dept")
print("="*50)
df_where = pd.read_sql_query("""
    SELECT d.dept_name,
           AVG(e.salary) AS avg_salary
    FROM employees e
    INNER JOIN departments d
        ON e.dept_id = d.dept_id
    WHERE e.city = 'Dallas'
    GROUP BY d.dept_name
""", conn)
print(df_where)

# --- HAVING example ---
print("\n" + "="*50)
print("HAVING — Departments with avg salary above 80000")
print("="*50)
df_having = pd.read_sql_query("""
    SELECT d.dept_name,
           AVG(e.salary) AS avg_salary
    FROM employees e
    INNER JOIN departments d
        ON e.dept_id = d.dept_id
    GROUP BY d.dept_name
    HAVING AVG(e.salary) > 80000
    ORDER BY avg_salary DESC
""", conn)
print(df_having)

# ==================================================
# AGGREGATIONS
# ==================================================

print("\n" + "="*50)
print("FULL DEPARTMETN SUMMARY")
print("="*50)

df_summary= pd.read_sql_query("""
   SELECT department,
          COUNT(*)    AS total_employees,
          SUM(salary) AS total_salary_cost,
          AVG(salary) AS avg_salary,
          MAX(salary) AS highest_salary,
          MIN(salary) AS lowest_salary 
    FROM employees
    GROUP BY department
    ORDER BY avg_salary DESC                                                                                                                                                                       
""", conn)
print(df_summary)

print("\n" + "="*50)
print("EMPLOYEES PER CITY")
print("="*50)

df_city =pd.read_sql_query ("""
   SELECT city,
          COUNT(id) AS total_employees
    FROM employees
    GROUP BY city
    ORDER BY total_employees DESC                                                                                                                                               
""", conn)
print(df_city)

print("\n" + "="*50)
print("DEPARTMENTS WITH TOTAL SALARY ABOVE 200000")
print("="*50)

df_having = pd.read_sql_query("""
    SELECT department,
           SUM(salary) AS total_salary_cost
    FROM employees
    GROUP BY department
    HAVING SUM(salary) > 200000
    ORDER BY total_salary_cost DESC
""", conn)
print(df_having)

print("\n" + "="*50)
print("AGGREGATIONS WITH JOIN — Dept name + budget")
print("="*50)
df_join_agg = pd.read_sql_query("""
    SELECT d.dept_name,
           d.budget,
           COUNT(e.id)    AS total_employees,
           AVG(e.salary)  AS avg_salary,
           SUM(e.salary)  AS total_salary_cost
    FROM employees e
    INNER JOIN departments d
        ON e.dept_id = d.dept_id
    GROUP BY d.dept_name, d.budget
    ORDER BY avg_salary DESC
""", conn)
print(df_join_agg)

# =====================================
# SUBQUERIES
# =====================================

print("\n" + "="*50)
print("SUBQUERY 1 - Above average earners")
print("="*50)

df_sub1 = pd.read_sql_query("""
   SELECT name,
          department,
          salary
    FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)
    ORDER BY salary DESC                                                                                                                                                               
""", conn)
print (df_sub1)

print("\n" + "="*50)
print ("SUBQUERY 2 - Highest paid employee")
print("="*50)

df_sub2 = pd.read_sql_query("""
   SELECT name,
          department,
          salary
    FROM employees
    WHERE salary = (SELECT MAX(salary) FROM employees)                                                                                                                                                                                          
""", conn)
print(df_sub2)

print("\n" + "="*50)
print("SUBQUERY 3 — Department avg salary above 80000")
print("="*50)
df_sub3 = pd.read_sql_query("""
    SELECT dept_summary.department,
           dept_summary.avg_salary
    FROM (
        SELECT department,
               AVG(salary) AS avg_salary
        FROM employees
        GROUP BY department
    ) AS dept_summary
    WHERE dept_summary.avg_salary > 80000
""", conn)
print(df_sub3)

# =================================================
# CTEs - Common Table Expressions
# ==================================================

print("\n" + "="*50)
print ("CTE 1 - Department average (readble version)")
print("="*50)

df_cte1 = pd.read_sql_query("""
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
""", conn)
print(df_cte1)

print("\n" + "="*50)
print("CTE 2 - Employees above their dept average")
print("="*50)

df_cte2 = pd.read_sql_query("""
    WITH dept_avg AS(
        SELECT department,
               AVG(salary) AS avg_salary
        FROM employees
        GROUP BY department

    )
    SELECT e.name,
           e.department,
           e.salary,
           ROUND (da.avg_salary,2) AS dept_avg
    FROM employees e
    INNER JOIN dept_avg da 
        ON e.department = da.department
    WHERE e.salary > da.avg_salary
    ORDER BY e.salary DESC;
""" , conn)
print(df_cte2)

print("\n" + "="*50)
print("CTE 3 - Employees Above Their Dept Average")
print("="*50)

df_cte3 = pd.read_sql_query("""
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
    ORDER BY e.salary DESC
""", conn)
print(df_cte3)

conn.close()
print("\nDatabase connection closed.")
