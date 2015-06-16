# ------------------------------------- Lattice paths ------------------------------------- #
#                                                                                           #
#       Starting in the top left corner of a 2×2 grid, and only being able to move          #
#           to the right and down, there are exactly 6 routes to the bottom right corner.   #
#                                                                                           #
#       How many such routes are there through a 20×20 grid?                                #
# ----------------------------------------------------------------------------------------- #
import time
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def eu15():
    SIZE = 20

    """ The answer is (SIZE * 2) choose (SIZE) """

    if SIZE % 2 == 0:
        return int(nCr(SIZE * 2, SIZE))

startTime = time.clock()
print (eu15())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
