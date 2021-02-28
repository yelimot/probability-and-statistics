# M. Yaşar Polatlı
# 250201075

import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import semicircular

# Experiment 1:

s1 = np.random.uniform(0, 1, 50000)  # 50000 values from standard uniform distribution (0,1) independently.

samples1 = [np.sum(random.choices(s1, k=2)) for i in range(50000)]  # 50000 sum samples from randomly chosen 2 values.

print("Experiment 1: ")
print("Sample mean is ", np.mean(samples1))
print("Sample standard deviation is ", np.std(samples1))
plt.figure()
plt.title("Experiment 1: Histogram for generated random variables")
plt.hist(s1, 100, density=True)
plt.show()
plt.title("Experiment 1: Histogram for sums of generated random variables")
plt.hist(samples1, 100, density=True)
# initializations for theoretical normal distribution curve
mu = np.mean(samples1)
sigma = np.std(samples1)
x = np.linspace(mu - 6*sigma, mu + 6*sigma, 200)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Experiment 2:

s2 = np.random.uniform(0, 1, 50000)  # 50000 values from standard uniform distribution (0,1) independently.

samples2 = [np.sum(random.choices(s2, k=10)) for i in range(50000)]  # sum samples of randomly chosen 10 values.

print("Experiment 2: ")
print("Sample mean is ", np.mean(samples2))
print("Sample standard deviation is ", np.std(samples2))
plt.figure()
plt.title("Experiment 2: Histogram for sums of generated random variables")
plt.hist(samples2, 100, density=True)
# initializations for theoretical normal distribution curve
mu = np.mean(samples2)
sigma = np.std(samples2)
x = np.linspace(mu - 6*sigma, mu + 6*sigma, 200)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Experiment 3:

s3 = np.random.uniform(0, 1, 50000)  # 50000 values from standard uniform distribution (0,1) independently.

samples3 = [np.sum(random.choices(s3, k=50)) for i in range(50000)]  # sum samples of randomly chosen 50 values.

print("Experiment 3: ")
print("Sample mean is ", np.mean(samples3))
print("Sample standard deviation is ", np.std(samples3))
plt.figure()
plt.title("Experiment 3: Histogram for sums of generated random variables")
plt.hist(samples3, 100, density=True)
# initializations for theoretical normal distribution curve
mu = np.mean(samples3)
sigma = np.std(samples3)
x = np.linspace(mu - 6*sigma, mu + 6*sigma, 200)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Experiment 4:

samples4 = np.array([])   # Array for sums of generated random variables.
samplesG = []   # Array for generated random variables.

i = 0
while i < 10000:    # Simulation continues 10000 times.

    sSum = 0  # Holds total value to check the conditions.
    sCount = 0  # Holds number of values which requested 100.

    while sCount < 101:  # Number of values is 100.
        if sSum < 40:
            a1 = np.random.uniform(0.5, 1.5)
            sSum += a1
            samplesG.append(a1)  # Generated random variables added corresponding array to observe via histogram.
        else:
            a2 = np.random.uniform(-0.5, 0.5)
            sSum += a2
            samplesG.append(a2)  # Generated random variables added corresponding array to observe via histogram.
        sCount += 1

    samples4 = np.append(samples4, sSum)  # Appends sums to corresponding array to observe whether it converges to normal or not.

    i += 1

print("Experiment 4: ")
print("Sample mean is ", np.mean(samples4))
print("Sample standard deviation is ", np.std(samples4))

plt.figure()
plt.title("Experiment 4: Histogram for generated random variables")
plt.hist(samplesG, 100, density=True)
plt.show()

plt.title("Experiment 4: Histogram for sums of generated random variables")
plt.hist(samples4, 100, density=True)
# initializations for theoretical normal distribution curve
mu = np.mean(samples4)
sigma = np.std(samples4)
x = np.linspace(mu - 6*sigma, mu + 6*sigma, 200)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Experiment 5:

s = semicircular.rvs(2, 1, size=50000)  # 50000 randomly generated values from a distribution of semi-circle of radius 1 centered at 2.

samples5 = [np.sum(random.choices(s, k=2)) for i in range(50000)]  # Number of values is 2.

print("Experiment 5: ")
print("Sample mean is ", np.mean(samples5))
print("Sample standard deviation is ", np.std(samples5))
plt.figure()
plt.title("Experiment 5: Histogram for generated random variables")
plt.hist(s, 100, density=True)
plt.show()
plt.title("Experiment 5: Histogram for sums of generated random variables")
plt.hist(samples5, 100, density=True)
# initializations for theoretical normal distribution curve
mu = np.mean(samples5)
sigma = np.std(samples5)
x = np.linspace(mu - 6*sigma, mu + 6*sigma, 200)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Experiment 6:

samples6 = [np.sum(random.choices(s, k=10)) for i in range(50000)]  # Number of values is 10.

print("Experiment 6: ")
print("Sample mean is ", np.mean(samples6))
print("Sample standard deviation is ", np.std(samples6))
plt.figure()
plt.title("Experiment 6: Histogram for sums of generated random variables")
plt.hist(samples6, 100, density=True)
# initializations for theoretical normal distribution curve
mu = np.mean(samples6)
sigma = np.std(samples6)
x = np.linspace(mu - 6*sigma, mu + 6*sigma, 200)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Experiment 7:

samples7 = [np.sum(random.choices(s, k=50)) for i in range(50000)]  # Number of values is 50.

print("Experiment 7: ")
print("Sample mean is ", np.mean(samples7))
print("Sample standard deviation is ", np.std(samples7))
plt.figure()
plt.title("Experiment 7: Histogram for sums of generated random variables")
plt.hist(samples7, 100, density=True)
# initializations for theoretical normal distribution curve
mu = np.mean(samples7)
sigma = np.std(samples7)
x = np.linspace(mu - 6*sigma, mu + 6*sigma, 200)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()
