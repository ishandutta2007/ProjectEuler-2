# --------------------------------------------------------- Squarefree Binomial Coefficients -------------------------------------------------- #
#                                                                                                                                               #
#       The binomial coefficients nCk can be arranged in triangular form, Pascal's triangle, like this:                                         #
#                                                                                                                                               #
#                                                                           1	                                                                #
#                                                                       1	1	                                                        #
#                                                                   1	    2       1	                                                        #
#                                                               1	3	3	1	                                                #
#                                                           1	    4       6       4       1	                                                #
#                                                       1	5	10	10	5	1	                                        #
#                                                   1       6       15      20      15      6       1	                                        #
#                                               1	7	21	35	35	21	7	1                                       #
#                                                                   .........                                                                   #
#                                                                                                                                               #
#       It can be seen that the first eight rows of Pascal's triangle contain twelve distinct numbers:                                          #
#           1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.                                                                                         #
#                                                                                                                                               #
#       A positive integer n is called squarefree if no square of a prime divides n. Of the twelve distinct numbers in the first eight rows     #
#       of Pascal's triangle, all except 4 and 20 are squarefree. The sum of the distinct squarefree numbers in the first eight rows is 105.    #
#                                                                                                                                               #
#       Find the sum of the distinct squarefree numbers in the first 51 rows of Pascal's triangle.                                              #
#                                                                                                                                               #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.numbers import is_square_free

def eu203():
    NUM_OF_ROWS = 51

    # Generate elements of pascal triangle
    p = [[1]]
    distinct_square_free = set()
    
    for i in range(1, NUM_OF_ROWS):
        l = [1]
        for j in range(1, i):
            l.append(p[i - 1][j - 1] + p[i - 1][j])

        l.append(1)

        p.append(l)

    # Search for "square free" elements
    for l in range(len(p)):
        for i in range((len(p[l]) + 1) // 2):
            if is_square_free(p[l][i]):
                distinct_square_free.update(set([p[l][i]]))
    
    return sum(distinct_square_free)

if __name__ == '__main__':
    startTime = time.clock()
    print (eu203())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
