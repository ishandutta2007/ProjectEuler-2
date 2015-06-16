# ------------------------------------------------------------- Counting summations --------------------------------------------------------------- #
#                                                                                                                                                   #
#       It is possible to write five as a sum in exactly six different ways:                                                                        # 
#                                                                                                                                                   #
#                           4 + 1                                                                                                                   #
#                           3 + 2                                                                                                                   #
#                           3 + 1 + 1                                                                                                               #
#                           2 + 2 + 1                                                                                                               #
#                           2 + 1 + 1 + 1                                                                                                           #
#                           1 + 1 + 1 + 1 + 1                                                                                                       #
#                                                                                                                                                   #
#       How many different ways can one hundred be written as a sum of at least two positive integers?                                              #
# ------------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def countWaysWithAtLeastTwo(n):
    mat = [[0 for x in range(n + 1)] for x in range(n)]

    for i in range(n + 1):
        mat[0][i] = 1

    for i in range(1, n):
        for j in range(0, n + 1):
            mat[i][j] = 0
            for k in range((j // (i + 1)) + 1):
                mat[i][j] += mat[i - 1][j - k * (i + 1)]

    return mat[n - 1][n] - 1

def eu76():
    NUMBER = 100

    return (countWaysWithAtLeastTwo(NUMBER))

startTime = time.clock()
print (eu76())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
