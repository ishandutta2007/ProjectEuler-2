# -------------------- Searching a triangular array for a sub-triangle having minimum-sum --------------------- #
#                                                                                                               #
#       In a triangular array of positive and negative integers, we wish to find a sub-triangle such that the   #
#       sum of the numbers it contains is the smallest possible.                                                #
#                                                                                                               #
#       In the example below, it can be easily verified that the marked triangle satisfies this condition       #
#       having a sum of −42.                                                                                    #
#                                                                                                               #
#                                                       15                                                      #
#                                                   -14     -7                                                  #
#                                               20      -13     -5                                              #
#                                           -3      8       23      -26                                         #
#                                       1       -4      -5      -18     5                                       #
#                                   -16     31      2       9       28      3                                   #
#                                                                                                               #
#       We wish to make such a triangular array with one thousand rows, so we generate 500500 pseudo-random     #
#       numbers sk in the range ±219, using a type of random number generator                                   #
#       (known as a Linear Congruential Generator) as follows:                                                  #
#                                                                                                               #
#               t := 0                                                                                          #
#               for k = 1 up to k = 500500:                                                                     #
#                   t := (615949*t + 797807) modulo 2^20                                                        #
#                   sk := t−2^19                                                                                #
#                                                                                                               #
#       Thus: s1 = 273519, s2 = −153582, s3 = 450905 etc                                                        #
#                                                                                                               #
#       Our triangular array is then formed using the pseudo-random numbers thus:                               #
#                                                                                                               #
#                                                       s1                                                      #
#                                                   s2      s3                                                  #
#                                               s4      s5      s6                                              #
#                                           s7      s8      s9      s10                                         #
#                                                       ...                                                     #
#                                                                                                               #
#       Sub-triangles can start at any element of the array and extend down as far as we like (taking-in the    #
#       two elements directly below it from the next row, the three elements directly below from the row        #
#       after that, and so on).                                                                                 #
#       The "sum of a sub-triangle" is defined as the sum of all the elements it contains.                      #
#                                                                                                               #
#       Find the smallest possible sub-triangle sum.                                                            #
# ------------------------------------------------------------------------------------------------------------- #
import time

def gen_linear_congruential_number():
    t = 0

    k = 1
    while (1):
        t = (615949 * t + 797807) % (2 ** 20)

        yield(t - (2 ** 19))

def find_smallest_sum_triangle(tri, tri_sums, start, size):
    min_ending_here = 0
    min_so_far = 0
    
    for l in range(size):
        min_ending_here = min_ending_here + (tri_sums[start[0] + l][start[1] + l + 1] - \
                                             tri_sums[start[0] + l][start[1]])
        min_so_far = min(min_so_far, min_ending_here)
        
    return min_so_far

def eu150():
    SIZE = 1000 # -38951741 -> 100, -177633252 -> 300
    
    g = gen_linear_congruential_number()
    smallest_sum = 0

    triangle = [[next(g) for i in range(j + 1)] for j in range(SIZE)]

    triangle_sums = [[0 for i in range(j + 2)] for j in range(SIZE)]
    for i in range(SIZE):
        s = 0
        for j in range(i + 1):
            triangle_sums[i][j] = s
            s += triangle[i][j]
        triangle_sums[i][j + 1] = s
    
    for i in range(SIZE):
        for j in range(i + 1):
            smallest_sum = min(smallest_sum, find_smallest_sum_triangle(triangle, triangle_sums, (i, j), SIZE - 1 - i))
            
    """SIZE = 6
    triangle = [[15], [-14, -7], [20, -13, -5], [-3, 8, 23, -26],
                [1, -4, -5, -18, 5], [-16, 31, 2, 9, 28, 3]]

    smallest_sum = smallest_sum_triangle(triangle, (1, 1), 4)"""
    
    return smallest_sum

if __name__ == "__main__":
    startTime = time.clock()
    print (eu150())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
