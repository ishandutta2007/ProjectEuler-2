# ----------------------------------------- Consecutive prime sum --------------------------------------------- #
#                                                                                                               #
#       The prime 41, can be written as the sum of six consecutive primes:                                      #
#                                                                                                               #
#                               41 = 2 + 3 + 5 + 7 + 11 + 13                                                    #
#                                                                                                               #
#       This is the longest sum of consecutive primes that adds to a prime below one-hundred.                   #
#                                                                                                               #
#       The longest sum of consecutive primes below one-thousand that adds to a prime,                          #
#       contains 21 terms, and is equal to 953.                                                                 #
#                                                                                                               #
#       Which prime, below one-million, can be written as the sum of the most consecutive primes?               #
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

def eu50():
    TOP = 1000000

    primes = GenPrimesTo(TOP)
    isPrime.HISTORY = dict([(i, False) for i in range(TOP)])
    for p in primes:
        isPrime.HISTORY[p] = True

    max_length = 1
    max_length_prime = 0

    for i in range(len(primes)):
        s = sum(primes[i : i + max_length])
        for l in range(i + max_length, len(primes)):
            s += primes[l]
            if (s > TOP):
                break
            if (isPrime(s)):
                max_length = l - i + 1
                max_length_prime = s

    return max_length_prime

if __name__ == "__main__":
    startTime = time.clock()
    print (eu50())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
