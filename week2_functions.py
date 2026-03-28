# =================================================
# Week 2 - Functions
# Author - Raida Tasnim Islam
# =================================================

# What is Functions?
# A reusable block of code you define once
# and call as many as times as you need
# Syntax: def function_name():

# --- First Function ---
def greet():
    print("Hello! I am Data Analyst in training")
    print("I will be ready in next 4 years")

# Calling the functions - this actually runs it
greet()

# ==================================================
# --- Functions with Parameters ---
# A parameter is a variables you pass into functions
# it goes inside the () when you define it
# ==================================================

def greet_person(name,job):
    print(f"Hello {name}!")
    print(f"Goal is to become a {job}.")
    print(f"you are going to make it")
    print()

# Now call it with different values each time
greet_person("Raida", "Data Analyst")
greet_person("Sarah", "Business Analyst")
greet_person("Ahmed", "Product Analyst")

# --- Functions with Return Values ---
# return sends a value Back to whoever called the functions
# This is how you calculate in real data work

def calculate_average(score1, score2, score3):
    total = score1 + score2 + score3
    average = round (total /3,2)
    return average 

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
      
def print_report(student_name, score1, score2, score3):
        avg = calculate_average(score1, score2, score3)
        grade = get_grade(avg)
        print(f"Student : {student_name}")
        print(f"Scores : {score1}, {score2}, {score3}")
        print(f"Average : {avg}")
        print(f"Grade : {grade}")
        print()


# --- Run the report 3 studens ---
print("=" * 40)
print("Students grade report")
print("=" * 40)
print()
print_report("Raida", 95, 88, 92)
print_report("Sarah", 78, 82, 75)
print_report("Ahmed", 65, 70, 60)

