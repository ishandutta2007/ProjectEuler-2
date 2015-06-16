# -------------------------------------------------------------- Modular inverses ------------------------------------------------------------- #
#                                                                                                                                               #
#       Consider the number 15.                                                                                                                 #
#       There are eight positive numbers less than 15 which are coprime to 15: 1, 2, 4, 7, 8, 11, 13, 14.                                       #
#       The modular inverses of these numbers modulo 15 are: 1, 8, 4, 13, 2, 11, 7, 14                                                          #
#       because                                                                                                                                 #
#       1*1 mod 15=1                                                                                                                            #
#       2*8=16 mod 15=1                                                                                                                         #
#       4*4=16 mod 15=1                                                                                                                         #
#       7*13=91 mod 15=1                                                                                                                        #
#       11*11=121 mod 15=1                                                                                                                      #
#       14*14=196 mod 15=1                                                                                                                      #
#       Let I(n) be the largest positive number m smaller than n-1 such that the modular inverse of m modulo n equals m itself.                 #
#       So I(15)=11.                                                                                                                            #
#       Also I(100)=51 and I(7)=1.                                                                                                              #
#       Find ∑I(n) for 3≤n≤2·10^7                                                                                                               #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.number_theory.congruence import crt

def i(n):
    for t in range(n - 2, 0, -1):
        if t*t%n == 1:
            return t

def factorize_sieve(n):
    numbers = [i for i in range(n + 1)]
    factors = [[] for i in range(n + 1)]

    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i] != 1:
            factors[i] = [i]

def eu480():
    for n in range(3, 50):
        print (n, i(n))

if __name__ == "__main__":
    startTime = time.clock()
    print (eu480())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
