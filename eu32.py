# ------------------------------------------ Pandigital products ---------------------------------------------- #
#                                                                                                               #
#       We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;#
#       for example, the 5-digit number, 15234, is 1 through 5 pandigital.                                      #
#                                                                                                               #
#       The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,     #
#       and product is 1 through 9 pandigital.                                                                  #
#                                                                                                               #
#       Find the sum of all products whose multiplicand/multiplier/product identity can be written as           #
#       a 1 through 9 pandigital.                                                                               #
#                                                                                                               #
#       HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.#
# ------------------------------------------------------------------------------------------------------------- #
import time
import functools
import itertools

def checkPandigitalProduct(s):
    a = int(s[0])
    b = int(s[1:5])
    c = int(s[5:])

    if (a * b == c):
        if (c in checkPandigitalProduct.HISTORY):
            return 0
        else:
            checkPandigitalProduct.HISTORY[c] = True
            return c

    a = int(s[0:2])
    b = int(s[2:5])
    c = int(s[5:])

    if (a * b == c):
        if (c in checkPandigitalProduct.HISTORY):
            return 0
        else:
            checkPandigitalProduct.HISTORY[c] = True
            return c
        
    return 0
checkPandigitalProduct.HISTORY = { }
    
def eu32():
    p = ["".join(p) for p in itertools.permutations("123456789")]
    s = 0

    for n in p:
        t = checkPandigitalProduct(n)
        if (t != 0):
            s += t
            
    return (s)

startTime = time.clock()
print (eu32())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
