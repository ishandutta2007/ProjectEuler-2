# ---------------------- Sum square difference ------------------------ #
#                                                                       #
#       The sum of the squares of the first ten natural numbers is,     #
#                   1^2 + 2^2 + ... + 10^2 = 385                        #
#       The square of the sum of the first ten natural numbers is,      #
#                   (1 + 2 + ... + 10)^2 = 55^2 = 3025                  #
#       Hence the difference between the sum of the squares of the      #
#       first ten natural numbers and the square of the sum is          #
#                           3025 − 385 = 2640.                          #
#       Find the difference between the sum of the squares of the       #
#       first one hundred natural numbers and the square of the sum.    #
# --------------------------------------------------------------------- #
import time
import math

def approach1(TOP):
    sumOfSquares = sum([i*i for i in range (TOP + 1)])
    squareOfSum = sum(range(TOP + 1))**2
    
    return squareOfSum - sumOfSquares

def approach2(TOP):
    sumOfSquares = int(TOP * (TOP + 1) * (2 * TOP + 1) / 6)
    squareOfSum = int((TOP * (TOP + 1) / 2)**2)
    
    return squareOfSum - sumOfSquares

def eu6():
    TOP = 100

    return approach2(TOP)

startTime = time.clock()
print (eu6())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
