'''
# 1. Plot the following equations on a graph using matplotlib and find their point of intersection:
# x + y = 5
# x− y = 1

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

x = np.linspace(0, 6, 400)
plt.plot(x, 5 - x, label='x + y = 5')
plt.plot(x, x - 1, label='x - y = 1')

sol = solve((Eq(symbols('x') + symbols('y'), 5), Eq(symbols('x') - symbols('y'), 1)))
plt.plot(float(sol[symbols('x')]), float(sol[symbols('y')]), 'ro', label=f'Intersection ({sol[symbols("x")]:.2f}, {sol[symbols("y")]:.2f})')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of x + y = 5 and x - y = 1')
plt.legend()
plt.grid(True)
plt.show()
'''


'''
# 2. Visualize the 3D linear system using matplotlib (as planes):
# x + y + z = 6
# x− y + z = 2
# 2x + y− z = 3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6, 400)
y = np.linspace(0, 6, 400)
X, Y = np.meshgrid(x, y)
Z1 = 6 - X - Y
Z2 = 2 - X + Y
Z3 = 3 - 2*X - Y

fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# for Z, color, label in zip([Z1, Z2, Z3], ['red', 'blue', 'green'],
#                         ['x+y+z=6', 'x−y+z=2', '2x+y−z=3']):
#     ax.plot_surface(X, Y, Z, alpha=0.5, color=color, label=label, rstride=10, cstride=10)
# ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
# plt.title('3D Linear System Visualization')
plt.show()
'''


'''
# 3. Write a Python program to determine whether the following system of linear equations is dependent
# (i.e., has infinitely many solutions):
# 2x + 3y = 6
# 4x + 6y = 12

import numpy as np
def is_dependent_system(a, b):
    A,b = np.array(a),np.array(b)

    return np.linalg.matrix_rank(A) == np.linalg.matrix_rank(np.column_stack((A, b))) < A.shape[1]
a = [[2, 3], [4, 6]]
b = [6, 12]
if is_dependent_system(a, b):
    print("The system of equations is dependent (infinitely many solutions).")
else:
    print("The system of equations is independent (unique solution).")
'''

'''
# 4. Visualize the system given in Question 3 using matplotlib.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = (6 - 2 * x) / 3
plt.plot(x, y, label='2x + 3y = 6 / 4x + 6y = 12')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dependent System of Equations')
plt.grid()
plt.legend()
plt.show()
'''


'''
# 5. Generate a 4 × 3 matrix with random integers using np.random.randint. Display its transpose using NumPy.

import numpy as np
matrix = np.random.randint(1, 10, (4, 3))
print(f"Original Matrix (4x3):\n{matrix}\nTranspose of the Matrix (3x4):\n{matrix.T}")
'''


'''
# 6. Define a 2×2 matrix. Calculate its determinant using np.linalg.det() and find its inverse using np.linalg.inv()
# (if it exists).

import numpy as np

a = np.array([list(map(int, row.split(','))) for row in input("Enter a 2x2 matrix (comma-separated rows, e.g., '1,2;3,4'): ").split(';')])

print(f"Input Matrix :\n{a}")
print(f"Determinant : {np.linalg.det(a)}")
print(f"Inverse Matrix :\n{np.linalg.inv(a)}" if np.linalg.det(a) != 0 else "Matrix is not invertible.")
'''

'''
# 7. Input a 3 × 3 matrix and write a program to check whether it is invertible or not.

import numpy as np

a = np.array([list(map(int, row.split(','))) for row in input("Enter a 3x3 matrix (comma-separated rows, e.g., '1,2,3;4,5,6;7,8,9'): ").split(';')])

print(f"Input Matrix :\n{a}")
print(f"Inverse Matrix :\n{a.__invert__()}" if np.linalg.det(a) != 0 else "Matrix is not invertible.")
'''


'''
# 8. Using the determinant method, check whether a given system of equations is consistent or inconsistent.

import numpy as np

def check(a):
    return np.linalg.matrix_rank(a) == np.linalg.matrix_rank(a[:, :-1]) == a.shape[1] - 1
a = np.array([list(map(int, row.split(','))) for row in input("Enter a matrix (comma-separated rows, e.g., '1,2,3;4,5,6;7,8,9'): ").split(';')])
print(f"Input Matrix :\n{a}")
print("The system of equations is consistent." if check(a) else "The system of equations is inconsistent.")
'''


'''
# 9. Input two matrices and find their element-wise product using NumPy.

import numpy as np
def product(a,b):
    return f"{(a @ b)}"if a.shape[1]*b.shape[0] else "Matrices must have the same dimensions for element-wise multiplication."
a = np.array([list(map(int, row.split(','))) for row in input("Enter first matrix (comma-separated rows, e.g., '1,2;3,4'): ").split(';')])
b = np.array([list(map(int, row.split(','))) for row in input("Enter second matrix (comma-separated rows, e.g., '5,6;7,8'): ").split(';')])
print(f"First Matrix:\n{a}\nSecond Matrix:\n{b}\nElement-wise Product:\n{product(a, b)}")
'''


'''
# 10. Plot the line y = 2x + 1 using matplotlib.

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 400)
plt.plot(x, 2 * x + 1, label='y = 2x + 1')
plt.xlabel('x'); plt.ylabel('y'); plt.title('Plot of y = 2x + 1')
plt.axhline(0, color='black', lw=0.5); plt.axvline(0, color='black', lw=0.5)
plt.grid(True); plt.legend(); plt.show()
'''

'''
# 11. Plot the line y = 3x using matplotlib. (Note: Correct from “vertical line”.)

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 400)
plt.plot(x, 3 * x, label='y = 3x')
plt.xlabel('x'); plt.ylabel('y'); plt.title('Plot of y = 3x')
plt.axhline(0, color='black', lw=0.5); plt.axvline(0, color='black', lw=0.5)
plt.grid(True); plt.legend(); plt.show()
'''


'''
# 12. Use SymPy to convert the following system to Row Reduced Echelon Form (RREF):
# [1 2 1]
# [2 4 0]
# [3 6 3]

import sympy as sp
def RREF(matrix):
    return f"{sp.Matrix(matrix).rref()[0]},\nPivoits: {sp.Matrix(matrix).rref()[1]}"
matrix = [[1, 2, 1], [2, 4, 0], [3, 6, 3]]
print(f"Row Reduced Echelon Form (RREF):\n{RREF(matrix)}")
'''

'''
# 13. Without using Gaussian elimination directly, solve the following system of equations using NumPy:
# [2 -6 6][x] = [-8]
# [2 3 -1][y] = [15]
# [4 -3 -1][z] = [19]

import numpy as np
A , B = np.array([[2, -6, 6], [2, 3, -1], [4, -3, -1]]),np.array([-8, 15, 19])
solution = np.linalg.solve(A, B)
print(f"Solution to the system of equations:\n x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")
'''


'''
# 14. Use NumPy to solve a 5×5 linear system generated with random integers using np.random.randint.
# Create a random 5 × 1 constant vector and solve using np.linalg.solve().

import numpy as np
A , B = np.random.randint(1, 10, (5, 5)),np.random.randint(1, 10, (5, 1))
solution = np.linalg.solve(A, B)
print("5x5 Linear System:")
print(f"Matrix A:\n{A}\nConstant Vector B:\n{B}\nSolution:\n{solution}")
'''

'''
# 15. Generate a 10 × 10 linear system using the random module and solve it using NumPy.

import numpy as np
A , B = np.random.randint(1, 10, (10, 10)),np.random.randint(1, 10, (10, 1))
solution = np.linalg.solve(A, B)
print("10x10 Linear System:")
print(f"Matrix A:\n{A}\nConstant Vector B:\n{B}\nSolution:\n{solution}")
'''
