# -------------------------------------- Writing 1/2 as a sum of inverse squares ------------------------------------------ #
#                                                                                                                           #
#       There are several ways to write the number 1/2 as a sum of inverse squares using distinct integers.                 #

#       For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:                                                   #
#                                                                                                                           #
#       
#       In fact, only using integers between 2 and 45 inclusive, there are exactly three ways to do it,                     #
#       the remaining two being: {2,3,4,6,7,9,10,20,28,35,36,45} and {2,3,4,6,7,9,12,15,28,30,35,36,45}.                    #

#       How many ways are there to write the number 1/2 as a sum of inverse squares using distinct integers                 #
#       between 2 and 80 inclusive?                                                                                         #
# ------------------------------------------------------------------------------------------------------------------------- #
import time
from fractions import Fraction

def a(f, target):
    if sum(f) < target:
        return

    if f == []:
        return
    
    if target == 0:
        print(1)
        return

    a(f[1:], target - f[0])
    a(f[1:], target)
    
def eu152():
    TOP = 40
    
    f = [i**2 for i in range(2, TOP + 1)]
    f = [Fraction(1, i) for i in f]

    f = f[1:]

    a(f, 0.25)
    
    return f

if __name__ == "__main__":
    startTime = time.clock()
    print (eu152())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
