# -------------------------------------------------- Sum of squares of unitary divisors ------------------------------------------------------- #
#                                                                                                                                               #
#       A unitary divisor d of a number n is a divisor of n that has the property gcd(d, n/d) = 1.                                              #
#       The unitary divisors of 4! = 24 are 1, 3, 8 and 24.                                                                                     #
#       The sum of their squares is 1^2 + 3^2 + 8^2 + 24^2 = 650.                                                                               #
#                                                                                                                                               #
#       Let S(n) represent the sum of the squares of the unitary divisors of n. Thus S(4!)=650.                                                 #
#                                                                                                                                               #
#       Find S(100 000 000!) modulo 1 000 000 009.                                                                                              #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.primes import prime_sieve

def exp_of_p_in_factorial(p, f):

    r = 0
    while f:
        r += f // p
        f //= p

    return r

def eu429():
    N = 10 ** 8
    MODULO = 1000000009

    primes = prime_sieve(N)

    # We need to find the sum of all subsets squared unarity divosors
    s = 1
    for p in primes:
        s *= 1 + pow(p * p, exp_of_p_in_factorial(p, N), MODULO)
        s %= MODULO
        
    return s

if __name__ == '__main__':
    startTime = time.clock()
    print (eu429())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
