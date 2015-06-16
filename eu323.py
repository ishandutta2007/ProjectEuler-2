# ------------------------------------------------ Bitwise-OR operations on random integers --------------------------------------------------- #
#                                                                                                                                               #
#       Let y0, y1, y2,... be a sequence of random unsigned 32 bit integers                                                                     #
#       (i.e. 0 ≤ yi < 2^32, every value equally likely).                                                                                       #
#                                                                                                                                               #
#       For the sequence xi the following recursion is given:                                                                                   #
#       -)  x0 = 0 and                                                                                                                          #
#       -)  xi = xi-1 | yi-1, for i > 0. ( | is the bitwise-OR operator)                                                                        #
#       It can be seen that eventually there will be an index N such that xi = 2^32 -1 (a bit-pattern of all ones) for all i ≥ N.               #
#                                                                                                                                               #
#       Find the expected value of N.                                                                                                           #
#       Give your answer rounded to 10 digits after the decimal point.                                                                          #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def eu323():
    E_ACC = 1
    E = 1

    m = 1
    while E > 1e-11:
        E = 1 - (1 - (1 / (2 ** m))) ** 32
        E_ACC += E
        m += 1

    return "{:.11}".format(E_ACC)

if __name__ == '__main__':
    startTime = time.clock()
    print (eu323())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
