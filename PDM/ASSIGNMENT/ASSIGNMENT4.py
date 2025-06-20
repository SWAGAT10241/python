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
        roll = random.randint(1, 7)
        if roll == 6:
            count += 1
    return count
print(f"Rolling a die 1000 times gives us {die()} times of rolling a 6.")
'''

# 3. Write a program to simulate the birthday problem to find out the probability that in a group of 23
# people, at least 2 share the same birthday.





'''
# 4. Given a bag with 3 red balls and 2 blue balls, write a program to find the probability of drawing 2 red
# balls without replacement.

from scipy.special import comb
def probability():
    total,red,blue = 5,3,2
    return (comb(red, 2) * comb(blue, 0)) / comb(total, 2)
print(f"The probability of drawing 2 red balls without replacement is {probability()}.")
'''


# # 5. Write a code to simulate the rolling of two six-sided dice 5000 times. Compute the experimental probability 
# # of getting a sum of 7.

# import random
# def dice(n = 5000):
#     count = 0
#     for i in range(n):
#         dice = random.randint(1,13)
#         if dice == 7:
#             count += 1
#     return count
# print(f"Rolling two dice 5000 times gives us {dice()} times of getting a sum of 7.")


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

# 7. Write a code to compute the probability of getting exactly k heads in n coin tosses for a fair coin.

import random
def coin(n):
    head = 0
    for i in range(n):
        toss = random.randint(0, 1)
        if toss == 0:
            head += 1
    return head
n = int(input("Enter the number of tosses: "))
print(f"Tossing a coin {n} times gives us {coin(n)} heads. ")

# 8. Plot the distribution of the number of heads when tossing 50 coins. Use matplotlib to visualize
# the results.
# 9. A sports analyst provides the following probabilities for an upcoming soccer match:
# • Probability that Real Madrid wins: P (R) = 0.40
# • Probability that FC Barcelona wins: P (B) = 0.50
# The only other possible outcome is a draw. Write a Python program that:
# (a) Stores the probabilities of Real Madrid and Barcelona winning.
# (b) Calculates and prints the probability of a draw.
# (Hint: Use the fact that the sum of all disjoint outcomes must be 1.)
# 10. Given a dataset of weather (e.g., temperature and rainfall), write a program to calculate the conditional
# probability that it rained given a certain temperature range.
# 11. Write a code to implement a function that uses Bayes’ Theorem to compute P (A | B) given P (B |
# A), P (A), and P (B).
# 12. Given a dictionary with temperature ranges and corresponding rain frequencies, write a code to calculate
# the conditional probability that it rained, given a specific temperature range.
# 13. Spam Filter Analyzer: Given the following probabilities:
# • P (T ) = 0.1
# • P (F | T ) = 0.95
# • P (F | T c) = 0.05
# Write a Python script to compute P (T | F ) using Bayes’ Theorem.
# 14. Given a discrete probability mass function (PMF), write a program to simulate the random variable
# and estimate its expected value through trials.
# 15. Using data from rolling a biased 10-sided die 1000 times, write a program to compute the expected
# value and variance.
# 16. Given a network of 5 web pages and their links (from a reference book), write code to perform two
# iterations of the PageRank algorithm.
# 17. Write a code to simulate a random surfer clicking links across a small internet of pages using a
# damping factor. Estimate and plot the visit frequency for each page.
