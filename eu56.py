# ------------------------------------------------------------- Powerful digit sum ------------------------------------------------------------ #
#                                                                                                                                               #
#       A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large:                         #
#       one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.                                  #
#                                                                                                                                               #
#       Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?                                         #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def getDigitalSum(n):
    r = 0

    while (n != 0):
        r += n % 10
        n //= 10

    return r

def eu56():
    TOP = 100

    max_digital_sum = 0

    for a in range(TOP):
        for b in range(TOP):
            if ((getDigitalSum(a ** b)) > max_digital_sum):
                max_digital_sum = getDigitalSum(a ** b) 

    return max_digital_sum

if __name__ == "__main__":
    startTime = time.clock()
    print (eu56())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
