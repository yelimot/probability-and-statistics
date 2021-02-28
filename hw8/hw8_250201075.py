"""M. Yaşar Polatlı
     250201075
    Homework 7"""

import numpy as np
import random
import matplotlib.pyplot as plt

# lists for storing data
class1 = []
class2 = []
class3 = []
crew = []

# reading data from the file
with open("titanic_data.txt","r",encoding = "utf-8") as file:
    for i in file:
        i.split("   ")
        if i[0] == "1":
            class1.append(int(i[2]))
        if i[0] == "2":
            class2.append(int(i[2]))
        if i[0] == "3":
            class3.append(int(i[2]))
        if i[0] == "0":
            crew.append(int(i[2]))

whole = class1 + class2 + class3 + crew
rest = class2 + class3 + crew

print("The averages for the whole data, crew data, first class, second class and third class data are %.2f, %.2f, %.2f, %.2f and %.2f respectively." % (np.mean(whole), np.mean(crew), np.mean(class1), np.mean(class2), np.mean(class3)))

print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

# mean 1 as delta, to decide whether given pooled samples exceed the threshold or not.
mean1 = np.mean(crew) - np.mean(class3)

plt1 = [] # array to observe pooled samples via histogram.
for i in range(10000): # the loop for the Monte Carlo simulation.
    sameLength = min(len(crew), len(class3)) # constructed pooled array must be the same length as original ones.
    for j in range(sameLength): # loop for the generating pooled array.
        z = np.random.randint(0, sameLength)
        crew.append(class3.pop(z))
        class3.append(crew.pop(z))
    plt1.append(np.mean(crew) - np.mean(class3)) # crucial operation for simulation.
                                                 # constructs sampled array by taking the difference of their means.

# plotting histograms:
plt.figure()
cdf1 = plt.hist(plt1, 100)
plt.figure()
# plotting histograms in same plot command.
plt.plot(cdf1[1][0:100], np.cumsum(cdf1[0])/cdf1[0].sum())
# pValue is found in this step by looking at where the intersections of these lines are.
pValue1 = np.interp(mean1, cdf1[1][0:100], np.cumsum(cdf1[0]) / cdf1[0].sum())
# marking the pValue in the same graph.
plt.axvline(mean1, 0, pValue1, color='orange')
plt.show()

print("The p-value for %.2f difference and less between means for crew and 3rd class is: %.2f" % (mean1, pValue1))

print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

# exactly same implementation but the pValue which explained below:
plt2 = []
mean2 = np.mean(class1) - np.mean(rest)

for i in range(10000):
    sameLength = min(len(class1), len(rest))
    for j in range(sameLength):
        z = np.random.randint(0, sameLength)
        class1.append(rest.pop(z))
        rest.append(class1.pop(z))
    plt2.append(np.mean(class1) - np.mean(rest))

plt.figure()
cdf2 = plt.hist(plt2, 100)
plt.figure()
plt.plot(cdf2[1][0:100], np.cumsum(cdf2[0])/cdf2[0].sum())

pValue2 = np.interp(mean2, cdf2[1][0:100], np.cumsum(cdf2[0]) / cdf2[0].sum()) # since the interpolation of the cdf and the mean of that sampling are not cross each other, pValue is calculated as 1 here.
plt.show()

if pValue2 == 1: # but it is not '1' mathematically, it equals '0', this step makes that correction.
    pValue2 = 0

print("The p-value for %.2f difference and more in means for 1st class and the rest is: %.2f" % (mean2, pValue2))
