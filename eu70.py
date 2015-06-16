# ------------------------------------------- Totient permutation ----------------------------------------- #
#                                                                                                           #
#       Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine            #
#       the number of positive numbers less than or equal to n which are relatively prime to n.             #
#       For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.  #
#                                                                                                           #
#       The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.              #
#                                                                                                           #
#       Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.             #
#                                                                                                           #
#       Find the value of n, 1 < n < 10&7, for which φ(n) is a permutation of n and the ratio n/φ(n)        #
#       produces a minimum.                                                                                 #
# --------------------------------------------------------------------------------------------------------- #
import time
import math
from itertools import product
from euler import primeSieve, isPermutation

def eu70():
    TOP = 10 ** 7
    RATIO = 0.3
    
    primes = primeSieve(int((1 + RATIO) * math.sqrt(TOP)))
    primes = [p for p in primes if p > int((1 - RATIO) * math.sqrt(TOP))]

    minRatio = TOP
    n = "Didn't find"

    for i in range(len(primes)):
        p1 = primes[i]

        for j in range(len(primes)):
            p2 = primes[j]

            curN = p1 * p2
            if (curN > TOP):
                break
            
            curPhi = (p1 - 1) * (p2 - 1)

            if isPermutation(curN, curPhi):
                if (curN / curPhi) < minRatio:
                    n = curN
                    minRatio = curN / curPhi
                
    return n
    
if __name__ == "__main__":
    startTime = time.clock()
    print (eu70())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
