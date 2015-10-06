# ------------------------------------------------------------ Constrained Sums --------------------------------------------------------------- #
#                                                                                                                                               #
#       Let S(n,k,b) represent the number of valid solutions to x1 + x2 + ... + xk ≤ n, where 0 ≤ xm ≤ b^m for all 1 ≤ m ≤ k.                   #
#                                                                                                                                               #
#       For example, S(14,3,2) = 135, S(200,5,3) = 12949440, and S(1000,10,5) mod 1 000 000 007 = 624839075.                                    #
#                                                                                                                                               #
#       Find (∑10 ≤ k ≤ 15 S(10k,k,k)) mod 1 000 000 007.                                                                                       #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from itertools import combinations

from euler.combinatorics import nCk

def S(n, k, b):
    mins = [0] * (k + 1)
    maxs = [b ** m for m in range(1, k + 1)]
    maxs.append(n)

    return count_integral_solutions(mins, maxs, n)
            
def count_integral_solutions(mins, maxs, max_target):
    if len(mins) != len(maxs):
        return -1

    for i in range(len(mins)):
        maxs[i] -= mins[i]
        max_target -= mins[i]

    ret = nCk(max_target + len(mins) - 1, len(mins) - 1)
    sign = -1

    for l in range(1, len(mins)):
        s = combinations(maxs, l)
        t = 0
        for c in s:
            tmp = max_target + len(mins) - 1 - sum(c) - l
            if tmp > 0:
                t += nCk(tmp, len(mins) - 1)
        ret += sign * t
        sign *= -1

    return ret
    
def eu528():
    MIN = 10
    MAX = 15
    MODULO = 1000000007
    
    ret = 0

    for k in range(MIN, MAX + 1):
        ret += S(10 ** k, k, k) % MODULO

    return ret % MODULO

if __name__ == '__main__':
    startTime = time.clock()
    print (eu528())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
