# --------------------------------------------------------------- Prime summations ---------------------------------------------------------------- #
#                                                                                                                                                   #
#       It is possible to write ten as the sum of primes in exactly five different ways:                                                            # 
#                                                                                                                                                   #
#                           7 + 3                                                                                                                   #
#                           5 + 5                                                                                                                   #
#                           5 + 3 + 2                                                                                                               #
#                           3 + 3 + 2 + 2                                                                                                           #
#                           2 + 2 + 2 + 2 + 2                                                                                                       #
#                                                                                                                                                   #
#       What is the first value which can be written as the sum of primes in over five thousand different ways?                                     #
# ------------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import math

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

def countWays(primes, value):
    primes = GenPrimesTo(value)

    mat = [[0 for x in range(value + 1)] for x in range(len(primes))]

    for i in range(value + 1):
        if (i % 2 == 0):
            mat[0][i] = 1
        else:
            mat[0][i] = 0

    for i in range(1, len(primes)):
        for j in range(0, value + 1):
            mat[i][j] = 0
            for k in range((j // primes[i]) + 1):
                mat[i][j] += mat[i - 1][j - k * primes[i]]

    return mat[len(primes) - 1][value]

def eu77():
    NUM_OF_WAYS = 5000

    i = 2
    while (countWays(GenPrimesTo(i), i) <= NUM_OF_WAYS):
        i += 1

    return i
    

startTime = time.clock()
print (eu77())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
