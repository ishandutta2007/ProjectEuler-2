# ------------------------------------------------ Combinatoric selections -------------------------------------------- #
#                                                                                                                       #
#       here are exactly ten ways of selecting three from five, 12345:                                                  #
#                                                                                                                       #
#                                   123, 124, 125, 134, 135, 145, 234, 235, 245, and 345                                #
#                                                                                                                       #
#       In combinatorics, we use the notation, 5C3 = 10.                                                                #
#                                                                                                                       #
#       In general,                                                                                                     #
#       nCr = n! / r!(n−r)!, where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.                                           #
#                                                                                                                       #
#       It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.                                      #
#                                                                                                                       #
#       How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?              #
# --------------------------------------------------------------------------------------------------------------------- #
import time
from euler.combinatorics import nCk  

def firstCoefficientGreaterThenTARGET(l):
    TARGET = 1000000

    cur = l // 2
    jump = cur // 2

    while (jump != 0):
        if (nCk(l, cur) > TARGET):
            cur -= jump
        else:
            cur += jump

        jump //= 2

    if (nCk(l, cur - 1) > TARGET):
        return cur - 1
    elif (nCk(l, cur) > TARGET):
        return cur
    elif (nCk(l, cur + 1) > TARGET):
        return cur + 1
    else:
        return cur + 2
    
def eu53():
    MAX_N = 100

    s = 0

    for l in range(23, MAX_N + 1):
        p = firstCoefficientGreaterThenTARGET(l)
        s += (l + 1) - 2 * p

    return s

startTime = time.clock()
print (eu53())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
