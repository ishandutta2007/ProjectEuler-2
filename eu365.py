# ------------------------------------------------------ A huge binomial coefficient ---------------------------------------------------------- #
#                                                                                                                                               #
#       The binomial coeffient C(10^18,10^9) is a number with more than 9 billion (9×10^9) digits.                                              #
#                                                                                                                                               #
#       Let M(n,k,m) denote the binomial coefficient C(n,k) modulo m.                                                                           #
#                                                                                                                                               #
#       Calculate ∑M(10^18,10^9,p*q*r) for 1000<p<q<r<5000 and p,q,r prime.                                                                     #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.primes import prime_sieve
from euler.combinatorics import nCk
from euler.number_theory.congruence import crt
from euler.numbers import to_base

def M(n, k, p):
    n_base_p = to_base(n, p)
    k_base_p = to_base(k, p)

    m = 1

    if len(n_base_p) < len(k_base_p):
        return 0

    for i in range(len(k_base_p)):
        if n_base_p[i] < k_base_p[i]:
            return 0
        
        m = (m * nCk(n_base_p[i], k_base_p[i])) % p

    return m

def eu365():
    N = 10 ** 18
    K = 10 ** 9
    
    MIN = 1000
    MAX = 5000
    
    primes = prime_sieve(MAX)
    primes = [p for p in primes if p > 1000]

    bcmp = [M(N, K, p) for p in primes]

    s = 0
    for p in range(len(primes)):
        for q in range(p + 1, len(primes)):
            if bcmp[p] == 0 and bcmp[q] == 0:
                tmp_r = 0
            else:
                tmp_r = crt([bcmp[p], bcmp[q]], [primes[p], primes[q]])
            tmp_m = primes[p] * primes[q]
            for r in range(q + 1, len(primes)):
                if tmp_r == 0 and bcmp[r] == 0:
                    continue
                
                s += crt([tmp_r, bcmp[r]], [tmp_m, primes[r]])
            
    return s

if __name__ == '__main__':
    startTime = time.clock()
    print (eu365())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
