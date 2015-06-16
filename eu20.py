# -------------------------------------------------- Factorial digit sum ---------------------------------------------- #
#                                                                                                                       #
#       n! means n × (n − 1) × ... × 3 × 2 × 1                                                                          #
#       For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,                                                          #
#       and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.                                  #
#                                                                                                                       #
#       Find the sum of the digits in the number 100!                                                                   #
# --------------------------------------------------------------------------------------------------------------------- #
import time
import math

def eu20():
    return sum([int(d) for d in str(math.factorial(100))])

startTime = time.clock()
print (eu20())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
