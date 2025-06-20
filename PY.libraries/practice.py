'''
# using the factorial function
import math
import tensorflow_datasets as tfds
print(math.factorial(20)/math.factorial(4)/math.factorial(20-4))

# import the special functions from sciPy
import scipy.special
print(scipy.special.comb(20,4))
'''

'''
import time
number = 1000000

# Check the current time
startTime = time.time()

# Create an empty list
list = []

# Add items to the list one by one
for counter in range(number):
    list.append(counter)

# Display the run time
print(time.time() - startTime)
'''

'''
import time
number = 1000000

# Check the current time
startTime = time.time()

# Create a list of 1000000 zeros
list = [None]*number

# Add items to the list one by one
for counter in range(number):
    list[counter] = counter

# Display the run time
print(time.time() - startTime)
'''

'''
import networkx as nx
import cv2
import matplotlib.pyplot as plt
graph_plot = nx.draw(nx.petersen_graph(), with_labels=True)
plt.show()
'''

'''
def square(x):
    return x ** 2

A = {1, 2, 3, 4}
B = {square(x) for x in A}

print("Domain (A):", A)
print("Range (B):", B)
'''

'''
# Define a relation as a set of tuples (input, output)
relation = {(1, 1), (2, 4), (3, 9), (2, 8)}  # This is NOT a function (2 maps to two values)
is_function = len(set(x for x, y in relation)) == len(relation)
print("Is this relation a function?", is_function)  # False
'''

'''
import tensorflow as tf
import tensorflow_datasets as tfds

# Load a dataset (CIFAR-10)
dataset, info = tfds.load("cifar10", with_info=True)

# Expected classes in CIFAR-10
expected_classes = {"airplane", "automobile", "bird", "cat", "deer","dog", "frog", "horse", "ship", "truck"}

# Extract actual classes from dataset info
actual_classes = set(info.features["label"].names)

# Find missing labels
missing_classes = expected_classes - actual_classes
print("Missing Classes:", missing_classes)
'''

'''
import tensorflow as tf
import pandas as pd

# Example dataset
data = {
    "height": [5.1, 6.2, 5.8, 6.0],
    "weight": [120, 180, 160, 175],
    "age": [25, 30, 28, 35],
    "eye_color": ["blue", "brown", "green", "hazel"],  # Not useful
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Define relevant features
relevant_features = {"height", "weight", "age"}
actual_features = set(df.columns)

# Filter out non-useful features
selected_features = actual_features & relevant_features
df_filtered = df[list(selected_features)]

print("Selected Features for Training:")
print(df_filtered)
'''
print("Decimal",bin(10))
print("Octal",oct(10))
print("Hex-decimal",hex(10))