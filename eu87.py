# ------------------------------------------ Prime power triples ---------------------------------------------- #
#                                                                                                               #
#       The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. #
#       In fact, there are exactly four numbers below fifty that can be expressed in such a way:                #
#                                                                                                               #
#                               28 = 2^2 + 2^3 + 2^4                                                            #
#                               33 = 3^2 + 2^3 + 2^4                                                            #
#                               49 = 5^2 + 2^3 + 2^4                                                            #
#                               47 = 2^2 + 3^3 + 2^4                                                            #
#                                                                                                               #
#       How many numbers below fifty million can be expressed as the sum of a prime square,                     #
#       prime cube, and prime fourth power?                                                                     #
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

def eu87():
    TOP = 50000000

    primes = GenPrimesTo(int(TOP ** 0.5))
    isPrime.HISTORY = dict([(i, False) for i in range(int(TOP ** 0.5))])
    for p in primes:
        isPrime.HISTORY[p] = True

    squares = [(p * p) for p in primes if (p * p < TOP)]
    cubes = [(p * p * p) for p in primes if (p * p * p < TOP)]
    forths = [(p * p * p * p) for p in primes if (p * p * p * p < TOP)]

    ret = [(i + j + k) for i in squares for j in cubes for k in forths]
    ret = [p for p in ret if (p < TOP)]
    
    return len(set(ret))

if __name__ == "__main__":
    startTime = time.clock()
    print (eu87())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
