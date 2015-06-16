# ------------------------------------------- Product-sum numbers --------------------------------------------- #
#                                                                                                               #
#       A natural number, N, that can be written as the sum and product of a given set of at least two natural  #
#       numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.#
#                                                                                                               #
#       For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.                                                                 #
#                                                                                                               #
#       For a given set of size, k, we shall call the smallest N with this property a minimal                   #
#       product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are         #
#       as follows.                                                                                             #
#                                                                                                               #
#               k=2: 4 = 2 × 2 = 2 + 2                                                                          #
#               k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3                                                                  #
#               k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4                                                          #
#               k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2                                                  #
#               k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6                                         #
#                                                                                                               #
#       Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only   #
#       counted once in the sum.                                                                                #
#                                                                                                               #
#       In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16},        #
#       the sum is 61.                                                                                          #
#                                                                                                               #
#       What is the sum of all the minimal product-sum numbers for 2≤k≤12000?                                   #
# ------------------------------------------------------------------------------------------------------------- #
import time
from math import log2, sqrt
import operator
import functools

def genNumbers(n_factors, min_factor, top):
    if (n_factors == 1):
        for i in range(min_factor, top + 1):
            yield [i]

    else:
        for h in range(min_factor, int(top ** (1.0 / n_factors)) + 1):
            g = genNumbers(n_factors - 1, h, top // h)
            for t in g:
                yield [h] + t
    
def eu88():
    TOP = 12000
    
    mps = [(2 * k) for k in range(TOP + 1)]

    top_num_of_factors = int(log2(2 * TOP))

    for n_factors in range(2, top_num_of_factors + 1):
        g = genNumbers(n_factors, 2, 2 * TOP)

        for n in g:
            ps = functools.reduce(operator.mul, [i for i in n])
            k = len(n) + ps - sum(n)

            if (k <= TOP and ps < mps[k]):
                mps[k] = ps

    mps = mps[2:]
    
    return sum(set(mps))

if __name__ == "__main__":
    startTime = time.clock()
    print (eu88())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
