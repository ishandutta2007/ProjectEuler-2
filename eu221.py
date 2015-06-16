# ------------------------------------------- Alexandrian Integers -------------------------------------------- #
#                                                                                                               #
#       We shall call a positive integer A an "Alexandrian integer", if there exist integers p, q, r such that: #
#                                                                                                               #
#                           A = p * q * r   and     1 / A = 1 / p + 1 / q + 1 / r                               #
#                                                                                                               #
#       For example, 630 is an Alexandrian integer (p = 5, q = −7, r = −18). In fact, 630 is the 6th            #
#       Alexandrian integer, the first 6 Alexandrian integers being: 6, 42, 120, 156, 420 and 630.              #
#                                                                                                               #
#       Find the 150000th Alexandrian integer.                                                                  #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math
  
def GenPrimesTo(n): 
    """ Gen list of all primes <= limit """
    size = n//2
    sieve = [1]*size 
    limit = int(n**0.5) 
      
    for i in range(1,limit): 
        if sieve[i]: 
            val = 2*i+1
            tmp = ((size-1) - i)//val  
            sieve[i+val::val] = [0]*tmp 
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def genAlexandrianIntegers():
    p = 1

    while (True):
        t = p * p + 1
        factorize(t)
        #for i in range(int(math.sqrt(t)), 0, -1):
        #    if (t % i == 0):
        #        yield (p * (p + i) * (p + (t // i)))
        yield(1)
        p += 1

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

def eu221():
    INDEX = 1000
    
    g = genAlexandrianIntegers()
    l = []
    
    for i in range(INDEX):
        #print(next(g))
        l.extend([next(g)])

    #return len(set(l))

if __name__ == "__main__":
    startTime = time.clock()
    print (eu221())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
