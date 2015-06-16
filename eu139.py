# -------------------------------------------- Pythagorean tiles ---------------------------------------------- #
#                                                                                                               #
#   Let (a, b, c) represent the three sides of a right angle triangle with integral length sides.               #
#   It is possible to place four such triangles together to form a square with length c.                        #
#                                                                                                               #
#   For example, (3, 4, 5) triangles can be placed together to form a 5 by 5 square with a 1 by 1 hole in       #
#   the middle and it can be seen that the 5 by 5 square can be tiled with twenty-five 1 by 1 squares.          #
#                                                                                                               #
#   However, if (5, 12, 13) triangles were used then the hole would measure 7 by 7 and these could not          #
#   be used to tile the 13 by 13 square.                                                                        #
#                                                                                                               #
#   Given that the perimeter of the right triangle is less than one-hundred million, how many Pythagorean       #
#   triangles would allow such a tiling to take place?                                                          #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

def gcd(a, b):
    """ returns the greatest common divisor of {a, b} """
    # a = m^2 - n^2, b = 2mn, c = m^2 + n^2
    # a + b + c = 2m(m + n) 
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)    
    
def genPythagorianTriplesToPerimeter(p):
    """ returns all pythagorian triples up to perimeter (a + b + c) p """
    for m in range(1, int(math.sqrt((p // 2 + 1))) + 1):
        for n in range(1, min(int(p // (2 * m)) + 1 - m, m)):
            if ((m - n) % 2 == 1):
                if (gcd(m, n) == 1):
                    a , b = min(m * m - n * n, 2 * m * n) , max(m * m - n * n, 2 * m * n)
                    c = m * m + n * n

                    k = 1
                    s = a + b + c
                    if (s <= p):
                        yield (a, b, c)

def eu139():
    TOP_P = 10 ** 8

    g = genPythagorianTriplesToPerimeter(TOP_P + 1)

    s = 0
    try:
        while True:
            t = next(g)
            if t[2] % (t[1] - t[0]) == 0:
                s += TOP_P // sum(t)
    except StopIteration:
        pass

    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu139())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
