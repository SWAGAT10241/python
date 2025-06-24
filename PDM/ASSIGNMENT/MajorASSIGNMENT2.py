# Background
# You are a data analyst for PharmaFlow, a pharmaceutical logistics company operating across four city
# zones: Zone A, Zone B, Zone C, and Zone D. Your responsibilities include analyzing historical delivery
# data and optimizing driver allocation.
# You are given the following:
# • Historical urgent delivery requests over 100 days.
# • Delivery times per package for each zone.
# • Package volume per day per zone.
# • Driver shift duration: 6 hours per day.
# Part A: Discrete Probability (Python + NumPy)
# Given Data:
# • Zone A: 28 days with urgent requests
# • Zone B: 22 days with urgent requests
# • Zone C: 30 days with urgent requests
# • Zone D: 20 days with urgent requests
# 1. Using NumPy, compute the empirical probability distribution for urgent delivery requests across the
# zones. Represent it as a NumPy array.
# 2. What is the probability that a request comes from Zone A or Zone C?

import numpy as np
urgent_requests = np.array([28, 22, 30, 20])
total_requests = np.sum(urgent_requests)
probability_distribution = urgent_requests / total_requests
print("Empirical Probability Distribution:", probability_distribution)
probability_A_or_C = probability_distribution[0] + probability_distribution[2]
print("Probability of a request from Zone A or Zone C:", probability_A_or_C)


# Part B: Linear Equations for Staffing Optimization
# Additional Data:
# • Packages per day: Zone A (10), Zone B (15), Zone C (12), Zone D (8)
# • Delivery time (in hours): Zone A (2), Zone B (1), Zone C (1.5), Zone D (3)
# • Each driver works 6 hours per day
# Objective: Determine the minimum number of drivers per zone using matrix equations.
# 1. Write the equation for each zone:
# driver hours × number of drivers= delivery time × packages per day
# Represent the above as a matrix equation Ax = b, where:
# • x: Number of drivers in Zones A–D
# • A: Diagonal matrix with 6s on the diagonal (representing 6-hour shifts)
# • b: Total delivery work per zone (in hours)
# Solve this system using NumPy, and round up to the nearest whole number of drivers.


packages_per_day = np.array([10, 15, 12, 8])
delivery_time = np.array([2, 1, 1.5, 3])
driver_hours = 6
total_delivery_work = packages_per_day * delivery_time
A = np.diag(np.full(4, driver_hours))
b = total_delivery_work
x = np.linalg.solve(A, b)
num_drivers = np.ceil(x).astype(int)
print("Minimum number of drivers per zone:", num_drivers)
