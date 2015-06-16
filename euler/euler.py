# -------------------------------------------  --------------------------------------------- #
from math import sqrt
from itertools import product
from functools import reduce
from operator import mul
from collections import Counter

def gcd(a, b):
    while (b != 0):
        a, b = b, a % b
        
    return abs(a)

def egcd(a, b):
    x, lastX = 0, 1
    y, lastY = 1, 0
    
    while (b != 0):
        q = a // b
        a, b = b, a % b
        x, lastX = lastX - q * x, x
        y, lastY = lastY - q * y, y
        
    return (lastX, lastY)

def primeSieve(n):  
    """ Gen list of all primes <= n """
    n += 1
    size = n // 2
    sieve = [1] * size  
    limit = int(n ** 0.5)  
        
    for i in range(1, limit):  
        if sieve[i]:  
            val = 2 * i + 1
            tmp = ((size - 1) - i) // val   
            sieve[i + val : :val] = [0] * tmp
            
    return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0] 

def isPrime(n):
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

    r = int(sqrt(n))
    c = 5

    while c <= r:
        if n % c == 0:
            return False
        if n % (c + 2) == 0:
            return False
        c += 6

    return True

def isProbablePrime(n, _precision_for_huge_n =8):
    """ Using Miller-Rabin algorithm """
    def _try_composite(a, d, n, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n  is definitely composite

    if n in isProbablePrime._known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in isProbablePrime._known_primes):
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
                   for a in isProbablePrime._known_primes[:_precision_for_huge_n])
isProbablePrime._known_primes = [2, 3]
isProbablePrime._known_primes += [x for x in range(5, 5000, 2) if isProbablePrime(x)]

def factorize(number):
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

def getDistinctFactors(n):
    return set(factorize(n))

def sumOfProperDivisors(n):
    s = 1
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            s += i
            s += n // i

    if int(sqrt(n)) ** 2 == n:
        s -= int(sqrt(n))
           
    return s
    
def totientSieve(n): 
    """ Generate list of phi(i) for i=2..n """
    spf = [0] * (n + 1)

    for a in range(2, n + 1):
        if (a % 2 == 0):
            spf[a] = 2
        else:
            spf[a] = a

    for a in range(3, int(sqrt(n)), 2):
        if (spf[a] == a):
            for m in range(a ** 2, n + 1, 2 * a):
                if (spf[m] == m):
                    spf[m] = a

    phi = [0] * (n + 1)

    for a in range(2, n + 1):
        if (spf[a] == a):
            phi[a] = a - 1
        else:
            p = spf[a]
            m = a // p

            if (spf[m] == p):
                f = p
            else:
                f = p - 1

            phi[a] = f * phi[m]
      
    return phi

def phi(x, factors = None):
    if (factors == None):
        factors = getDistinctFactors(x)
        
    for p in factors:
        x -= x // p

    return x

def phiInverse(n):
    def calcInversePhi(n, primes):
        if (n == 1):
            return [1, 2]
            
        if (len(primes) == 1):
            p = primes[0]
            t = 0
            if (n % (p - 1) != 0):
                return []
            t = 1
            n //= (p - 1)
            while (n % p == 0):
                n //= p
                t += 1

            if (n == 1):
                return [p ** t]
            else:
                return []

        p = primes[0]
        ret = calcInversePhi(n, primes[1:])
        
        e = 1
        t = p - 1
        while (True):
            if (n % t != 0):
                break
            rec = calcInversePhi(n // t, primes[1:])
            
            if (rec == []):
                curV = [p ** e]
            else:
                curV = [p ** e * v for v in rec]

            ret.extend(curV)
            
            e += 1
            t *= p

        return ret
        
    def getPrimes(n):
        factors = Counter(factorize(n))

        b = list(factors)
        e = [factors[i] for i in b]
        d = []
    
        for v in product(*[range(d + 1) for d in e]):
            d.extend([(reduce(mul,[b[i] ** v[i] for i in range(len(b))]))])

        primes = [(p + 1) for p in d if isProbablePrime(p + 1)]

        return list(reversed(primes))

    primes = getPrimes(n)
    
    return list(sorted(set([x for x in calcInversePhi(n, primes) if x > n + 1])))

def isPermutation(n1, n2):
    if (n1 - n2) % 9 != 0: # fast reject
        return False

    return sorted(str(n1)) == sorted(str(n2))

def isPalindromic(n):
    """ Check if n is a palindrom """
    return (str(n) == str(n)[::-1])

def isDigitFifthNumber(n):
    return (n == sum([int(d) ** 5 for d in str(n)]))

def isAmicableNumber(n):
    if n == 1 or n == 2:
        return False
    
    d = sumOfProperDivisors(n)
    return (sumOfProperDivisors(d) == n and d != n)

def isAbundantNumber(n):
    if (not n in isAbundantNumber.MEMORY):
        isAbundantNumber.MEMORY[n] = (sumOfProperDivisors(n) > n)
        
    return isAbundantNumber.MEMORY[n]
isAbundantNumber.MEMORY = {}

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
