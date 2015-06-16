# ----------------------------------------------------------- Modular Cubes, part 1 ----------------------------------------------------------- #
#                                                                                                                                               #
#       For a positive number n, define S(n) as the sum of the integers x, for which 1 < x < n and x^3 ≡ 1 mod n.                               #
#                                                                                                                                               #
#       When n=91, there are 8 possible values for x, namely : 9, 16, 22, 29, 53, 74, 79, 81.                                                   #
#       Thus, S(91)=9+16+22+29+53+74+79+81=363.                                                                                                 #
#                                                                                                                                               #
#       Find S(13082761331670030).                                                                                                              #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from itertools import product

from euler.numbers import get_distinct_factors
from euler.number_theory.congruence import crt

def getUnitRootsModN(f, k):
    ret = [i for i in range(1, f) if (i ** k % f == 1)]

    return ret

def eu271():
    N = 13082761331670030

    s = 0
    third_unit_root_mod_n = { }
    
    factors = sorted(list(get_distinct_factors(N)))
    third_unit_root_mod_n = [0 for i in range(len(factors))]
    
    for i, f in enumerate(factors):
        third_unit_root_mod_n[i] = getUnitRootsModN(f, 3)

    for r in product(*third_unit_root_mod_n):
        s += crt(list(r), factors)
        
    return s - 1

if __name__ == "__main__":
    startTime = time.clock()
    print (eu271())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
