# ----------------------------------------- Red, green, and blue tiles ---------------------------------------- #
#                                                                                                               #
#       Using a combination of black square tiles and oblong tiles chosen from: red tiles measuring two units,  #
#       green tiles measuring three units, and blue tiles measuring four units, it is possible to tile a row    #
#       measuring five units in length in exactly fifteen different ways.                                       #
#                                                                                                               #
#       How many ways can a row measuring fifty units in length be tiled?                                       #
#                                                                                                               #
#       NOTE: This is related to problem 116.                                                                   #
# ------------------------------------------------------------------------------------------------------------- #
import time

def F(mb, mt, n):
    if n in F.MEMORY:
        return F.MEMORY[n]

    ret = 1

    if (n < mb):
        return ret

    for size in range(mb, mt + 1):
        for start in range(n - size + 1):
            ret += F(mb, mt, n - size - start)

    F.MEMORY[n] = ret
    
    return ret
F.MEMORY = { }

def eu117():
    LEN = 50
    
    return F(2, 4, LEN)

if __name__ == "__main__":
    startTime = time.clock()
    print (eu117())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
