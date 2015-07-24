# --------------------------------------------------------- Square on the Inside -------------------------------------------------------------- #
#                                                                                                                                               #
#       Let ABCD be a quadrilateral whose vertices are lattice points lying on the coordinate axes as follows:                                  #
#                                                                                                                                               #
#       A(a, 0), B(0, b), C(−c, 0), D(0, −d), where 1 ≤ a, b, c, d ≤ m and a, b, c, d, m are integers.                                          #
#                                                                                                                                               #
#       It can be shown that for m = 4 there are exactly 256 valid ways to construct ABCD. Of these 256 quadrilaterals,                         #
#       42 of them strictly contain a square number of lattice points.                                                                          #
#                                                                                                                                               #
#       How many quadrilaterals ABCD strictly contain a square number of lattice points for m = 100?                                            #                                                     #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from itertools import product

from euler.number_theory.basics import gcd

def internal_lattice_points(a, b, c, d):
    # Using Pick's theorm
   
    t = internal_lattice_points.prod_minus_gcds[(a, b)]
    t += internal_lattice_points.prod_minus_gcds[(b, c)]
    t += internal_lattice_points.prod_minus_gcds[(c, d)]
    t += internal_lattice_points.prod_minus_gcds[(d, a)]
    
    return t // 2 + 1
internal_lattice_points.prod_minus_gcds = { }
    
def eu504():
    M = 100

    r = 0
    squares = set([(i ** 2) for i in range(1, (M ** 2) + 1)])
    
    for i in range(1, M + 1):
        for j in range(i, M + 1):
            internal_lattice_points.prod_minus_gcds[(i, j)] = internal_lattice_points.prod_minus_gcds[(j, i)] = (i * j) - gcd(i, j)
           
    for a, b, c, d in product([i + 1 for i in range(M)], repeat = 4):
        if internal_lattice_points(a, b, c, d) in squares:
            r += 1
            
    return r

if __name__ == '__main__':
    startTime = time.clock()
    print (eu504())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
