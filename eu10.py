# ----------------------- Summation of primes ------------------------- #
#                                                                       #
#       The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.           #
#       Find the sum of all the primes below two million.               #
# --------------------------------------------------------------------- #
import time
import math
import operator
import functools
from euler import primeSieve

def eu10():
    TOP = 2000000

    primes = primeSieve(TOP)
       
    return sum(primes)

startTime = time.clock()
print (eu10())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
