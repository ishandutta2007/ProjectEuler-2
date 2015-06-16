# ----------------------------------------------------------- Under The Rainbow --------------------------------------------------------------- #
#                                                                                                                                               #
#       70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.                                                         #
#                                                                                                                                               #
#       What is the expected number of distinct colors in 20 randomly picked balls?                                                             #
#                                                                                                                                               #
#       Give your answer with nine digits after the decimal point (a.bcdefghij).                                                                #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import math

from euler.combinatorics import nCk

def eu493():
    NUM_OF_COLORS = 7
    BALLS_EACH_COLOR = 10
    TOT_PICK = 20
    
    return str(7 * (1 - nCr((NUM_OF_COLORS - 1) * BALLS_EACH_COLOR, TOT_PICK) / nCk(NUM_OF_COLORS * BALLS_EACH_COLOR, TOT_PICK)))[:11]

if __name__ == '__main__':
    startTime = time.clock()
    print (eu493())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")

