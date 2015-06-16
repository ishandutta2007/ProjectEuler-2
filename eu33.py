# ---------------------------------------- Digit canceling fractions ------------------------------------------ #
#                                                                                                               #
#       The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to            #
#       simplify it may incorrectly believe that 49/98 = 4/8, which is correct,                                 #
#       is obtained by cancelling the 9s.                                                                       #
#                                                                                                               #
#       We shall consider fractions like, 30/50 = 3/5, to be trivial examples.                                  #
#                                                                                                               #
#       There are exactly four non-trivial examples of this type of fraction, less than one in value,           #
#       and containing two digits in the numerator and denominator.                                             #
#                                                                                                               #
#       If the product of these four fractions is given in its lowest common terms,                             #
#       find the value of the denominator.                                                                      #
# ------------------------------------------------------------------------------------------------------------- #
import time
import fractions

def eu33():
    prod = fractions.Fraction(1)
    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(1, 10):
                if ((10*a + b) / (10*b + c) == (a / c)):
                    prod *= a
                    prod /= c

    return prod.denominator

startTime = time.clock()
print (eu33())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
