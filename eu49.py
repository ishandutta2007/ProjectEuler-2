# ------------------------------------------ Prime permutations ----------------------------------------------- #
#                                                                                                               #
#       The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,                #
#       is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit            #
#       numbers are permutations of one another.                                                                #
#                                                                                                               #
#       There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, #
#       but there is one other 4-digit increasing sequence.                                                     #
#                                                                                                               #
#       What 12-digit number do you form by concatenating the three terms in this sequence?                     #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math
import functools
import itertools

def isPrime(n):
    if (n in isPrime.HISTORY):
        return isPrime.HISTORY[n]

    """ Checks if n is prime """
    if n < 0:
        isPrime.HISTORY[n] = False
        return False
    
    if n == 1:
        isPrime.HISTORY[n] = False
        return False
    if n < 4:
        isPrime.HISTORY[n] = True
        return True
    if n % 2 == 0:
        isPrime.HISTORY[n] = False
        return False
    if n < 9:
        isPrime.HISTORY[n] = True
        return True
    if n % 3 == 0:
        isPrime.HISTORY[n] = False
        return False

    r = int(math.sqrt(n))
    c = 5

    while c <= r:
        if n % c == 0:
            isPrime.HISTORY[n] = False
            return False
        if n % (c + 2) == 0:
            isPrime.HISTORY[n] = False
            return False
        c += 6

    isPrime.HISTORY[n] = True
    return True
isPrime.HISTORY = {}

def GenPrimesTo(n):
    """ Gen list of all primes <= limit """
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def eu49():
    TOP = 9999

    primes = GenPrimesTo(TOP)
    isPrime.HISTORY = dict([(i, False) for i in range(1000)])
    for p in primes:
        isPrime.HISTORY[p] = True

    for i in range(1000, 10000):
        if (isPrime(i)):
            per = set([int("".join(p)) for p in itertools.permutations(str(i))])
            per = [p for p in per if (isPrime(p) == True and len(str(p)) == len(str(i)))]
            per.remove(i)

            for p in per:
                if ((2 * p - i) in per):
                    if (p > i):
                        print ("".join([str(i), str(p), str(2 * p - i)]))

if __name__ == "__main__":
    startTime = time.clock()
    print (eu49())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
