# --------------------------------------------------------- Prime pair connection ------------------------------------------------------------- #
#                                                                                                                                               #
#       Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 1219 is the smallest number such that the last digits      #
#       are formed by p1 whilst also being divisible by p2.                                                                                     #
#                                                                                                                                               #
#       In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes, p2 > p1, there exist values of n for which      #
#       the last digits are formed by p1 and n is divisible by p2. Let S be the smallest of these values of n.                                  #
#                                                                                                                                               #
#       Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.                                                                    #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from euler import primeSieve, digitsCount, egcd

def PrimePairConnection(p1, p2):
    c = digitsCount(p1)

    a = 10 ** c
    b = p2 - p1
    n = p2

    # We need so solve ax = b (mod n)x
    r, s = egcd(a, n)

    x = r * b % p2
    
    return a * x + p1
    
def eu134():
    TOP = 1000003
    
    primes = primeSieve(TOP)

    primes.remove(2)
    primes.remove(3)

    s = 0

    for i in range(len(primes) - 1):
        p1 = primes[i]
        p2 = primes[i + 1]

        s += PrimePairConnection(p1, p2)
        
    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu134())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
