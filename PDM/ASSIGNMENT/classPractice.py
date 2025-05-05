'''
# 1 . t= (1, 2, 3, 4, 5, 6, 7, 8) is a given tuple. Print first four elements of the tuple and the last three elements of the tuple.

t = (1,2,3,4,5,6,7,8)
print(t[:4])
'''

'''
# 2. QIP2=(Rohit, Anjan, Soumya, Nitish, Niladri, Sancheeta, Ashu, Meghna, Sainandan, Imtiyaz, Amit, Chota Anshu, Bada Anshu Akansha, Prateek, Anurag, Coffee Anshu).Consider this tuple of strings and sort it alphabetically.

QIP2 = ('Rohit', 'Anjan', 'Soumya', 'Nitish', 'Niladri', 'Sancheeta', 'Ashu', 'Meghna', 'Sainandan', 'Imtiyaz', 'Amit', 'Chota Anshu', 'Bada Anshu', 'Akansha', 'Prateek', 'Anurag', 'Coffee Anshu')
print(sorted(QIP2))
'''

'''
# 3. Compute the cartesian product of the given sets.
# setl = {1, 2, 3)
# set2 = (4, 5)
# set3 = {6, 7)

set1 = {1, 2, 3}
set2 = {4, 5}
set3 = {6, 7}

cart = []
for i in set1:
    for j in set2:
        for k in set3:
            cart.append((i,j,k))
print(cart)
'''

'''
# 4. Define a function to find the frequency of the characters of a String in a dictionary.

def frequency(str):
    freq = {}
    for i in str :
        if i in freq:
            freq[i] +=1
        else:
            freq[i] = 1
        print(freq)


str = input("Enter a string: ")
frequency(str)
'''
'''
# 5. Define a function to find the sum of all prime numbers in a tuple.

import math

def PrimeSum(num):
    sum = 0
    for i in num :
        if i > 1 :
            for j in range(2,int(math.sqrt(i)+1)):
                if i % j == 0:
                    break
                else:
                    sum += i
    return sum

num = (1,2,3,4,5,6,7,8,9,10) # 2+3+5+7 = 17
print(PrimeSum(num))
'''

'''
# 6. Consider the following dictionary:
# words = { 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
# 8: "Eight", 14 :"Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19:
# "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70:
# "Seventy", 80: "Eighty", 90: "Ninety" }
# Using this dictionary, define a function to convert a number n (0<n<100) to words.

def convert(n):
    if n < 20:
        return words[n]
    else :
        return (words[n//10*10] + " " + words[n%10])
    
words = { 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
8: "Eight", 14 :"Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19:
"Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70:
"Seventy", 80: "Eighty", 90: "Ninety" }

print(convert(21))
'''
'''
# 7. You are given a list of tuples, where each tuple contains three integers representing the sides of a triangle. Write a Python program to filter out the tuples that represent valid triangles based on the Triangle Inequality Theorem. list of tuples: [(3, 4, 5), (1, 2, 3), (6, 8, 10), (2, 2, 5), (7, 24, 25)]|

def validTriangle(tri):
    for i in tri:
        if (i[0] + i[1] > i[2]) and (i[1] + i[2] > i[0]) and (i[0] + i[2] > i[1]):
            print(i)

tri = [(3, 4, 5), (1, 2, 3), (6, 8, 10), (2, 2, 5), (7, 24, 25)]
validTriangle(tri)
'''


'''
# 8. Check If a tuple forms an arithmetic progression or not?

def is_arithmetic_progression(t):
    if len(t) < 2:
        return True
    diff = t[1] - t[0]
    for i in range(2, len(t)):
        if t[i] - t[i - 1] != diff:
            return False
    return True

t = (1, 3, 5, 7, 9)
print(is_arithmetic_progression(t))  

t = (2, 4, 8, 10)
print(is_arithmetic_progression(t))  
'''


'''
# 9. Define two matrices using numpy. Find the product of these two matrices.

import numpy as np

np1 = np.array([[1,2],[3,4]])
np2 = np.array([[5,6],[7,8]])

print(np.dot(np1,np2))
'''