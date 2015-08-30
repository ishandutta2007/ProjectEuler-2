def prime_sieve(n):  
    """ Gen list of all primes <= n """
    n += 1
    size = n // 2
    sieve = [1] * size  
    limit = int(n ** 0.5)  

    for i in range(1, limit):  
        if sieve[i]:  
            val = 2 * i + 1
            tmp = ((size - 1) - i) // val   
            sieve[i + val : : val] = [0] * tmp

    return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0] 

def full_prime_sieve(n):
    """ Return vector ofiiani of ptimes <= n ** """
    sieve = [1] * (n + 1) 
    limit = int(n ** 0.5)  

    sieve[0] = sieve[1] = 0
    for i in range(2, limit + 1):  
        if sieve[i]:    
            sieve[i + i : : i] = [0] * (n // i - 1)

    return sieve
    
def is_prime(n):
    """ Checks if n is prime """
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

    r = int(n ** 0.5)
    c = 5

    while c <= r:
        if n % c == 0:
            return False
        if n % (c + 2) == 0:
            return False
        c += 6

    return True

def is_prime_with_history(n):
    if (n in is_prime_with_history.HISTORY):
        return is_prime_with_history.HISTORY[n]

    """ Checks if n is prime """
    if n < 0:
        is_prime_with_history.HISTORY[n] = False
        return False
    
    if n == 1:
        is_prime_with_history.HISTORY[n] = False
        return False
    if n < 4:
        is_prime_with_history.HISTORY[n] = True
        return True
    if n % 2 == 0:
        is_prime_with_history.HISTORY[n] = False
        return False
    if n < 9:
        is_prime_with_history.HISTORY[n] = True
        return True
    if n % 3 == 0:
        is_prime_with_history.HISTORY[n] = False
        return False

    r = int(n ** 0.5)
    c = 5

    while c <= r:
        if n % c == 0:
            is_prime_with_history.HISTORY[n] = False
            return False
        if n % (c + 2) == 0:
            is_prime_with_history.HISTORY[n] = False
            return False
        c += 6

    is_prime_with_history.HISTORY[n] = True
    return True
is_prime_with_history.HISTORY = {}

def is_probable_prime(n, _precision_for_huge_n = 8):
    """ Using Miller-Rabin algorithm """
    
    def _try_composite(a, d, n, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n  is definitely composite

    if n in is_probable_prime._known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in is_probable_prime._known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in is_probable_prime._known_primes[:_precision_for_huge_n])
is_probable_prime._known_primes = [2, 3]
is_probable_prime._known_primes += [x for x in range(5, 5000, 2) if is_probable_prime(x)]

def next_prime(n):
    """ Returns the next prime after 'n'"""
    r = n + 1
    if r % 2 == 0:
        r += 1

    while not is_probable_prime(r):
        r += 1

    return r
