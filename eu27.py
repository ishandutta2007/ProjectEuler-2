# ------------------------------------------- Quadratic primes ------------------------------------------------ #
#                                                                                                               #
#       Euler discovered the remarkable quadratic formula:                                                      #
#                                                                                                               #
#                                           n² + n + 41                                                         #
#                                                                                                               #
#       It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However,   #
#       when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,                                        #
#       and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.                                    #
#                                                                                                               #
#       The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive    #
#       values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.                          #
#                                                                                                               #
#       Considering quadratics of the form:                                                                     #
#                                                                                                               #
#                               n² + an + b, where |a| < 1000 and |b| < 1000                                    #
#                                                                                                               #
#                               where |n| is the modulus/absolute value of n                                    #
#                               e.g. |11| = 11 and |−4| = 4                                                     #
#                                                                                                               #
#       Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum   #
#       number of primes for consecutive values of n, starting with n = 0.                                      #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

from euler.primes import is_prime_with_history

def genQuadraticFormula(a, b):
    n = 0
    
    while (True):
        yield (n**2 + a * n + b)
        n += 1

def eu27():
    MAX = 1000

    max_len = 0
    ret = 0
    
    for a in range(1 - MAX, MAX + 1):
        for b in range(1 - MAX, MAX + 1):
            p = genQuadraticFormula(a, b)
            l = 0
            t = next(p)
            while (is_prime_with_history(t)):
                l += 1
                t = next(p)

            if (l > max_len):
                max_len = l
                ret = a * b
                
    return ret

startTime = time.clock()
print (eu27())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
