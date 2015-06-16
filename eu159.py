# ---------------------------------------- Digital root sums of factorisations -------------------------------------------- #
#                                                                                                                           #
#       A composite number can be factored many different ways. For instance, not including multiplication by one,          #
#       24 can be factored in 7 distinct ways:                                                                              #
#                                                                                                                           #
#               24 = 2x2x2x3                                                                                                #
#               24 = 2x3x4                                                                                                  #
#               24 = 2x2x6                                                                                                  #
#               24 = 4x6                                                                                                    #
#               24 = 3x8                                                                                                    #
#               24 = 2x12                                                                                                   #
#               24 = 24                                                                                                     #
#                                                                                                                           #
#       Recall that the digital root of a number, in base 10, is found by adding together the digits of that number,        #
#       and repeating that process until a number is arrived at that is less than 10. Thus the digital root of 467 is 8.    #
#                                                                                                                           #
#       We shall call a Digital Root Sum (DRS) the sum of the digital roots of the individual factors of our number.        #
#                                                                                                                           #
#       The chart below demonstrates all of the DRS values for 24.                                                          #
#                                                                                                                           #
#                                           Factorisation	Digital Root Sum                                            #
#                                           2x2x2x3             9                                                           #
#                                           2x3x4               9                                                           #
#                                           2x2x6               10                                                          #
#                                           4x6                 10                                                          #
#                                           3x8                 11                                                          #
#                                           2x12                5                                                           #
#                                           24                  6                                                           #
#                                                                                                                           #
#       The maximum Digital Root Sum of 24 is 11.                                                                           #
#       The function mdrs(n) gives the maximum Digital Root Sum of n. So mdrs(24)=11.                                       #
#       Find ∑mdrs(n) for 1 < n < 1,000,000.                                                                                #
# ------------------------------------------------------------------------------------------------------------------------- #
import time
from euler.numbers import digital_root 

def eu159():
    TOP = 10 ** 6

    mdrs = [digital_root(i) for i in range(TOP + 1)]

    for j in range(2, TOP):
        drs_j = mdrs[j]
        for k in range(2, j + 1):
            n = j * k

            if n >= TOP:
                break
            
            mdrs[n] = max(mdrs[n], drs_j + mdrs[k]);

    return sum(mdrs[2: TOP])

if __name__ == "__main__":
    startTime = time.clock()
    print (eu159())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
