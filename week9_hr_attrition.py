# =========================================
# Project 2 - HR Employee Attrition Analysis
# Author: Raida Tasnim Islam
# Dataset: IBM HR Analytics - Kaggle
# ===========================================

# Business Questions:
# Q1: Which departments have highest attrition rate?
# Q2: What charaterisitcs predict attrition?
# Q3: What is the financial cost of attrition?
#
# Hypothesis: Overtime and burnout is the primary
# Driver or employee attrition at IBM
# =============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Step 3: Load the dataset ---
df = pd.read_csv(r"C:\Users\Raida\Documents\python-learning\hr_attrition.csv")

# --- Step 4: First look ---
print("Shape:", df.shape)
print()
print("First 5 rows:")
print(df.head())
print()
print("All column names:")
print(df.columns.tolist())
print()
print("Missing valunes:")
print(df.isnull().sum())
print()
print("Attition value counts:")
print(df["Attrition"].value_counts())
print()