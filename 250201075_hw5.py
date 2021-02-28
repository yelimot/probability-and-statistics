# M. Yaşar Polatlı
# 250201075
"""
As a starting note I would like to say that I call the functions many times to get correct observations about
samples. And it takes some time (about 50 seconds) in my computer. I hope your computer faster than mine but if not so
please wait for the code to finish its operations.
"""

import random
import numpy as np
import math


def rollDiceSum():  # Sums randomized rolled dices.
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    rollSum = roll1 + roll2
    return rollSum

def gameMachine():  # Function represents the game which name is craps.
    firstRoll = rollDiceSum()  # Keep the value of first some in order to evaluations.
    if firstRoll == 7 or firstRoll == 11:
        return True

    elif firstRoll == 2 or firstRoll == 3 or firstRoll == 12:
        return False

    else:
        while True:
            otherRoll = rollDiceSum()  # otherRoll comparisons continues until it equals the kept firstRoll or equals 7.
            if firstRoll == otherRoll:
                return True
            if otherRoll == 7:
                return False

# GamblerA function which includes his betting strategy.
def gamblerA(hisMoney):
    betA = 1
    temp = hisMoney  # temp, holds the initial money to find the gain at the end of the game.
    while ((2 * temp) > hisMoney) and hisMoney >= betA:
        if gameMachine():
            hisMoney += betA
        else:
            hisMoney -= betA
            betA *= 2

    return hisMoney - temp  # this is gain, and function returns the gain.

# GamblerB function which includes her betting strategy.
def gamblerB(hisMoney):
    roundNo = 1
    temp = hisMoney  # temp, holds the initial money to find the gain at the end of the game.
    betB = 1  # dummy variable to start the while loop with the correct condition (hisMoney >= betB).
    
    while (hisMoney - temp < 500) and hisMoney >= betB:
        """ In this function we can use 'inverse transform method' in order to get the betB function with some x which 
          is randomly generated pseudo numbers in the interval of 0<x<r. Since we have pdf, we can reach the cdf 
          by integrate the pdf. And after that inverse of CDF enables us to apply inverse transform method. """
        x = np.random.uniform(0, roundNo)  # randomly generated numbers in (0,r].
        betB = math.sqrt(x) * roundNo  # correct betB (not dummy variable); inverse of the CDF.

        if gameMachine():
            hisMoney += betB
            roundNo += 1
        else:
            hisMoney -= betB
            roundNo += 1

    return hisMoney - temp  # gain

# *********************************************************************************************************************

#  Simulations: All the simulations are inside of same while loop.


possibilitySamples = np.array([])  # Creation of empty numpy arrays to store generated samples for each question.
samplesA = np.array([])
samplesA2 = np.array([])
samplesB = np.array([])
samplesB2 = np.array([])

x = 0
while x < 50000:  # Calls functions 50000 times, generates samples each call, appends them to the corresponding array.
    possibilitySamples = np.append(possibilitySamples, gameMachine())
    samplesA = np.append(samplesA, gamblerA(1000))
    samplesA2 = np.append(samplesA2, gamblerA(1000000))
    samplesB = np.append(samplesB, gamblerB(100))
    samplesB2 = np.append(samplesB2, gamblerB(10000))
    x += 1

#  Taking mean of these samples gives the expected value.
print("1. Probability of winning a round of craps: ", np.mean(possibilitySamples))
print("2. Expected gain of the gambler A if he has $1.000: ", np.mean(samplesA))
print("3. Expected gain of the gambler A if he has $1.000.000: ", np.mean(samplesA2))
print("4. Expected gain of the gambler B if he has $100: ", np.mean(samplesB))
print("5. Expected gain of the gambler B if he has $10.000: ", np.mean(samplesB2))
