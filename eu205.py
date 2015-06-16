# -------------------------------------- Dice Game -------------------------------------------- #
#                                                                                               #
#       Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.        #
#       Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.        #
#                                                                                               #
#       Peter and Colin roll their dice and compare totals: the highest total wins.             #
#       The result is a draw if the totals are equal.                                           #
#                                                                                               #
#       What is the probability that Pyramidal Pete beats Cubic Colin?                          #
#       Give your answer rounded to seven decimal places in the form 0.abcdefg                  #
# --------------------------------------------------------------------------------------------- #
import time
from itertools import product
from fractions import Fraction

def eu205():
    peter   = [0 for i in range(36 + 1)]
    colin   = [0 for i in range(36 + 1)]
    colinF  = [0 for i in range(36 + 1)]
             
    for p in product(range(1, 4 + 1), repeat = 9):
        peter[sum(p)] += 1

    for p in product(range(1, 6 + 1), repeat = 6):
        colin[sum(p)] += 1

    for i in range(1, len(colin)):
        colinF[i] = colinF[i - 1] + colin[i]

    peterT = 4 ** 9
    colinT = 6 ** 6

    prob = Fraction()
    
    for i in range(1, len(peter)):
        prob += Fraction(peter[i], peterT) * Fraction(colinF[i - 1], colinT)
        
    return round(prob.numerator / prob.denominator, 7)

if __name__ == "__main__":
    startTime = time.clock()
    print (eu205())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
