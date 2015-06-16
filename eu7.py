# ---------------------- Sum square difference ------------------------ #
#                                                                       #
#       The sum of the squares of the first ten natural numbers is,     #
#                   1^2 + 2^2 + ... + 10^2 = 385                        #
#       The square of the sum of the first ten natural numbers is,      #
#                   (1 + 2 + ... + 10)^2 = 55^2 = 3025                  #
#       Hence the difference between the sum of the squares of the      #
#       first ten natural numbers and the square of the sum is          #
#                           3025 − 385 = 2640.                          #
#       Find the difference between the sum of the squares of the       #
#       first one hundred natural numbers and the square of the sum.    #
# --------------------------------------------------------------------- #
import time
import math
from euler import isPrime

def isPrime1(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
    
def eu7():
    LIMIT = 10001

    candidate = 1
    numOfPrimes = 1

    while (numOfPrimes != LIMIT):
        candidate += 2
        
        if isPrime(candidate):
            numOfPrimes += 1        

    return candidate

startTime = time.clock()
print (eu7())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
