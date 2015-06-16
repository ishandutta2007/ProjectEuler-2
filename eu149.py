# ---------------------------------- Searching for a maximum-sum subsequence ---------------------------------- #
#                                                                                                               #
#       Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers in   #
#       any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).                    #
#                                                                                                               #
#                                       −2	5	3	2                                               #
#                                       9	−6	5	1                                               #
#                                       3	2	7	3                                               #
#                                       −1	8	−4	8                                               #
#                                                                                                               #
#                                                                                                               #
#       Now, let us repeat the search, but on a much larger scale:                                              #
#                                                                                                               #
#       First, generate four million pseudo-random numbers using a specific form of what is known as            #
#       a "Lagged Fibonacci Generator":                                                                         #
#                                                                                                               #
#       For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007k3] (modulo 1000000) − 500000.                           #
#       For 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.                         #
#       
#       Thus, s10 = −393027 and s100 = 86613.                                                                   #
#                                                                                                               #
#       The terms of s are then arranged in a 2000×2000 table, using the first 2000 numbers to fill the         #
#       first row (sequentially), the next 2000 numbers to fill the second row, and so on.                      #
#                                                                                                               #
#       Finally, find the greatest sum of (any number of) adjacent entries in any direction                     #
#       (horizontal, vertical, diagonal or anti-diagonal).                                                      #
# ------------------------------------------------------------------------------------------------------------- #
import time

def gen_lagged_fib_number():
    S = [0 for i in range(55)]
    
    for k in range(1, 55 + 1):
        S[k - 1] = (100003 - 200003 * k + 300007 * (k ** 3)) % 1000000 - 500000
        yield S[k - 1]

    while (1):
        k += 1
        Sk = (S[0] + S[31]) % 1000000 - 500000 # No need to add 1,000,000
        S = S[1:] + [Sk]
        
        yield Sk

# Using Kadane's algorithm
# http://en.wikipedia.org/wiki/Maximum_subarray_problem
def kadanes_algorithm(arr, start, step, size):
    max_ending_here = 0
    max_so_far = 0
    
    for i in range(size):
        max_ending_here = max(0, max_ending_here + arr[start[0] + i * step[0]][start[1] + i * step[1]])
        max_so_far = max(max_so_far, max_ending_here)
        
    return max_so_far

def eu149():
    SIZE = 2000
    table = [[0 for i in range(SIZE)] for i in range(SIZE)]

    g = gen_lagged_fib_number()
    greatest_sum = 0

    # Init table
    for i in range(SIZE):
        for j in range(SIZE):
            table[i][j] = next(g)

    # Horizontal search
    for i in range(SIZE):
        greatest_sum = max(greatest_sum,
                           kadanes_algorithm(table, (i, 0), (0, 1), SIZE))

    # Vertical search
    for j in range(SIZE):
        greatest_sum = max(greatest_sum,
                           kadanes_algorithm(table, (0, j), (1, 0), SIZE))

    # Diagonal search
    for d in range(SIZE):
        greatest_sum = max(greatest_sum,
                           kadanes_algorithm(table, (0, d), (1, 1), SIZE - d))

        greatest_sum = max(greatest_sum,
                           kadanes_algorithm(table, (d, 0), (1, 1), SIZE - d))

    # Anti-diagonal search
    for d in range(SIZE):
        greatest_sum = max(greatest_sum,
                           kadanes_algorithm(table, (SIZE - 1, d), (-1, 1), SIZE - d))

        greatest_sum = max(greatest_sum,
                           kadanes_algorithm(table, (SIZE - 1 - d, 0), (-1, 1), SIZE - d))

    return greatest_sum

if __name__ == "__main__":
    startTime = time.clock()
    print (eu149())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
