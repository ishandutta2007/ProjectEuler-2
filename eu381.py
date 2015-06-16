# ----------------------------------------------------------- (prime-k) factorial ------------------------------------------------------------- #
#                                                                                                                                               #
#       For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.                                                                                #
#                                                                                                                                               #
#       For example, if p=7,                                                                                                                    #
#       (7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.                                             #
#       As 872 mod(7) = 4, S(7) = 4.                                                                                                            #
#                                                                                                                                               #
#       It can be verified that ∑S(p) = 480 for 5 ≤ p < 100.                                                                                    #
#                                                                                                                                               #
#       Find ∑S(p) for 5 ≤ p < 10^8.                                                                                                            #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.primes import prime_sieve
from euler.number_theory.basics import modular_multiplicative_inverse

def S(p):
    # [(p-1)! + (p-2)! + (p-3)! + (p-4)! + (p-5)!] mod p
    # = (p-1)! * [1 + 1/(p-1) + 1/(p-1)(p-2) + 1/(p-1)(p-2)(p-3) + 1/(p-1)(p-2)(p-3)(p-4)] mod p
    # = (p-1)! * [1 + 1/(-1) + 1/(-1)(-2) + 1/(-1)(-2)(-3) + 1/(-1)(-2)(-3)(-4)] mod p
    # = (p-1)! * [1/(-1)(-2) + 1/(-1)(-2)(-3) + 1/(-1)(-2)(-3)(-4)] mod p
    # = (p-1)! * [1/2 + 1/(-6) + 1/24] mod p
    # = (p-1)! * [12/24 - 4/24 + 1/24] mod p
    # = (p-1)! * (9/24) mod p
    # = (p-1)! * (3/8) mod p
    # = (p-1)! mod p * (3/8) mod p
    # = (-1) * (3/8) mod p [Wilson's theorem]
    # = (-3/8) mod p
    
    return (p - 3) * modular_multiplicative_inverse(8, p) % p

    # Improved solution:
    #k = 3 * p % 8
    #return (k*p - 3) // 8

def eu381():
    TOP = 10 ** 8
    
    primes = prime_sieve(TOP)[2:]
    
    return sum([S(p) for p in primes])

if __name__ == '__main__':
    startTime = time.clock()
    print (eu381())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
