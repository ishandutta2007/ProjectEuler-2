# --------------------------------------------------------- Prime generating integers --------------------------------------------------------- #
#                                                                                                                                               #
#       Consider the divisors of 30: 1,2,3,5,6,10,15,30.                                                                                        #
#       It can be seen that for every divisor d of 30, d+30/d is prime.                                                                         #
#                                                                                                                                               #
#       Find the sum of all positive integers n not exceeding 100,000,000                                                                       #
#       such that for every divisor d of n, d+n/d is prime.                                                                                     #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from euler.primes import full_prime_sieve

def eu357():
    TOP = 10 ** 8
    s = 0
    
    prime = full_prime_sieve(TOP)
    
    t = 0
    candidates = [1] * (TOP + 1)
    # Number must be in form 4k + 2
    for n in range(2, TOP, 4):
        if candidates[n]:
            if prime[n + 1] and prime[2 + (n // 2)] and all (prime[d + (n // d)] for d in range(3, int(n ** 0.5) + 1) if (n % d == 0)):
                s += n
            else:
                j = 1
                n_sj2 = n * j * j
                while n_sj2 < TOP:
                    candidates[n_sj2] = 0
                    j += 1
                    n_sj2 = n * j * j

    return 1 + s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu357())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
