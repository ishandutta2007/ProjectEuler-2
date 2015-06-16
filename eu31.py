# ------------------------------------------------ Coin sums -------------------------------------------------- #
#                                                                                                               #
#       In England the currency is made up of pound, £, and pence, p, and there are eight coins                 #
#       in general circulation:                                                                                 #
#                                                                                                               #
#                           1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).                                 #
#                                                                                                               #
#       It is possible to make £2 in the following way:                                                         #
#                                                                                                               #
#                               1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p                                       #
#                                                                                                               #
#       How many different ways can £2 be made using any number of coins?                                       #
# ------------------------------------------------------------------------------------------------------------- #
import time

def eu31(coins, value):
    mat = [[0 for x in range(value + 1)] for x in range(len(coins))]

    for i in range(value + 1):
        mat[0][i] = 1

    for i in range(1, len(coins)):
        for j in range(0, value + 1):
            mat[i][j] = 0
            for k in range((j // coins[i]) + 1):
                mat[i][j] += mat[i - 1][j - k * coins[i]]

    return mat[len(coins) - 1][value]

startTime = time.clock()
print (eu31([1, 2, 5, 10, 20, 50, 100, 200], 200))
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
