# ----------------------------------------------------------- Prime cube partnership ---------------------------------------------------------- #
#                                                                                                                                               #
#       There are some prime values, p, for which there exists a positive integer, n, such that the expression n3 + n2p is a perfect cube.      #
#                                                                                                                                               #
#       For example, when p = 19, 83 + 82×19 = 123.                                                                                             #
#                                                                                                                                               #
#       What is perhaps most surprising is that for each prime with this property the value of n is unique,                                     #
#       and there are only four such primes below one-hundred.                                                                                  #
#                                                                                                                                               #
#       How many primes below one million have this remarkable property?                                                                        #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from euler import isProbablePrime

def eu131():
    TOP = 1000000

    c = 0

    i = 1
    while (True):
        p = (i + 1) ** 3 - i ** 3
        i += 1
        
        if (p >= TOP):
            break
        
        if (isProbablePrime(p)):
            c += 1

    return c

if __name__ == "__main__":
    startTime = time.clock()
    print (eu131())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
