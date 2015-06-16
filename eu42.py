#-------------------------------------------------- Coded triangle numbers -------------------------------------------- #
#                                                                                                                       #
#       The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);                                     #
#       so the first ten triangle numbers are:                                                                          #
#                                                                                                                       #
#                               1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ..                                                 #
#                                                                                                                       #
#       By converting each letter in a word to a number corresponding to its alphabetical position                      #
#       and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.   #
#       If the word value is a triangle number then we shall call the word a triangle word.                             #
#                                                                                                                       #
#       Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand      #
#       common English words, how many are triangle words?                                                              #
# --------------------------------------------------------------------------------------------------------------------- #
import time
import math

def genTriangleNumbers(t):
    genTriangleNumbers.TRIANGLES = [0] * (t + 1)
    for i in range(t + 1):
        genTriangleNumbers.TRIANGLES[i] = i * (i + 1) // 2
genTriangleNumbers.TRIANGLES = []

def scoreWord(w):
    c = 0
    for i in range(len(w)):
        c += ord(w[i]) - ord('A') + 1

    return c

def eu42(words):
    genTriangleNumbers(300)
    
    total = sum([1 for w in words if (scoreWord(w) in genTriangleNumbers.TRIANGLES)])
            
    return total
            

startTime = time.clock()
fsock = open("eu42.txt", "r")
words = fsock.read()
fsock.close()
words = words.replace("\"", "")
words = words.split(",")
print (eu42(words))
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
