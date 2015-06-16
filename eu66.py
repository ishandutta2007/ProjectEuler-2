# ----------------------------------------------------------- Diophantine equation ------------------------------------------------------------ #
#                                                                                                                                               #
#       Consider quadratic Diophantine equations of the form:                                                                                   #
#                                                                                                                                               #
#                       x2 – Dy2 = 1                                                                                                            #
#                                                                                                                                               #
#       For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.                                                                #
#                                                                                                                                               #
#       It can be assumed that there are no solutions in positive integers when D is square.                                                    #
#                                                                                                                                               #
#       By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:                                                     #
#                                                                                                                                               #
#                       3^2 – 2×2^2 = 1                                                                                                         #
#                       2^2 – 3×1^2 = 1                                                                                                         #
#                       9^2 – 5×4^2 = 1                                                                                                         #
#                       5^2 – 6×2^2 = 1                                                                                                         #
#                       8^2 – 7×3^2 = 1                                                                                                         #
#                                                                                                                                               #
#       Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.                                             #
#                                                                                                                                               #
#       Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.                                      #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from euler.number_theory.pell import solve_pell_equation

def eu66():
    TOP = 1000

    squares = [i ** 2 for i in range(int(TOP ** 0.5) + 1)]
    t = [i for i in range(TOP + 1) if i not in squares]
    
    largest_x = 2
    d = 0

    for N in t:
        p = solve_pell_equation(N, 1)
        s = next(p)
        s = next(p) # Skip trivial solution
        
        if (s[0] > largest_x):
            largest_x = s[0]
            d = N

    return d

if __name__ == "__main__":
    startTime = time.clock()
    print (eu66())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
