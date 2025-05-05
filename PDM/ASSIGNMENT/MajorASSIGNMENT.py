# Scenario: University Enrollment System
# A university is developing a student enrollment system that manages student information using sets, logic,
# and relations. The system should be able to:
# • Store and manipulate student data using sets.
# • Implement logical operations to filter students based on conditions.
# • Analyze relationships between students and courses using relations.
# • Generate truth tables for logical conditions used in decision-making.

# Dataset: Student Enrollment Data
# The following dataset contains student IDs, names, enrolled courses, and participation in extracurricular
# activities.

# Student ID Name Courses CGPA Extracurricular
# 101 Alice {Math, CS} 8.9 True
# 102 Bob {Math, Physics} 7.8 False
# 103 Charlie {CS, Physics} 8.0 True
# 104 David {Math, Physics} 6.5 False
# 105 Eve {CS} 7.2 True
# 106 Frank {Math, CS, Physics} 9.1 False
# 107 Grace {Physics} 6.8 False
# 108 Hannah {Math} 7.5 True

# Table 1: Student Enrollment Data

# Task 1: Working with Relations (Reflexive, Symmetric, Transitive)
# Problem Statement
# 1. Create a dataframe using the library PANDAS from the given table. Print the dataframe.
# 2. From the dataframe, define a relation where two students are related if they are enrolled in at least
# one common course.
# 3. Check if is Reflexive, Symmetric, and Transitive.

import pandas as pd

pf = pd.read_csv('/Users/swagatsouravdhar/SEMISTER2/PYTHON/PDM/ASSIGNMENT/MajorASSIGNMENT.csv').rename(columns=lambda x: x.strip())
print(pf)


# Task 2: Logical Operations on Student Data
# Problem Statement
# 1. A student qualifies for a research grant if:
# • They have a CGPA 8.5 OR
# • They have a CGPA 7.5 AND participate in extracurricular activities
# Create a truthtable for this argument.
# 2. Create a new column called Scholarship Eligibility that contains True if the student qualifies for the
# scholarship, and False otherwise. Print the updated dataframe.

print(f"Qualifies for a research\n{pf[(pf['CGPA'] >= 8.5) | ((pf['CGPA'] >= 7.5) & (pf['Extracurricular'] == True))]}")
from scipy import symbols,AND,OR,NOT
from sympy.logic.boolalg import truth_table
Student_ID,Name,Courses,CGPA,Extracurricular = ('Student_ID,Name,Courses,CGPA,Extracurricular')
print("Student_ID,Name,Courses,CGPA,Extracurricular")
for i in pf:
    print(i)
    if pf['CGPA'] >= 8.5 or (pf['CGPA'] >= 7.5 and pf['Extracurricular'] == True):
        print("True")
    else:
        print("False")