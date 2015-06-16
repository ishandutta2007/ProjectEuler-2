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

def ChampernownesConstantDigit(n):
    """ Return's dn of the Champernowne's constant """

    e       = 1 # length of numbers
    mult    = 10 ** e
    
    while (n > (9 * e * (mult // 10))): # skip digits
        n -= (9 * e * (mult // 10))
        e += 1
        mult *= 10

    return int(str((mult // 10) + (n - 1) // e)[(n - 1) % e])
    
def eu40():
    TOP = 7

    m = 1
    for i in range(TOP):
        m *= ChampernownesConstantDigit(10 ** i)

    return m

if __name__ == "__main__":
    startTime = time.clock()
    print (eu40())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
