# --------------------------------------- Investigating the primality of numbers of the form 2n^2-1 ------------------------------------------- #
#                                                                                                                                               #
#       Consider numbers t(n) of the form t(n) = 2n^2-1 with n > 1.                                                                             #
#       The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.                                                                          #
#       It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.                                                                           #
#       For n ≤ 10000 there are 2202 numbers t(n) that are prime.                                                                               #
#                                                                                                                                               #
#       How many numbers t(n) are prime for n ≤ 50,000,000 ?                                                                                    #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.primes import prime_sieve
from euler.number_theory.congruence import legendre_symbol, Tonelli_Shanks

def eu216():
    TOP = 5 * 10 ** 7

    p = [1 for i in range(TOP + 1)]
    p[0] = p[1] = 0
    primes = set(prime_sieve(int(2 ** 0.5 * TOP))[1:])

    for prime in primes:
        if legendre_symbol((prime + 1) // 2, prime) == 1:
            x0, x1 = Tonelli_Shanks((prime + 1) // 2, prime)

            if x0 <= TOP and not (2 * x0**2 - 1) in primes:
                p[x0] = 0
            if x1 <= TOP and not (2 * x1**2 - 1) in primes:
                p[x1] = 0

            p[x0 + prime : : prime] = [0] * ((TOP - x0) // prime)
            p[x1 + prime : : prime] = [0] * ((TOP - x1) // prime)

    return sum(p)

if __name__ == '__main__':
    startTime = time.clock()
    print (eu216())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
