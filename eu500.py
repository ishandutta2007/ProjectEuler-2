# --------------------------------------------------------- Problem 500!!! -------------------------------------------------------------------- #
#                                                                                                                                               #
#       The number of divisors of 120 is 16.                                                                                                    #
#       In fact 120 is the smallest number having 16 divisors.                                                                                  #
#                                                                                                                                               #
#       Find the smallest number with 2^500500 divisors.                                                                                        #
#       Give your answer modulo 500500507.                                                                                                      #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import heapq

from euler.primes import prime_sieve
        
def genFactor(EXP, MODULO):
    primes = prime_sieve(8000000) # 8000000 / ln(800000) > 500500 (EXP)
    p_i = 1
    
    candidates = []

    heapq.heappush(candidates, primes[0])
    
    while True:
        if candidates[0] < primes[p_i]:
            yield heapq.heappushpop(candidates, candidates[0] ** 2) % MODULO
        else:
            yield primes[p_i] % MODULO
            heapq.heappush(candidates, primes[p_i] ** 2)
            p_i += 1
    
def eu500():
    EXP = 500500
    MODULO = 500500507

    p = genFactor(EXP, MODULO)

    r = 1
    for i in range(EXP):
        r = (r * next(p)) % MODULO
        
    return r

if __name__ == '__main__':
    startTime = time.clock()
    print (eu500())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
