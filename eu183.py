# ------------------------------------------ Maximum product of parts ----------------------------------------- #
#                                                                                                               #
#       Let N be a positive integer and let N be split into k equal parts, r = N/k, so that N = r + r + ... + r.#
#       Let P be the product of these parts, P = r × r × ... × r = r^k.                                         #
#                                                                                                               #
#       For example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2,                    #
#       then P = 2.2^5 = 51.53632.                                                                              #
#                                                                                                               #
#       Let M(N) = Pmax for a given value of N.                                                                 #
#                                                                                                               #
#       It turns out that the maximum for N = 11 is found by splitting eleven into four equal parts which leads #
#       to Pmax = (11/4)4; that is, M(11) = 14641/256 = 57.19140625, which is a terminating decimal.            #
#                                                                                                               #
#       However, for N = 8 the maximum is achieved by splitting it into three equal parts, so M(8) = 512/27,    #
#       which is a non-terminating decimal.                                                                     #
#                                                                                                               #
#       Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if M(N) is a terminating decimal.       #
#                                                                                                               #
#       For example, ΣD(N) for 5 ≤ N ≤ 100 is 2438.                                                             #
#                                                                                                               #
#       Find ΣD(N) for 5 ≤ N ≤ 10000.                                                                           #
# ------------------------------------------------------------------------------------------------------------- #
import time
from fractions import gcd
from math import log, e

def M(n):
    k1 = n // e # The maximum of (n / k) ^ k is at k = n / e
    k2 = k1 + 1

    if ((k1 * log(n / k1)) > (k2 * log(n / k2))):
        return k1 // gcd(n, k1) # The denominator
    else:
        return k2 // gcd(n, k2)

    #Naive approach, calc ln(M) instead of M
    """p = log(n)

    for i in range(2, n):
        #p_tmp = i * log(n / i)

        if (p > p_tmp):
            break

        p = p_tmp

    return p, (i - 1) // gcd(n, i - 1)"""

def D(n):
    Mn = M(n)

    denominator = Mn

    while (denominator % 2 == 0):
        denominator //= 2
    while (denominator % 5 == 0):
        denominator //= 5

    if (denominator != 1):
        return n
    else:
        return -n
    
def eu183():
    TOP = 10000

    tot = 0
    for n in range(5, TOP + 1):
        tot += D(n)

    return tot

if __name__ == "__main__":
    startTime = time.clock()
    print (eu183())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
