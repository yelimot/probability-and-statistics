# M. Yasar Polatli
# 250201075

import numpy as np
from matplotlib import pyplot as plt
import math

numSamples = 100000
numBins = 100

# For the random variable Y, Fy(y) = y**2. this is cdf of Y. we need to find pdf of Y to apply to rejection method.
# So let us find pdf by derivating the cdf: fy(y) = 2*y.
# This is probability density function of Y.
def fy(y):
    if y < 0:
        fy = 0
    elif y <= 1:
        fy = 2*y
    else:
        fy = 0
    return fy

# At this step we generate arrays that we are going to use to plot graph. And plot the graph.
Fy_array = []
ind = []
for i in range(-100, 200):
    Fy_array.append(fy(i / 100))
    ind.append(i / 100)
plt.figure()
plt.title('Pdf of Y')
plt.plot(ind, Fy_array)

# rejection method
print('----------------------------- Sample rejection method -----------------------------')

# These are the extended borderlines of pdf.
c = 3
a = -1
b = 2
Y = []
i = 0

# Rejection method, briefly checks the generated random numbers whether less than the pdf or not. And append them to a
# array to plot the histogram.
while i < numSamples:
    u = np.random.rand()
    v = np.random.rand()
    x = (b - a) * u + a
    y = c * v
    if y <= fy(x):
        Y.append(x)
        i = i + 1

# Histograms.
plt.figure()
plt.title('Histogram of the generated Y samples (pdf)')
hY = plt.hist(Y, numBins, density=True)
plt.figure()
plt.title('Normalized cumulative sum of histogram values for the generated Y samples (cdf)')
plt.plot(hY[1][0:numBins], np.cumsum(hY[0]) / hY[0].sum())
plt.show()

print('-------------------------- Inverse transformation method --------------------------')


# For the random variable X, fx(x) (pdf) is given. We are going to find cdf of X by integrating the given pdf.

# Cdf of X.
def Fx(x):
    if x < 0:
        return 0
    elif x <= 10:
        return ((9 * np.log(np.abs(3 * x + 2))) / 25) - (9 * np.log(2)) / 25
    else:
        return 0

# Cdf distribution graph.
fx_array = []
ind = []
for i in range(0, 1000):
    fx_array.append(Fx(i / 100))
    ind.append(i / 100)
plt.figure()
plt.title('Cdf of X')
plt.plot(ind, fx_array)

# Inverse of cdf to use in inverse transformation method.
def Fx_inverse(u):
    return (np.e ** ((25 * u + 9 * np.log(2)) / 9) - 2) / 3

# Inverse transform method.
U = []
X = []
for i in range(numSamples):
    U.append(np.random.rand())
    X.append(Fx_inverse(U[i]))

# Histograms.
plt.figure()
plt.title('Histograms of the generated U and X samples (pdf)')
hU = plt.hist(U, numBins, alpha=0.5, density=True)
hX = plt.hist(X, numBins, alpha=0.5, density=True)
plt.figure()
plt.title('Normalized cumulative sum of histogram values for the generated U and X samples (cdf)')
plt.plot(np.cumsum(hU[0]) / hU[0].sum())
plt.plot(np.cumsum(hX[0]) / hX[0].sum())
plt.show()
