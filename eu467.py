# ------------------------------------------------------------- Superinteger ------------------------------------------------------------------ #
#                                                                                                                                               #
#       An integer s is called a superinteger of another integer n if the digits of n form a subsequence of the digits of s.                    #
#       For example, 2718281828 is a superinteger of 18828, while 314159 is not a superinteger of 151.                                          #
#                                                                                                                                               #
#       Let p(n) be the nth prime number, and let c(n) be the nth composite number. For example, p(1) = 2, p(10) = 29, c(1) = 4 and c(10) = 18. #
#       {p(i) : i ≥ 1} = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...}                                                                              #
#       {c(i) : i ≥ 1} = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, ...}                                                                              #
#                                                                                                                                               #
#       Let PD the sequence of the digital roots of {p(i)} (CD is defined similarly for {c(i)}):                                                #
#       PD = {2, 3, 5, 7, 2, 4, 8, 1, 5, 2, ...}                                                                                                #
#       CD = {4, 6, 8, 9, 1, 3, 5, 6, 7, 9, ...}                                                                                                #
#                                                                                                                                               #
#       Let Pn be the integer formed by concatenating the first n elements of PD (Cn is defined similarly for CD).                              #
#       P10 = 2357248152                                                                                                                        #
#       C10 = 4689135679                                                                                                                        #
#                                                                                                                                               #
#       Let f(n) be the smallest positive integer that is a common superinteger of Pn and Cn.                                                   #
#       For example, f(10) = 2357246891352679, and f(100) mod 1 000 000 007 = 771661825.                                                        #
#                                                                                                                                               #
#       Find f(10 000) mod 1 000 000 007.                                                                                                       #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from math import log

from euler.primes import full_prime_sieve
from euler.numbers import digital_root

def smallest_superinteger(a, b):
    pass

def eu467():
    N = 100
    MODULO = 1000000007

    primes = full_prime_sieve(N * int(log(N)) * 2)

    p = [i for i in range(len(primes)) if primes[i] == 1][:N]
    c = [i for i in range(4, len(primes)) if primes[i] == 0][:N]

    P = [digital_root(n) for n in p]
    C = [digital_root(n) for n in c]

    print(P)
    print(C)

    return smallest_superinteger(P, C) % MODULO

if __name__ == '__main__':
    startTime = time.clock()
    print (eu467())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
