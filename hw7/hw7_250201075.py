"""
M. Yaşar Polatlı
250201075
HW07
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import binom
from math import pow

# 2 paramaters; n = 40, p = 0.3
# theoretical expected value of this distribution is 40*0.3 = 12
# theoretical variance of this distribution is 40*0.3*0.7 = 8.4

# I created myself the simulation function for binomial distribution, due to the negligence of being requested.
# But i didn't use it in my code becasue it is slower than binom.rvs in my old computer. But it is completely working, you can try.

# Samples is a list of the number of successes from each trial of N experiments.
def binomial_dist(N):
    samples = []
    for i in range(N):
        successes = 0
        for i in range(40):
            if random.uniform(0, 1) < 0.3:
                successes += 1
        samples.append(successes)
    return samples

# in order to apply Method of Moments we need the mean of the sample, this function handles it.
def sample_mean(N):
    expc = np.mean(binom.rvs(40, 0.3, size=N)) # you can replace binom.rvs with my function 'binomial_dist(N)'
    return expc                                 # but it is slower.

# in order to apply Method of Moments we need the variance of the sample, this function handles it.
def sample_variance(N):
    varc = np.var(binom.rvs(40, 0.3, size=N))
    return varc

# estimated p parameter using outcome equation from Method of Moments.
def estimated_p(N):
    return 1 - (sample_variance(N)/sample_mean(N))

# estimated n parameter using outcome equation from Method of Moments.
def estimated_n(N):
    return pow(sample_mean(N),2)/(sample_mean(N) - sample_variance(N))

# histogram plotting and printing the results for p.
def printry_p():
    plt.figure()
    plt.title("Histogram for estimated p")
    for N in [200,800,3200]:
        arr1 = []

        for i in range(1000): # simulation loop for 1000 times.
            arr1.append(estimated_p(N))

        if N == 200: # plots the graphs according to N with coloring.
            plt.hist(arr1, 100, density=True, color="skyblue", label='200', alpha=0.7)
        if N == 800:
            plt.hist(arr1, 100, density=True, color="navajowhite", label='800', alpha=0.7)
        if N == 3200:
            plt.hist(arr1, 100, density=True, color="lightgreen", label='3200', alpha=0.7)
        # prints the results for each N value.
        print("Mean for estimated p for sample size of ", N, "is ", np.mean(arr1))
        print("Standard deviation for estimated p for sample size of ", N, "is ", np.std(arr1))
    plt.legend()
    plt.show()

# histogram plotting and printing the results for p.
def printry_n():
    plt.figure()
    plt.title("Histogram for estimated n")
    for N in [200,800,3200]:
        arr2 = []

        for i in range(1000):
            arr2.append(estimated_n(N))

        if N == 200:
            plt.hist(arr2, 100, density=True, color="skyblue", label='200', alpha=0.7)
        if N == 800:
            plt.hist(arr2, 100, density=True, color="navajowhite", label='800', alpha=0.7)
        if N == 3200:
            plt.hist(arr2, 100, density=True, color="lightgreen", label='3200', alpha=0.7)
        print("Mean for estimated n for sample size of ", N, "is ", np.mean(arr2))
        print("Standard deviation for estimated n for sample size of ", N, "is ", np.std(arr2))
    plt.legend()
    plt.show()

# function calls to observe the results.
printry_n()
printry_p()
