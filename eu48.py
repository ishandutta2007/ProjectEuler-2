# ---------------------------------------------- Self powers -------------------------------------------------- #
#                                                                                                               #
#       The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.                                                #
#                                                                                                               #
#       Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.                              #
# ------------------------------------------------------------------------------------------------------------- #
import time

def eu48():
    TOP = 1000

    return sum([i**i for i in range(TOP + 1)]) % 10000000000

if __name__ == "__main__":
    startTime = time.clock()
    print (eu48())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
