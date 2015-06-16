# ------------------------------------------------- Digit factorial chains -------------------------------------------- #
#                                                                                                                       #
#       The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:      #
#           1! + 4! + 5! = 1 + 24 + 120 = 145                                                                           #
#                                                                                                                       #
#       Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;         #
#       it turns out that there are only three such loops that exist:                                                   #
#           169 → 363601 → 1454 → 169                                                                                   #
#           871 → 45361 → 871                                                                                           #
#           872 → 45362 → 872                                                                                           #
#                                                                                                                       #
#       It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,       #
#           69 → 363600 → 1454 → 169 → 363601 (→ 1454)                                                                  #
#           78 → 45360 → 871 → 45361 (→ 871)                                                                            #
#           540 → 145 (→ 145)                                                                                           #
#                                                                                                                       #
#       Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain              #
#       with a starting number below one million is sixty terms.                                                        #
#                                                                                                                       #
#       How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?           #
# --------------------------------------------------------------------------------------------------------------------- #
import time
import math

def nextFactorialElement(n):
    """ Returns the next factorial element """
    c = 0
    while (n):
        c += factorials[n % 10]
        n = n // 10

    return c

    " return sum([factorials[int(i)] for i in str(n)]) " # It's the slower way...

def genFactorialsChain(n):
    """ Calculate the length of the chain starting with n """
    if n in l:
        return l[n]

    l[n] = 1 + genFactorialsChain(nextFactorialElement(n))

    return l[n]

def getFactorialsChain(n):
    """ Generate the factorials chain starting with n, and its length """
    length = genFactorialsChain(n)

    i = 1
    s = str(n)
    while (i < length):
        s += " -> "
        n = nextFactorialElement(n)
        s += str(n)
        i += 1

    s += " ( -> " + str(nextFactorialElement(n)) + " )"
    
    return s,length

def eu74():
    TOP = 1000000
    LEN = 60

    count = 0
    for i in range(2, TOP):
        if genFactorialsChain(i) == LEN:
            count += 1

    return count

startTime = time.clock()
factorials = [math.factorial(i) for i in range(10)]
l = {1:1, 2:1, 145:1, 169:3, 363601:3, 1454:3, 871:2, 45361:2, 872:2, 45362:2, 40585:1}
print (eu74())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
