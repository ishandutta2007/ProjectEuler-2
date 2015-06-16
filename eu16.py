# ------------------------------------ Power digit sum ------------------------------------ #
#                                                                                           #
#       2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.                   #
#       What is the sum of the digits of the number 2^1000?                                 #
# ----------------------------------------------------------------------------------------- #
import time
import math

def eu16():
    EXP = 1000

    return sum([int(i) for i in str(2**EXP)])

startTime = time.clock()
print (eu16())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
