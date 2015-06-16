# -------------------------------------------------------------- Palindromic sums ----------------------------------------------------------------- #
#                                                                                                                                                   #
#       The palindromic number 595 is interesting because it can be written as the sum of consecutive squares:                                      #
#                                       6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.                                                                 #
#                                                                                                                                                   #
#       There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes    #
#       is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.                    #
#                                                                                                                                                   #
#       Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.               #
# ------------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from euler.numbers import is_palindrome

def eu125():
    TOP = 10 ** 8
    
    sum_of_squares_to_n = [0]
    diff_of_squares_to_n = set()

    i = 1
    n = 0

    n += i * i
    while i*i < TOP:
        sum_of_squares_to_n.append(n)
        i += 1
        n += i * i

    for i in range(len(sum_of_squares_to_n)):
        for j in range(i + 2, len(sum_of_squares_to_n)):
            d = sum_of_squares_to_n[j] - sum_of_squares_to_n[i]
            if d < TOP and is_palindrome(d):
                diff_of_squares_to_n.add(d)
    
    return sum(diff_of_squares_to_n)
                                
if __name__ == "__main__":
    startTime = time.clock()
    print (eu125())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
