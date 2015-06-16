# -------------------------------------- Lexicographic permutations ------------------------------------------- #
#                                                                                                               #
#       A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation       #
#       of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,       #
#       we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:                       #
#                                                                                                               #
#                                   012   021   102   120   201   210                                           #
#                                                                                                               #
#       What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?          #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

def eu24():
    INDEX = 1000000
    
    permutation = ""
    digits = list(range(10))
    
    for d in range (9, -1 , -1):
        tmp = 0
        while (INDEX > math.factorial(d)):
            tmp += 1
            INDEX -= math.factorial(d)
        permutation += str(digits[tmp])
        digits.pop(tmp)

    permutation += "".join(digits)

    return (permutation)

startTime = time.clock()
print (eu24())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
