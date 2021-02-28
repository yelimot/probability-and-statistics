Probability and statistics:

Homeworks and coding exercises from CENG 222 (IZTECH).

- HW1: Write a small code in Python to visualize the relation between p and variance for Berounlli distribution. Plot a p-variance graph and comment on the result (just with a couple of comment lines in the code).

- HW2: Implementation for Binomial distribution by simulating Bernoulli trials is already given in the course materials. Generate the same distribution by using sub-intervals approach that is proposed for any arbitrary discrete distribution. Plot the histogram of 1000 generated samples.

- HW3: Investigate the Monty Hall problem. Implement the simulation of the game with two possible strategies (change the selected door / keep the selected door) and calculate the probability of winning for both strategies using the simulation.
 
- HW4: {Monte Carlo Simulations - Continuous} In this assignment you are expected to implement the rejection method for Y and the inverse transformation method for X.
  -  For Y, plot the pdf of the distribution. 
  -  For X, plot the cdf of the distribution. 
  -  For both Y and X, plot the histogram and the cumulative sum of histogram values of the generated samples.
 
- HW5: Two gamblers start playing craps with two different strategies: 
1. Gambler A starts with betting $1 and doubles the bet after every loss, so that the first win would recover all previous losses plus win a profit equal to the original stake. He stops if he doubles his gambling money or he does not have enough money for the next bet. 
2. Gambler B bets an amount with the probability density function f(x) = (2*x) / (r^2), 0<x<r, where r is the current round number. He stops if he wins 5500 or does not have enough money for the next bet. 

Craps rules are as the following: Each round, two dice are rolled: If their sum is 7 or 11, gambler wins. If the sum is 2, 3, or 12, gambler lose. Otherwise, the dice are rolled until either the initial sum is repeated, in which case the gambler wins or a sum of 7, in which case the gambler loses.

By using Monte Carlo method, 
1. calculate the probability of winning a round of craps. 
2. calculate the expected gain of the gambler A if he has $1.000 for gambling. 
3. calculate the expected gain of the gambler A if he has $1.000.000 for gambling. 
4. calculate the expected gain of the gambler B if he has $100 for gambling. 
5. calculate the expected gain of the gambler B if he has $10.000 for gambling. 
