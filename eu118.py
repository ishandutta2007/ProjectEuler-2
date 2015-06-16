# ------------------------------------------ Pandigital prime sets -------------------------------------------- #
#                                                                                                               #
#       Using all of the digits 1 through 9 and concatenating them freely to form decimal integers,             #
#       different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements           #
#       belonging to it are prime.                                                                              #
#                                                                                                               #
#       How many distinct sets containing each of the digits one through nine exactly once contain              #
#       only prime elements?                                                                                    #
# ------------------------------------------------------------------------------------------------------------- #
import time
import itertools

from euler.primes import prime_sieve
from euler.primes import is_probable_prime
    
def prime_sets(n, last, l):    
    if l == 0:
        return 1

    c = 0
    e = 10
    for i in range(1, l + 1):
        p = n % e
        r = n // e

        if p > last and (p in prime_sets.primes if p < 10 ** 7 else is_probable_prime(p)):
            c += prime_sets(r, p, l - i)

        e *= 10

    return c    
prime_sets.primes = []

def eu118():
    NO_OF_DIGITS = 9
    DIGITS = list([str(d) for d in range(1, NO_OF_DIGITS + 1)])

    prime_sets.primes = frozenset(prime_sieve(10 ** 7))
    
    count = 0
    for p in itertools.permutations(DIGITS):
        n = int("".join(p))

        count += prime_sets(n, 0, NO_OF_DIGITS)
        
    return count

if __name__ == "__main__":
    startTime = time.clock()
    print (eu118())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
