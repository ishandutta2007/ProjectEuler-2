# ---------------------------------------- Tribonacci non-divisors -------------------------------------------- #
#                                                                                                               #
#       The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201 ...                                 #
#       is defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.                                             #
#                                                                                                               #
#       It can be shown that 27 does not divide any terms of this sequence.                                     #
#       In fact, 27 is the first odd number with this property.                                                 #
#                                                                                                               #
#       Find the 124th odd number that does not divide any terms of the above sequence.                         #
# ------------------------------------------------------------------------------------------------------------- #
import time

def gen_tribonacci_sequence_mod_m(m):
    t1 = 1
    t2 = 1
    t3 = 1

    yield t1
    yield t2
    yield t3

    while True:
        t1, t2, t3 = t2, t3, (t1 + t2 + t3) % m

        yield t3

def gen_next_tribonacci_odd_non_divisor():
    d = 3

    while True:
        g = gen_tribonacci_sequence_mod_m(d)

        t1 = next(g)
        t2 = next(g)
        t3 = next(g)
    
        while True:
            t1, t2, t3 = t2, t3, next(g)
    
            if t3 == 0:
                break
            elif t1 * t2 * t3 == 1:
                yield d
                break
            
        d += 2

def eu225():
    TARGET = 124

    g = gen_next_tribonacci_odd_non_divisor()
    
    for i in range(TARGET):
        d = next(g)
    
    return d

if __name__ == "__main__":
    startTime = time.clock()
    print (eu225())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
