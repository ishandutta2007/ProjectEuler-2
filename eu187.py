# ------------------------------------------------- Semiprimes ------------------------------------------------ #
#                                                                                                               #
#       A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3;      #
#       12 = 2 × 2 × 3.                                                                                         #
#                                                                                                               #
#       There are ten composites below thirty containing precisely two, not necessarily distinct,               #
#       prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.                                                     #
#                                                                                                               #
#       How many composite integers, n < 108, have precisely two, not necessarily distinct, prime factors?      #
# ------------------------------------------------------------------------------------------------------------- #
import time
from math import sqrt
from euler import primeSieve

def eu187():
    TOP = 10 ** 8

    primes = primeSieve(TOP // 2)

    i = 0
    c = 0
    l = len(primes) - 1
    
    while (primes[i] <= int(sqrt(TOP))):
        while (primes[l] > (TOP / primes[i])):
            l -= 1
            
        c += (l - i + 1)

        i += 1

    return c

if __name__ == "__main__":
    startTime = time.clock()
    print (eu187())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
