# ==============================================
# Week 8 : SQL with Python and SQLite
# Author : Raida Tasnim Islam
# ==============================================

import sqlite3
import pandas as pd

# --- Connect to Database ---
# This creates a new database file called company.db
conn = sqlite3.connect("company.db")
cursor = conn.cursor ()
print("Database connected.")

# --- Create employees table ---
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id          INTEGER PRIMARY KEY,
        name        TEXT,
        department  TEXT,
        city        TEXT,
        salary      INTEGER,
        years       INTEGER
    )
""")
print("Table created.")

# --- Insert Employee Data ---
employees = [
    (1, "Raida Islam",   "Analytics",   "Dallas",   85000, 3),
    (2, "James Smith",    "Marketing",   "Austin",  72000, 5),
    (3, "Priya Patel",     "Analytics",  "Raleigh", 91000, 7),
    (4, "Carlos Garcia",   "Sales",      "Dallas",  68000, 2),
    (5, "Emma Wilson",     "Marketing",  "Austin",  88000, 4),
    (6, "David Chen",      "Analytics",  "Dallas",  79000, 6),
    (7, "Sofia Martinez",  "Sales",      "Raleigh", 74000, 3),
    (8, "Marcus Johnson",  "Marketing",  "Dallas",  93000, 8),
    (9, "Aisha Brown",     "Analytics",  "Austin",  96000, 5),
    (10,"Tom Davis",       "Sales",      "Austin",  71000, 1)
]

cursor.executemany("""
     INSERT OR IGNORE INTO employees
    VALUES (?,?,?,?,?,?)
""", employees)

conn.commit()
print("Data Inserted.")

# ================================================
# SQL Queries - Asking Questions to the Database 
# ================================================

# --- Query 1 : See all the employees ---
print("=" * 50)
print("ALL EMPLOYEES")
print("=" * 50)

df1 = pd.read_sql_query ("SELECT * FROM EMPLOYEES", conn)
print(df1)
print()

# --- Query 2 : Only Analytics Department ---
print("=" * 50)
print("ANALYTICS DEPARTMENT ONLY")
print("=" * 50)

df2 = pd.read_sql_query("""
    SELECT name, city, salary
    FROM employees
    WHERE department = 'Analytics'
""", conn)
print(df2)
print()

# --- Query 3 : Employees earning above 80000 ---
print("=" * 50)
print("HIGH EARNERS - SALARY ABOVE 80000")
print("=" * 50)
df3 = pd.read_sql_query("""
    SELECT name, city, salary
    FROM employees
    WHERE salary >80000
    ORDER BY salary DESC
""" , conn)
print(df3)
print()

# --- Query 4: Average Salary by Department ---
print("=" * 50)
print("AVERAGE SALARY BY DEPARTMENT")
print("=" *50)
df4 = pd.read_sql_query("""
    SELECT department, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department
    ORDER BY avg_salary DESC
""" , conn)
print(df4)
print()

#--- Query 5 : Dallas Employee only ---
print("=" * 50)
print("DALLAS EMPLOYEE ONLY")
print("=" * 50)
df5 = pd.read_sql_query("""
     SELECT name, department, salary
     FROM employees
     WHERE city = "Dallas"
     ORDER BY salary DESC                                                    
""", conn)
print(df5)
print()