from itertools import product as _product
from operator import mul as _mul
from functools import reduce as _reduce

def factorize(number):
    """Factorize natural number.

    """
    factors = []
    org = number
    n = 2

    if (org in factorize.MEMORY):
        return factorize.MEMORY[org]
    
    while (True):
        if (number in factorize.MEMORY):
            factors.extend(factorize.MEMORY[number])
            factorize.MEMORY[org] = factors
            return factors
        if (number < 2):
            factorize.MEMORY[org] = factors
            return factors
        if (n > 1 + (number ** 0.5)):
            factors.append(number)
            factorize.MEMORY[org] = factors
            return factors
        if (number % n == 0):
            factors.append(n)
            number = number // n 
        else:
            n += 1
factorize.MEMORY = {}

def get_distinct_factors(n):
    """Return the discinct factors of natural number.

    """
    
    return set(factorize(n))

def is_square_free(number):
    """Check if a number is square free

    """    
    if (number in factorize.MEMORY):
        return factorize.MEMORY[number]

    if number % 4 == 0:
        is_square_free.MEMORY[number] = False
        
        return False

    for n in range(3, int(number ** 0.5) + 1):
        if number % n == 0:
            number //= n

        if number % n == 0:
            is_square_free.MEMORY[number] = False
            
            return False

    is_square_free.MEMORY[number] = True

    return True        
is_square_free.MEMORY = { 1: True }

def radical(n):
    """Return the radical of natural number.

    """
    factors = get_distinct_factors(n)

    r = 1
    for f in factors:
        r *= f

    return r

def radical_sieve(n):
    numbers = [i for i in range(n + 1)]
    radicals = [1 for _ in range(n + 1)]
    
    for i in range(2, n + 1):
        if numbers[i] == i:
            for j in range(i, n + 1, i):
                while numbers[j] % i == 0:
                    numbers[j] //= i

                radicals[j] *= i

    return radicals

def get_divisors(n, with_negative=False):
    """Return all the divisors of a number.

    Including the number itself.
    """
    factors = { }
    divisors = [ ]
    
    for f in factorize(n):
        try:
            factors[f] = factors[f] + 1
        except KeyError:
            factors[f] = 1

    for c in factors.values():
        c = list(range(c))

    f = tuple(factors.keys())
    c = tuple(factors.values())

    for p in _product(*[list(range(t + 1)) for t in c]):
        d = int(_reduce(_mul, ([f[i] ** p[i] for i in range(len(f))])))
        divisors.append(d)

    if with_negative:
        divisors.extend([-d for d in divisors])
        
    return sorted(divisors)

def log_floor(n, base):
    r = 0

    while n >= base:
        r += 1
        n //= base

    return r

def is_permutation(n1, n2):
    if (n1 - n2) % 9 != 0: # fast reject
        return False

    return sorted(str(n1)) == sorted(str(n2))

def is_palindrome(n):
    """ Check if n is a palindrome. """

    return (str(n) == str(n)[::-1])

"""def is_amicable_number(n):
    if n == 1 or n == 2:
        return False
    
    d = sumOfProperDivisors(n)
    return (sumOfProperDivisors(d) == n and d != n)

def is_abundant_number(n):
    if (not n in isAbundantNumber.MEMORY):
        isAbundantNumber.MEMORY[n] = (sumOfProperDivisors(n) > n)
        
    return isAbundantNumber.MEMORY[n]
isAbundantNumber.MEMORY = {}"""

def digitsCount(n):
    s = 0

    while (n):
        s += 1
        n //= 10

    return s

def digitsSum(n):
    s = 0

    while (n):
        s += n % 10
        n //= 10

    return s

def digital_root(n):
    return (n - 1) % 9 + 1

def digital_root_consecutive(n):
    if n < 10:
        return

    c = 0
    while n:
        c += n % 10
        n //= 10

    return c

def is_digit_fifth_power_number(n):
    return (n == sum([int(d) ** 5 for d in str(n)]))
