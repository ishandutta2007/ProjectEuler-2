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

def A(n):
    i = 1
    a = 1 % n
    
    while (a != 0):
        i += 1
        a = (a * 10 + 1) % n

    return i

def eu129():
    TOP = 1000000

    n = TOP + 1

    while (True):
        if (gcd(n, 10) != 1):
            n += 1
            continue

        if (A(n) > TOP):
            return n

        n += 1

if __name__ == "__main__":
    startTime = time.clock()
    print (eu129())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
