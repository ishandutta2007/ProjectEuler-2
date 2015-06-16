# ------------------------ Smallest multiple -------------------------- #
#                                                                       #
#       2520 is the smallest number that can be divided by              #
#       each of the numbers from 1 to 10 without any remainder.         #
#       What is the smallest positive number that is                    #
#       evenly divisible by all of the numbers from 1 to 20?            #
# --------------------------------------------------------------------- #
import time
import math
import operator
import functools
from euler import primeSieve

def eu5():
    TOP = 20

    primes = primeSieve(TOP)
    exponents = [int(math.log10(TOP)//math.log10(p)) for p in primes]
    
    return functools.reduce(operator.mul, [primes[i] ** exponents[i] for i in range(len(primes))])

startTime = time.clock()
print (eu5())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
