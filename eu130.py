# ------------------------------------------------- Composites with prime repunit property ---------------------------------------------------- #
#                                                                                                                                               #
#       A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111. #
#                                                                                                                                               #
#       Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k,                             #
#       for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.                       #
#                                                                                                                                               #
#       You are given that for all primes, p > 5, that p − 1 is divisible by A(p). For example, when p = 41, A(41) = 5,                         #
#       and 40 is divisible by 5.                                                                                                               #
#                                                                                                                                               #
#       However, there are rare composite values for which this is also true; the first five examples being 91, 259, 451, 481, and 703.         #
#                                                                                                                                               #
#       Find the sum of the first twenty-five composite values of n for which                                                                   #
#       GCD(n, 10) = 1 and n − 1 is divisible by A(n).                                                                                          #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.primes import prime_sieve
from euler.number_theory.basics import gcd

def A(n):
    i = 1
    a = 1 % n
    
    while (a != 0):
        i += 1
        a = (a * 10 + 1) % n

    return i

def eu130():
    TOP = 25

    primes = prime_sieve(1000000)

    c = 0
    tot = 0
    for i in range(91, 1000000):
        if i in primes:
            continue

        if (gcd(i, 10) != 1):
            continue

        if (i - 1) % A(i) == 0:
            c += 1
            tot += i

        if c == TOP:
            break

    return tot

if __name__ == '__main__':
    startTime = time.clock()
    print (eu130())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
