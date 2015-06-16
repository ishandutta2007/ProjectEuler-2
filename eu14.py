# ------------------------------- Longest Collatz sequence -------------------------------- #
#                                                                                           #
#       The following iterative sequence is defined for the set of positive integers:       #
#           n → n/2 (n is even)                                                             #
#           n → 3n + 1 (n is odd)                                                           #
#                                                                                           #
#       Using the rule above and starting with 13, we generate the following sequence:      #
#                       13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1                          #
#                                                                                           #
#       It can be seen that this sequence (starting at 13 and finishing at 1)               #
#           contains 10 terms.                                                              #
#       Although it has not been proved yet (Collatz Problem),                              #
#           it is thought that all starting numbers finish at 1.                            #
#                                                                                           #
#       Which starting number, under one million, produces the longest chain?               #
#       NOTE: Once the chain starts the terms are allowed to go above one million.          #
# ----------------------------------------------------------------------------------------- #
import time

def nextCollatzElement(n):
    """ Returns the next Collatz element """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def checkCollatzSequence(n):
    if n in l:
        return l[n]

    l[n] = 1 + checkCollatzSequence(nextCollatzElement(n))

    return l[n]

def eu14():
    TOP = 1000000

    maxIndex = 1
    l[1] = 1
    
    for i in range(2, TOP):
        t = checkCollatzSequence(i)
        if t > l[maxIndex]:
            maxIndex = i

    return maxIndex

startTime = time.clock()
l = {}
print (eu14())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
