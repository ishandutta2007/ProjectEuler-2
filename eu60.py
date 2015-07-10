# -------------------------------------------- Prime pair sets ------------------------------------------------ #
#                                                                                                               #
#       The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them    #
#       in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097         #
#       are prime. The sum of these four primes, 792, represents the lowest sum for a set                       #
#       of four primes with this property.                                                                      #
#                                                                                                               #
#       Find the lowest sum for a set of five primes for which any two primes concatenate to produce            #
#       another prime.                                                                                          #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

from euler.primes import is_prime_with_history, prime_sieve

def addToSet(primesPairSet, p):
    l1 = 1
    l2 = 0

    tmp = p
    while (tmp != 0):
        l1 *= 10
        tmp //= 10
    
    for prime in primesPairSet:
        if (not is_prime_with_history(prime * l1 + p)):
            return False
        
        tmp = prime
        l2 = 1
        while (tmp != 0):
            l2 *= 10
            tmp //= 10

        if (not is_prime_with_history(p * l2 + prime)):
            return False

    return True

def genPrimesPairSet(primes, size, primesPairSet):
    if (size == 0):
        return True, sum(primesPairSet)

    for p in primes:
        if (addToSet(primesPairSet, p)):
            ret = genPrimesPairSet(primes, size - 1, primesPairSet + [p])
            if (ret[0]):
                return True, ret[1]

    return False, 0
            
def eu60():
    TOP = 10000
    FAMILY_SIZE = 5

    primes = prime_sieve(TOP)
    is_prime_with_history.HISTORY = dict([(i, False) for i in range(TOP)])
    for p in primes:
        is_prime_with_history.HISTORY[p] = True

    return genPrimesPairSet(primes, FAMILY_SIZE, [])[1]

if __name__ == "__main__":
    startTime = time.clock()
    print (eu60())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
