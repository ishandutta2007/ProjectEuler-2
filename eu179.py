# ---------------------------- Consecutive positive divisors ------------------------------ #
#                                                                                           #
#       Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same       #
#       number of positive divisors. For example, 14 has the positive divisors              #
#       1, 2, 7, 14 while 15 has 1, 3, 5, 15.                                               #
# ----------------------------------------------------------------------------------------- #
import time

def eu179():
    TOP = 10 ** 7

    divisors = [0] * TOP
    s = 0
    
    for i in range(2, TOP // 2 + 1):
        for j in range(2 * i, TOP, i):
            divisors[j] += 1

    for i in range(2, TOP - 1):
        if (divisors[i] == divisors[i + 1]):
            s += 1

    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu179())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
