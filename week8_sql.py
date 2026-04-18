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

conn.close()
print("\nDatabase connection closed.")