# ----------------------------------------------------------- Repunit nonfactors -------------------------------------------------------------- #
#                                                                                                                                               #
#       A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111. #
#                                                                                                                                               #
#       Let us consider repunits of the form R(10^n).                                                                                           #
#                                                                                                                                               #
#       Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is divisible by 17.                                                #
#       Yet there is no value of n for which R(10^n) will divide by 19. In fact, it is remarkable that 11, 17, 41, and 73 are the only          #
#       four primes below one-hundred that can be a factor of R(10^n).                                                                          #
#                                                                                                                                               #
#       Find the sum of all the primes below one-hundred thousand that will never be a factor of R(10^n).                                       #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.primes import prime_sieve

def A(n):
    i = 1
    a = 1 % n
    
    while (a != 0):
        i += 1
        a = (a * 10 + 1) % n

    return i

def eu133():
    TOP = 100000

    primes = prime_sieve(TOP)[3:]

    tot = 0
    for p in primes:
        a = A(p)

        while a % 2 == 0:
            a //= 2
        while a % 5 == 0:
            a //= 5

        if a != 1:
            tot += p
            
    return tot + (2 + 3 + 5)

if __name__ == '__main__':
    startTime = time.clock()
    print (eu133())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
