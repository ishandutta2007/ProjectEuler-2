# ------------------------ Largest prime factor ------------------------------- #
#                                                                               #
#       The prime factors of 13195 are 5, 7, 13 and 29.                         #
#       What is the largest prime factor of the number 600851475143 ?           #
# ----------------------------------------------------------------------------- #
import time
import math

def eu3():
    num = 600851475143

    while (num % 2 == 0):
        num /= 2
    
    lastFact = 3
    maxFact = int(math.sqrt(num))

    while (lastFact <= maxFact):
        while (num % lastFact == 0):
            num /= lastFact

        lastFact += 1
        maxFact = int(math.sqrt(num))

    if (num == 1):
        return lastFact
    else:
        return int(num)

startTime = time.clock()
print (eu3())
elapsedTime = time.clock() - startTime
print ("Time spent in (function name) is: ", elapsedTime, " sec")
