# --------------------------------------------- Digit factorials ---------------------------------------------- #
#                                                                                                               #
#       145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.                                          #
#                                                                                                               #
#       Find the sum of all numbers which are equal to the sum of the factorial of their digits.                #
#                                                                                                               #
#       Note: as 1! = 1 and 2! = 2 are not sums they are not included.                                          #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math
import fractions

def isFactorialElement(n):
    """ Returns the next factorial element """
    org = n
    c = 0
    while (n):
        c += isFactorialElement.factorials[n % 10]
        n = n // 10

    return (org == c)
isFactorialElement.factorials = [math.factorial(i) for i in range(10)]

def eu34():
    tot = 0
    TOP = 7 * isFactorialElement.factorials[9] # 6 * 9!

    return sum([i for i in range(3, TOP + 1) if (isFactorialElement(i))])        

startTime = time.clock()
print (eu34())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
