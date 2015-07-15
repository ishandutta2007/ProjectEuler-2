# ------------------------------------------------------------ Strong Repunits ---------------------------------------------------------------- #
#                                                                                                                                               #
#       The number 7 is special, because 7 is 111 written in base 2, and 11 written in base 6                                                   #
#       (i.e. 7_10 = 11_6 = 111_2). In other words, 7 is a repunit in at least two bases b > 1.                                                 #
#                                                                                                                                               #
#       We shall call a positive integer with this property a strong repunit.                                                                   #
#       It can be verified that there are 8 strong repunits below 50: {1,7,13,15,21,31,40,43}.                                                  #
#       Furthermore, the sum of all strong repunits below 1000 equals 15864.                                                                    #
#                                                                                                                                               #
#       Find the sum of all strong repunits below 1012.                                                                                         #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def eu346():
    TOP = 10 ** 12
    
    repunits = []
    base = 2
    
    for base in range(2, TOP):
        repunit = 1
        repunits_base = []
        
        while repunit < base + 1:
            repunit = repunit * base + 1

        stop = True
        
        while (True):
            repunit = repunit * base + 1

            if repunit < TOP:
                repunits_base.append(repunit)
                stop = False
            else:
                break

        if stop == True:
            break
        
        repunits.append(repunits_base)

    repunits_unique = set()
    
    for i in range(len(repunits)):
        repunits_unique.update(set(repunits[i]))
        
    return 1 + sum(repunits_unique)

if __name__ == '__main__':
    startTime = time.clock()
    print (eu346())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
