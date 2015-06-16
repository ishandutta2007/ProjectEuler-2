# --------------------------------------- Square root digital expansion --------------------------------------- #
#                                                                                                               #
#       It is well known that if the square root of a natural number is not an integer, then it is irrational.  #
#       The decimal expansion of such square roots is infinite without any repeating pattern at all.            #
#                                                                                                               #
#       The square root of two is 1.41421356237309504880..., and the digital sum of the first                   #
#       one hundred decimal digits is 475.                                                                      #
#                                                                                                               #
#       For the first one hundred natural numbers, find the total of the digital sums of the first one hundred  #
#       decimal digits for all the irrational square roots.                                                     #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math
from decimal import *

def eu80():
    r = [i ** 2 for i in range(1, 10 + 1)]
    ir = [i for i in range(1, 100 + 1) if i not in r]

    getcontext().prec = 102

    c = 0
    for n in ir:
        d = Decimal(n).sqrt()
        d_s = str(d).replace('.', '')
        
        c += sum([int(i) for i in d_s[:100]])

    return c

if __name__ == "__main__":
    startTime = time.clock() 
    print (eu80())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
