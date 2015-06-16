# --------------------------------------------------------- Large repunit factors ------------------------------------------------------------- #
#                                                                                                                                               #
#       A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.                             #
#                                                                                                                                               #
#       For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime factors is 9414.                                           #                                                                         #
#                                                                                                                                               #
#       Find the sum of the first forty prime factors of R(109).                                                                                #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from euler import primeSieve

def eu132():
    TOP = 1000000
    TARGET = 10 ** 9

    primes = primeSieve(TOP)

    c = 0
    s = 0

    for p in primes:
        if (pow(10, TARGET, 9 * p) == 1):
            s += p
            c += 1

            if (c == 40):
                return s
            
if __name__ == "__main__":
    startTime = time.clock()
    print (eu132())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
