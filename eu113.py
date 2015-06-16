# ----------------------------------------- Non-bouncy numbers ------------------------------------------------ #
#                                                                                                               #
#       Working from left-to-right if no digit is exceeded by the digit to its left it is called                #
#       an increasing number; for example, 134468.                                                              #
#                                                                                                               #
#       Similarly if no digit is exceeded by the digit to its right it is called a decreasing number;           #
#       for example, 66420.                                                                                     #
#                                                                                                               #
#       We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number;           #
#       for example, 155349.                                                                                    #
#                                                                                                               #
#       As n increases, the proportion of bouncy numbers below n increases such that there are only             #
#       12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 10^10.     #
#                                                                                                               #
#       How many numbers below a googol (10^100) are not bouncy?                                                #
# ------------------------------------------------------------------------------------------------------------- #
import time

def countIncreasingNumbersWithLen(l):
    def countIncreasingNumbers(l, lastDigit):
        if (l == 1):
            countIncreasingNumbers.HISTORY[(l, lastDigit)] = 1
            return 1

        if ((l, lastDigit) in countIncreasingNumbers.HISTORY):
            return countIncreasingNumbers.HISTORY[(l, lastDigit)]
        
        s = 0
        for i in range(1, lastDigit + 1):
            s += countIncreasingNumbers(l - 1, i)

        countIncreasingNumbers.HISTORY[(l, lastDigit)] = s

        return s
    countIncreasingNumbers.HISTORY = { }
    
    s = 0

    for i in range(1, 10):
        s += countIncreasingNumbers(l, i)

    return s

def countDecreasingNumbersWithLen(l):
    def countDecreasingNumbers(l, lastDigit):
        if (l == 1):
            if (lastDigit == 0):
                countDecreasingNumbers.HISTORY[(l, lastDigit)] = 0
            else:
                countDecreasingNumbers.HISTORY[(l, lastDigit)] = 1
            return countDecreasingNumbers.HISTORY[(l, lastDigit)]

        if ((l, lastDigit) in countDecreasingNumbers.HISTORY):
            return countDecreasingNumbers.HISTORY[(l, lastDigit)]
        
        s = 0
        for i in range(9, lastDigit - 1, -1):
            s += countDecreasingNumbers(l - 1, i)

        countDecreasingNumbers.HISTORY[(l, lastDigit)] = s

        return s
    countDecreasingNumbers.HISTORY = { }
    
    s = 0

    for i in range(9, -1, -1):
        s += countDecreasingNumbers(l, i)

    return s

def eu113():
    TOP = 10 ** 100

    s = 0
    
    for l in range(1, len(str(TOP))):
        s += countIncreasingNumbersWithLen(l)
        s += countDecreasingNumbersWithLen(l)
        s -= 9

    return s

    # BETTER WAY
    #count = 0
    #for i in range(1,101):
    #      count += nCr(8+i,i)
    #      count += nCr(9+i,i)
    #      count -= 10
    #print (count)

if __name__ == "__main__":
    startTime = time.clock()
    print (eu113())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
