# ------------------------------------------------------------ Same differences --------------------------------------------------------------- #
#                                                                                                                                               #
#       Given the positive integers, x, y, and z, are consecutive terms of an arithmetic progression, the least value of the positive integer,  #
#       n, for which the equation, x^2 − y^2 − z^2 = n, has exactly two solutions is n = 27:                                                    #
#                                                                                                                                               #
#                               34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27                                                                      #
#                                                                                                                                               #
#       It turns out that n = 1155 is the least value which has exactly ten solutions.                                                          #
#                                                                                                                                               #
#       How many values of n less than one million have exactly ten distinct solutions?                                                         #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
    
def eu135():
    TOP = 10 ** 6
    TARGET = 10

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
    print (eu135())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
