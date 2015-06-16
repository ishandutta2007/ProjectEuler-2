# -------------------------------------- 1000-digit Fibonacci number ------------------------------------------ #
#                                                                                                               #
#       The Fibonacci sequence is defined by the recurrence relation:                                           #
#                                                                                                               #
#                       Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.                                              #
#                                                                                                               #
#       Hence the first 12 terms will be:                                                                       #
#                                                                                                               #
#                       F1 = 1                                                                                  #
#                       F2 = 1                                                                                  #
#                       F3 = 2                                                                                  #
#                       F4 = 3                                                                                  #
#                       F5 = 5                                                                                  #
#                       F6 = 8                                                                                  #
#                       F7 = 13                                                                                 #
#                       F8 = 21                                                                                 #
#                       F9 = 34                                                                                 #
#                       F10 = 55                                                                                #
#                       F11 = 89                                                                                #
#                       F12 = 144                                                                               #
#                                                                                                               #
#       The 12th term, F12, is the first term to contain three digits.                                          #
#                                                                                                               #
#       What is the first term in the Fibonacci sequence to contain 1000 digits?                                #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

# Generates the fibonacci series
def fibonacci():
    a = 0
    b = 1

    while (True):
        yield b

        b += a
        a = b - a
    
def eu25():
    LENGTH = 1000

    count = 1
    iterator = fibonacci()
    fib = next(iterator)
    while (len(str(fib)) < LENGTH):
        fib = next(iterator)
        count += 1

    return (count)

startTime = time.clock()
print (eu25())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
