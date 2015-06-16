# ---------------------------------------------- Singular integer right triangles ------------------------------------------------- #
#                                                                                                                                   #
#       It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle       #
#       in exactly one way, but there are many more examples.                                                                       #
#                                                                                                                                   #
#                           12 cm: (3,4,5)                                                                                          #
#                           24 cm: (6,8,10)                                                                                         #
#                           30 cm: (5,12,13)                                                                                        #
#                           36 cm: (9,12,15)                                                                                        #
#                           40 cm: (8,15,17)                                                                                        #
#                           48 cm: (12,16,20)                                                                                       #
#                                                                                                                                   #
#       In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle,                #
#       and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly        #
#       three different integer sided right angle triangles.                                                                        #
#                                                                                                                                   #
#                           120 cm: (30,40,50), (20,48,52), (24,45,51)                                                              #
#                                                                                                                                   #
#       Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided                  #
#       right angle triangle be formed?                                                                                             #
# --------------------------------------------------------------------------------------------------------------------------------- #
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

def genPrimitivePythagorianTriplesWithPerimeter(p):
    """ returns all primitive pythagorian triples up to perimeter (a + b + c) p """
    ret = []
    
    for m in range(1, int(math.sqrt((p // 2 + 1))) + 1):
        for n in range(1, min(int(p // (2 * m)) + 1 - m, m)):
            if ((m - n) % 2 == 1):
                if (gcd(m, n) == 1):
                    a , b = min(m * m - n * n, 2 * m * n) , max(m * m - n * n, 2 * m * n)
                    c = m * m + n * n

                    if ((a + b + c) <= p):
                        ret += [(a, b, c)]
    return ret

def eu75():
    TOP = 1500000

    primitives      = genPrimitivePythagorianTriplesWithPerimeter(TOP + 1)
    primitivesSums  = [sum(p) for p in primitives]
    
    L = [0 for i in range(TOP + 1)]

    for p in primitivesSums:
        for i in range(p, TOP + 1, p):
            L[i] += 1
    
    s = 0
    for p in L:
        if (p == 1):
            s += 1

    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu75())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
