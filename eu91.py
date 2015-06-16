# -------------------------------- Right triangles with integer coordinates ----------------------------------- #
#                                                                                                               #
#       The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin,  #
#       O(0,0), to form ΔOPQ.                                                                                   #
#                                                                                                               #
#       There are exactly fourteen triangles containing a right angle that can be formed when each              #
#       co-ordinate lies between 0 and 2 inclusive; that is,                                                    #
#                               0 ≤ x1, y1, x2, y2 ≤ 2.                                                         #
#                                                                                                               #
#       Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?                             #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math    
    
def eu91():
    MAX = 50

    s = 0
    
    for x1 in range(MAX + 1):
        for y1 in range(MAX + 1):
            d1 = x1 * x1 + y1 * y1
            if (d1 == 0):
                continue
            for x2 in range(x1, MAX + 1):
                for y2 in range(MAX + 1):
                    d2 = x2 * x2 + y2 * y2
                    if (d2 == 0):
                        continue
                    if (x1 == x2 and y1 >= y2):
                        continue
                    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                    a, b, c = sorted([d1, d2, d])
                    if (a + b == c):
                        s += 1
    
    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu91())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
