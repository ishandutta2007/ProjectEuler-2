# --------------------------------------- Counting block combinations I --------------------------------------- #
#                                                                                                               #
#       A row measuring seven units in length has red blocks with a minimum length of three units placed on it, #
#       such that any two red blocks (which are allowed to be different lengths) are separated by at least      #
#       one black square. There are exactly seventeen ways of doing this.                                       #
#                                                                                                               #
#       How many ways can a row measuring fifty units in length be filled?                                      #
#                                                                                                               #
#       NOTE: Although the example above does not lend itself to the possibility, in general it is permitted to #
#       mix block sizes. For example, on a row measuring eight units in length you could use                    #
#       red (3), black (1), and red (4).                                                                        #
# ------------------------------------------------------------------------------------------------------------- #
import time

def F(m, n):
    if m in F.MEMORY:
        return F.MEMORY[m]

    ret = 1

    if (n > m):
        return ret

    for s in range(m - n + 1):
        for b in range(n, m - s + 1):
            ret += F(m - s - b - 1, n)

    F.MEMORY[m] = ret
    
    return ret
F.MEMORY = { }

def eu114():
    LEN = 50
    
    return F(LEN, 3)

if __name__ == "__main__":
    startTime = time.clock()
    print (eu114())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
