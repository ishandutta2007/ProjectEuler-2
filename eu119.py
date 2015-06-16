# ------------------------------------------ Digit power sum -------------------------------------------------- #
#                                                                                                               #
#       The number 512 is interesting because it is equal to the sum of its digits raised to some power:        #
#       5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number with this property is 614656 = 28^4.          #
#                                                                                                               #
#       We shall define an to be the nth term of this sequence and insist that a number must contain at least   #
#       two digits to have a sum.                                                                               #
#                                                                                                               #
#       You are given that a2 = 512 and a10 = 614656.                                                           #
#                                                                                                               #
#       Find a30.                                                                                               #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math
    
def digitPowerSum():
    def sumOfDigits(n):
        s = 0

        while (n != 0):
            s += n % 10
            n //= 10

        return s
    
    l = 2

    while (True):
        r = []
        for s in range(2, min(9 * l + 1, int(10 ** (l / 2)))):
            mi = int(math.log(10 ** (l - 1), s)) + 1
            ma = int(math.log(10 ** l - 1, s))
            c = [(s ** e) for e in range(mi, ma + 1)]
            c = [t for t in c if (sumOfDigits(t) == s)]
            
            r.extend(set(c))

        r = sorted(r)

        for d in r:
            yield d

        l += 1            
        
def eu119():
    INDEX = 30
    
    a = digitPowerSum()
    
    for i in range(INDEX):
        t = next(a)

    return t

if __name__ == "__main__":
    startTime = time.clock()
    print (eu119())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
