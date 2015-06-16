# ---------------------------------------------------------- Prime digit replacements ------------------------------------------------------------ -#
#                                                                                                                                                   #
#       By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83,         #
#       are all prime.                                                                                                                              #
#                                                                                                                                                   #
#       By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes              #
#       among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003,              #
#       being the first member of this family, is the smallest prime with this property.                                                            #
#                                                                                                                                                   #
#       Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,                       #
#       is part of an eight prime value family.                                                                                                     #
# ------------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import math
import itertools
from euler.primes import is_prime

def check_family_size_8(p, places):
    places = list(reversed(places))

    n = 0
    d = 0
    for i in range(len(places) + len(str(p))):
        n *= 10
        d *= 10
        if i not in places:
            n += p % 10
            p //= 10
        else:
            d += 1

    org = n
    c = 0

    if 0 in places:
        n += d
        for a in range(9):
            if not is_prime(n):
                c += 1

            n += d

            if c > 1:
                return False
    else:
        for a in range(10):
            if not is_prime(n):
                c += 1

            n += d

            if c > 2:
                return False

    return org + d   

def eu51():
    # Check for 5-digits number
    for n in range(11, 99 + 1):
        for p in itertools.combinations([0, 1, 2, 3], 3):
            if check_family_size_8(n, p) == True:
                return check_family_size_8(n, p)

    # Check for 6-digits number
    for n in range(111, 999 + 1):
        for p in itertools.combinations([0, 1, 2, 3, 4], 3):
            if check_family_size_8(n, p):
                return check_family_size_8(n, p)
            
                                
if __name__ == "__main__":
    startTime = time.clock()
    print (eu51())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
