# ------------------------------------------ How many reversible numbers are there below one-billion? ----------------------------------------- #
#                                                                                                                                               #
#       Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits.                   #
#       For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible.          #
#       Leading zeroes are not allowed in either n or reverse(n).                                                                               #
#                                                                                                                                               #
#       There are 120 reversible numbers below one-thousand.                                                                                    #                                                                                                                                            #
#                                                                                                                                               #
#       How many reversible numbers are there below one-billion (10^9)?                                                                         #                                                                                                          #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import math

def getReversed(n):
    r = 0

    while (n != 0):
        r *= 10
        r += n % 10
        n //= 10

    return r

def isEntirelyOdd(n):
    while (n != 0):
        if (n % 2 == 0):
            return False

        n //= 10

    return True

def isReversible(n):
    if (n % 10 == 0):
        return False

    s = n + getReversed(n)

    return isEntirelyOdd(s)

def eu145():
    TOP = 10 ** 9

    s = 0
    for i in range(1, TOP):
        if (isReversible(i)):
            s += 1

    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu145())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
