# ------------------------------------------------------------- Binary Circles ---------------------------------------------------------------- #
#                                                                                                                                               #
#       2^N binary digits can be placed in a circle so that all the N-digit clockwise subsequences are distinct.                                #
#                                                                                                                                               #
#       For N=3, two such circular arrangements are possible, ignoring rotations:                                                               #
#                                                                                                                                               #
#                                           0                           0                                                                       #
#                                       1       0                   1       0                                                                   #
#                                   1               0           0               0                                                               #
#                                       1       1                   1       1                                                                   #
#                                           0                           1                                                                       #
#                                                                                                                                               #
#       For the first arrangement, the 3-digit subsequences, in clockwise order, are:                                                           #
#       000, 001, 010, 101, 011, 111, 110 and 100.                                                                                              #
#                                                                                                                                               #
#       Each circular arrangement can be encoded as a number by concatenating the binary digits starting with the subsequence of all zeros      #
#       as the most significant bits and proceeding clockwise. The two arrangements for N=3 are thus represented as 23 and 29:                  #
#                                                                                                                                               #
#                                                               00010111 base2 = 23                                                             #
#                                                               00011101 base2 = 29                                                             #
#                                                                                                                                               #
#       Calling S(N) the sum of the unique numeric representations, we can see that S(3) = 23 + 29 = 52.                                        #
#                                                                                                                                               #
#       Find S(5).                                                                                                                              #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from itertools import product

def sum_binary_circles(c, l, last, N):
    if l == set():
        return int(c[:-N + 1], 2)

    candidates = [n for n in l if n[:-1] == last[1:]]

    if len(candidates) == 0:
        return 0

    s = 0
    for candidate in candidates:
        new_l = l.copy()
        new_l.remove(candidate)
        s += sum_binary_circles(c + candidate[-1], new_l, candidate, N)
    
    return s

def eu265():
    N = 5
    
    l = ["".join(p) for p in product(['0','1'], repeat=N)]

    s = sum_binary_circles(l[0], set(l[1:]), l[0], N)

    return s

if __name__ == '__main__':
    startTime = time.clock()
    print (eu265())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
