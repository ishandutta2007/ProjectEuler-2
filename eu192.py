# ------------------------------------------------------------ Best Approximations ------------------------------------------------------------ #
#                                                                                                                                               #
#       Let x be a real number.                                                                                                                 #
#       A best approximation to x for the denominator bound d is a rational number r/s in reduced form, with s ≤ d, such that any rational      #
#       number which is closer to x than r/s has a denominator larger than d:                                                                   #
#                                                                                                                                               #
#                                                           |p/q-x| < |r/s-x| -> q > d                                                          #
#       For example, the best approximation to √13 for the denominator bound 20 is 18/5 and the best approximation to √13 for the               #
#       denominator bound 30 is 101/28.                                                                                                         #
#                                                                                                                                               #
#       Find the sum of all denominators of the best approximations to √n for the denominator bound 10^12,                                      #
#       where n is not a perfect square and 1 < n ≤ 100000.                                                                                     #  
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from euler.number_theory.convergents import gen_sqrt_best_approximations

def eu192():
    TOP = 100000
    BOUND = 10 ** 12

    squares = [i ** 2 for i in range(int(TOP ** 0.5) + 1)]
    t = [i for i in range(TOP + 1) if i not in squares]
    s = 0

    for n in t:
        g = gen_sqrt_best_approximations(n)

        best_approx_d = 1
        approx = next(g)

        while (approx[1] < BOUND):
            best_approx_d = approx[1]
            approx = next(g)

        s += best_approx_d
            
    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu192())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
