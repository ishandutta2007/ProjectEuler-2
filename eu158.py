# -------- Exploring strings for which only one character comes lexicographically after its neighbour to the left --------- #
#                                                                                                                           #
#       Taking three different letters from the 26 letters of the alphabet, character strings of length three can be formed.#
#       Examples are 'abc', 'hat' and 'zyx'.                                                                                #
#       When we study these three examples we see that for 'abc' two characters come lexicographically after                #
#       its neighbour to the left.                                                                                          #
#       For 'hat' there is exactly one character that comes lexicographically after its neighbour to the left.              #
#       For 'zyx' there are zero characters that come lexicographically after its neighbour to the left.                    #
#       In all there are 10400 strings of length 3 for which exactly one character comes lexicographically after            #
#       its neighbour to the left.                                                                                          #
#                                                                                                                           #
#       We now consider strings of n ≤ 26 different characters from the alphabet.                                           #
#       For every n, p(n) is the number of strings of length n for which exactly one character comes lexicographically      #
#       after its neighbour to the left.                                                                                    #
#                                                                                                                           #
#       What is the maximum value of p(n)?                                                                                  #
# ------------------------------------------------------------------------------------------------------------------------- #
import time
from euler.combinatorics import nCk

def eu158():
    alphabet_len = 26
    TOP = 3

    decreasing_string_of_len_tot = [nCk(alphabet_len, i) for i in range(1, alphabet_len + 1)]

    mult = [0 for i in range(alphabet_len)]
    for l in range(2, alphabet_len):
        mult[l - 1] = mult[l - 2] + (2**(l - 1) - 1) #sum([nCk(l - 1, t) for t in range(1, l)])

    p = [decreasing_string_of_len_tot[n] * mult[n] for n in range(alphabet_len)]
    
    return max(p)

if __name__ == "__main__":
    startTime = time.clock()
    print (eu158())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
