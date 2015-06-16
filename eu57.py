# ----------------------------------------------------------- Square root convergents --------------------------------------------------------- #
#                                                                                                                                               #
#       It is possible to show that the square root of two can be expressed as an infinite continued fraction.                                  #
#                                                                                                                                               #
#                       √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...                                                                    #
#                                                                                                                                               #
#       By expanding this for the first four iterations, we get:                                                                                #
#                                                                                                                                               #
#                       1 + 1/2 = 3/2 = 1.5                                                                                                     #
#                       1 + 1/(2 + 1/2) = 7/5 = 1.4                                                                                             #
#                       1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...                                                                            #
#                       1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...                                                                    #
#                                                                                                                                               #
#       The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,                                          #
#       is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.                       #
#                                                                                                                                               #
#       In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?                         #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def genConvergents(a):
    n = [0] * (len(a) + 2)
    d = [0] * (len(a) + 2)

    n[-2], n[-1] = 0, 1
    d[-2], d[-1] = 1, 0
    
    for i in range(0, len(a)):
        n[i] = (a[i] * n[i - 1]) + n[i - 2]
        d[i] = (a[i] * d[i - 1]) + d[i - 2]

        yield(n[i], d[i])

def eu57():
    TOP = 1000

    frac = [2] * TOP
    frac[0] = 1

    a = genConvergents(frac)
    s = 0
    
    for i in range(TOP):
        c = (next(a))
        if (len(str(c[0])) > len(str(c[1]))):
            s += 1

    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu57())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
