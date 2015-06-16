# ------------------------------------------ Red, green or blue tiles ----------------------------------------- #
#                                                                                                               #
#       A row of five black square tiles is to have a number of its tiles replaced with coloured oblong tiles   #
#       chosen from red (length two), green (length three), or blue (length four).                              #
#                                                                                                               #
#       If red tiles are chosen there are exactly seven ways this can be done.                                  #
#                                                                                                               #
#       If green tiles are chosen there are three ways.                                                         #
#                                                                                                               #
#       And if blue tiles are chosen there are two ways.                                                        #
#                                                                                                               #
#       Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the black tiles        #
#       in a row measuring five units in length.                                                                #
#                                                                                                               #
#       How many different ways can the black tiles in a row measuring fifty units in length be replaced        #
#       if colours cannot be mixed and at least one coloured tile must be used?                                 #
#                                                                                                               #
#       NOTE: This is related to problem 117.                                                                   #
# ------------------------------------------------------------------------------------------------------------- #
import time

def R(n):
    for i in range(3, n + 1):
        r = 0

        for j in range(i - 1):
            r += R.MEMORY[j]

        r += i - 1

        R.MEMORY[i] = r

    return R.MEMORY[n]
R.MEMORY = {0: 0, 1: 0, 2: 1}

def G(n):
    for i in range(4, n + 1):
        r = 0

        for j in range(i - 2):
            r += G.MEMORY[j]

        r += i - 2

        G.MEMORY[i] = r

    return G.MEMORY[n]
G.MEMORY = {0: 0, 1: 0, 2: 0, 3: 1}

def B(n):
    for i in range(5, n + 1):
        r = 0

        for j in range(i - 3):
            r += B.MEMORY[j]

        r += i - 3

        B.MEMORY[i] = r

    return B.MEMORY[n]
B.MEMORY = {0: 0, 1: 0, 2: 0, 3: 0, 4: 1}


def eu116():
    LEN = 50

    return (R(LEN) + G(LEN) + B(LEN))

if __name__ == "__main__":
    startTime = time.clock()
    print (eu116())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
