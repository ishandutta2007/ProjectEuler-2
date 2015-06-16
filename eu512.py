# -------------------------------------------------------------- Counting fractions -------------------------------------------------------------- #
#                                                                                                                                                  #
#       Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.            #
#       If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:                                               #
#                   1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8                        #
#       It can be seen that there are 21 elements in this set.                                                                                     #
#       How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?                                             #
# ------------------------------------------------------------------------------------------------------------------------------------------------ #
import time

from euler import primeSieve

def GenTotientTo(n):
    """ Generate list of phi(i) for i=2..n """
    primes = primeSieve(n)

    phi = [i for i in range(n+1)]
    for p in primes:
        for j in range (p, n+1, p):
            phi[j] -= phi[j] // p

    phi[0] = phi[1] = 0
    
    return phi 
    
def eu72():
    MAX_DENOMINATOR = 1000000

    return (GenTotientTo(MAX_DENOMINATOR))

startTime = time.clock()
print (sum(eu72()))
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
