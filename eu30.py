# ------------------------------------------- Digit fifth powers ---------------------------------------------- #
#                                                                                                               #
#       Surprisingly there are only three numbers that can be written as the sum of fourth powers of            #
#       their digits:                                                                                           #
#                                                                                                               #
#                                          1634 = 1^4 + 6^4 + 3^4 + 4^4                                         #
#                                          8208 = 8^4 + 2^4 + 0^4 + 8^4                                         #
#                                          9474 = 9^4 + 4^4 + 7^4 + 4^4                                         #
#                                                                                                               #
#       As 1 = 14 is not a sum it is not included.                                                              #
#       The sum of these numbers is 1634 + 8208 + 9474 = 19316.                                                 #
#                                                                                                               #
#       Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.         #
# ------------------------------------------------------------------------------------------------------------- #
import time
from euler.numbers import is_digit_fifth_power_number

def eu30():
    TOP = 6 * 9**5 # < 7-digits number
    
    count = 0
    for i in range(2, TOP + 1):
        if is_digit_fifth_power_number(i):
            count += i
    
    return count

startTime = time.clock()
print (eu30())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
