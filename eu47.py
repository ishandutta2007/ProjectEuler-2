# --------------------------------------- Distinct primes factors --------------------------------------------- #
#                                                                                                               #
#       The first two consecutive numbers to have two distinct prime factors are:                               #
#                                                                                                               #
#                                           14 = 2 × 7                                                          #
#                                           15 = 3 × 5                                                          #
#       The first three consecutive numbers to have three distinct prime factors are:                           #
#                                                                                                               #
#                                           644 = 2² × 7 × 23                                                   #
#                                           645 = 3 × 5 × 43                                                    #
#                                           646 = 2 × 17 × 19.                                                  #                                                                                                               #
#                                                                                                               #
#       Find the first four consecutive integers to have four distinct prime factors. What is the first         #
#       of these numbers?                                                                                       #
# ------------------------------------------------------------------------------------------------------------- #
import time
from euler import getDistinctFactors

def eu47():
    TARGET = 4
    
    n = 2
    while (True):
        if (len(getDistinctFactors(n)) != TARGET):
            n += 1
            continue
        if (len(getDistinctFactors(n + 1)) == TARGET and
            len(getDistinctFactors(n + 2)) == TARGET and
            len(getDistinctFactors(n + 3)) == TARGET ):
                return n
        n += 1
                
if __name__ == "__main__":
    startTime = time.clock()
    print (eu47())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
