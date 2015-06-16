# ---------------------------------------------------------- Singleton difference ------------------------------------------------------------- #
#                                                                                                                                               #
#       The positive integers, x, y, and z, are consecutive terms of an arithmetic progression. Given that n is a positive integer,             #
#       the equation, x^2 − y^2 − z^2 = n, has exactly one solution when n = 20:                                                                #
#                                                                                                                                               #
#                                                       13^2 − 10^2 − 7^2 = 20                                                                  #
#                                                                                                                                               #
#       In fact there are twenty-five values of n below one hundred for which the equation has a unique solution.                               #
#                                                                                                                                               #
#       How many values of n less than fifty million have exactly one solution?                                                                 #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
    
def eu136():
    TOP = 50 * 10 ** 6
    TARGET = 1

    # (z + 2d)^2 - (z + d)^2 - z^2 = n
    # -z^2 + 2zd + 3d^2 = n
    # -z^2 - zd + 3zd + 3d^2 = n
    # -z(z + d) + 3d(z + d) = n
    # (3d - z)(d + z) = n  --> u = 3d - z, v = d + z  --> uv = n
    # d = (u + v) / 4
    # z = (3v - u) / 4
    
    solutions = [0 for i in range(TOP + 1)]

    for u in range(1, TOP):
        for v in range(u // 3 + 1, TOP // u + 1):
            if (u + v) % 4 == 0 and \
               (3*v - u) % 4 == 0:
                solutions[u * v] += 1
            
    s = sum([1 for i in range(TOP) if solutions[i] == TARGET])

    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu136())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
