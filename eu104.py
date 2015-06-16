# ------------------------------------------ Pandigital multiples --------------------------------------------- #
#                                                                                                               #
#       Take the number 192 and multiply it by each of 1, 2, and 3:                                             #
#                                                                                                               #
#                           192 × 1 = 192                                                                       #
#                           192 × 2 = 384                                                                       #
#                           192 × 3 = 576                                                                       #
#                                                                                                               #
#       By concatenating each product we get the 1 to 9 pandigital, 192384576.                                  #
#       We will call 192384576 the concatenated product of 192 and (1,2,3)                                      #
#                                                                                                               #
#       The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,                       #
#       giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).               #
#                                                                                                               #
#       What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product     #
#       of an integer with (1,2, ... , n) where n > 1?                                                          #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

def isPandigital(n):
    p = str(n)

    return (len(p) == 9 and all(d in p for d in [str(i) for i in range(1, 10)]))

def fibonacci():
    a = 0
    b = 1

    while (True):
        yield b

        b += a
        a = b - a
        
def fibonacciModulo(mod):
    a = 0
    b = 1

    while (True):
        yield b

        b += a
        a = b - a
        b = b % mod

def eu104():
    fib = fibonacciModulo(1000000000)
    fib1 = fibonacci()
    
    flag = True
    
    i = 1
    f = next(fib)
    f1 = next(fib1)

    while (True):
        while (not isPandigital(f)):
            i += 1
            f = next(fib)
            f1 = next(fib1)
    
        if (isPandigital(str(f1)[:9])):
            flag = False            

        if (flag == False):
            break
        
        i += 1
        f = next(fib)
        f1 = next(fib1)
        
    return i  

if __name__ == "__main__":
    startTime = time.clock()
    print (eu104())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
