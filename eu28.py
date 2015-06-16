# ---------------------------------------- Number spiral diagonals -------------------------------------------- #
#                                                                                                               #
#       Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral             #
#       is formed as follows:                                                                                   #
#                                                                                                               #
#                                          21 22 23 24 25                                                       #
#                                          20  7  8  9 10                                                       #
#                                          19  6  1  2 11                                                       #
#                                          18  5  4  3 12                                                       #
#                                          17 16 15 14 13                                                       #
#                                                                                                               #
#       It can be verified that the sum of the numbers on the diagonals is 101.                                 #
#                                                                                                               #
#       What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?        #
# ------------------------------------------------------------------------------------------------------------- #
import time

def eu28():
    LEN = 1001

    s = 0
    
    s += sum([(i ** 2) for i in range(1, LEN + 1, 2)])
    s += sum([i ** 2 - i + 1 for i in range(1, LEN + 1, 2)])
    s += sum([(i - 2) ** 2 + i - 1 for i in range(1, LEN + 1, 2)])
    s += sum([(i - 2) ** 2 + 2 * i - 2 for i in range(1, LEN + 1, 2)])

    s -= 3 # We counted 1 four times

    return s

startTime = time.clock()
print (eu28())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
