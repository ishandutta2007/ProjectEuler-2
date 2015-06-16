# ------------------------------------- Goldbach's other conjecture ------------------------------------------- #
#                                                                                                               #
#       It was proposed by Christian Goldbach that every odd composite number can be written as the sum         #
#       of a prime and twice a square.                                                                          #
#                                                                                                               #
#                                           9 = 7 + 2×1^2                                                       #
#                                           15 = 7 + 2×2^2                                                      #
#                                           21 = 3 + 2×3^2                                                      #
#                                           25 = 7 + 2×3^2                                                      #
#                                           27 = 19 + 2×2^2                                                     #
#                                           33 = 31 + 2×1^2                                                     #
#                                                                                                               #
#       It turns out that the conjecture was false.                                                             #
#                                                                                                               #
#       What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?     #
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

def eu46():
    TOP = 1000

    primes = GenPrimesTo(TOP)
    isPrime.HISTORY = dict([(i, False) for i in range(1000)])
    for p in primes:
        isPrime.HISTORY[p] = True

    n = 3
    flag = True
    while (flag == True):
        if (isPrime(n) == True):
            n += 2
            continue

        flag = False
        
        for s in range(1, int(math.sqrt(n // 2)) + 1):
            if isPrime(n - 2 * (s ** 2)) == True:
                #print(n,"=",n - 2 * (s ** 2),"+ 2 *",s,"^ 2")
                n += 2
                flag = True
                break

        if (flag == False):
            print (n)

if __name__ == "__main__":
    startTime = time.clock()
    print (eu46())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
