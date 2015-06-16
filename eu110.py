# --------------------------------------- Diophantine reciprocals II ------------------------------------------ #
#                                                                                                               #
#       In the following equation x, y, and n are positive integers.                                            #
#                                                                                                               #
#                       (1 / x) + (1 / y) = (1 / n)                                                             #
#                                                                                                               #
#       It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value      #
#       of n for which the total number of distinct solutions exceeds one hundred.                              #
#                                                                                                               #
#       What is the least value of n for which the number of distinct solutions exceeds four million?           #
#                                                                                                               #
#       NOTE: This problem is a much more difficult version of problem 108 and as it is well beyond the         #
#       limitations of a brute force approach it requires a clever implementation.                              #
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

genCandidates.PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 39, 41, 43]

def eu110():
    NUM_OF_SOLUTIONS = 4000000
    DIVOSORS_OF_N_SQUARE = 2 * NUM_OF_SOLUTIONS - 1

    g = genCandidates()

    n, f = next(g)

    while (functools.reduce(operator.mul, [(2 * i + 1) for i in f]) < DIVOSORS_OF_N_SQUARE):
        n, f = next(g)

    return n

if __name__ == "__main__":
    startTime = time.clock()
    print (eu110())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
