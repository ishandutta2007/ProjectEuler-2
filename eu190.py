# ---------------------------------------- Maximising a weighted product -------------------------------------- #
#                                                                                                               #
#       Let Sm = (x1, x2, ... , xm) be the m-tuple of positive real numbers with x1 + x2 + ... + xm = m         #
#       for which Pm = x1 * x22 * ... * xmm is maximised.                                                       #
#                                                                                                               #
#       For example, it can be verified that [P10] = 4112 ([ ] is the integer part function).                   #
#                                                                                                               #
#       Find Σ[Pm] for 2 ≤ m ≤ 15.                                                                              #
# ------------------------------------------------------------------------------------------------------------- #
import time

def P(m):
    d = sum(range(1, m + 1))

    S = [(m / d * i) for i in range(1, m + 1)]

    p = 1

    for i in range(len(S)):
        p *= S[i] ** (i + 1)
    
    return int(p)
    
def eu190():
    MIN = 2
    MAX = 15

    c = 0
    for m in range(MIN, MAX + 1):
        c += P(m)
    
    return c

if __name__ == "__main__":
    startTime = time.clock()
    print (eu190())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
