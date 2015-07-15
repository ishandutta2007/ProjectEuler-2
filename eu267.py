# ----------------------------------------------------------------- Billionaire --------------------------------------------------------------- #
#                                                                                                                                               #
#       You are given a unique investment opportunity.                                                                                          #
#                                                                                                                                               #
#       Starting with £1 of capital, you can choose a fixed proportion, f, of your capital to bet on a fair coin toss repeatedly                #
#       for 1000 tosses.                                                                                                                        #
#                                                                                                                                               #
#       Your return is double your bet for heads and you lose your bet for tails.                                                               #
#                                                                                                                                               #
#       For example, if f = 1/4, for the first toss you bet £0.25, and if heads comes up you win £0.5 and so then have £1.5.                    #
#       You then bet £0.375 and if the second toss is tails, you have £1.125.                                                                   #
#                                                                                                                                               #
#       Choosing f to maximize your chances of having at least £1,000,000,000 after 1,000 flips,                                                #
#       what is the chance that you become a billionaire?                                                                                       #
#                                                                                                                                               #
#       All computations are assumed to be exact (no rounding),                                                                                 #
#       but give your answer rounded to 12 digits behind the decimal point in the form 0.abcdefghijkl.                                          #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from math import log, ceil

from euler.combinatorics import nCk
from euler.calculus import gradient_descent

def eu267():
    def f(x):
        n = 9 * log(10) - 1000 * log(1 - x)
        d = log(1 + 2 * x) - log(1 - x)

        return n / d
    
    x_min = gradient_descent(f, 0, 1)

    heads = ceil(f(x_min))

    # Using cumulative distribution function
    p = 0
    for i in range(heads):
        p += nCk(1000, i)
    p /= (2 ** 1000)
    
    return round(1 - p, 12)
        
if __name__ == "__main__":
    startTime = time.clock()
    print (eu267())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
