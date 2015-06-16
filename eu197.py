# ---------------------------- Investigating the behaviour of a recursively defined sequence -------------------------- #
#                                                                                                                       #
#       Given is the function f(x) = ⌊2^(30.403243784-x2)⌋ × 10-9 ( ⌊ ⌋ is the floor-function),                          #
#       the sequence un is defined by u0 = -1 and un+1 = f(un).                                                         #
#                                                                                                                       #
#       Find un + un+1 for n = 10^12.                                                                                   #
#       Give your answer with 9 digits after the decimal point.                                                         #
# --------------------------------------------------------------------------------------------------------------------- #
import time

def genF():
    x = -1

    yield x

    while True:
        x = int(2 ** (30.403243784 - x**2)) * 1e-9
        yield x

def eu197():
    LIMIT = 10 ** 12

    f = genF()

    c, b, a = next(f), next(f), next(f)
    
    while abs(a - c) > 1e-10:
        c, b, a = b, a, next(f)

    return str(a+b)[:11]

startTime = time.clock()
print (eu197())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
