# m yasar polatli
# 250201075

import numpy as np
from matplotlib import pyplot as plt

# we can find the p by using the formula '(b-a)u + a = p'

p = 0.2
N = 20
Y = []
for j in range(1000):

    # an array for storing values less or equal than sub-intervals
    X = [[],[],[],[],[]]

    for i in range(N):
        u = np.random.rand()
        # generation of sub-intervals
        r = np.linspace(0,p,5)
        x = u < r[0]
        X[0].append(x)
        x = u < r[1]
        X[1].append(x)
        x = u < r[2]
        X[2].append(x)
        x = u < r[3]
        X[3].append(x)
        x = u < r[4]
        X[4].append(x)

    # summation of successes
    y = sum(X[0]) + sum(X[1]) + sum(X[2]) + sum(X[3]) + sum(X[4])
    Y.append(y)

plt.figure()
plt.hist(Y, bins=range(0, N+1), density=True)
plt.show()
