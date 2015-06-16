# ------------------------------------------ Counting rectangles ---------------------------------------------- #
#                                                                                                               #
#       By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains                  #
#       eighteen rectangles:                                                                                    #
#                                                                                                               #
#       Although there exists no rectangular grid that contains exactly two million rectangles,                 #
#       find the area of the grid with the nearest solution.                                                    #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

def CountRectangles(m, n):
    s = 0
    
    #for i in range(1, m + 1):
    #    for j in range(1, n + 1):
    #        s += (m + 1 - i) * (n + 1 - j)

    #for i in range(m + 1):
    #    for j in range(n + 1):
    #        s += i * j

    s = m * (m + 1) * n * (n + 1) // 4
            
    return s
    
def eu85():
    # m * (m + 1) * n * (n + 1) ~ 4*TARGET
    # m^2 + m - (4 * TARGET / (n * (n + 1))) = 0
    # m ~ sqrt(16 * TARGET / (n * (n + 1))) / 2
    TARGET = 2000000

    diff = 1000
    best_i = 0
    best_j = 0
    
    for i in range(1, 10000):
        d = int(math.sqrt(16 * TARGET / (i * (i + 1))) // 2)
        for j in range(d - 1, d + 1):
            if (abs(CountRectangles(i, j) - TARGET) < diff):
                diff = abs(CountRectangles(i, j) - TARGET)
                best_i = i
                best_j = j

    return best_i * best_j

if __name__ == "__main__":
    startTime = time.clock()
    print (eu85())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
