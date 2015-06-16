# ------------------------------------------- Concealed Square ------------------------------------------------ #
#                                                                                                               #
#       Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,                         #
#       where each “_” is a single digit.                                                                       #
# ------------------------------------------------------------------------------------------------------------- #
import time

def checkNumber(n):
    n_square = pow(n, 2)

    n_square //= 100

    for i in range(8, 0, -1):
        if (n_square % 10 != i):
            return False

        n_square //= 100

    return True    
    
def eu206():
    # The number is divisible by 10. 17 digits left
    # Units digit is 3 or 7
    FACTOR = 10

    n = 100000000
    while (True):
        if (checkNumber(n + 3)):
            return 10 * (n + 3)
        if (checkNumber(n + 7)):
            return 10 * (n + 7)

        n += 10
        
if __name__ == "__main__":
    startTime = time.clock()
    print (eu206())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
