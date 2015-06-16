# ---------------------------------------------------------------- Crazy Function ------------------------------------------------------------- #
#                                                                                                                                               #
#       For fixed integers a, b, c, define the crazy function F(n) as follows:                                                                  #
#       F(n) = n - c for all n > b                                                                                                              #
#       F(n) = F(a + F(a + F(a + F(a + n)))) for all n ≤ b.                                                                                     #
#                                                                                                                                               #
#       Also, define S(a, b, c) = Sigma{n = 0..b, F(n)}.                                                                                        #
#                                                                                                                                               #
#       For example, if a = 50, b = 2000 and c = 40, then F(0) = 3240 and F(2000) = 2040.                                                       #
#       Also, S(50, 2000, 40) = 5204240.                                                                                                        #
#                                                                                                                                               #
#       Find the last 9 digits of S(217, 721, 127).                                                                                             #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def S(a, b, c):
    def F(n):
        if n > b:
            return n - c
        else:
            return F(a + F(a + F(a + F(a + n))))

    r = 0
    for n in range(b + 1):
        c += F(n)

    return c

def eu340():
    pass
        
if __name__ == "__main__":
    startTime = time.clock()
    print (eu340())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
