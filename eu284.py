# ------------------------------------------------------------ Steady Squares ----------------------------------------------------------------- #
#                                                                                                                                               #
#       The 3-digit number 376 in the decimal numbering system is an example of numbers with the special property                               #
#       that its square ends with the same digits: 376^2 = 141376. Let's call a number with this property a steady square.                      #
#                                                                                                                                               #
#       Steady squares can also be observed in other numbering systems. In the base 14 numbering system,                                        #
#       the 3-digit number c37 is also a steady square: c37^2 = aa0c37, and the sum of its digits is c+3+7=18 in the same numbering system.     #
#       The letters a, b, c and d are used for the 10, 11, 12 and 13 digits respectively,                                                       #
#       in a manner similar to the hexadecimal numbering system.                                                                                #
#                                                                                                                                               #
#       For 1 ≤ n ≤ 9, the sum of the digits of all the n-digit steady squares in the base 14 numbering system is 2d8 (582 decimal).            #
#       Steady squares with leading 0's are not allowed.                                                                                        #
#                                                                                                                                               #
#       Find the sum of the digits of all the n-digit steady squares in the base 14 numbering system for                                        #
#       1 ≤ n ≤ 10000 (decimal) and give your answer in the base 14 system using lower case letters where necessary.                            #                                                                                        #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.number_theory.basics import modular_multiplicative_inverse
from euler.numbers import to_base
                   
def eu284():
    TOP = 10000

    s = 1 # 1 is steady square in all bases

    seven = 7 ** TOP
    two = 2 ** TOP

    x = seven % two
    y = (-1 * modular_multiplicative_inverse(x, two)) % two

    n1 = to_base(seven * y + 1, 14)
    n2 = to_base(seven * (two - y), 14)

    c = 1
    for i in range(len(n1)):
        if n1[i] == '0':
            continue

        if 'a' <= n1[i] <= 'd':
            s += c * (ord(n1[i]) - ord('a') + 10)
        else:
            s += c * int(n1[i])
        c += 1
                   
    c = 1
    for i in range(len(n2)):
        if n2[i] == '0':
            continue

        if 'a' <= n2[i] <= 'd':
            s += c * (ord(n2[i]) - ord('a') + 10)
        else:
            s += c * int(n2[i])
        c += 1

    return to_base(s, 14)
    
if __name__ == '__main__':
    startTime = time.clock()
    print (eu284())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
