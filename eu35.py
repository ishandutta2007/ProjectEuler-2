# --------------------------------------------- Circular primes ----------------------------------------------- #
#                                                                                                               #
#       The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,     #
#       are themselves prime.                                                                                   #
#                                                                                                               #
#       There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.           #
#                                                                                                               #
#       How many circular primes are there below one million?                                                   #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math
import fractions

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

def isCircularPrime(p):
    """ Checks if p is circular prime """
    if (any(d in str(p) for d in {'0', '2', '4', '5', '6', '8' })): # Prime can't end with those digits
        return False
    
    l = len(str(p))
    for i in range(l - 1):
        p = int(str(p)[1:] + str(p)[0])
        if (not p in isCircularPrime.PRIMES):
            return False

    return True
isCircularPrime.PRIMES = []

def eu35():
    TOP = 1000000

    primes = GenPrimesTo(TOP)

    isCircularPrime.PRIMES = primes
    
    return sum([1 for p in primes if isCircularPrime(p)]) + 2

startTime = time.clock()
print (eu35())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
