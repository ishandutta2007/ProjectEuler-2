# --------------------------------------- Generalised Hamming Numbers ----------------------------------------- #
#                                                                                                               #
#       A Hamming number is a positive number which has no prime factor larger than 5.                          #
#       So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.                                #
#       There are 1105 Hamming numbers not exceeding 10^8.                                                      #
#                                                                                                               #
#       We will call a positive number a generalised Hamming number of type n, if it has no prime factor        #
#       larger than n.                                                                                          #
#       Hence the Hamming numbers are the generalised Hamming numbers of type 5.                                #
#                                                                                                               #
#       How many generalised Hamming numbers of type 100 are there which don't exceed 10^9?                     #
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

def countGeneralizedHammingNumbers(index, top):
    if (index == len(countGeneralizedHammingNumbers.PRIMES) - 1):
        return int(math.log(top, 2)) + 1

    s = 0

    new_top = top
    while (new_top >= 1):
        s += countGeneralizedHammingNumbers(index + 1, new_top)
        new_top /= countGeneralizedHammingNumbers.PRIMES[index]

    return s

def eu204():
    N = 100
    TOP = 10 ** 9

    countGeneralizedHammingNumbers.PRIMES = list(reversed(GenPrimesTo(N)))
    t = countGeneralizedHammingNumbers(0, TOP)

    return t

if __name__ == "__main__":
    startTime = time.clock()
    print (eu204())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
