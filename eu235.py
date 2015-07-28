# ---------------------------------------------------- An Arithmetic Geometric sequence ------------------------------------------------------- #
#                                                                                                                                               #
#       Given is the arithmetic-geometric sequence u(k) = (900-3k)r^(k-1).                                                                      #
#       Let s(n) = Σk=1...n[u(k)].                                                                                                              #
#                                                                                                                                               #
#       Find the value of r for which s(5000) = -600,000,000,000.                                                                               #
#                                                                                                                                               #
#       Give your answer rounded to 12 places behind the decimal point.                                                                         #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time      

from euler.calculus import Newton_Raphson

def eu235():
    f = lambda x: (-14100 * (x ** 5001) + 14103 * (x ** 5000) + (6 * 10 ** 11) * (x ** 2) - (12 * 10 ** 11 + 900) * x + (6 * 10 ** 11 + 897))

    return round(Newton_Raphson(f, 1.1, 1e-13), 12)
    
if __name__ == '__main__':
    startTime = time.clock()
    print (eu235())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
