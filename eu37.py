# ------------------------------------------ Truncatable primes ----------------------------------------------- #
#                                                                                                               #
#       The number 3797 has an interesting property. Being prime itself, it is possible to continuously         #
#       remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.                 #
#       Similarly we can work from right to left: 3797, 379, 37, and 3.                                         #
#                                                                                                               #
#       Find the sum of the only eleven primes that are both truncatable from left to right and right to left.  #
#                                                                                                               #
#       NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.                                       #
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

def genRightTruncatable():
    rt = { "2", "3", "5", "7" }
    digits = { "1", "3", "5", "7", "9" }

    new_rt = { r + d for r in rt for d in digits if isPrime(int(r + d))}
    
    while (rt != (new_rt | rt)):
        rt = rt | new_rt
        new_rt = { r + d for r in rt for d in digits if isPrime(int(r + d))}
        
    return new_rt

def isLeftTruncatable(n):
    while (len(n) != 1):
        if (not isPrime(int(n))):
            return False
        n = str(n)[1:]

    return (isPrime(int(n)))

def eu37():
    rt = genRightTruncatable()
    t = {r for r in rt if isLeftTruncatable(r)}

    return sum({int(p) for p in t})

startTime = time.clock()
print (eu37())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
