# ----------------------------------------- The hyperexponentiation of a number --------------------------------------- #
#                                                                                                                       #
#       The hyperexponentiation or tetration of a number a by a positive integer b, denoted by a↑↑b or ba,              #
#       is recursively defined by:                                                                                      #
#                                                                                                                       #
#                       a↑↑1 = a,                                                                                       #
#                       a↑↑(k+1) = a^(a↑↑k).                                                                            # 
#                                                                                                                       #
#       Thus we have e.g. 3↑↑2 = 33 = 27, hence 3↑↑3 = 3^27 = 7625597484987 and 3↑↑4                                    #
#       is roughly 10^3.6383346400240996*10^12.                                                                         #
#                                                                                                                       #
#       Find the last 8 digits of 1777↑↑1855.                                                                           #
# --------------------------------------------------------------------------------------------------------------------- #
import time

def tetration(a,b,n):
    """ Calculate b↑↑e (mod n) """
    t = 1
    
    for i in range(b):
        t1 = pow(a, t, n)
        t = t1

    return t1

def eu188():
    BASE = 1777
    EXP = 1855
    MODULO = 10 ** 8

    return tetration(BASE, EXP, MODULO)

if __name__ == "__main__":
    startTime = time.clock()
    print (eu188())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
