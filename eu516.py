# ----------------------------------------------------------- 5-smooth totients --------------------------------------------------------------- #
#                                                                                                                                               #
#       5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.                                                               #
#       5-smooth numbers are also called Hamming numbers.                                                                                       #
#       Let S(L) be the sum of the numbers n not exceeding L such that Euler's totient function φ(n) is a Hamming number.                       #
#       S(100)=3728.                                                                                                                            #
#                                                                                                                                               #
#       Find S(10^12). Give your answer modulo 2^32.                                                                                            #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import heapq

from euler.primes import is_probable_prime

def gen_hamming_numbers():
    FACTORS = [2, 3, 5]
    h = [1]
 
    while (True):
        n = heapq.heappop(h)
        yield n
                 
        for i in range(0, len(FACTORS)):
            tmp = (n * FACTORS[i])
            if (tmp not in h):
                heapq.heappush(h, (n * FACTORS[i]))

def sum_hamming_numbers(h, depth):    
    s = h * sum_hamming_numbers._PRIMES[depth]

    if s > sum_hamming_numbers._TOP:
        return 0

    if depth == len(sum_hamming_numbers._PRIMES) - 1:
        return s
    else:
        return (s + sum_hamming_numbers(h, depth + 1) + \
                    sum_hamming_numbers(s, depth + 1)) % sum_hamming_numbers._MODULO
sum_hamming_numbers._TOP = 0
sum_hamming_numbers._MODULO = 0
sum_hamming_numbers._PRIMES = []
    
def eu516():
    TOP = 10 ** 12
    MODULO = 2 ** 32

    sum_hamming_numbers._TOP = TOP
    sum_hamming_numbers._MODULO = MODULO
    
    g = gen_hamming_numbers()

    hamming = []

    c = next(g)
    while c <= TOP:
        hamming.append(c)
        c = next(g)

    sum_hamming_numbers._PRIMES = [(h + 1) for h in hamming if (h + 1 <= TOP) and (h + 1 not in hamming) and is_probable_prime(h + 1)]

    s = 0
    for h in hamming:
        s = (s + sum_hamming_numbers(h, 0)) % MODULO

    return (s + sum(hamming)) % MODULO

if __name__ == '__main__':
    startTime = time.clock()
    print (eu516())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
