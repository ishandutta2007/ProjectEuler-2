# ------------------------------------------- Reciprocal cycles ----------------------------------------------- #
#                                                                                                               #
#       A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions           #
#       with denominators 2 to 10 are given:                                                                    #
#                                                                                                               #
#                               1/2	= 	0.5                                                             #
#                               1/3	= 	0.(3)                                                           #
#                               1/4	= 	0.25                                                            #
#                               1/5	= 	0.2                                                             #
#                               1/6	= 	0.1(6)                                                          #
#                               1/7	= 	0.(142857)                                                      #
#                               1/8	= 	0.125                                                           #
#                               1/9	= 	0.(1)                                                           #
#                               1/10	= 	0.1                                                             #
#                                                                                                               #
#   Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has              #
#   a 6-digit recurring cycle.                                                                                  #
#                                                                                                               #
#   Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part. #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

def getDecRepresentation(n, d):
    s = ""
    i = 1
    cycleLength = 0
    HISTORY = {}

    s += str(n // d)
    n %= d

    if (n != 0):
        s += '.'
        
    while (n != 0):
        n *= 10
        
        if (n in HISTORY):
            cycleLength = i - HISTORY[n]
            break
        HISTORY[n] = i
        
        i += 1
        s += str(n // d)
        n %= d

    # Wrap the cycle with ()
    if (cycleLength != 0):
        s = s[:len(s) - cycleLength] + "(" + s[len(s) - cycleLength:]
        s += ")"
        
    return (s, cycleLength)

def eu26():
    MAX_DEMONINATOR = 1000
    m = 0
    t = 0

    for d in range(1, MAX_DEMONINATOR):
        t = getDecRepresentation(1, d)
        if t[1] > m:
            m = t[1]
            longest = d

    return longest

startTime = time.clock()
print (eu26())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
