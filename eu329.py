# --------------------------------------------------------------- Prime Frog ------------------------------------------------------------------ #
#                                                                                                                                               #
#       Susan has a prime frog.
#       Her frog is jumping around over 500 squares numbered 1 to 500. He can only jump one square to the left or to the right,                 #
#       with equal probability, and he cannot jump outside the range [1;500].                                                                   #
#       (if it lands at either end, it automatically jumps to the only available square on the next move.)                                      #
#                                                                                                                                               #
#       When he is on a square with a prime number on it, he croaks 'P' (PRIME) with probability 2/3 or 'N' (NOT PRIME)                         #
#       with probability 1/3 just before jumping to the next square.                                                                            #
#       When he is on a square with a number on it that is not a prime he croaks 'P' with probability 1/3 or 'N'                                #
#       with probability 2/3 just before jumping to the next square.                                                                            #
#                                                                                                                                               #
#       Given that the frog's starting position is random with the same probability for every square,                                           #
#       and given that she listens to his first 15 croaks, what is the probability that she hears the sequence PPPPNNPPPNPPNPN?                 #
#                                                                                                                                               #
#       Give your answer as a fraction p/q in reduced form.                                                                                     #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from fractions import Fraction

from euler.primes import full_prime_sieve

def eu329():
    TOP = 500
    SEQ = 'PPPPNNPPPNPPNPN'
    
    primes = full_prime_sieve(TOP)
    primes = ["P" if primes[i] == 1 else "N" for i in range(TOP + 1)]

    croaks = [[0 for j in range(TOP)] for i in range(len(SEQ))]

    k = len(SEQ) - 1
    for j in range(TOP):
        croaks[0][j] = Fraction(2 if primes[j + 1]==SEQ[k] else 1, 3)

    for i in range(1, len(SEQ)):
        k -= 1

        croaks[i][0] = Fraction(2 if primes[1]==SEQ[k] else 1, 3) * croaks[i - 1][1]
        for j in range(1, TOP - 1):
            croaks[i][j] = Fraction(2 if primes[j + 1]==SEQ[k] else 1, 3) * \
                           (croaks[i - 1][j - 1] + croaks[i - 1][j + 1]) / 2
        croaks[i][TOP - 1] = Fraction(2 if primes[TOP]==SEQ[k] else 1, 3) * croaks[i - 1][TOP - 2]

    
    return sum(croaks[len(SEQ) - 1]) / TOP

if __name__ == '__main__':
    startTime = time.clock()
    print (eu329())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
