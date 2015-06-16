# ------------------- Special Pythagorean triplet --------------------- #
#                                                                       #
#       A Pythagorean triplet is a set of three natural numbers,        #
#       a < b < c, for which,                                           #
#                           a^2 + b^2 = c^2                             #
#                                                                       #
#       For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.                     #
#       There exists exactly one Pythagorean triplet for which          #
#               a + b + c = 1000.                                       #
#       Find the product abc.                                           #
# --------------------------------------------------------------------- #
import time
import math
from euler import gcd 

def genPythagorianTriplesWithPerimeter(p):
    """ returns all pythagorian triples up to perimeter (a + b + c) p """
    for m in range(1, int(math.sqrt((p // 2 + 1))) + 1):
        for n in range(1, min(int(p // (2 * m)) + 1 - m, m)):
            if ((m - n) % 2 == 1):
                if (gcd(m, n) == 1):
                    a , b = min(m * m - n * n, 2 * m * n) , max(m * m - n * n, 2 * m * n)
                    c = m * m + n * n

                    if (p % (a + b + c) == 0):
                        k = (p // (a + b + c))
                        return (a * b * c * (k ** 3))

def eu9():
    P = 1000

    return (genPythagorianTriplesWithPerimeter(P))

if __name__ == "__main__":
    startTime = time.clock()
    print (eu9())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
