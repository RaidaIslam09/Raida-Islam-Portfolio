# ==============================================
# Week 3 - Lists
# Author : Raida Tasnim Islam
# ==============================================

# --- Creating list ----
customers = ["Raida", "Sarah", "Ahmed","John","Maria"]
salaries = ["85000", "72000", "91000", "68000","95000"]
active = [True,False,True,True,False]

# --- Accessing items by Index ---
print(customers[0])
print(customers[1])
print(customers[2])
print(customers[3])
print(customers[4])

# --- length of a list ---
print(len(customers))

# --- adding an item ---
customers.append("Fatima")
print(customers)

# --- Looping through a list ---
print()
print("Customers Report")
for customer in customers:
    print(f"Processing: {customer}")

# --- Exercises ---
customers = ["Raida", "Sarah", "Ahmed", "John", "Maria",]
sales = [15000, 8000, 23000, 5000, 19000]
active = [True, False, True, False, True]

print()
print("=" * 40)
print("Active Customer Report")
print("=" * 40)
for i in range(len(customers)):
    if active [i]:
       print(f"customer : {customers[i]}")
       print(f"sales : ${sales[i]}")
       print()

