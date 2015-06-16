# --------------------------------------------------------- Problem 500!!! -------------------------------------------------------------------- #
#                                                                                                                                               #
#       The number of divisors of 120 is 16.                                                                                                    #
#       In fact 120 is the smallest number having 16 divisors.                                                                                  #
#                                                                                                                                               #
#       Find the smallest number with 2^500500 divisors.                                                                                        #
#       Give your answer modulo 500500507.                                                                                                      #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def genN():
    while True:
        yield 1
        yield 2
        yield 3
        yield 4
        yield 3
        yield 2
        
def eu506():
    g = genN()

    n = 1
    c = 0

    while n < 100:
        c = 0
        s = 0
        while c != n:
            t = next(g)
            c += t
            s = 10*s + t            

        print (c, s, s % 123454321)
        n += 1

if __name__ == '__main__':
    startTime = time.clock()
    print (eu506())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
