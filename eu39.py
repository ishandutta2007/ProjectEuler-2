# ----------------------------------------- Integer right triangles ------------------------------------------- #
#                                                                                                               #
#       If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},                    #
#       there are exactly three solutions for p = 120.                                                          #
#                                                                                                               #
#                       {20,48,52}, {24,45,51}, {30,40,50}                                                      #
#                                                                                                               #
#       For which value of p ≤ 1000, is the number of solutions maximised?                                      #
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
                    while (k * s <= p):
                        #print (a * k, b * k, c * k, "p =", s * k)
                        genPythagorianTriplesToPerimeter.WAYS[s * k] += 1
                        k += 1
genPythagorianTriplesToPerimeter.WAYS = [0] * (1000 + 1)

def eu39():
    TOP_P = 1000

    genPythagorianTriplesToPerimeter(TOP_P + 1)
    
    return genPythagorianTriplesToPerimeter.WAYS.index(max(genPythagorianTriplesToPerimeter.WAYS))

if __name__ == "__main__":
    startTime = time.clock()
    print (eu39())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
