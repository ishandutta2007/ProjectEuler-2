# ------------------------------------------ Numbers for which Euler’s totient function equals 13! -------------------------------------------- #
#                                                                                                                                               #
#       The first number n for which φ(n)=13! is 6227180929.                                                                                    #
#                                                                                                                                               #
#       Find the 150,000th such number.                                                                                                         #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import math
from euler.euler import phiInverse
    
def eu248():
    N = math.factorial(13)
    TARGET = 150000
    
    a = phiInverse(N)

    return a[TARGET - 1]

if __name__ == "__main__":
    startTime = time.clock()
    print (eu248())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
