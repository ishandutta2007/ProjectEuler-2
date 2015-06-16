# --------------------------------------------- Pandigital prime ---------------------------------------------- #
#                                                                                                               #
#       We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.#
#       For example, 2143 is a 4-digit pandigital and is also prime.                                            #
#                                                                                                               #
#       What is the largest n-digit pandigital prime that exists?                                               #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math
import functools
import itertools

def isPrime(n):
    """ Checks if n is prime """
    if n < 0:
        return False
    
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    r = int(math.sqrt(n))
    c = 5

    while c <= r:
        if n % c == 0:
            return False
        if n % (c + 2) == 0:
            return False
        c += 6

    return True
    
def eu41():
    for i in range (9, 1, -1):
        digits = "".join([str(d) for d in range(i, 0, -1)])
        p = ["".join(p) for p in itertools.permutations(digits)]
        s = 0

        for n in p:
            if (isPrime(int(n))):
                return n

if __name__ == "__main__":
    startTime = time.clock()
    print (eu41())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
