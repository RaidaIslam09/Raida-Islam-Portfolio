# =======================================
# Week 7 - Matplotlib Data visulization
# Author - Raida Tasnim Islam
# =======================================

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Load Titanic Data ---
df = pd.read_csv(r"C:\Users\Raida\Documents\python-learning\titanic.csv")

# --- Clean the data ---
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Has_Cabin"] = df["Cabin"].notna()
df=df.drop("Cabin", axis=1)
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode(0))

# ======================================
# Chart 1 - Survival Rate by Passenger Class
# Question - Did first class survived more than third?
# ======================================

# --- Calculate survival rate by class ---
survival_by_class = df.groupby("Pclass")["Survived"].mean()

# --- Create the figure- think of this as a blank canvas ---
plt.figure(figsize=(8,5))

# --- Draw the bars ---
plt.bar(
    survival_by_class.index, 
    survival_by_class.values,
    color=["steelblue", "orange", "green"],
    edgecolor = "Black",
    width=0.5
)

# --- Add three required levels ---
plt.title ("Titanic Survival Rate by Passenger Class", fontsize=14)
plt.xlabel("Passenger Class(1=First, 2=Second, 3=Third)", fontsize=12)
plt.ylabel("Survival Rate (0=0% , 1=100%)", fontsize=12)

# ---Add value labels on top of each bar
for i, value in enumerate(survival_by_class.values):
    plt.text(i+1, value+0.01, f"{value:1%}",
             ha="center",fontsize=11)
    
# --- Add a horizontal line at 50% for references
plt.axhline(y=0.5, color="red", linestyle="--", 
            label="50% survival line")
plt.legend() 

# --- Save the file as an image file ---
plt.savefig("chart1_survival_by_class.png",
            bbox_inches="tight",dpi=150)

plt.show()
print("Chart 1 saved.")
print()

# ==========================================
# Chart 2 - Survival Rate by Gender
# Question - Did Gender dertermine survival?
# ==========================================

# --- calculate survival rate by gender ---
survival_by_gender = df.groupby("Sex") ["Survived"].mean()

# --- Open new canvas ---
plt.figure(figsize=(8,5))

# --- Draw the bars ---
plt.bar(
    survival_by_gender.index,
    survival_by_gender.values,
    color=["red", "blue"],
    edgecolor="black",
    width=0.4
)

#--- Add the three required levels ---
plt.title("Titanic Survival Rate by Gender", fontsize=14)
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Survival Rate(0=0% , 1=100%)", fontsize=12)

# --- Add percentage lavels on three bars ---
for i, value in enumerate(survival_by_gender.values):
    plt.text(i, value+0.01, f"{float(value):.1%}",
             ha="center" , fontsize=11)
    
# --- Add a references line at 50%
plt.axhline (y=0.5, color="green",linestyle="--",
             label="50% survival line")
plt.legend()

# --- Save and Show ---
plt.savefig("chart2_survival_by_gender.png",
            bbox_inches="tight", dpi=150)

plt.show()
print("chart 2 saved.")
print()

