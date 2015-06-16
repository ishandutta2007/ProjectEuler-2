# ----------------------- Largest palindrome product -------------------------- #
#                                                                               #
#       A palindromic number reads the same both ways.                          #
#       The largest palindrome made from the product of                         #
#       two 2-digit numbers is 9009 = 91 × 99.                                  #
#       Find the largest palindrome made from the product of                    #
#       two 3-digit numbers.                                                    #
# ----------------------------------------------------------------------------- #
import time
import math
from euler import isPalindromic
    
def eu4():
    largest = 0
    
    a = 999
    while (a >= 100):
        b = 999
        while (b >= a):
           if ((a * b) < largest):
               break
            
           if (isPalindromic(a * b)):
               largest = a * b
               break
           b -= 1
        a -= 1
        
    return largest

startTime = time.clock()
print (eu4())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
