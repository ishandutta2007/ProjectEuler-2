# ------------------------------------------ Modified Fibonacci golden nuggets ---------------------------------------- #
#                                                                                                                       #
#   Consider the infinite polynomial series AG(x) = xG1 + x^2G2 + x^3G3 + ..., where Gk is the kth term of the          #
#   second order recurrence relation Gk = Gk−1 + Gk−2, G1 = 1 and G2 = 4; that is, 1, 4, 5, 9, 14, 23, ... .            #
#                                                                                                                       #
#   For this problem we shall be concerned with values of x for which AG(x) is a positive integer.                      #
#                                                                                                                       #
#   The corresponding values of x for the first five natural numbers are shown below.                                   #
#                                                                                                                       #
#                                       x	    AG(x)                                                               #
#                                       (√5−1)/4    1                                                                   #
#                                       2/5	    2                                                                   #
#                                       (√22−2)/6   3                                                                   #
#                                       (√137−5)/14 4                                                                   #
#                                       1/2	    5                                                                   #
#                                                                                                                       #
#   We shall call AG(x) a golden nugget if x is rational, because they become increasingly rarer;                       #
#   for example, the 20th golden nugget is 211345365.                                                                   #
#                                                                                                                       #
#   Find the sum of the first thirty golden nuggets.                                                                    #
# --------------------------------------------------------------------------------------------------------------------- #
import time
from euler.number_theory.pell import solve_pell_equation

def genModifiedFibGoldenNuggets():
    # Fibonacci generating function is: (x + 3x^2) / (1 - x - x^2)
    # x + 3x^2 = n - nx - nx^2 -> (n + 3)x^2 + (n + 1)x - n = 0
    # det = (n + 1)^2 + 4n(n+3) = 5n^2 + 14n + 1 (naural square)
    # 5n^2 + 14n + 1 = b^2 -> 25n^2 + 70n + 5 = 5b^2 -> (5n + 7)^2 - 5b^2 = 44, a = (5n + 7)
    # a^2 - 5b^2 = 44  Pell's equation

    p = solve_pell_equation(5, 44)
    n = next(p)
    n = next(p) # Skip the n=0 solution
        
    while True:
        if (n[0] - 7) % 5 == 0:
            yield (n[0] - 7) // 5
        n = next(p)

def eu140():
    N = 30

    s = 0
    
    g = genModifiedFibGoldenNuggets()
    for i in range(N):
        s += next(g)

    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu140())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
