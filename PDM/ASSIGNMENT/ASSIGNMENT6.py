'''
# 1. Write a program that asks the user to choose between sequential, selection, and repetitive flow tasks
# and executes accordingly.

def choice():
    options = {'1': "Sequential Flow", '2': "Selection Flow", '3': "Repetitive Flow"}
    print("Choose a task:\n1. Sequential Flow\n2. Selection Flow\n3. Repetitive Flow")
    print(f"You chose {options.get(input('Enter the number of your choice: '), 'an invalid option.')}")
choice()
'''


'''
# 2. Write a program that counts how many even and odd numbers are in a list. Measure the execution
# time of the program and discuss its time complexity.

import time
def count_even_odd(numbers):
    start = time.time()
    even = sum(1 for n in numbers if n % 2 == 0)
    odd = len(numbers) - even
    end = time.time()
    print(f"Even count: {even}, Odd count: {odd}\nExecution time: {end - start:.6f} seconds")

nums = list(map(int, input("Enter numbers separated by space: ").split()))
count_even_odd(nums)
'''


'''
# 3. Write a program to check if a number is prime. Improve the algorithm from O(n) to O(√n).

import math,time
def prime(num):
    if num < 2:
        return False
    return all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))

start = time.time()
n = int(input("Enter a number to check if it is prime: "))
result = prime(n)
end = time.time()
print(f"Is the number prime? {result}\nExecution time: {end - start:.6f} seconds")
'''


'''
# 4. Write a program to merge two sorted arrays into a single sorted array. Measure the execution time of
# the program and discuss its time complexity.

import time
def merge(arr1, arr2):
    start = time.time();merged_array = sorted(arr1 + arr2);end = time.time()
    return f"Merging array: {merged_array}\nExecution time: {end - start:.6f} seconds"

arr1 = list(map(int, input("Enter first sorted array (space-separated): ").split()))
arr2 = list(map(int, input("Enter second sorted array (space-separated): ").split()))
print(merge(arr1, arr2))
'''


'''
# 5. Write a program to find the first duplicate element from a given list. Measure the execution time of
# the program and discuss its time complexity.

import time
def duplicate(element):
    t0 = time.time();result = next((x for x in element if element.count(x) > 1), None);t1 = time.time()
    return f"First duplicate element: {result}\nExecution time: {t1 - t0:.6f} seconds"

elements = list(map(int, input("Enter elements separated by space: ").split()))
print(duplicate(elements))
'''


'''
# 6. Write a program to find all the duplicate elements from a given list. Measure the execution time of
# the program and discuss its time complexity.

import time
from collections import Counter
def duplicate(element):
    start = time.time();counts = Counter(element);duplicates = [item for item, count in counts.items() if count > 1];end = time.time()
    return f"Duplicate elements: {duplicates}\nExecution time: {end - start:.6f} seconds"

elements = list(map(int, input("Enter elements separated by space: ").split()))
print(duplicate(elements))
'''


'''
# 7. Write a program to identify the element that appears most frequently in a list. Measure the execution
# time of the program and discuss its time complexity.

import time
def frequent(lst):
    start = time.time();most_frequent = max(set(lst), key=lst.count);end = time.time()
    return f"Most frequent element: {most_frequent}\nExecution time: {end - start:.6f} seconds"
elements = list(map(int, input("Enter elements separated by space: ").split()))
print(frequent(elements))
'''


'''
# 8. Write a Python program to implement the linear search algorithm to find a target value in a list.
# (a) If the target is found, return its index.
# (b) If not found, return−1.
# Additionally, measure the execution time of the program and discuss its time complexity.

import time
def linearSearch(n, x):
    for i in range(len(n)):
        if n[i] == x:
            return f"Element is found at index {i}."
    return -1

lst = list(map(int, input("Enter elements separated by space: ").split()))
x = int(input("Enter your searching elements: "))
ti = time.time();print(f"{linearSearch(lst, x)}");tf = time.time()
print(f"Execution time: {tf - ti:.6f} seconds")
'''


'''
# 9. Write a Python program to implement the binary search algorithm to find a target value in a list.
# (a) If the target is found, return its index.
# (b) If not found, return -1.
# Additionally, measure the execution time of the program and discuss its time complexity.

import time
def bin_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

arr = list(map(int, input("Enter elements separated by space: ").split()))
x = int(input("Enter your search elements: "))
start = time.time();print(f"{bin_search(arr, x)}");end = time.time()
print(f"Execution time: {end - start:.6f} seconds")
'''


'''
# 10. Write a program that compares the number of comparisons made by linear search and binary search on the
# same sorted list.

import time

def linear_search(lst, target):
    for i, v in enumerate(lst):
        if v == target:
            return i
    return -1

def binary_search(lst, target):
    l, r = 0, len(lst) - 1
    while l <= r:
        mid = (l + r) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

def compare(lst, target):
    t0 = time.time(); li = linear_search(lst, target); t1 = time.time()
    t2 = time.time(); bi = binary_search(lst, target); t3 = time.time()
    return (f"Linear Search: Index {li}, Time {t1-t0:.6f} seconds\n"
            f"Binary Search: Index {bi}, Time {t3-t2:.6f} seconds")

lst = list(map(int, input("Enter sorted elements separated by space: ").split()))
target = int(input("Enter the target element to search: "))
print(compare(lst, target))
'''


'''
# 11. Write a program that counts how many times each number appears in a list. Measure the execution
# time of the program and discuss its time complexity.

import time
from collections import Counter
def count(number):
    start = time.time();counts = Counter(number);end = time.time()
    return f"Number counts: {counts}\nExecution time: {end - start:.6f} seconds"
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(count(numbers))
'''


'''
# 12. Create a program that prints all pairs of elements from a list. Measure the execution time of the
# program and discuss its time complexity.

import time
def prints(lst):
    t0 = time.time();pairs = [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i + 1, len(lst))];t1 = time.time()
    return f"Pairs of elements: {pairs}\nExecution time: {t1 - t0:.6f} seconds"
lst = list(map(int, input("Enter elements separated by space: ").split()))
print(prints(lst))
'''


'''
# 13. Write a program that repeatedly divides a number n by 2 and counts how many steps it takes to reach
# 1. Measure the execution time of the program and discuss its time complexity.

import time
def count_steps(n):
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps
n = int(input("Enter a number to divide by 2 until it reaches 1: "))
ti = time.time();steps = count_steps(n);tf = time.time()
print(f"Number of steps to reach 1: {steps}\nExecution time: {tf - ti:.6f} seconds")
'''


'''
# 14. Write a Python program to implement a recursive function for computing Fibonacci numbers. Measure the
# execution time of the program and discuss its time complexity.

import time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter a number to compute Fibonacci series up to n: "))
start = time.time();series = fibonacci(n);end = time.time()
print(f"Fibonacci series up to {n}: {series}\nExecution time: {end - start:.6f} seconds")
'''