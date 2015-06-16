# -------------------------------------------------------------- Counting fractions -------------------------------------------------------------- #
#                                                                                                                                                  #
#       Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.            #
#       If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:                                               #
#                   1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8                        #
#       It can be seen that there are 21 elements in this set.                                                                                     #
#       How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?                                             #
# ------------------------------------------------------------------------------------------------------------------------------------------------ #
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

def GenTotientTo(n):
    """ Generate list of phi(i) for i=2..n """
    primes = GenPrimesTo(n)
    phi = [i for i in range(n+1)]
    for p in primes:
        for j in range (p, n+1, p):
            phi[j] *= ( (p-1) / p )

    phi[0] = phi[1] = 0
    phi = [int(p) for p in phi]
    
    return phi
    
    
def eu243():
    MAX_DENOMINATOR = 50000000

    p = GenTotientTo(MAX_DENOMINATOR)
    for i in range(2, len(p)):
        p[i] /= (i - 1)

    i = 2
    while(p[i] >= 15499/94744):
        i += 1

    return (i)

startTime = time.clock()
print (eu243())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
