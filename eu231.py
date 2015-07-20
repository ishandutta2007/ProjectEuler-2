# ---------------------------------------------- The prime factorisation of binomial coefficients --------------------------------------------- #
#                                                                                                                                               #
#       The binomial coefficient 10C3 = 120.                                                                                                    #
#       120 = 23 × 3 × 5 = 2 × 2 × 2 × 3 × 5, and 2 + 2 + 2 + 3 + 5 = 14.                                                                       #
#       So the sum of the terms in the prime factorisation of 10C3 is 14.                                                                       #
#                                                                                                                                               #
#       Find the sum of the terms in the prime factorisation of 20000000C15000000.                                                              #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.primes import prime_sieve

def exponent_of_p_in_binomial_coefficient(n, k, p):
    # Read http://sriasat.files.wordpress.com/2012/12/eureka.pdf for more details
    # and https://en.wikipedia.org/wiki/Factorial#Number_theory about Legendre's formula
    r = 0
    pj = p

    n_minus_k = n - k
    while (pj <= n):
        r += (n // pj) - (k // pj) - (n_minus_k // pj)
        pj *= p

    return r

def eu231():
    n = 20 * 10 ** 6
    k = 15 * 10 ** 6

    primes = prime_sieve(n)

    s = 0
    for p in primes:
        s += p * exponent_of_p_in_binomial_coefficient(n, k, p)

    return s    

if __name__ == '__main__':
    startTime = time.clock()
    print (eu231())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
