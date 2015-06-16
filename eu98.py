#----------------------------------------------------- Anagramic squares ---------------------------------------------- #
#                                                                                                                       #
#       By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number:    #
#       1296 = 36^2. What is remarkable is that, by using the same digital substitutions, the anagram, RACE,            #
#       also forms a square number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and specify   #
#       further that leading zeroes are not permitted, neither may a different letter have the same digital value       #
#       as another letter.                                                                                              #
#                                                                                                                       #
#       Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand      #
#       common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be        #
#       an anagram of itself).                                                                                          #
#                                                                                                                       #
#       What is the largest square number formed by any member of such a pair?                                          #
#                                                                                                                       #
#       NOTE: All anagrams formed must be contained in the given text file.                                             #
# --------------------------------------------------------------------------------------------------------------------- #
import time
from math import sqrt, ceil, floor

def mapWordToSquare(w, s):
    m = { }

    for i in range(len(w)):
        if (int(str(s)[i]) in m and m[int(str(s)[i])] != w[i]):
            return -1
        
        m[int(str(s)[i])] = w[i]
          
    return m

def checkAnagramicSquares(w1, w2):
    if (len(w1) != len(w2)):
        return False
    
    l = len(w1)

    if l not in checkAnagramicSquares.ANAGRAMIC_SQUARES:
        #print("start len:", l)
        anagramic_square = []
        squares_len_l = [i ** 2 for i in range(ceil(sqrt(10 ** (l - 1))), floor(sqrt(10 ** l - 1)) + 1)]

        for i in range(len(squares_len_l)):
            s1 = sorted(str(squares_len_l[i]))
            for j in range(i + 1, len(squares_len_l)):
                if (s1 == sorted(str(squares_len_l[j]))):
                    anagramic_square += [(squares_len_l[i], squares_len_l[j])]
        
        checkAnagramicSquares.ANAGRAMIC_SQUARES[l] = anagramic_square
        #print("end len:", l)

    for s1, s2 in checkAnagramicSquares.ANAGRAMIC_SQUARES[l]:
        m1 = mapWordToSquare(w1, s1)
        m2 = mapWordToSquare(w2, s2)

        if (m1 == m2 and m1 != -1):
            #print(w1, w2, s1, s2)
        
checkAnagramicSquares.ANAGRAMIC_SQUARES = { }

def eu98(words):
    max_len = max([len(w) for w in words])

    for l in range(1, max_len + 1):
        words_len_l = [w for w in words if (len(w) == l)]

        for i in range(len(words_len_l)):
            for j in range(i + 1, len(words_len_l)):
                if (sorted(words_len_l[i]) == sorted(words_len_l[j])):
                    checkAnagramicSquares(words_len_l[i], words_len_l[j])
        
    return max_len
            
if __name__ == "__main__":
    startTime = time.clock()
    fsock = open("eu98.txt", "r")
    words = fsock.readlines()
    fsock.close()
    words = [n.replace("\"", "") for n in words]
    words = words[0].split(",")
    print (eu98(words))
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
