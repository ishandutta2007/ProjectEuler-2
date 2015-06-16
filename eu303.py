# -------------------------------------------------------- Multiples with small digits ----------------------------------------------------------- #
#                                                                                                                                                  #
#       For a positive integer n, define f(n) as the least positive multiple of n that, written in base 10, uses only digits ≤ 2.                  #
#                                                                                                                                                  #
#       Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.                                                                                   #
#                                                                                                                                                  #
#       Also, sigma, n = 1 to 100 (f(n) / n) = 11363107.                                                                                           #
#                                                                                                                                                  #
#       Find sigma, n = 1 to 10000 (f(n) / n)                                                                                                      #
# ------------------------------------------------------------------------------------------------------------------------------------------------ #
import time

def genSmallDigitsNumbers():
    for i in range(len(genSmallDigitsNumbers.HISTORY)):
        yield genSmallDigitsNumbers.HISTORY[i]
        
    c = len(genSmallDigitsNumbers.HISTORY)
    i = str(genSmallDigitsNumbers.HISTORY[c - 1])

    while (True):
        l = len(i)
        if (i[l - 1]) == "0":
            i = i[:l - 1] + "1"
        elif (i[l - 1]) == "1":
            i = i[:l - 1] + "2"
        else:
            while i[l - 1] == "2":
                i = i[:l - 1] + "0" + i[l:]
                l -= 1
            if (l == 0):
                i = "1" + i[:]
            else:
                if i[l - 1] == "0":
                    i = i[:l - 1] + "1" + i[l:]
                elif i[l - 1] == "1":
                    i = i[:l - 1] + "2" + i[l:]

        if (c < 10000000):
            genSmallDigitsNumbers.HISTORY.append(int(i))
        yield int(i)
genSmallDigitsNumbers.HISTORY = [1]

def f(n):
    sdn = genSmallDigitsNumbers()

    f = next(sdn)
    
    while f % n != 0:
        f = next(sdn)

    return f
    
def eu303():
    TOP = 10000
    s = 0

    for i in range(1, TOP + 1):
        s += f(i) // i

    return s
        
if __name__ == "__main__":
    startTime = time.clock()
    print (eu303())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
