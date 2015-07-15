# ------------------------------------------------ Largest integer divisible by two primes ---------------------------------------------------- #
#                                                                                                                                               #
#       The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is 96, as 96=32*3=2^5*3.                                    #
#       For two distinct primes p and q let M(p,q,N) be the largest positive integer ≤N only divisible by both p and q and M(p,q,N)=0           #
#       if such a positive integer does not exist.                                                                                              #
#                                                                                                                                               #
#       E.g. M(2,3,100)=96.                                                                                                                     #
#       M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.                                                                         #
#       Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100 that is divisible by both 2 and 73.                            #
#                                                                                                                                               #
#       Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.                                                                              #
#                                                                                                                                               #
#       Find S(10 000 000).                                                                                                                     #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.primes import prime_sieve
from euler.numbers import log_floor

def M(p, q, N):
    n = N // (p * q)

    ret = 0

    for j in range(log_floor(n, q) + 1):
        r =  (p ** (log_floor(n, p) + 1)) * (q ** (j + 1))
        if r > ret:
            ret = r

        n //= q

    return ret

def S(N):
    primes = prime_sieve(N)

    s = set()
    i = 0
    while (True):
        j = i + 1
        stop = True
        while (primes[i] * primes[j] <= N):
            s.add(M(primes[i], primes[j], N))
            stop = False

            j += 1

        if stop:
            break

        i += 1

    return sum(s)

def eu347():
    TOP = 10 ** 7
    
    return S(TOP)

if __name__ == '__main__':
    startTime = time.clock()
    print (eu347())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
