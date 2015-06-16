# ------------------------------------------------------------- Totient Chains ---------------------------------------------------------------- #
#                                                                                                                                               #
#       Let φ be Euler's totient function, i.e. for a natural number n, φ(n) is the number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.             #
#                                                                                                                                               #
#       By iterating φ, each positive integer generates a decreasing chain of numbers ending in 1.                                              #
#       E.g. if we start with 5 the sequence 5,4,2,1 is generated.                                                                              #
#       Here is a listing of all chains with length 4:                                                                                          #
#                                                                                                                                               #
#                                   5,4,2,1                                                                                                     #
#                                   7,6,2,1                                                                                                     #
#                                   8,4,2,1                                                                                                     #
#                                   9,6,2,1                                                                                                     #
#                                   10,4,2,1                                                                                                    #
#                                   12,4,2,1                                                                                                    #
#                                   14,6,2,1                                                                                                    #
#                                   18,6,2,1                                                                                                    #
#                                                                                                                                               #
#       Only two of these chains start with a prime, their sum is 12.                                                                           #
#                                                                                                                                               #
#       What is the sum of all primes less than 40000000 which generate a chain of length 25?                                                   #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import math
from euler import totientSieve, isProbablePrime

def eu214():
    TOP = 40000000
    
    t = totientSieve(TOP)

    t[1] = 1
    for i in range(2, TOP + 1):
        t[i] = 1 + t[t[i]]

    b = [i for i in range(len(t)) if (t[i] == 25 and isProbablePrime(i))]

    return sum(b)
        
if __name__ == "__main__":
    startTime = time.clock()
    print (eu214())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
