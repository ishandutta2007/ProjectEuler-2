# --------------------------------------------------- Square digit chains --------------------------------------------- #
#                                                                                                                       #
#       A number chain is created by continuously adding the square of the digits in a number to form a new number      #
#       until it has been seen before.                                                                                  #
#                                                                                                                       #
#       For example,                                                                                                    #
#                                                                                                                       #
#               44 → 32 → 13 → 10 → 1 → 1                                                                               #
#               85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89                                                         #
#                                                                                                                       #
#       Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing          #
#       is that EVERY starting number will eventually arrive at 1 or 89.                                                #
#                                                                                                                       #
#       How many starting numbers below ten million will arrive at 89?                                                  #
# --------------------------------------------------------------------------------------------------------------------- #
import time
import math
    
def nextSquareDigitElement(n):
    """ Returns the next square digit element """
    s = 0
    while (n):
        s += nextSquareDigitElement.SQUARES[n % 10]
        n //= 10
    return s
nextSquareDigitElement.SQUARES = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

   #" return sum([factorials[int(i)] for i in str(n)]) " # It's the slower way...

def genSquareDigitChain(n):
    """ Calculate the length of the chain starting with n """
    if n in genSquareDigitChain.HISTORY:
        return genSquareDigitChain.HISTORY[n]

    genSquareDigitChain.HISTORY[n] = genSquareDigitChain(nextSquareDigitElement(n))

    return genSquareDigitChain.HISTORY[n]
genSquareDigitChain.HISTORY = {1:1, 89:89}

def eu92():
    TOP = 10000000
    count = 0

    for i in range(1, TOP):
        if genSquareDigitChain(i) == 89:
            count += 1

    return count

startTime = time.clock()
print (eu92())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
