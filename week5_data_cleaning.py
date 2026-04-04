# ===========================================
# Week 5 : Data cleaning
# Author : Raida Tasnim Islam
# ===========================================

import pandas as pd
import numpy as np

# --- Load the messy data ---
df = pd.read_csv(r"C:\Users\Raida\Documents\python-learning\messy_data.csv")

# --- step 1 : First look ---
print("Shape:, df.shape")
print()
print("First look:")
print()
print(df)
print()
print("Data types:")
print(df.info())
print()

# --- Step 2: Check missing data ---
print("Missing values per column:")
print(df.isnull().sum())

# ===========================================
# Cleaning Steps
# ===========================================

# --- Step 3 : Remove duplicates ---
print("Before removing duplicates:", df.shape)
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)
print()

# --- Step 4: Fix fake salary values ---
# Replace "N/A" and "abc" with Nan so pandas recognizes them as missing
df["salary"] = df["salary"].replace("N/A",np.nan)
df["salary"] = df["salary"].replace("abc",np.nan)

# --- Replace outliner 999999 with Nan ---
df["salary"] = df["salary"].replace(999999,np.nan)
df["salary"] = df["salary"].replace("999999",np.nan)

print("Salary column after fixing values:")
print(df["salary"])
print()

# --- Step 5: Convert Salary with numbers ---
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
print("Salary data type after conversion:", df["salary"].dtype)
print()

# --- Step 6: Fill missing salary with department average ---
df["salary"] = df.groupby("department") ["salary"].transform(
    lambda x:x.fillna(x.mean())
)

print("Missing values after filling salary:")
print(df.isnull().sum())
print()

# --- Step 7: Fill missing name with Unknown ---
df["name"] = df["name"].fillna("Unknown")

# --- Step 8: Fill missing data with Not available ---
df["start_date"] = df["start_date"].fillna("Not Available")

# --- Step 9: Strip hidden spaces from department ---
df["department"] = df["department"].str.strip()

# --- Step 10: Final clean dataset ---
print("clean dataset:")
print(df)
print()
print("Final missing values")
print(df.isnull().sum())
print()

# --- Step 11: Flag remaining missing salaries ---
# sales debt has no valid salaries to average from 
# Fill with company wide average as best estimate

company_avg = df["salary"].mean()
df["salary"] = df["salary"].fillna (round(company_avg,2))

print("Final clean dataset:")
print(df)
print()
print("Final missing values:")
print(df.isnull().sum())
print()
print (f"Company average salary used for Sales: ${round(company_avg,2)}")
print()