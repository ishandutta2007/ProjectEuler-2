# ------------------------------------------------------ Robot Walks ------------------------------------------------------ #
#                                                                                                                           #
#       A robot moves in a series of one-fifth circular arcs (72°), with a free choice of a clockwise or an                 #
#       anticlockwise arc for each step, but no turning on the spot.                                                        #
#                                                                                                                           #
#       One of 70932 possible closed paths of 25 arcs starting northward is                                                 #
#                                                                                                                           #
#                                                                                                                           #
#       Given that the robot starts facing North, how many journeys of 70 arcs in length can it take that return it,        #
#       after the final arc, to its starting position?                                                                      #
#       (Any arc may be traversed multiple times.)                                                                          #
# ------------------------------------------------------------------------------------------------------------------------- #
import time
from euler.combinatorics import nCk

def eu208():
    NO_OF_ARCS = 25

    no_of_circles = NO_OF_ARCS // 5

    s = 0
    for i in range(no_of_circles + 1):
        no_of_clockwise_arcs = i * 5
        s += nCk(NO_OF_ARCS, no_of_clockwise_arcs)

    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu208())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
