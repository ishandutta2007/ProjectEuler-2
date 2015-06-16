# ----------------------------- Using up to one million tiles how many different "hollow" square laminae can be formed? ------------------------------- #
#                                                                                                                                                       #
#       We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical and horizontal symmetry.       #
#       For example, using exactly thirty-two square tiles we can form two different square laminae:                                                    #
#                                                                                                                                                       #
#                                               * * * * * *             * * * * * * * * *                                                               #
#                                               * * * * * *             *               *                                                               #
#                                               * *     * *             *               *                                                               #
#                                               * *     * *             *               *                                                               #
#                                               * * * * * *             *               *                                                               #
#                                               * * * * * *             *               *                                                               #
#                                                                       *               *                                                               #
#                                                                       *               *                                                               #
#                                                                       * * * * * * * * *                                                               #
#                                                                                                                                                       #
#       With one-hundred tiles, and not necessarily using all of the tiles at one time, it is possible to form forty-one different square laminae.      #
#                                                                                                                                                       #
#       Using up to one million tiles how many different square laminae can be formed?                                                                  #
# ----------------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from math import ceil

def eu173():
    TOP = 1000000

    c = 0
    for a in range(3, (TOP + 4) // 4 + 1):
        min_b = 1 if (a ** 2 - TOP) <= 0 else ceil((a ** 2 - TOP) ** 0.5)
        c += (a - 2 - min_b) // 2 + 1

    return c

if __name__ == "__main__":
    startTime = time.clock()
    print (eu173())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
