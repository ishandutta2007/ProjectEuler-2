# ------------------------------------------------------------- Prime connection -------------------------------------------------------------- #
#                                                                                                                                               #
#       Two positive numbers A and B are said to be connected (denoted by "A ↔ B") if one of these conditions holds:                            #
#       (1) A and B have the same length and differ in exactly one digit; for example, 123 ↔ 173.                                               #
#       (2) Adding one digit to the left of A (or B) makes B (or A); for example, 23 ↔ 223 and 123 ↔ 23.                                        #
#                                                                                                                                               #
#       We call a prime P a 2's relative if there exists a chain of connected primes between 2 and P and no prime in the chain exceeds P.       #
#                                                                                                                                               #
#       For example, 127 is a 2's relative. One of the possible chains is shown below:                                                          #
#       2 ↔ 3 ↔ 13 ↔ 113 ↔ 103 ↔ 107 ↔ 127                                                                                                      #
#       However, 11 and 103 are not 2's relatives.                                                                                              #
#                                                                                                                                               #
#       Let F(N) be the sum of the primes ≤ N which are not 2's relatives.                                                                      #
#       We can verify that F(10^3) = 431 and F(10^4) = 78728.                                                                                   #
#                                                                                                                                               #
#       Find F(10^7).                                                                                                                           #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import math

from euler.primes import prime_sieve

def is_conntcted_type_a(a, b):
    if a <= b:
        return False

    diff = a - b

    while diff and diff % 10 == 0:
        diff //= 10

    return diff < 10

def is_conntcted_type_b():
    pass

def eu425():
    TOP = 10 ** 3

    primes = prime_sieve(TOP)
    primes_l = []
    for l in range(round(math.log(TOP, 10))):
        primes_l.append([p for p in primes if len(str(p)) == (l + 1)])

    
    #print (primes_l)
    prime_relative = [[2, 3, 5, 7]]
    for l in range(1, round(math.log(TOP, 10))):
        prime_relative.append([p for p in primes_l[l] if (p % (10 ** l)) in prime_relative[l - 1]])
        #print ("type 2", l, prime_relative[l])

        for pr in set(prime_relative[l]):
            prime_relative[l].extend([p for p in primes_l[l] if is_conntcted_type_a(p, pr) == True])
        prime_relative[l] = list(set(prime_relative[l]))
        #print ("type 1", l, prime_relative[l])

    print (primes_l[1])
    print (prime_relative[1])
    s = 0
    for l in range(round(math.log(TOP, 10))):
        s += sum([p for p in primes_l[l] if p not in prime_relative[l]])
        
    return s
    

if __name__ == "__main__":
    startTime = time.clock()
    print (eu425())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")


