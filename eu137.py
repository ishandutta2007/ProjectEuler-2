# ---------------------------------------------- Fibonacci golden nuggets --------------------------------------------- #
#                                                                                                                       #
#   Consider the infinite polynomial series AF(x) = xF1 + x^2F2 + x^3F3 + ..., where Fk is the kth term in              #
#   the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ; that is, Fk = Fk−1 + Fk−2, F1 = 1 and F2 = 1.                       #
#                                                                                                                       #
#   For this problem we shall be interested in values of x for which AF(x) is a positive integer.                       #
#                                                                                                                       #
#   Surprisingly AF(1/2)	= 	(1/2).1 + (1/2)^2.1 + (1/2)^3.2 + (1/2)^4.3 + (1/2)^5.5 + ...                   #
#        	                = 	1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...                                             #
#        	                = 	2                                                                               #
#                                                                                                                       #
#   The corresponding values of x for the first five natural numbers are shown below.                                   #
#                                                                                                                       #
#                                       x	    AF(x)                                                               #
#                                       √2−1	    1                                                                   #
#                                       1/2	    2                                                                   #
#                                       (√13−2)/3   3                                                                   #
#                                       (√89−5)/8   4                                                                   #
#                                       (√34−3)/5   5                                                                   #
#                                                                                                                       #
#   We shall call AF(x) a golden nugget if x is rational, because they become increasingly rarer; for example,          #
#   the 10th golden nugget is 74049690.                                                                                 #
#                                                                                                                       #
#   Find the 15th golden nugget.                                                                                        #
# --------------------------------------------------------------------------------------------------------------------- #
import time
from euler.number_theory.pell import solve_pell_equation

def genFibGoldenNuggets():
    # Fibonacci generating function is: x / (1 - x - x^2)
    # x = n - nx - nx^2 -> nx^2 + (n + 1)x - n = 0
    # det = (n + 1)^2 + 4n^2 = 5n^2 + 2n + 1 (naural square)
    # 5n^2 + 2n + 1 = b^2 -> 25n^2 + 10n + 1 + 4 - 5b^2 = 0 -> (5n + 1)^2 - 5b^2 = -4, a = 5n + 1
    # a^2 - 5b^2 = -4 -> Pell's equation

    # n + 1, 2n are the legs of pythagorian triplet

    p = solve_pell_equation(5, -4)
    n = next(p)
    n = next(p) # Skip the n=0 solution
        
    while True:
        if n[0] % 5 == 1:
            yield (n[0] - 1) // 5
        n = next(p)

def eu137():
    N = 15
    
    g = genFibGoldenNuggets()
    for i in range(N):
        t = next(g)

    return t

if __name__ == "__main__":
    startTime = time.clock()
    print (eu137())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
