# -------------------------------------------------------- Counting fractions in a range --------------------------------------------------------- #
#                                                                                                                                                  #
#       Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.            #
#                                                                                                                                                  #
#       If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:                                               #
#                                                                                                                                                  #
#                   1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8                        #
#                                                                                                                                                  #
#       It can be seen that there are 3 fractions between 1/3 and 1/2.                                                                             #
#                                                                                                                                                  #
#       How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?                                   #
# ------------------------------------------------------------------------------------------------------------------------------------------------ #
import time
import math
from euler import digitsSum

def f(n):
    if n in f.HISTORY:
        return f.HISTORY[n]
    
    f.HISTORY[n] = f.FACTORIALS[n % 10] + f(n // 10)

    return f.HISTORY[n]
f.FACTORIALS = [math.factorial(d) for d in range(10)]
f.HISTORY = { 0: 0}

def sf(n):
    return digitsSum(f(n))

def eu254():
    TOP = 20

    m = 0
    for i in range(10000000):
        t = sf(i)
        if t > m:
            m = t

    return m
        
if __name__ == "__main__":
    startTime = time.clock()
    print (eu254())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
