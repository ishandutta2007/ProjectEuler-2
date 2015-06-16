# --------------------------------------------- Spiral primes ------------------------------------------------- #
#                                                                                                               #
#       Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side            #
#       length 7 is formed.                                                                                     #
#                                                                                                               #
#                                          37 36 35 34 33 32 31                                                 #
#                                          38 17 16 15 14 13 30                                                 #
#                                          39 18  5  4  3 12 29                                                 #
#                                          40 19  6  1  2 11 28                                                 #
#                                          41 20  7  8  9 10 27                                                 #
#                                          42 21 22 23 24 25 26                                                 #
#                                          43 44 45 46 47 48 49                                                 #
#                                                                                                               #
#       It is interesting to note that the odd squares lie along the bottom right diagonal,                     #
#       but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime;      #
#       that is, a ratio of 8/13 ≈ 62%.                                                                         #
#                                                                                                               #
#       If one complete new layer is wrapped around the spiral above, a square spiral with side length 9        #
#       will be formed. If this process is continued, what is the side length of the square spiral for which    #
#       the ratio of primes along both diagonals first falls below 10%?                                         #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

def isProbablePrime(n, _precision_for_huge_n=8):
    """ Using Miller-Rabin algorithm """
    def _try_composite(a, d, n, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n  is definitely composite

    if n in isProbablePrime._known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in isProbablePrime._known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in isProbablePrime._known_primes[:_precision_for_huge_n])
isProbablePrime._known_primes = [2, 3]
#isProbablePrime._known_primes += [x for x in range(5, 1000, 2) if isProbablePrime(x)]

def eu58():
    PERCENTAGE = 0.1
   
    l = 3
    n = 3
    d = 4

    while (n / d >= PERCENTAGE):
        l += 2
        if (isProbablePrime(l ** 2)):
            n += 1
        if isProbablePrime(l ** 2 - l + 1):
            n += 1
        if isProbablePrime((l - 2) ** 2 + l - 1):
            n += 1
        if isProbablePrime((l - 2) ** 2 + 2 * l - 2):
            n += 1
            
        d += 4

    return l - 2

if __name__ == "__main__":
    startTime = time.clock()
    print (eu58())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
