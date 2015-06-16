# ----------------------------------------------------------------- 250250 -------------------------------------------------------------------- #
#                                                                                                                                               #
#       Find the number of non-empty subsets of {1^1, 2^2, 3^3,..., 250250^250250}, the sum of whose elements is divisible by 250.              #
#       Enter the rightmost 16 digits as your answer.                                                                                           #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import math

def powmod(b, e, m):
    """ return b^e mod m """
    r = 1
    b = b % m

    while (e):
        if (e % 2 == 1):
            r = r * b % m
        e //= 2
        b = b * b % m

    return r

def eu250():
    TOP     = 250250
    MODULOS = 250
    
    freq = [0] * MODULOS
    for i in range(1, TOP + 1):
        freq[pow(i, i, MODULOS)] += 1

    #subsets = [[0 for i in range(MODULOS)] for i in range(MODULOS)]
    
    tot = 0

    """tot += freq[0]

    subsets[0] = freq[:]
    
    for l in range(2, MODULOS + 1): # caculate for subsets with size l
        for s in range(1, (l + 1) // 2):
            for i in range(MODULOS):
                for j in range(MODULOS):
                    subsets[l - 1][(i + j) % MODULOS] += subsets[s - 1][i] * subsets[l - s - 1][j]

        if (l % 2 == 0):
            for i in range(MODULOS):
                for j in range(i, MODULOS):
                    subsets[l - 1][(i + j) % MODULOS] += subsets[l // 2 - 1][i] * subsets[l // 2 - 1][j]
        
    #return subsets"""
    for i in range(MODULOS):
        print (i + 1, freq[i])
    return freq

if __name__ == "__main__":
    startTime = time.clock()
    print (eu250())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
