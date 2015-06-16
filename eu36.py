# ---------------------------------------- Double-base palindromes -------------------------------------------- #
#                                                                                                               #
#       The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.                           #
#                                                                                                               #
#       Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.        #
#                                                                                                               #
#       (Please note that the palindromic number, in either base, may not include leading zeros.)               #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

def isPalindromic(n):
    return (n == "".join(list(reversed(n))))

def toBinary(d):
    n = int(d)
    b = ""

    while (n != 0):
        b = str(n % 2) + b
        n //= 2

    return b

def eu36():
    l = {}
    
    for a in {1, 3, 5, 7, 9}:
        for b in range(10):
            for c in range(10):
                # 1-digit number
                n = str(a)
                if (isPalindromic(toBinary(n))):
                    l[n] = 0
                    
                # 2-digit number
                n = (str(a)+str(a))
                if (isPalindromic(toBinary(n))):
                    l[n] = 0

                # 3-digit number
                n = (str(a)+str(b)+str(a))
                if (isPalindromic(toBinary(n))):
                    l[n] = 0

                # 4-digit number
                n = (str(a)+str(b)+str(b)+str(a))
                if (isPalindromic(toBinary(n))):
                    l[n] = 0

                # 5-digit number
                n = (str(a)+str(b)+str(c)+str(b)+str(a))
                if (isPalindromic(toBinary(n))):
                    l[n] = 0
                    
                # 6-digit number
                n = (str(a)+str(b)+str(c)+str(c)+str(b)+str(a))
                if (isPalindromic(toBinary(n))):
                    l[n] = 0

    return sum([int(i) for i in set(l)])

startTime = time.clock()
print (eu36())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
