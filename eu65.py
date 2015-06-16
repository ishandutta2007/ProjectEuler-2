# -------------------------------------------------------------- Convergents of e ------------------------------------------------------------- #
#                                                                                                                                               #
#       The square root of 2 can be written as an infinite continued fraction.                                                                  #
#                                                                                                                                               #
#                       √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... )))                                                                                  #
#                                                                                                                                               #
#       The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum.                                #
#       In a similar way, √23 = [4;(1,3,1,8)].                                                                                                  #
#                                                                                                                                               #
#       It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations.      #
#       Let us consider the convergents for √2.                                                                                                 #
#                                                                                                                                               #
#       1 + 1/2                                         = 3/2                                                                                   #
#       1 + 1/(2 + 1/2)                                 = 7/5                                                                                   #
#       1 + 1/(2 + 1/(2 + 1/2))                         = 17/12                                                                                 #
#       1 + 1/(2 + 1/(2 + 1/(2 + 1/2)))                 = 41/29                                                                                 #
#                                                                                                                                               #
#       Hence the sequence of the first ten convergents for √2 are:                                                                             #
#                                                                                                                                               #
#       1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...                                                            #
#                                                                                                                                               #
#       What is most surprising is that the important mathematical constant,                                                                    #
#       e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].                                                                                       #
#                                                                                                                                               #
#       The first ten terms in the sequence of convergents for e are:                                                                           #
#                                                                                                                                               #
#       2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...                                                                   #
#                                                                                                                                               #
#       The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.                                                                #
#                                                                                                                                               #
#       Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.                                        #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def getDigitalSum(n):
    r = 0

    while (n != 0):
        r += n % 10
        n //= 10

    return r

def genConvergents(a):
    n = [0] * (len(a) + 2)
    d = [0] * (len(a) + 2)

    n[-2], n[-1] = 0, 1
    d[-2], d[-1] = 1, 0
    
    for i in range(0, len(a)):
        n[i] = (a[i] * n[i - 1]) + n[i - 2]
        d[i] = (a[i] * d[i - 1]) + d[i - 2]

        yield(n[i], d[i])

def eu65():
    TOP = 100

    frac = [1] * TOP
    frac[0] = 2

    for i in range(1, int(TOP / 3) + 1):
        frac[2 + 3 * (i - 1)] = 2 * i
        
    a = genConvergents(frac)    
    
    for i in range(TOP):
        c = (next(a))

    return getDigitalSum(c[0])

if __name__ == "__main__":
    startTime = time.clock()
    print (eu65())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
