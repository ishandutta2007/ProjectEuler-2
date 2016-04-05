# ------------------------- Find the 200th prime-proof sqube containing the contiguous sub-string "200" --------------------------------------- #
#                                                                                                                                               #
#       We shall define a sqube to be a number of the form, p^2*q^3, where p and q are distinct primes.                                         #
#       For example, 200 = 5^2*2^3 or 120072949 = 23^2*61^3.                                                                                    #      
#                                                                                                                                               #
#       The first five squbes are 72, 108, 200, 392, and 500.                                                                                   #
#                                                                                                                                               #
#       Interestingly, 200 is also the first number for which you cannot change any single digit to make a prime; we shall call such numbers,   #
#       prime-proof. The next prime-proof sqube which contains the contiguous sub-string "200" is 1992008.                                      #
#                                                                                                                                               #
#       Find the 200th prime-proof sqube containing the contiguous sub-string "200".                                                            #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.primes import prime_sieve, is_probable_prime

def check200(n):
    while n > 100:
        if n % 1000 == 200:
            return True

        n //= 10

    return False

def check_prime_proof(n):
    l = len(str(n))

    a = n // 10
    b = n % 10

    for d in range(10):
        if d == b:
            continue

        t = 10 * a
        t += d

        if is_probable_prime(t):
            return False

    if n % 10 in [0, 2, 4, 6, 8, 5]:
        return True
    
    e = 10
    for i in range(1, l - 1):
        a = n // (e * 10)
        b = (n // e) % 10
        c = n % e
        
        for d in range(10):
            if d == b:
                continue

            t = 10 * a
            t += d
            t *= e
            t += c

            if is_probable_prime(t):
                return False

        e *= 10

    e = 10 ** (l - 1)
    b = (n // e) % 10
    c = n % e

    for d in range(1, 10):
        if d == b:
            continue

        t = d
        t *= e
        t += c

        if is_probable_prime(t):
            return False
            
    return True

def eu200():
    TOP = 5000000
    MAX_SIZE = 10 ** 12

    primes = prime_sieve(TOP)

    p = []
    for i in range(len(primes)):
        t1 = primes[i] ** 2

        if t1 > MAX_SIZE:
            break
        
        for j in range(i + 1, len(primes)):
            t2 = t1 * primes[j] ** 3
            p.append(t2)
            if t2 > MAX_SIZE:
                break

    for i in range(len(primes)):
        t1 = primes[i] ** 3

        if t1 > MAX_SIZE:
            break
        
        for j in range(i + 1, len(primes)):
            t2 = t1 * primes[j] ** 2
            p.append(t2)
            if t2 > MAX_SIZE:
                break

    p = list(sorted(p))

    c = 0
    for n in p:
        if check200(n) == True and check_prime_proof(n) == True:
            c += 1
            if c == 200:
                return n        
            
if __name__ == '__main__':
    startTime = time.clock()
    print (eu200())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
