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

def addToSet(primesPairSet, p):
    l1 = 1
    l2 = 0

    tmp = p
    while (tmp != 0):
        l1 *= 10
        tmp //= 10
    
    for prime in primesPairSet:
        if (not isPrime(prime * l1 + p)):
            return False
        
        tmp = prime
        l2 = 1
        while (tmp != 0):
            l2 *= 10
            tmp //= 10

        if (not isPrime(p * l2 + prime)):
            return False

    return True

def genPrimesPairSet(primes, size, primesPairSet):
    if (size == 0):
        print (sum(primesPairSet))
        return True

    for p in primes:
        if (addToSet(primesPairSet, p)):
            if (genPrimesPairSet(primes, size - 1, primesPairSet + [p])):
                return True
            
def eu60():
    TOP = 10000
    FAMILY_SIZE = 5

    primes = GenPrimesTo(TOP)
    isPrime.HISTORY = dict([(i, False) for i in range(TOP)])
    for p in primes:
        isPrime.HISTORY[p] = True

    return genPrimesPairSet(primes, FAMILY_SIZE, [])

if __name__ == "__main__":
    startTime = time.clock()
    print (eu60())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
