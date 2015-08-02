# ----------------------------------------------------------------- abc-hits ------------------------------------------------------------------ #
#                                                                                                                                               #
#       The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 2^3 × 3^2 × 7, so rad(504) = 2 × 3 × 7 = 42.#
#                                                                                                                                               #
#       We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:                                                         #
#                                                                                                                                               #
#           GCD(a, b) = GCD(a, c) = GCD(b, c) = 1                                                                                               #
#           a < b                                                                                                                               #
#           a + b = c                                                                                                                           #
#           rad(abc) < c                                                                                                                        #
#                                                                                                                                               #
#       For example, (5, 27, 32) is an abc-hit, because:                                                                                        #
#                                                                                                                                               #
#           GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1                                                                                           #
#           5 < 27                                                                                                                              #
#           5 + 27 = 32                                                                                                                         #
#           rad(4320) = 30 < 32                                                                                                                 #
#                                                                                                                                               #
#       It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.                         #
#                                                                                                                                               #
#       Find ∑c for c < 120000.                                                                                                                 #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from operator import mul
from functools import reduce

from euler.number_theory.basics import gcd
from euler.numbers import radical_sieve


def eu127():
    TOP = 120000
    
    radicals = radical_sieve(TOP)
    radicals_s = list(sorted([(i, radicals[i]) for i in range(len(radicals))], key = lambda x: x[1]))[1:]

    s = 0
    for c in range(3, TOP):            
        for a in radicals_s:
            if a[0] > (c + 1) // 2:
                continue

            if a[1] * radicals[c] >= c:
                break

            if a[1] * radicals[c - a[0]] * radicals[c] < c:
                if gcd(a[0], c) == 1:
                    s += c

    return s

if __name__ == '__main__':
    startTime = time.clock()
    print (eu127())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
