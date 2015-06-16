# --------------------------------------- Diophantine reciprocals I ------------------------------------------- #
#                                                                                                               #
#       In the following equation x, y, and n are positive integers.                                            #
#                                                                                                               #
#                       (1 / x) + (1 / y) = (1 / n)                                                             #
#                                                                                                               #
#       For n = 4 there are exactly three distinct solutions:                                                   #
#                                                                                                               #
#                       (1 / 5) + (1 / 20) = (1 / 4)                                                            #
#                       (1 / 6) + (1 / 12) = (1 / 4)                                                            #
#                       (1 / 8) + (1 / 8)  = (1 / 4)                                                            #
#                                                                                                               #
#       What is the least value of n for which the number of distinct solutions exceeds one-thousand?           #
#                                                                                                               #
#       NOTE: This problem is an easier version of problem 110; it is strongly advised that you                 #
#       solve this one first.                                                                                   #
# ------------------------------------------------------------------------------------------------------------- #
import time
import heapq
import operator
import functools

def genCandidates():
    h = [(1, [0 for p in genCandidates.PRIMES])]

    while (True):
        n,f = heapq.heappop(h)
        yield n,f
        
        tmp = (n * 2, [f[0] + 1] + f[1:])
        if (tmp not in h):
            heapq.heappush(h, (n * 2, [f[0] + 1] + f[1:]))
            
        for i in range(1, len(genCandidates.PRIMES)):
            if (f[i] < f[i - 1]):
                tmp = (n * genCandidates.PRIMES[i], f[:i] + [f[i] + 1] + f[i + 1:])
                if (tmp not in h):
                    heapq.heappush(h, (n * genCandidates.PRIMES[i], f[:i] + [f[i] + 1] + f[i + 1:]))

genCandidates.PRIMES = [2, 3, 5, 7, 11, 13, 17]

def eu108():
    NUM_OF_SOLUTIONS = 1000
    DIVOSORS_OF_N_SQUARE = 2 * NUM_OF_SOLUTIONS - 1

    g = genCandidates()

    n, f = next(g)

    while (functools.reduce(operator.mul, [(2 * i + 1) for i in f]) < DIVOSORS_OF_N_SQUARE):
        n, f = next(g)

    return n

if __name__ == "__main__":
    startTime = time.clock()
    print (eu108())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
