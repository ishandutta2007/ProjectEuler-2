# ---------------------------------------------------------- Odd period square roots ---------------------------------------------------------- #
#                                                                                                                                               #
#       All square roots are periodic when written as continued fractions and can be written in the form:                                       #
#                                                                                                                                               #
#                       √ N = a0 + 1/(a1 + 1/(a2 + 1/(a3 + ... )))                                                                              #
#                                                                                                                                               #
#       For example, let us consider √23:                                                                                                       #
#                                                                                                                                               #
#       √23 = 4 + √23 - 4 = 4 + 1/(1/(√23 - 4)) = 4 + 1/(1 + (√23 - 3) / 7)                                                                     #
#                                                                                                                                               #
#       If we continue we would get the following expansion:                                                                                    #
#                                                                                                                                               #
#       √23 = 4 + 1/(1 + 1/(3 + 1/(1 + 1/8 + ...)))                                                                                             #
#                                                                                                                                               #
#       The process can be summarised as follows:                                                                                               #
#                                                                                                                                               #
#       a0 = 4, 1/(√23 - 4) = (√23 + 4)/7   = 1 + (√23 - 3)/7                                                                                   #
#       a1 = 1, 7/(√23 - 3) = 7(√23 + 3)/14 = 3 + (√23 - 3)/2                                                                                   #
#       a2 = 3, 2/(√23 - 2) = 2(√23 + 3)/14 = 1 + (√23 - 4)/7                                                                                   #
#       a3 = 1, 7/(√23 - 4) = 4(√23 + 4)/7  = 8 + (√23 - 4)                                                                                     #
#       a4 = 8, 1/(√23 - 4) = (√23 + 4)/7   = 1 + (√23 - 3)/7                                                                                   #
#       a5 = 1, 7/(√23 - 3) = 7(√23 + 3)/14 = 3 + (√23 - 3)/2                                                                                   #
#       a6 = 3, 2/(√23 - 3) = 2(√23 + 3)/14 = 1 + (√23 - 4)/7                                                                                   #
#       a7 = 1, 7/(√23 - 4) = 7(√23 + 4)/7  = 8 + (√23 - 4)                                                                                     #
#                                                                                                                                               #
#       It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)],                                #
#       to indicate that the block (1,3,1,8) repeats indefinitely.                                                                              #
#                                                                                                                                               #
#       The first ten continued fraction representations of (irrational) square roots are:                                                      #
#                                                                                                                                               #
#       √2=[1;(2)],         period=1                                                                                                            #
#       √3=[1;(1,2)],       period=2                                                                                                            #
#       √5=[2;(4)],         period=1                                                                                                            #
#       √6=[2;(2,4)],       period=2                                                                                                            #
#       √7=[2;(1,1,1,4)],   period=4                                                                                                            #
#       √8=[2;(1,4)],       period=2                                                                                                            #
#       √10=[3;(6)],        period=1                                                                                                            #
#       √11=[3;(3,6)],      period=2                                                                                                            #
#       √12= [3;(2,6)],     period=2                                                                                                            #
#       √13=[3;(1,1,1,1,6)], period=5                                                                                                           #
#                                                                                                                                               #
#       Exactly four continued fractions, for N ≤ 13, have an odd period.                                                                       #
#                                                                                                                                               #
#       How many continued fractions for N ≤ 10000 have an odd period?                                                                          #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import math

def getSqrtConvergent(n):
    history = { }
    
    a = []
    m = []
    d = []

    a.append(int(math.sqrt(n)))
    m.append(0)
    d.append(1)

    history[(a[0], m[0], d[0])] = 0

    i = 0
    while (True):
        m.append(a[i] * d[i] - m[i])
        d.append((n - (m[i + 1] ** 2)) / d[i])
        a.append(math.floor((math.sqrt(n) + m[i + 1]) / d[i + 1]))

        i += 1

        if ((a[i], m[i], d[i]) in history):
            l = history[(a[i], m[i], d[i])]
            del a[-1]
            del m[-1]
            del d[-1]
            return i - l
        
        history[(a[i], m[i], d[i])] = i

    return a

def eu64():
    TOP = 10000

    squares = [i ** 2 for i in range(int(math.sqrt(TOP)) + 1)]
    t = [i for i in range(TOP + 1) if i not in squares]
    s = 0

    for n in t:
        if getSqrtConvergent(n) % 2 == 1:
            s += 1
            
    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu64())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
