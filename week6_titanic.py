# ========================================
# Week 6 : Titanic Dataset Analysis
# Author : Raida Tasnim Islam
# ========================================

# --- Business Question ---
# 1. How does fare correlation with passenger class and embarkation port?
# 2. Which demographics predict survival?
# 3. How did cabin class impact survival rates 
# ===========================================

import pandas as pd
import numpy as np

# --- Load the dataset ---
df = pd.read_csv (r"C:\Users\Raida\Documents\python-learning\titanic.csv")

# --- First look ---
print("Shape:", df.shape)
print()
print("First 5 rows:")
print(df.head())
print()
print("Column Information:")
print()
print("Missing Values:")
print(df.isnull().sum())
print()

# ============================================
# Cleaning Dataset
# ============================================

# --- Step 1 : Fill missing age with Median ---
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
print(f"Median age used : {median_age}")

# --- Step 2 : Create has Cabin flag ---
df["Has_Cabin"] = df["Cabin"].notna()
df = df.drop("Cabin" , axis=1)

# --- Step 3: Fill missing Embarked with mode ---
most_common_port = df["Embarked"].mode() [0]
df["Embarked"] = df["Embarked"].fillna (most_common_port)
print(f"Most Common Port used : {most_common_port}")

# --- Verify Cleaning ---
print()
print("Missing Values after cleaning:")
print(df.isnull().sum())
print()
print("Shape after cleaning" , df.shape)
print()
print ("First 5 rows after cleaning")
print(df.head())
print()

# =======================================
# Analysis Question 1
# Fare vs Passenger class and Embarkation Port
# =======================================

print("Average fare by passenger class:")
print(df.groupby("Pclass")["Fare"].mean().round(2))
print()

print("Average fare by embarkation port:")
print(df.groupby("Embarked")["Fare"].mean().round(2))
print()

print("Average fare by class AND port:")
print(df.groupby(["Pclass","Embarked"])["Fare"].mean().round(2))
print()

# ===========================================
# Analysis Question 2
# Demographic AND Survival
# ===========================================

print("Survival rate by Passenger class:")
print(df.groupby("Pclass")["Survived"].mean().round(3))
print()

print("Survival rate by Gender:")
print(df.groupby("Sex")["Survived"].mean().round(3))
print()

print("Survival rate by class and Gender:")
print(df.groupby(["Pclass","Sex"])["Survived"].mean().round(3))
print()

print("Survival rate by Cabin class:")
print(df.groupby("Has_Cabin")["Survived"].mean().round(3))
print()

# =======================================
# Analysis Question 3
# Fare distribution and Survival
# ========================================

print("Average fare - survivors and non-survivors:")
print(df.groupby("Survived")["Fare"].mean().round(2))
print()

print("Average age - survivors and non-survivors:")
print(df.groupby("Survived")["Age"].mean().round(2))
print()

print("Survival rate by embarkation port:")
print(df.groupby("Embarked")["Survived"].mean().round(3))
print()