#------------------------------------------------------ Coin partitions ----------------------------------------------- #
#                                                                                                                       #
#       Let p(n) represent the number of different ways in which n coins can be separated into piles.                   #
#       For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.                    #
#                                                                                                                       #
#       OOOOO                                                                                                           #
#       OOOO   O                                                                                                        #
#       OOO   OO                                                                                                        #
#       OOO   O   O                                                                                                     #
#       OO   OO   O                                                                                                     #
#       OO   O   O   O                                                                                                  #
#       O   O   O   O   O                                                                                               #
#                                                                                                                       #
#       Find the least value of n for which p(n) is divisible by one million.                                           #                                                                                                   #
# --------------------------------------------------------------------------------------------------------------------- #
import time
import math

def genGeneralizedPentagonalNumbers():
    i = 1

    while (True):
        if (i not in genGeneralizedPentagonalNumbers.HISTORY):
            genGeneralizedPentagonalNumbers.HISTORY[i] = i * (3 * i - 1) // 2
        yield genGeneralizedPentagonalNumbers.HISTORY[i]
        i_neg = 0 - i
        if (i_neg not in genGeneralizedPentagonalNumbers.HISTORY):
            genGeneralizedPentagonalNumbers.HISTORY[i_neg] = i_neg * (3 * i_neg - 1) // 2
        yield genGeneralizedPentagonalNumbers.HISTORY[i_neg]
        i += 1
        
genGeneralizedPentagonalNumbers.HISTORY = {1:1}

def partitionPModulo(n):
    if (n < 0):
        return 0

    if (n in partitionPModulo.HISTORY):
        return partitionPModulo.HISTORY[n]

    s = 0
    gp = genGeneralizedPentagonalNumbers()
    gpe = next(gp)
    i = 0
    while (gpe <= n):
        sign = (-1) ** int(i / 2)
        s += partitionPModulo(n - gpe) * sign
        gpe = next(gp)
        i = (i + 1) % 4

    partitionPModulo.HISTORY[n] = s % partitionPModulo.MODULOS
    
    return partitionPModulo.HISTORY[n]
partitionPModulo.HISTORY = {0: 1}
partitionPModulo.MODULOS = 1000000
    
def eu78():
    n = 1

    while (partitionPModulo(n) != 0):
        n += 1
        
    return n

if __name__ == "__main__":
    startTime = time.clock()
    print (eu78())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
