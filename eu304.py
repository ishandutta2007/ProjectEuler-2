# ----------------------------------------------- Primonacci -------------------------------------------------- #
#                                                                                                               #
#       For any positive integer n the function next_prime(n) returns the smallest prime p                      #
#       such that p>n.                                                                                          #
#                                                                                                               #
#       The sequence a(n) is defined by:                                                                        #
#       a(1)=next_prime(10^14) and a(n)=next_prime(a(n-1)) for n>1.                                             #
#                                                                                                               #
#       The fibonacci sequence f(n) is defined by: f(0)=0, f(1)=1 and f(n)=f(n-1)+f(n-2) for n>1.               #
#                                                                                                               #
#       The sequence b(n) is defined as f(a(n)).                                                                #
#                                                                                                               #
#       Find ∑b(n) for 1≤n≤100 000. Give your answer mod 1234567891011.                                         #
# ------------------------------------------------------------------------------------------------------------- #
import time
from euler.primes import is_probable_prime

def fib_mod_m(n, m):
    i = 3
    t = -1
    while t != 0:
        t = (fib_mod_m.MEMORY[i - 1] + fib_mod_m.MEMORY[i - 2]) % 1234567891011
        fib_mod_m.MEMORY[i] = t
        i += 1

    return i    
fib_mod_m.MEMORY = { 1: 0, 2: 1 }

def next_prime(n):
    """Return the next prime number p>n."""
    
    n += 1
    
    while not is_probable_prime(n, 8):
        n += 1

    return n

def eu304():
    START = 10**14
    MODULO = 1234567891011

    p = next_prime(START)
    return fib_mod_m(1, 1)
    """for i in range(100):
        #print(p)
        p = next_prime(p)
    
    return p"""

if __name__ == "__main__":
    startTime = time.clock()
    print (eu304())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
