# ----------------------------------------------------------- Prime square remainders --------------------------------------------------------- #
#                                                                                                                                               #
#       Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)^n + (pn+1)^n is divided by pn^2.                   #
#                                                                                                                                               #
#       For example, when n = 3, p3 = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.                                                                        #
#                                                                                                                                               #
#       The least value of n for which the remainder first exceeds 10^9 is 7037.                                                                #
#                                                                                                                                               #
#       Find the least value of n for which the remainder first exceeds 10^10.                                                                  #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from euler.primes import prime_sieve

def get_square_remainder(a, n):
    if n % 2 == 1:
        return (2*n*a) % (a**2)
    else:
        return 2
  
def eu123():
    TOP = 10 ** 6
    TARGET = 10 ** 10
    
    primes = prime_sieve(TOP)
           
    i = 0
    while get_square_remainder(primes[i], i + 1) < TARGET:
           i += 2

    return i + 1

if __name__ == "__main__":
    startTime = time.clock()
    print (eu123())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
