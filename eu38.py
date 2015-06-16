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

def isConcatanatedPandigitalProduct(seed, n):
    m = [str(seed * i) for i in range(1, n + 1)]

    p = "".join(m)

    return (len(p) == 9 and all(d in p for d in [str(i) for i in range(1, 10)]))
    
def eu38():
    N = 2
    
    for n in range(9876, -1, -1):
        if (isConcatanatedPandigitalProduct(n, N)):            
            return ("".join([str(n * i) for i in range(1, N + 1)]))

startTime = time.clock()
print (eu38())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
