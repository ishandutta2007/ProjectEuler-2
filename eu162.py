# ----------------------------------------- Hexadecimal numbers ------------------------------------------- #
#                                                                                                           #
#       In the hexadecimal number system numbers are represented using 16 different digits:                 #
#                                                                                                           #
#                               0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F                                             #
#                                                                                                           #
#       The hexadecimal number AF when written in the decimal number system equals 10x16+15=175.            #
#                                                                                                           #
#       In the 3-digit hexadecimal numbers 10A, 1A0, A10, and A01 the digits 0,1 and A are all present.     #
#       Like numbers written in base ten we write hexadecimal numbers without leading zeroes.               #
#                                                                                                           #
#       How many hexadecimal numbers containing at most sixteen hexadecimal digits exist with all of        #
#       the digits 0,1, and A present at least once?                                                        #
#       Give your answer as a hexadecimal number.                                                           #
#                                                                                                           #
#       (A,B,C,D,E and F in upper case, without any leading or trailing code that marks the number          #
#       as hexadecimal and without leading zeroes , e.g. 1A3F and not: 1a3f and not 0x1a3f and not $1A3F    #
#       and not #1A3F and not 0000001A3F)                                                                   #
# --------------------------------------------------------------------------------------------------------- #
import time

def eu162():
    MAX_LEN = 16

    s = 0
    for l in range(3, MAX_LEN + 1):
        s += (15 * 16 ** (l - 1)) - \
             (43 * 15 ** (l - 1)) + \
             (41 * 14 ** (l - 1)) - \
             (13 ** l)

    return hex(s)[2:].upper()
    
if __name__ == "__main__":
    startTime = time.clock()
    print (eu162())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
