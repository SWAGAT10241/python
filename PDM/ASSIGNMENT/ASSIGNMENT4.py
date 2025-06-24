'''
# 1. Write a code to simulate tossing a fair coin 1000 times. Count and display the number of heads and tails.

import random

def tossing(n = 1000):
    head = 0
    tail = 0
    for i in range(n):
        toss = random.randint(0, 1)
        if toss == 0:
            head += 1
        else:
            tail += 1
    return head, tail
print(f"Tossing a coin 1000 times gives us {tossing()[0]} heads and {tossing()[1]} tails.")
'''


'''
# 2. Write a program to simulate rolling a six-sided die 1000 times and calculate the probability of rolling a 6.

import random
def die(n = 1000):
    count = 0
    for i in range(n):
        roll = random.randint(1, 6)
        if roll == 6:
            count += 1
    return count
print(f"Rolling a die 1000 times gives us {die()} times of rolling a 6.")
'''


'''
# 3. Write a program to simulate the birthday problem to find out the probability that in a group of 23
# people, at least 2 share the same birthday.

import random

def birthday(n = 23):
    birthdays = []
    for i in range(n):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            return True
        birthdays.append(birthday)
    return False

def birthday_simulation(trials = 10000):
    count = 0
    for i in range(trials):
        if birthday():
            count += 1
    return count / trials
print(f"The probability that in a group of 23 people, at least 2 share the same birthday is {birthday_simulation()}.")
'''


'''
# 4. Given a bag with 3 red balls and 2 blue balls, write a program to find the probability of drawing 2 red
# balls without replacement.

from scipy.special import comb
def probability():
    total,red,blue = 5,3,2
    return (comb(red, 2) * comb(blue, 0)) / comb(total, 2)
print(f"The probability of drawing 2 red balls without replacement is {probability()}.")
'''


'''
# 5. Write a code to simulate the rolling of two six-sided dice 5000 times. Compute the experimental probability 
# of getting a sum of 7.

import random
def dice(n = 5000):
    count = 0
    for i in range(n):
        dice = random.randint(1,6) + random.randint(1,6)
        if dice == 7:
            count += 1
    return count
print(f"Rolling two dice 5000 times gives us {dice()} times of getting a sum of 7.")
'''


'''
# 6. For a given finite sample space and equally likely outcomes, write a function that computes the probability
# of any event (subset of the sample space).

def probability(sample,event):
    sample = set(sample)
    event = set(event)
    if event.issubset(sample):
        return len(event) / len(sample)
    else:
        raise ValueError("Event is not a subset of the sample space.")
sample_space = {1, 2, 3, 4, 5, 6}
event = {1, 2}
print(f"The probability of the event {event} in the sample space {sample_space} is {probability(sample_space, event)}.")
'''


'''
# 7. Write a code to compute the probability of getting exactly k heads in n coin tosses for a fair coin.

import math
def coin(n,k,p):
    binom = math.comb(n,k)
    coin = binom * (p ** k ) * ((1-p)**(n-k))
    return coin
n , k , p = 10 ,3 ,0.5
print(f"{coin(n,k,p)}")
'''


'''
# 8. Plot the distribution of the number of heads when tossing 50 coins. Use matplotlib to visualize the results.

import matplotlib.pyplot as plt
import random

coin_tosses = lambda n: sum(random.randint(0, 1) for _ in range(n))

def plot_distribution():
    x = list(range(1, 51))
    y = list(map(coin_tosses, x))

    plt.bar(x, y)
    plt.xlabel('Number of Coins')
    plt.ylabel('Number of Heads')
    plt.title('Distribution of Heads when Tossing Coins')
    plt.xticks(x)
    plt.show()
plot_distribution()
'''


'''
# 9. A sports analyst provides the following probabilities for an upcoming soccer match:
# • Probability that Real Madrid wins: P (R) = 0.40
# • Probability that FC Barcelona wins: P (B) = 0.50
# The only other possible outcome is a draw. Write a Python program that:
# (a) Stores the probabilities of Real Madrid and Barcelona winning.
# (b) Calculates and prints the probability of a draw.
# (Hint: Use the fact that the sum of all disjoint outcomes must be 1.)

def probability():
    P_R,P_B = 0.40,0.50
    P_draw = 1 - (P_R + P_B)
    return P_draw
print(f"The probability of a draw is {probability():.2f}.")
'''


'''
# 10. Given a dataset of weather (e.g., temperature and rainfall), write a program to calculate the conditional
# probability that it rained given a certain temperature range.

import pandas as pd

pf = pd.read_csv("/Users/swagatsouravdhar/SEMISTER2/PYTHON/PDM/ASSIGNMENT/temperature.csv").rename(columns=lambda x: x.strip())

def probability(temp_range):
    rain = pf[pf['Temperatures'] == temp_range]['Rain Frequency'].values[0]
    temp = pf[pf['Temperatures'] == temp_range]['Frequency'].values[0]
    if temp == 0:
        return 0.0
    return rain / temp
temp = "51-60"
print(f"The probability of rain at {temp} degrees is {probability(temp):.2f}.")
'''


'''
# 11. Write a code to implement a function that uses Bayes’ Theorem to compute P (A | B) given P (B | A),
# P (A), and P (B).

def bayes_theorem(output,a,b):
    return (output * a) / b
output = 0.8
a = 0.6
b = 0.7
print(f"P(A|B) = {bayes_theorem(output,a,b)}")
'''


'''
# 12. Given a dictionary with temperature ranges and corresponding rain frequencies, write a code to calculate
# the conditional probability that it rained, given a specific temperature range.

import pandas as pd

pf = pd.read_csv("/Users/swagatsouravdhar/SEMISTER2/PYTHON/PDM/ASSIGNMENT/temperature.csv").rename(columns=lambda x: x.strip())

def probability(temp_range):
    rain = pf[pf['Temperatures'] == temp_range]['Rain Frequency'].values[0]
    temp = pf[pf['Temperatures'] == temp_range]['Frequency'].values[0]
    if temp == 0:
        return 0.0
    return rain / temp
temp = "51-60"
print(f"The probability of rain at {temp} degrees is {probability(temp):.2f}.")
'''


'''
# 13. Spam Filter Analyzer: Given the following probabilities:
# • P (T ) = 0.1
# • P (F | T ) = 0.95
# • P (F | T c) = 0.05
# Write a Python script to compute P (T | F ) using Bayes’ Theorem.

def spam_filter():
    P_T = 0.1
    P_F_given_T = 0.95
    P_F_given_not_T = 0.05
    P_not_T = 1 - P_T

    P_F = (P_F_given_T * P_T) + (P_F_given_not_T * P_not_T)

    P_T_given_F = (P_F_given_T * P_T) / P_F
    return P_T_given_F
print(f"P(T|F) = {spam_filter()}")
'''


'''
# 14. Given a discrete probability mass function (PMF), write a program to simulate the random variable
# and estimate its expected value through trials.

import random
def pmf_simulation(pmf, trials=10000):
    outcomes = list(pmf.keys())
    probabilities = list(pmf.values())
    expected_value = 0
    for _ in range(trials):
        outcome = random.choices(outcomes, probabilities)[0]
        expected_value += outcome
    return expected_value / trials
pmf = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4}
print(f"Expected value of the random variable is {pmf_simulation(pmf)}")
'''


'''
# 15. Using data from rolling a biased 10-sided die 1000 times, write a program to compute the expected
# value and variance.

import random
def pmf_simulation(pmf, trials=10000):
    outcomes = list(pmf.keys())
    probabilities = list(pmf.values())
    expected_value = 0
    for _ in range(trials):
        outcome = random.choices(outcomes, probabilities)[0]
        expected_value += outcome
    return expected_value / trials
pmf = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4}
print(f"Expected value of the random variable is {pmf_simulation(pmf)}")
'''
