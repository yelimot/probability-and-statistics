import matplotlib.pyplot as plt
import numpy as np

p = np.arange(0., 1., 0.01) # returns an array which consist of evenly spaced values from 0 to 1.
x1 = 1 #indicator of the probability of x1 
x2 = 0 #indicator of the probability of x2
expected = x1*p + x2*(1-p) # expected value of bernuolli distribution is basically equals p.
variance = ((x1 - expected)**2)*p + ((x2 - expected)**2)*(1-p)

plt.plot(p,variance)
plt.xlabel("p")
plt.ylabel("variance")
plt.show()
