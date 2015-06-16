# ------------------------------------- Investigating a Prime Pattern ----------------------------------------- #
#                                                                                                               #
#       The smallest positive integer n for which the numbers n^2+1, n^2+3, n^2+7, n^2+9, n^2+13, and n^2+27    #
#       are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.              #
#                                                                                                               #
#       What is the sum of all such integers n below 150 million?                                               #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math
from euler import isProbablePrime

def genPossibleModulo():
    for i in range(len(genPossibleModulo.FIRST_PRIMES)):
        p = genPossibleModulo.FIRST_PRIMES[i]
        genPossibleModulo.MODULOS[p] = []
        for r in range(p):
            if all((r + d) % p != 0 for d in genPossibleModulo.D):
                genPossibleModulo.MODULOS[p].append(r)
genPossibleModulo.FIRST_PRIMES = isProbablePrime._known_primes[0 : 10]
genPossibleModulo.MODULOS = { }
genPossibleModulo.D = {1, 3, 7, 9, 13, 27}

def eu146():
    TOP = 150000000

    genPossibleModulo()

    s = 0

    for n in range(10, TOP, 10):
        nSquare = n * n
        flag = True
        for p in genPossibleModulo.FIRST_PRIMES:
            m = genPossibleModulo.MODULOS[p]
            if (nSquare % p not in m):
                flag = False
                break

        if (flag == True):
            if (isProbablePrime(nSquare + 1) and
                isProbablePrime(nSquare + 3) and
                isProbablePrime(nSquare + 7) and
                isProbablePrime(nSquare + 9) and
                isProbablePrime(nSquare + 13) and
                isProbablePrime(nSquare + 27) and
                not isProbablePrime(nSquare + 19) and
                not isProbablePrime(nSquare + 21) ):
                s += n

    return s    
    
if __name__ == "__main__":
    startTime = time.clock()
    print (eu146())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
