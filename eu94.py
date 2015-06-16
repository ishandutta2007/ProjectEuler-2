# -------------------------------------- Almost equilateral triangles ----------------------------------------- #
#                                                                                                               #
#       It is easily proved that no equilateral triangle exists with integral length sides and integral area.   #
#       However, the almost equilateral triangle 5-5-6 has an area of 12 square units.                          #
#                                                                                                               #
#       We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the   #
#       third differs by no more than one unit.                                                                 #
#                                                                                                               #
#       Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area  #
#       and whose perimeters do not exceed one billion (1,000,000,000).                                         #
# ------------------------------------------------------------------------------------------------------------- #
import time
from math import sqrt

def eu94():
    TOP_PERIMETER = 10 ** 9
    
    per_sum = 0

    # Find (x, x, x + 1) triangles
    # A = sqrt([(3x + 1) / 2] * [(x + 1) / 2]^2 * [(x - 1) / 2])
    #   = [(x + 1) / 4] * sqrt(3x^2 - 2x - 1) -> x must be odd
    # B = sqrt([(3x + 1) / 2] * [(x - 1) / 2]^2 * [(x + 1) / 2])
    #   = [(x - 1) / 4] * sqrt(3x^2 + 2x - 1) -> x must be odd
    a = 3
    b = -2
    c = -1
    countA = 0
    sumA = 0
    countB = 0
    sumB = 0
    
    for i in range(3, TOP_PERIMETER // 3, 2):
        a += 12 * i - 12 # = 3 * (4 * (i - 2) + 4)
        b -= 4
        deltaA = a + b + c
        deltaB = a - b + c
        if (int(sqrt(deltaA)) ** 2 == deltaA):
            #print(i, deltaA)
            sumA += i
            countA += 1
            
        if (int(sqrt(deltaB)) ** 2 == deltaB):
            #print(i, deltaB)
            sumB += i
            countB += 1
            
    per_sum += sumA * 3 + countA
    per_sum += sumB * 3 - countB
    
    return per_sum

if __name__ == "__main__":
    startTime = time.clock()
    print (eu94())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
