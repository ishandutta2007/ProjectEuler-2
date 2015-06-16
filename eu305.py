# ----------------------------------------- Champernowne's constant ------------------------------------------- #
#                                                                                                               #
#       An irrational decimal fraction is created by concatenating the positive integers:                       #
#                                                                                                               #
#                   0.123456789101112131415161718192021...                                                      #
#                                                                                                               #
#       It can be seen that the 12th digit of the fractional part is 1.                                         #
#                                                                                                               #
#       If dn represents the nth digit of the fractional part, find the value of the following expression.      #
#                                                                                                               #
#                   d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000                                       #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

def champernownes_starting_position_of_n(n):
    """ Return's the starting position of the nth number in Champerowne's constant. """

    l = len(str(n))
    d = 0
    
    for i in range(1, l):
        d += (9 * 10**(i - 1)) * i
    d += (n - 10**(l - 1)) * l

    return d + 1        
    
def eu305():
    TOP = 7

    pass

if __name__ == "__main__":
    startTime = time.clock()
    print (eu305())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
