# -------------------------------------------- Bouncy numbers ------------------------------------------------- #
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
#       Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers         #
#       below one-thousand (525) are bouncy. In fact, the least number for which the proportion of              #
#       bouncy numbers first reaches 50% is 538.                                                                #
#                                                                                                               #
#       Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion  #
#       of bouncy numbers is equal to 90%.                                                                      #
#                                                                                                               #
#       Find the least number for which the proportion of bouncy numbers is exactly 99%.                        #
# ------------------------------------------------------------------------------------------------------------- #
import time

def isIncreasingNumber(n):
    if (n < 10):
        return True

    last = n % 10
    n //= 10

    while (n != 0):
        d = n % 10

        if (d > last):
            return False
        
        n //= 10
        last = d

    return True

def isDecreasingNumber(n):
    if (n < 10):
        return True

    last = n % 10
    n //= 10

    while (n != 0):
        d = n % 10

        if (d < last):
            return False
        
        n //= 10
        last = d

    return True

def isBouncyNumber(n):
    return (not isIncreasingNumber(n) and not isDecreasingNumber(n))

def eu112():
    TOP = 10000000

    n = 0
    d = 0
    for i in range(1, TOP):
        if (isBouncyNumber(i) == True):
            n += 1
        d += 1

        if (n / d == 0.99):
            return i

if __name__ == "__main__":
    startTime = time.clock()
    print (eu112())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
