# m yasar polatli
# 250201075

import numpy as np
from random import randint
import matplotlib.pyplot as plt

# simulation class
class Simulation:
    def __init__(self):
        #1000 times trials for accuracy
        trials = 1000
        self.trials = trials
        self.meanScores = []
        self.count = []

    def Simulate(self):
        # it will apply 1000 times
        for i in range(1, self.trials):
            scores = []

            # current trials that attempted
            for _ in range(1, i):
                scores.append(self.TakeChoice())

            # append data for visualize
            self.meanScores.append(np.mean(scores))
            self.count.append(i)
            # printing probability of winning continuously
            print("probability of winning: ", (np.mean(scores)))

        # shows results
        self.ShowResults()

    def TakeChoice(self):
        # determines the right answer and a guess
        prize = randint(0, 2)
        guess = randint(0, 2)

        # return 1 means win
        if prize == guess:
            return 1
        else:
            return 0

    def ShowResults(self):
        # plots graph with attempts on x-axis and mean score on y-axis
        plt.plot(self.count, self.meanScores)
        plt.show()

# simulation for switching class accordance with base class which is simulation class
class SimulationWithSwitching(Simulation):
    def TakeChoice(self):
        # determines the right answer and a guess again
        prize = randint(0, 2)
        guess = randint(0, 2)

        # creates new guesses and removes our guess
        newGuesses = [0, 1, 2]
        newGuesses.remove(guess)

        # deletes it by checking whether the prize on there or not
        if newGuesses[0] == prize:
            del newGuesses[1]
        elif newGuesses[1] == prize:
            del newGuesses[0]
        else:
            del newGuesses[randint(0, len(newGuesses)) - 1]

        guess = newGuesses[0]

        # checks and returns 1 if its correct
        if prize == guess:
            return 1
        else:
            return 0

# main program starts here with taking option to play

print("press 1 to play without switching")
print("press 2 to play with switching")
choice = int(input("How do you want to play?: "))

# calls functions according to the input received

if choice == 1:
    simulation = Simulation()
elif choice == 2:
    simulation = SimulationWithSwitching()

# base function call
simulation.Simulate()
