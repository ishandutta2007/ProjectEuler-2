# -------------------------------------------- Ordered fractions ------------------------------------------ #
#                                                                                                           #
#       Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,             #
#       it is called a reduced proper fraction.                                                             #
#                                                                                                           #
#       If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:        #
#                                                                                                           #
#                           1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,                          #
#                           4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8                                #
#                                                                                                           #
#       It can be seen that 2/5 is the fraction immediately to the left of 3/7.                             #
#                                                                                                           #
#       By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size,        #
#       find the numerator of the fraction immediately to the left of 3/7.                                  #
# --------------------------------------------------------------------------------------------------------- #
import time
import math

def eu71():
    TOP = 10 ** 6
    FRAC = (3, 7)

    best_n = 0
    best_d = 1

    d      = TOP
    min_d  = 1
    
    while (d >= min_d):
        n = (FRAC[0] * d - 1) // FRAC[1]

        if best_n * d < n * best_d:
            best_n = n
            best_d = d
            delta  = (FRAC[0] * d) - (n * FRAC[1])
            min_d  = (d // delta) + 1

        d -= 1

    #print (best_n, '/', best_d)
    return best_n
    
if __name__ == "__main__":
    startTime = time.clock()
    print (eu71())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
