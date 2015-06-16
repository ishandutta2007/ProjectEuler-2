# ---------------------------------------------------------- Repunit divisibility ------------------------------------------------------------- #
#                                                                                                                                               #
#       A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111. #
#                                                                                                                                               #
#       Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k,                             #
#       for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.                       #
#                                                                                                                                               #
#       The least value of n for which A(n) first exceeds ten is 17.                                                                            #
#                                                                                                                                               #
#       Find the least value of n for which A(n) first exceeds one-million.                                                                     #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.number_theory.basics import gcd
from euler.numbers import radical

def eu127():
    TOP = 120000

    tot = 0
    for c in range(3, TOP):
        for a in range(c // 2):
            if gcd(a, c) != 1:
                continue

            if radical(a * (c - a) * c) < c:
                print (a, c - a, c)
                tot += c

    return tot

if __name__ == "__main__":
    startTime = time.clock()
    print (eu127())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
