'''
# 1. Write a Python program that takes a decimal number as input and converts it to its binary, octal, and
# hexadecimal representations.
# Instructions:
# • The program should ask the user to input a decimal number.
# • Convert the number to binary, octal, and hexadecimal.
# • Output all three representations.

def convert(n):
    return f"Binary: {bin(n)}\nOctal: {oct(n)}\nHexadecimal: {hex(n)}"
n = int(input("Enter a decimal number: "))
print(convert(n))
'''


'''
# 2. Write a Python program to convert a binary number to its decimal equivalent. The program should
# take a binary number as input and return the corresponding decimal value.
# Example:
# • Input: 1101
# • Output: 13

def convert(binary):
    return (int(binary, 2))
binary = input("Enter a binary number: ")
print(f"decimal number : {convert(binary)}")
'''


'''
# 3. Write a Python program that takes a binary number as input and converts it to its octal and hexadeci-
# mal equivalents.
# Instructions:
# • The program should ask the user to input a binary number.
# • Convert the binary number to octal and hexadecimal.
# • Output the results.

def convert(binary):
    return f"Octal: {oct(int(binary, 2))}\nHexadecimal: {hex(int(binary, 2))}"
input = input("Enter a binary number: ")
print(convert(input))
'''


'''
# 4. Write a Python program that converts a given decimal number to its binary, octal, and hexadecimal
# equivalents. The program should take an integer as input and output its binary, octal, and hexadecimal
# representations.
# Example:
# • Input: 345
# • Output:
# • Binary: 101011001
# • Octal: 531
# • Hexadecimal: 159

def convert(n):
    return f"Binary: {bin(n)}\nOctal: {oct(n)[2:]}\nHexadecimal: {hex(n)[2:]}"
n = int(input("Enter your decimal number : "))
print(convert(n))
'''


'''
# 5. Write a Python program to find the Two’s complement representation of a given integer (positive or
# negative) using an 8-bit representation.
# Instructions:
# The program should ask the user to input an integer.
# If the number is positive, find its binary form.
# If the number is negative, compute the Two’s complement in 8 bits.
# Output the Two’s complement.

def twos_complement(n):
    if n >= 0:
        binary = bin(n)[2:].zfill(8)
    else:
        n = abs(n)
        binary = bin((1 << 8) + n)[2:]
    return binary
n = int(input("Enter an integer: "))
print(f"Two's complement: {twos_complement(n)}")
'''


'''
# 6. • Using the given dataset write a Python program to display the customers who live in the USA
# and in the state of Georgia using the AND operator. Display the relevant columns: CustomerID,
# Country, State, City, and Zip Code.

# Hint: Use the & (AND) operator to combine conditions for the Country and State columns.
# • Using the given dataset write a Python program to display the customers who live either in
# the USA or in the state of Ontario using the OR operator. Display the relevant columns: Cus-
# tomerID, Country, State, City, and Zip Code.

# Hint: Use the |(OR) operator to combine conditions for Country and State.
# • Using the given dataset write a Python program to display the customers who do not live in the
# USA using the NOT operator. Display the relevant columns: CustomerID, Country, State, City,
# and Zip Code.

# Hint: Use the ! = (NOT EQUAL) operator to exclude customers from the USA.
# • using the given dataset write a Python program to display the customers who live either in India or
# in the state of Georgia (USA) using the OR operator. Display the relevant columns: CustomerID,
# Country, State, City, and Zip Code.

# Hint: Use the |(OR) operator to combine conditions for Country and State.
# • Using the given dataset write a Python program to display the customers who do not live in
# India or Germany using the NOT operator. Display the relevant columns: CustomerID, Country,
# State, City, and Zip Code.

# Hint: Use the ! = (NOT EQUAL) operator to exclude customers from India and Germany.

import pandas as pd

pf = pd.read_csv('/Users/swagatsouravdhar/SEMISTER2/PYTHON/PDM/ASSIGNMENT/Netflix_customer_dataset.csv').rename(columns=lambda x: x.strip())

print("Customers in the USA and Georgia:")
print(pf[(pf['Country'] == 'USA') & (pf['State'] == 'Georgia')][['Customer id', 'Country', 'State', 'Zip code']])

print("\nCustomers in the USA or Ontario:")
print(pf[(pf['Country'] == 'USA') | (pf['State'] == 'Ontario')][['Customer id', 'Country', 'State', 'Zip code']])

print("\nCustomers not in the USA:")
print(pf[pf['Country'] != 'USA'][['Customer id', 'Country', 'State', 'Zip code']])

print("\nCustomers in India or Georgia (USA):")
print(pf[(pf['Country'] == 'India') | (pf['State'] == 'Georgia')][['Customer id', 'Country', 'State', 'Zip code']])

print("\nCustomers not in India or Germany:")
print(pf[(pf['Country'] != 'India') & (pf['Country'] != 'Germany')][['Customer id', 'Country', 'State', 'Zip code']])
'''


'''
# 7. Write a python program that creates a data frame from a dictionary of lists and demonstrates basic
# operations like displaying data, getting column information, and accessing specific rows.
# • Write a python program to filter rows in a DataFrame based on students with an average mark
# • Write a python program to filter rows in a DataFrame based on students with an average mark
# greater than 85.
# • Write a python program to handle missing data in a DataFrame by filling missing values or
# dropping rows/columns that contain NaN.

import pandas as pd
import numpy as np
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Marks': [85, 90, np.nan, 95],
}
df = pd.DataFrame(data)
print("Data Frame:\n",df)
print("\nColumn Information:\n",df.info())
print("\nAccessing Specific Rows:\n",df.iloc[1])
print("\nFiltering Rows with Average Marks:\n",df[df['Marks'] > 85])
print("\nHandling Missing Data (Dropping Rows):\n",df.dropna())
'''


'''
# 8. Write a python program to create two data frames and merge those two data frames on a common column.

import pandas as pd
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
data2 = {
    'Name': ['Alice', 'Bob', 'David'],
    'Salary': [70000, 80000, 90000],
    'Department': ['HR', 'Finance', 'IT']
}
df1,df2 = pd.DataFrame(data1),pd.DataFrame(data2)
merged_df = pd.merge(df1, df2, on='Name', how='inner')
print("Merged Data Frame:\n", merged_df)
'''


'''
# 9. Write a python program to create a data frame of an office with 60 employees and sort the data frame
# by one or more columns.

import pandas as pd
import numpy as np
data = {
    'Employee ID': np.arange(1, 61),
    'Name': ['Employee ' + str(i) for i in range(1, 61)],
    'Department': ['HR', 'Finance', 'IT', 'Marketing'] * 15,
    'Salary': np.random.randint(30000, 100000, size=60),
    'Joining Date': pd.date_range(start='2020-01-01', periods=60, freq='ME')
}
df = pd.DataFrame(data)
print("Sorted Data Frame:\n", df.sort_values(by=['Department', 'Salary'], ascending=[True, False]))
'''


'''
# 10. Write a Python program to:
# • Define a list list1 = [1, 2, 3] and an integer int1 = 10.
# • Print the memory addresses of both list1 and int1 using the id() function.
# • Modify the list by appending a new element (list1.append(4)) and modify the integer by incre-
# menting it (int1 += 1).
# • Print the memory addresses again after the modifications.

list1 = [1, 2, 3]
int1 = 10
print(f"Memory address of list1 before modification: {id(list1)}")
print(f"Memory address of int1 before modification: {id(int1)}")
list1.append(4)
int1 += 1
print(f"Memory address of list1 after modification: {id(list1)}")
print(f"Memory address of int1 after modification: {id(int1)}")
'''


'''
# 11. Write a Python program that assigns the numbers 10 and 10 to two different variables num1 and num2.
# Check if both variables reference the same memory location using the id() function.
# Assign two larger integers (e.g., 1000 and 1000) to num3 and num4 and check their memory locations.
# Explain why small integers might reference the same memory location, but larger integers might not.

num1 = 10
num2 = 10
print(f"Memory address of num1: {id(num1)}")
print(f"Memory address of num2: {id(num2)}")
num3 = 1000
num4 = 1000
print(f"Memory address of num3: {id(num3)}")
print(f"Memory address of num4: {id(num4)}")
# Explanation:
# Small integers (like 10) are cached by Python, meaning that they are stored in a memory pool for efficiency.
# When you create multiple variables with the same small integer value, they reference the same memory location.
# However, larger integers (like 1000) are not cached in the same way, so different variables with the same larger
# integer value may reference different memory locations.
# This is due to Python's memory management and optimization techniques for small integers.
'''


'''
# 12. Write a Python program to retrieve and display the MAC address of the device on which the program is running.
# The MAC address should be displayed in two different formats:
# Format 1: AA:AA:AA:BB:BB:BB
# Format 2: AAAA-AABB-BBBB

import uuid
def get_mac_address():
    mac = uuid.getnode()
    mac_str = ':'.join(('%012X' % mac)[i:i + 2] for i in range(0, 12, 2))
    mac_str2 = '-'.join(('%012X' % mac)[i:i + 4] for i in range(0, 12, 4))
    return mac_str, mac_str2
mac1, mac2 = get_mac_address()
print(f"MAC Address Format 1: {mac1}")
print(f"MAC Address Format 2: {mac2}")
'''


'''
# 13. Use the uuid module to fetch the MAC address, then format and display it in the specified formats.
# Hint: Use uuid.getnode() to retrieve the MAC address as a 48-bit integer.
# Format the address appropriately using string manipulation.

import uuid
def get_mac_address():
    mac = uuid.getnode()
    mac_str = ':'.join(('%012X' % mac)[i:i + 2] for i in range(0, 12, 2))
    mac_str2 = '-'.join(('%012X' % mac)[i:i + 4] for i in range(0, 12, 4))
    return mac_str, mac_str2
mac1, mac2 = get_mac_address()
print(f"MAC Address Format 1: {mac1}")
print(f"MAC Address Format 2: {mac2}")
'''


'''
# 14. Write a python program using scipy for a restaurant to create meal combos by choosing 3 items from
# a menu of 10 dishes. How many different meal combos can you offer?
# Formula:
# C(n, k) = [n!]/[k!(n−k)! (1)]
# where,
# n is the total number of items (10 dishes).
# k is the number of items to choose (3 items).

from scipy.special import comb
def meal_combos(n, k):
    return comb(n, k, exact=True)
n , k  = 10, 3
print(f"Number of different meal combos: {meal_combos(n, k)}")
'''


'''
# 15. Write a python program using scipy for a problem where in a lottery, you must select 6 numbers from
# a total of 49. You want to know how many different combinations of 6 numbers can be chosen from 49.

from scipy.special import comb
def lottery_combinations(n, k):
    return comb(n, k, exact=True)
n = 49
k = 6
print(f"Number of different lottery combinations: {lottery_combinations(n, k)}")
'''



# 16. Write a python program using scipy for a treasure hunt game for kids provides clues encrypted using a Caesar
# cipher. One clue reads: ”KHOOR ZRUOG”, and the kids are told that the letters are shifted by 3 positions.

from scipy.special import comb
def caesar_cipher_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted += chr(shifted)
        else:
            decrypted += char
    return decrypted
ciphertext = "KHOOR ZRUOG"
shift = 3
print(f"Decrypted message: {caesar_cipher_decrypt(ciphertext, shift)}")



'''
# 17. Write a python program using scipy for a traveling salesman who drives around to visit N cities,
# including his home city, to try to sell his balloons and then return home. He wants to minimize the
# distance he travels so that his fuel costs are as small as possible.

import numpy as np
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment
def traveling_salesman(cities):
    n = len(cities)
    distance_matrix = cdist(cities, cities, metric='euclidean')
    row_ind, col_ind = linear_sum_assignment(distance_matrix)
    total_distance = distance_matrix[row_ind, col_ind].sum()
    return total_distance
cities = np.array([[0, 0], [1, 2], [3, 1], [4, 4]])
print(f"Total distance traveled by the salesman: {traveling_salesman(cities)}")
'''