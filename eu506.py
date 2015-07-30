# --------------------------------------------------------- Clock sequence -------------------------------------------------------------------- #
#                                                                                                                                               #
#       Consider the infinite repeating sequence of digits:                                                                                     #
#       1234321234321234321...                                                                                                                  #
#                                                                                                                                               #
#       Amazingly, you can break this sequence of digits into a sequence of integers such that the sum of the digits in the n'th value is n.    #
#                                                                                                                                               #
#       The sequence goes as follows:                                                                                                           #
#       1, 2, 3, 4, 32, 123, 43, 2123, 432, 1234, 32123, ...                                                                                    #
#                                                                                                                                               #
#       Let vn be the n'th value in this sequence. For example, v_2 = 2, v_5 = 32 and v_11 = 32123.                                             #
#                                                                                                                                               #
#       Let S(n) be v_1 + v_2 + ... + v_n. For example, S(11) = 36120, and S(1000) mod 123454321 = 18232686.                                    #
#                                                                                                                                               #
#       Find S(10^14) mod 123454321.                                                                                                            #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.number_theory.basics import modular_multiplicative_inverse

def gen_clock_sequence():
    seq = [1, 2, 3, 4, 3, 2]

    n = 1
    i = 0

    while True:
        s = 0
        r = 0
        while s < n:
            s += seq[i]
            r = r * 10 + seq[i]
            i = (i + 1) % len(seq)

        yield r

        n += 1
        
def eu506():
    N = 10 ** 14
    MODULO = 123454321
    
    g = gen_clock_sequence()

    q, r = divmod(N, 15)

    base = [next(g) for _ in range(15)]
    inc = [(next(g) % (10 ** 6)) for _ in range(15)]

    inv = modular_multiplicative_inverse(10 ** 6 - 1, MODULO)

    b = (pow(10 ** 6, q, MODULO) - 1) * inv * sum(base)
    i = (((pow(10 ** 6, q, MODULO) - 1) * inv) - q) * inv * sum(inc)

    b_r = pow(10 ** 6, q, MODULO) * sum(base[:r])
    i_r = (pow(10 ** 6, q, MODULO) - 1) * inv * sum(inc[:r])
    
    return (b + i + b_r + i_r) % MODULO    

if __name__ == '__main__':
    startTime = time.clock()
    print (eu506())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
