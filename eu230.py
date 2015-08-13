# ------------------------------------------------------------ Fibonacci Words ---------------------------------------------------------------- #
#                                                                                                                                               #
#       For any two strings of digits, A and B, we define FA,B to be the sequence (A,B,AB,BAB,ABBAB,...)                                        #
#       in which each term is the concatenation of the previous two.                                                                            #
#                                                                                                                                               #
#       Further, we define D_A,B(n) to be the nth digit in the first term of F_A,B that contains at least n digits.                             #
#                                                                                                                                               #
#       Example:                                                                                                                                #
#                                                                                                                                               #
#       Let A=1415926535, B=8979323846. We wish to find D_A,B(35), say.                                                                         #
#                                                                                                                                               #
#       The first few terms of F_A,B are:                                                                                                       #
#           1415926535                                                                                                                          #
#           8979323846                                                                                                                          #
#           14159265358979323846                                                                                                                #
#           897932384614159265358979323846                                                                                                      #
#           1415926535897932384689793238461415{9}265358979323846                                                                                #
#                                                                                                                                               #
#       Then D_A,B(35) is the 35th digit in the fifth term, which is 9.                                                                         #
#                                                                                                                                               #
#       Now we use for A the first 100 digits of π behind the decimal point:                                                                    #
#                                                                                                                                               #
#           1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679                                #
#                                                                                                                                               #
#       and for B the next hundred digits:                                                                                                      #
#                                                                                                                                               #
#           8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196 .                              #
#                                                                                                                                               #
#       Find ∑n = 0,1,...,17   10^n× _DA,B((127+19n)×7^n) .                                                                                     #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def d(a, b, n):
    def find_digit_in_fibonacci_word(word_index, digit_index):
        if word_index == 0:
            return int(a[digit_index - 1])
        elif word_index == 1:
            return int(b[digit_index - 1])
        
        if digit_index <= lengths[word_index - 2]:
            return find_digit_in_fibonacci_word(word_index - 2, digit_index)
        else:
            return find_digit_in_fibonacci_word(word_index - 1, digit_index - lengths[word_index - 2])
        
    lengths = [len(a), len(b)]

    while lengths[-1] < n:
        lengths.append(lengths[-2] + lengths[-1])

    if len(a) >= n:
        return int(a[n - 1])
    
    return find_digit_in_fibonacci_word(len(lengths) - 1, n)

def eu230():
    TOP = 17
    
    A = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
    B = '8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'

    ret = 0
    for n in range(TOP, -1, -1):
        ret = ret * 10 + d(A, B, ((127 + (19 * n)) * (7 ** n)))

    return ret
if __name__ == '__main__':
    startTime = time.clock()
    print (eu230())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
