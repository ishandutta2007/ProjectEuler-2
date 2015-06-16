# -------------------------------------------------- Permuted multiples ----------------------------------------------- #
#                                                                                                                       #
#       It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,                #
#       but in a different order.                                                                                       #
#                                                                                                                       #
#       Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.               #
# --------------------------------------------------------------------------------------------------------------------- #
import time

def getDigits(n):
    ret = []

    while (n != 0):
        ret.append(n % 10)
        n //= 10

    return sorted(ret)

def eu52():
    MAX_MULT = 6

    n = 1

    while (True):
        digits = getDigits(n)
        flag = True

        for m in range(2, MAX_MULT + 1):
            if digits != getDigits(n * m):
                flag = False
                break

        if flag == True:
            return n

        n += 1
            
        #if any(digits != getDigits(n * m) for m in range(2, MAX_MULT + 1)):
        #    n += 1
        #    continue

        #return n

startTime = time.clock()
print (eu52())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
