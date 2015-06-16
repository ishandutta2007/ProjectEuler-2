# ---------------------------- Numbers for which no three consecutive digits have a sum greater than a given value ---------------------------- #
#                                                                                                                                               #
#       How many 20 digit numbers n (without any leading zero) exist such that no three consecutive digits of n have a sum greater than 9?      #                                                            #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def calc(d0, d1, remaining):
    if (remaining == 0):
        return 1

    if ((d0, d1, remaining) in calc.MEMORY):
        return calc.MEMORY[(d0, d1, remaining)]
    
    s = 0

    for i in range(10 - d0 - d1):
        s += calc(d1, i, remaining - 1)

    calc.MEMORY[(d0, d1, remaining)] = s

    return s
calc.MEMORY = { }
    
def eu164():
    LEN = 20

    s = 0
    for i in range(1, 10):
        s += calc(0, i, LEN - 1)

    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu164())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
