# ----------------------------------------------------------- Arranged probability ------------------------------------------------------------ #
#                                                                                                                                               #
#       If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random,      #
#       it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.                                            #                                                                                      #
#                                                                                                                                               #
#       The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random,                                    #
#       is a box containing eighty-five blue discs and thirty-five red discs.                                                                   #
#                                                                                                                                               #
#       By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total,                                              #
#       determine the number of blue discs that the box would contain.                                                                          #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from euler.number_theory.pell import solve_pell_equation
    
def eu100():
    TOP = 10 ** 12
    #   b/t * (b-1)/(t-1) = 0.5
    #   2b*(b-1) = t*(t-1)
    #   2*[(b-0.5)^2 - 0.25] = (t-0.5)^2 - 0.25
    #   2*(b-0.5)^2 - 0.5 = (t-0.5)^2 - 0.25
    #   8*(b-0.5)^2 - 2 = 4*(t-0.5)^2 - 1
    #   4*(t-0.5)^2 - 8*(b-0.5)^2 = -1
    #   (2t - 1)^2 - 2*(2b - 1)^2 = -1
    #   solve pell equation X^2 - 2Y^2 = -1
    #   2t-1 = x =? t = (1+x)/2
    #   b = (1+y) / 2
    #   find solution where t > 10**12 => x > 2*10**12
    p = solve_pell_equation(2, -1)
    s = next(p)

    while (s[0] <= 2 * TOP):
        s = next(p)

    b = (1 + s[1]) // 2
    t = (1 + s[0]) // 2
    
    return b

if __name__ == "__main__":
    startTime = time.clock()
    print (eu100())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
