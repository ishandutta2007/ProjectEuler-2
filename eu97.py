# ----------------------------------------------- Large non-Mersenne prime -------------------------------------------- #
#                                                                                                                       #
#       The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime        #
#       of the form 2^6972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes,              #
#       of the form 2p−1, have been found which contain more digits.                                                    #
#                                                                                                                       #
#       However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits:                  #
#                                                       28433×2^7830457+1.                                              #
#       Find the last ten digits of this prime number.                                                                  #
# --------------------------------------------------------------------------------------------------------------------- #
import time
import math

def DecToBinary(x):
    """ Generates the binary representation of x """

    e = ''
    i = 0
        
    while (True):
        e = str((x % 2)) + e
        x = int(x / 2)
        if (x == 0):
            break
    return e   

def FastExpo(b,e,n):
    """ Calculate b^e (mod n) """
    z = 1
    e = DecToBinary(e)
    
    for j in range (0, len(e)):
        t = n
        z = (z**2) % n
        if (e[j] == '1'):
            z = (b * z) % n

    return z

def eu97():
    COEFFICIENT = 28433
    BASE = 2
    EXP = 7830457
    MODULO = 10000000000

    n = FastExpo(BASE, EXP, MODULO)
    n = (COEFFICIENT * n + 1) % MODULO

    return n

if __name__ == "__main__":
    startTime = time.clock()
    print (eu97())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
