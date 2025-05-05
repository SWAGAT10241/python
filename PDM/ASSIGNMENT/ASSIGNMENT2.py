'''
# 1. Verify whether the following two logical expressions are equivalent using Python and the sympy
# library:
# P ∧(Q ∨R) ≡(P ∧Q) ∨(P ∧ R)
# Hint: Use the function simplify logic from the sympy library.

from sympy import symbols, Or, And, simplify_logic
P ,Q, R = symbols('P Q R')
expr1 = And(P, Or(Q, R))
expr2 = Or(And(P, Q), And(P, R))
print(simplify_logic(expr1).equals(simplify_logic(expr2)))
'''


'''
# 2. Write a Python program to generate the truth table for the following Boolean function:
# F (A, B, C) = (A ∨ B) ∧(¬C)

from sympy import symbols
from sympy.logic.boolalg import Or, And, Not,truth_table

a, b, c = symbols('a b c')
expr = And(Or(a, b), Not(c))
print(" A | B | C | F(a, b, c)")
print("-------------------------")

for values,result in truth_table(expr, [a, b, c]):
    print(f" {int(values[0])} | {int(values[1])} | {int(values[2])} | {int(bool(result))}")
'''


'''
# 3. Write a Python program to generate the truth table for the following Boolean function without using
# the sympy library:
# F (A, B, C) = (A ∨ B) ⊕ (B ∧ C)

# my method
def F(A, B, C):
    return (A or B) != (B and C)
print(" A | B | C | F(A, B, C)")
print("-------------------------")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            result = F(A, B, C)
            print(f" {A} | {B} | {C} | {int(result)}")

# sir method
from sympy.logic.boolalg import And, Or, Xor
from itertools import product
variables = ["A", "B", "C"]
def expression (A,B,C) :
    return Xor (Or(A, B), And (B, C))
for values in product ([0,1], repeat=3):
    A, B,C = values
    result = expression(A, B,C)
    print(f" {int(values[0])} | {int(values[1])} | {int(values[2])} | {int(bool(result))}")
'''


'''
# 4. Write a Python program to simplify the following Boolean expression using the sympy library:
# F (A, B, C) = (A ∧ B) ∨ (¬A ∧ C) ∨ (B ∧ C)

from sympy import symbols, Or, And, Not, simplify_logic
A, B, C = symbols('A B C')
expr = Or(And(A, B), And(Not(A), C), And(B, C))
print("Original expression:", expr)
print("Simplified expression:",simplify_logic(expr))
'''


'''
# 5. Write a Python program to check whether the following logical statement is a tautology:(P ∨Q) ∨¬ P

from sympy import symbols, Or, Not
from sympy.logic.boolalg import truth_table
P, Q = symbols('P Q')
expr = Or(Or(P, Q), Not(P))
for values,result in truth_table(expr, [P, Q]):
    if not result:
        print("The statement is not a tautology.")
        break
else:
    print("The statement is a tautology.")
'''


'''
# 6.Find the Disjunctive Normal Form (DNF) and Conjunctive Normal Form (CNF) of the Boolean function:
# F (A, B, C) = (A ∧B) ∨ (¬A ∧ C) ∨ (B ∧ C)

from sympy import symbols, Or, And, Not
from sympy.logic.boolalg import to_dnf, to_cnf
A, B, C = symbols('A B C')
expr = Or(And(A, B), And(Not(A), C), And(B, C))
print("DNF:", to_dnf(expr, simplify=True))
print("CNF:", to_cnf(expr, simplify=True))
'''


'''
# 7. A Boolean function F is self-dual if:
# F (A, B, C, ...) =¬F (¬A,¬B,¬C, ...)
# Check whether the function
# F (A, B) = A ∨B
# is self-dual using Python.

from sympy import symbols, Or, Not
A, B = symbols('A B')
expr = Or(A, B)
is_self_dual = expr.equals(Not(expr.subs({A: Not(A), B: Not(B)})))
print("The function is self-dual." if is_self_dual else "The function is not self-dual.")
'''


'''
# 8. Write a Python function to prove that the product of an even integer and any integer is even.

def prove(a):
    return (a % 2 == 0) and (num1 % 2 == 0) and (num2 % 2 == 0)

num1,num2 = map(int,input("Enter an even integer: ").split())
print(f"The product of {num1} and {num2} is even: {prove(num1 * num2)}")
'''


'''
# 9. Prove by induction that the sum of the first n odd numbers is equal to n^2, i.e.,
# 1 + 3 + 5 +···+ (2n−1) = n^2.

def proof(n):
    sum = 0
    for i in range(1,2*n,2):
        sum += i
    return (sum == pow(n,2))

n = int(input("Enter your end term : "))
print(proof(n))
'''


'''
# 10. Given the following truth table:
# A B C F (A, B, C)
# 0 0 0 0
# 0 0 1 1
# 0 1 0 1
# 0 1 1 1
# 1 0 0 1
# 1 0 1 1
# 1 1 0 1
# 1 1 1 1
#  Write a Python program to construct a simplified Boolean expression that represents this function.

from sympy import symbols, Or, And, Not, simplify_logic

A, B, C = symbols('A B C')
F = Or(
    And(Not(A), Not(B), C),
    And(Not(A), B, Not(C)),
    And(Not(A), B, C),
    And(A, Not(B), Not(C)),
    And(A, Not(B), C),
    And(A, B, Not(C)),
    And(A, B, C)
)
print("Original expression:", F)
print("Simplified expression:", simplify_logic(F))
'''


'''
# 11.Given the following truth table for a Boolean function F (A, B, C), determine its **Conjunctive Normal Form (CNF)**.
# A B C F (A, B, C)
# 0 0 0 0
# 0 0 1 1
# 0 1 0 0
# 0 1 1 1
# 1 0 0 1
# 1 0 1 1
# 1 1 0 0
# 1 1 1 1
# Write a Python program to:
# (a) Identify the rows where F (A, B, C) = 0.
# (b) Construct the CNF expression using these rows.
# (c) Output the simplified CNF form.

from sympy import symbols, Or, And, Not, simplify_logic

A, B, C = symbols('A B C')
rows_with_zero = [
    (0, 0, 0),
    (0, 1, 0),
    (1, 1, 0)
]

cnf_expr = And(
    Or(A, B, C),
    Or(A, Not(B), C),
    Or(Not(A), Not(B), C)
)

print(f"CNF Expression: {cnf_expr}")
print(f"Simplified CNF Expression: {simplify_logic(cnf_expr , form='cnf')}")
'''


'''
# 12. Implement a function that checks whether the sum of two even numbers is always even.

def Even(n):
    return (n % 2 == 0) and (n1 % 2 == 0) and (n2 % 2 == 0)

n1,n2 = map(int,input("Enter an even integer: ").split())
print(f"is sum of two even numbers is always even {Even(n1+n2)}")
'''


'''
# 13. Write a function that verifies whether the sum of three consecutive integers is always a multiple of 3.

def is_multiple_of_3(n1, n2, n3):
    return (n1 + n2 + n3) % 3 == 0 and (n1 == n2 - 1) and (n2 == n3 - 1)
n1,n2,n3 = map(int,input("Enter an consecutive integer: ").split())
print(f"The sum of {n1}, {n2}, and {n3} is a multiple of 3: {is_multiple_of_3(n1, n2, n3)}")
'''


'''
# 14. Create a function that verifies whether the product of two odd numbers is always odd.

def is_odd(n):
    return (n % 2 != 0)

n1 = int(input("Enter first odd number: "))
n2 = int(input("Enter second odd number: "))
print(f"The product of {n1} and {n2} is odd: {is_odd(n1 * n2)}")
'''


'''
# 15. Write a function that assumes the existence of a smallest positive rational number and leads to a contradiction.

from fractions import Fraction

def smallest_positive_rational():
    smallest_rational = Fraction(1)
    smaller_rational = smallest_rational / 2
    print(f"Assuming the smallest positive rational number is {smallest_rational} leads to a contradiction.")
    print(f"We found a smaller positive rational number: {smaller_rational}.")

smallest_positive_rational()
'''


'''
# 16. Create a function that proves an odd number cannot be equal to twice an integer.

def prove(n):
    return ((n and 1) != 0) == 2 * n
n = int(input("Enter an odd number: "))
print(f"The odd number {n} is equal to twice an integer: {prove(n)}")
'''


'''
# 17. Write a function that checks whether the sum of a rational number and an irrational number is always irrational.

def sum(rational, irrational):
    return (rational + irrational) != rational
rational = float(input("Enter a rational number: "))
irrational = float(input("Enter an irrational number: "))
print(f"The sum of {rational} and {irrational} is irrational: {sum(rational, irrational)}")
'''


'''
# 18. Write a Python program that demonstrates proof by induction for the sum of the first n natural numbers:
# 1 + 2 + 3 +···+ n = n(n + 1)/2

def proof(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return (sum == (n * (n + 1)) / 2)
n = int(input("Enter your end term : "))
print(proof(n))
'''


'''
# 19. The sum of the first (n + 1) powers of 2 is claimed to be:
# 1 + 2 + 4 +···+ 2^n = 2^n
# for all n ≥0.
# Write a Python program to verify whether this formula holds for different values of n.

def proof(n):
    sum = 0
    for i in range(0,n+1):
        sum += pow(2,i)
    return (sum == pow(2,n+1))
n = int(input("Enter your end term : "))
print(proof(n))
'''


'''
# 20. The sum of the reciprocals of the first n natural numbers is claimed to be:
# 1 +1/2 +1/3 +···+1/n = ln(n)
# for all n ≥1.
# Write a Python program to verify whether this formula holds for different values of n.

import math
def proof(n):
    sum = 0
    for i in range(1,n+1):
        sum += 1/i
    return (sum == math.log10(n))
n = int(input("Enter your end term : "))
print(proof(n))
'''
