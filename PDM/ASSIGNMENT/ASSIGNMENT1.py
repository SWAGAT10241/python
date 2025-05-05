'''
# 1. At Delhi University, students enroll in different courses. Given two sets:
# Set A: Students enrolled in Mathematics = { ”Amit”, ”Bhavna”, ”Chirag”, ”Deepak”, ”Esha” }
# Set B: Students enrolled in Physics = { ”Chirag”, ”Deepak”, ”Farhan”, ”Geeta”, ”Harsh” }
# Write a Python program to:
# a) Find students enrolled in either Mathematics or Physics.
# b) Find students enrolled in both Mathematics and Physics .
# c) Find students enrolled in Mathematics but not in Physics .
# d) Find students enrolled in Physics but not in Mathematics.

set1 = {"Amit", "Bhavna", "Chirag", "Deepak", "Esha" }
set2 = {"Chirag", "Deepak", "Farhan", "Geeta", "Harsh"}
print(f"students enrolled in either Mathematics or Physics {set1.union(set2)}")
print(f"students enrolled in both Mathematics or Physics {set1.intersection(set2)}")
print(f"students enrolled in Mathematics but not in Physics {set1.difference(set2)}")
print(f"students enrolled in Physics but not in Mathematics {set2.difference(set1)}")
'''


'''
# 2. A tech company maintains records of employees with expertise in Python and Java. The HR team
# wants to analyze skill distribution using in-built set functions. Given the following sets:
# Set A (Employees skilled in Python) = { ”Amit”, ”Bhavna”, ”Chirag”, ”Deepak”, ”Esha”, ”Farhan”
# }
# Set B (Employees skilled in Java) = { ”Chirag”, ”Deepak”, ”Farhan”, ”Gaurav”, ”Harsh” }
# Write a Python program to perform the following operations using in-built set functions:
# a) Find whether ”Deepak” is skilled in Python.
# b) Check if all Python-skilled employees are also skilled in Java.

set1 = {"Amit", "Bhavna", "Chirag", "Deepak", "Esha", "Farhan"}
set2 = {"Chirag", "Deepak", "Farhan", "Gaurav", "Harsh"}

print(f"Deepak is skilled in Python: {'Deepak' in set1}")
print(f"All Python-skilled employees are also skilled in Java: {set1.issubset(set2)}")
'''


'''
# 3. Using the same data given in (Q2), find the following:
# a) Check if at least one employee has both skills
# b) Find employees skilled in either Python or Java, but not both.
# c) Make a copy of the Python-skilled employee set.
# d) Clear the Java-skilled employee set

set1 = {"Amit", "Bhavna", "Chirag", "Deepak", "Esha", "Farhan"}
set2 = {"Chirag", "Deepak", "Farhan", "Gaurav", "Harsh"}

print(f"At least one employee has both skills: {set1.intersection(set2)}")
print(f"Employees skilled in either Python or Java, but not both : {set1.symmetric_difference(set2)}")
print(f"Copy of the Python-skilled employee set: {set1.copy()}")
set2.clear()
print(f"Java-skilled employee set: {set2}")
'''


'''
# 4. ITER is conducting course registration for the new semester. Each student can enroll in any of the
# available subjects. Given a list of students and a list of subjects, generate all possible student-subject
# enrollment pairs.
# • Students: Asutosh, Ayushman, Mohit, Priya
# • Subjects: Mathematics, Physics, Computer Science, Economics

students = {"Asutosh", "Ayushman", "Mohit", "Priya"}
subjects = {"Mathematics", "Physics", "Computer Science", "Economics"}


for i in students:
    for j in subjects:
        print(f"({i}, {j})")
'''


'''
# 5. A board game uses two dice. Find all possible outcomes of rolling the dice.

print(f"All possible outcomes of rolling the dice")

for i in range(1,7):
    for j in range(1,7):
        print(f"({i},{j})", end= " ")
'''


'''
# 6. In a social media app, friendships are symmetric: If A is a friend of B, then B must also be a friend
# of A. Define a Python function to verify if a given friendship relation is symmetric and complete the
# missing pairs if necessary. Given two relations are:
# • R1 : {(”Anurag”, ”Nitish”), (”Priyabrata”, ”Koustav”), (”Prateek”, ”Asutosh”)}
# • R2 : {(”Priya”, ”Nikita”), (”Nikita”, ”Priya”), (”Sancheeta”, ”Shreyashree”),(”Shreyashree”,
# ”Sancheeta”)}

def friendships(a):
    to_add = []
    for i in a:
        if (i[1], i[0]) not in a:
            to_add.append((i[1], i[0]))
    a.update(to_add)
    return a

R1 = {("Anurag", "Nitish"), ("Priyabrata", "Koustav"), ("Prateek", "Asutosh")}
R2 = {("Priya", "Nikita"), ("Nikita", "Priya"), ("Sancheeta", "Shreyashree"),("Shreyashree","Sancheeta")}

print(f"Completed symmetric relation : {friendships(R1)}")
print(f"Completed symmetric relation : {friendships(R2)}")
'''


'''
# 7. At City Library, books are categorized based on genre and age group. The library wants to establish
# a relation that maps which genres are recommended for which age groups.
# • Genres (Set A) = { ”Fiction”, ”Non-Fiction”, ”Mystery”, ”Science”, ”Fantasy” }
# • AgeGroup (Set B) = { ”Children”, ”Teen”, ”Adult” }
# The relation R follows these constraints:
# i. Children can read Fiction and Fantasy.
# ii. Teens can read all genres except Non-Fiction.
# iii. Adults can read all genres.
# Write a Python program to generate and print the valid (Genre, AgeGroup) pairs forming the relation R.

A = { "Fiction", "Non-Fiction", "Mystery", "Science", "Fantasy" }
B = { "Children", "Teen", "Adult" }

for genre in A:
    for age_group in B:
        if (age_group == "Children" and genre in {"Fiction", "Fantasy"}) or \
            (age_group == "Teen" and genre != "Non-Fiction") or \
            (age_group == "Adult"):
            print(f"({genre}, {age_group})")
'''


'''
# 8. In a family tree, every person is related to themselves (reflexive relation). Given a parent-child rela-
# tion, check if it includes reflexivity.
# • people= {”Alice”, ”Bob”, ”Charlie”}
# • parent&child= {(”Alice”, ”Bob”), (”Bob”, ”Charlie”)}

people = {"Alice", "Bob", "Charlie"}
parent_child= {("Alice", "Bob"), ("Bob", "Charlie")}

# Check reflexivity
for person in people:
    if (person, person) not in parent_child:
        parent_child.add((person, person))

print(f"Reflexive relation: {parent_child}")
'''


'''
# 9. A professor teaches exactly one subject. Given a set of professor-subject assignments, check if it
# forms a function.
# • professor&subject= {(”Dr. Smith”, ”Math”), (”Dr. Johnson”, ”Physics”), (”Dr. Smith”,”Physics”)}

def is_function(professor_subject):
    subjects = {}
    for prof, subj in professor_subject:
        if prof in subjects and subjects[prof] != subj:
            return False
        subjects[prof] = subj
    return True

professor_subject = {("Dr. Smith", "Math"), ("Dr. Johnson", "Physics"), ("Dr. Smith", "Physics")}
print(f"Is the professor-subject assignment a function? {is_function(professor_subject)}")
'''

'''
# 10. A flight network records direct flights between cities. If there is a flight from A to B and from B to C,
# then there should be a direct or indirect flight from A to C (transitive relation). Check if the relation
# is transitive.
# • flights= {(”New York”, ”London”), (”London”, ”Paris”), (”Paris”, ”Berlin”), (”New York”,”Paris”)}

flights= {("New York", "London"), ("London", "Paris"), ("Paris", "Berlin"), ("New York", "Paris")}
def is_transitive(flights):
    for (a, b) in flights:
        for (c, d) in flights:
            if b == c and (a, d) not in flights:
                return False
    return True

print(f"Is the flight network transitive? {is_transitive(flights)}")
'''


'''
# 11. In a company, an employee can have a supervisor. If A supervises B, then B cannot supervise A (anti-
# symmetric relation). Given a list of supervision relations, check if the relation is anti-symmetric.
# • supervision= {(”Alice”, ”Bob”), (”Alice”, ”Charlie”), (”Bob”, ”David”)}

supervision= {("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David")}
for (a,b) in supervision:
    if (b,a) in supervision:
        print(f"Relation is not anti-symmetric: {supervision}")
        break
else:
    print(f"Relation is anti-symmetric: {supervision}")
'''


'''
# 12. At XYZ University, students have the opportunity to join various clubs based on their interests. The
# university has three prominent clubs: the Coding Club, which has 120 members; the Robotics Club,
# with 95 members; and the AI Club, which consists of 80 students. However, some students are
# members of multiple clubs. Specifically, 30 students are part of both the Coding and Robotics Club,
# 25 students are in both the Robotics and AI Club, and 20 students are enrolled in both the Coding
# and AI Club. Additionally, there are 10 students who are members of all three clubs. The university
# administration wants to determine the total number of unique students participating in at least one of
# these clubs by applying the Inclusion-Exclusion Principle.

coding_club = 120
robotics_club = 95
ai_club = 80
coding_robotics = 30
robotics_ai = 25
coding_ai = 20
coding_robotics_ai = 10
print(f"total number of unique students participating in at least one of these clubs: {coding_club + robotics_club + ai_club - coding_robotics - robotics_ai - coding_ai + coding_robotics_ai}")
'''

'''
# 13. At Green Valley University, students actively participate in various extracurricular activities. The
# university has three major student communities: Music Club (M): 150 members Drama Club (D):
# 110 members,Dance Club (N): 90 members Some students are members of multiple clubs:
# • Students in both Music and Drama: 40
# • Students in both Drama and Dance: 35
# • Students in both Music and Dance: 25
# • Students in all three clubs: 15
# The university administration wants to find the total number of students who are registered for both
# the Music and Drama Club, regardless of whether they are also part of the Dance Club.

Music_Club = 150
Drama_Club = 110
Dance_Club = 90
Music_Drama = 40
Drama_Dance = 35
Music_Dance = 25
Music_Drama_Dance = 15
print(f"total number of students who are registered for both the Music and Drama Club: {Music_Drama - Music_Drama_Dance}")
'''


'''
# 14. At Tech University, students can enroll in various advanced courses based on the prerequisite courses
# they have completed. The university wants to determine a relation between prerequisite courses and
# advanced courses based on specific eligibility criteria.
# • Prerequisite Courses (Set A) = { ”Math-101”, ”Physics-101”, ”CS-101”, ”Statistics-101” }
# • Advanced Courses (Set B) = { ”Machine Learning”, ”Quantum Computing”, ”Data Science”,
# ”Computer Vision”, ”AI Ethics” }
# The eligibility criteria are as follows:
# a) Machine Learning and Data Science require Math-101 or Statistics-101.
# b) Quantum Computing requires Math-101 and Physics-101.
# c) Computer Vision requires CS-101 and Math-101.
# d) AI Ethics is open to all students who have completed any one prerequisite.
# Write a Python program to generate the complete relation R, representing which prerequisite course
# allows enrollment in which advanced course.

Prerequisite_Courses = { "Math-101", "Physics-101", "CS-101", "Statistics-101" }
Advanced_Courses = { "Machine Learning", "Quantum Computing", "Data Science", "Computer Vision", "AI Ethics" }
relations = {
    "Machine Learning": {"Math-101", "Statistics-101"},
    "Data Science": {"Math-101", "Statistics-101"},
    "Quantum Computing": {"Math-101", "Physics-101"},
    "Computer Vision": {"CS-101", "Math-101"},
    "AI Ethics": Prerequisite_Courses
}

for course, prerequisites in relations.items():
    print(f"___{course}___")
    for prerequisite in prerequisites:
        print(f"{prerequisite}")
'''


'''
# 15. A group of employees is classified based on whether they share the same birth month. If two employ-
# ees have the same birth month, they are related. Consider the following relation,
# birthmonth= {(”Neha”, ”Vikas”), (”Vikas”, ”Neha”), (”Vikas”, ”Raj”), (”Raj”, ”Vikas”), (”Neha”,
# ”Raj”)} Check whether the given relation is an equivalence relation or not.

def is_equivalence_relation(relation):
    for person in relation:
        if (person[1], person[0]) not in relation:
            return False
    for person1 in relation:
        for person2 in relation:
            if person1[1] == person2[0] and (person1[0], person2[1]) not in relation:
                return False
    return True

birthmonth= {("Neha", "Vikas"), ("Vikas", "Neha"), ("Vikas", "Raj"), ("Raj", "Vikas"), ("Neha", "Raj")}
print(f"Is the birth month relation an equivalence relation? \n{is_equivalence_relation(birthmonth)}")
'''


'''
# 16. A city classifies people as neighbors if they live in the same PIN code area. If two people live in the
# same PIN code, they are related.
# Write a Python program that checks if this relation is:
# a) Reflexive: Every person belongs to their own neighborhood.
# b) Symmetric: If A is related to B, then B is related to A.

def check_relation(relation):

    is_reflexive = True
    for person in relation:
        if (person[0], person[0]) not in relation or (person[1], person[1]) not in relation:
            is_reflexive = False
            break
    
    is_symmetric = True
    for person in relation:
        if (person[1], person[0]) not in relation:
            is_symmetric = False
            break
    
    return is_reflexive, is_symmetric

relation = {("A", "B"), ("B", "A"), ("B", "C"), ("C", "B")}
reflexive, symmetric = check_relation(relation)

print(f"Is the relation reflexive? {reflexive}")
print(f"Is the relation symmetric? {symmetric}")
'''


'''
# 17. Check whether the relation given in (Q16) is transitive or not.

def is_transitive(relation):
    for a, b in relation:
        for c, d in relation:
            if b == c and (a, d) not in relation:
                return False
    return True

relation = {("A", "B"), ("B", "A"), ("B", "C"), ("C", "B")}
print(is_transitive(relation))
'''


'''
# 18. A school conducted a survey to find out how many students play Cricket and Football. The survey
# results are:
# Students who play Cricket: 40
# Students who play Football: 35
# Students who play both Cricket and Football: 15
# Write a Python program to draw a Venn Diagram representing this data.

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

Cricket = 40
Football = 35
both = 15

only_Cricket = Cricket - both
only_Football = Football - both

venn_labels = {'10': float(only_Cricket), '01': float(only_Football), '11': float(both)}
venn2(subsets=venn_labels, set_labels=('Cricket', 'Football'))

plt.title("Venn Diagram of Students Playing Cricket and Football")
plt.show()
'''


'''
# 19. A school surveyed students subject preferences. The three subjects were Mathematics, Science, and
# English. The survey found: Students who like Mathematics: 30
# Students who like Science: 25
# Students who like English: 20
# Students who like both Mathematics and Science: 10
# Students who like both Science and English: 8
# Students who like both Mathematics and English: 7
# Students who like all three subjects: 5
# Write a Python program to draw a Venn Diagram representing this data.

import matplotlib.pyplot as plt
from matplotlib_venn import venn3
Mathematics = 30
Science = 25
English = 20
MathematicsScience = 10
ScienceEnglish = 8
MathematicsEnglish = 7
MathematicsScienceEnglish = 5

set_labels=('Mathematics', 'Science', 'English')
venn3(subsets={'100': Mathematics - MathematicsScience - MathematicsEnglish + MathematicsScienceEnglish,
                '010': Science - MathematicsScience - ScienceEnglish + MathematicsScienceEnglish,
                '001': English - MathematicsEnglish - ScienceEnglish + MathematicsScienceEnglish,
                '110': MathematicsScience - MathematicsScienceEnglish,
                '101': MathematicsEnglish - MathematicsScienceEnglish,
                '011': ScienceEnglish - MathematicsScienceEnglish,
                '111': MathematicsScienceEnglish},
                set_labels=('Mathematics', 'Science', 'English'))
plt.show()
'''


'''
# 20. A group of students were surveyed about their knowledge of Hindi and English. The survey found:
# Students who know Hindi: 50
# Students who know English: 40
# Students who know both Hindi and English: 20
# Write a Python program to draw a Venn Diagram representing this data.

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

Hindi = 50
English = 40
both = 20

set_labels=('Hindi', 'English')
venn_labels = {'10': float(Hindi - both), '01': float(English - both), '11': float(both)}
venn2(subsets=venn_labels, set_labels=set_labels)

plt.show()
'''