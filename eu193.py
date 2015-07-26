# --------------------------------------------------------------- Squarefree Numbers ---------------------------------------------------------- #
#                                                                                                                                               #
#       A positive integer n is called squarefree, if no square of a prime divides n, thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree,             #
#       but not 4, 8, 9, 12.                                                                                                                    #
#                                                                                                                                               #
#       How many squarefree numbers are there below 2^50?                                                                                       #  
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.number_theory.mobius import mobius_sieve

def eu193():
    N = 2 ** 50

    mobius = mobius_sieve(int(N ** .5) + 1)
    
    Q = 0
    for n in range(1, int(N ** 0.5) + 1):
        Q += mobius[n] * (N // (n ** 2))

    return Q

if __name__ == "__main__":
    startTime = time.clock()
    print (eu193())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
