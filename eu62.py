# -------------------------------- Cubic permutations --------------------------------- #
#                                                                                       #
#       The cube, 41063625 (345^3), can be permuted to produce two other cubes:         #
#                       56623104 (384^3) and 66430125 (405^3).                          #
#       In fact, 41063625 is the smallest cube which has exactly three permutations     #
#           of its digits which are also cube.                                          #
#                                                                                       #
#       Find the smallest cube for which exactly five permutations                      #
#           of its digits are cube.                                                     #
# ------------------------------------------------------------------------------------- #
import time
import math

class multiset:
    def __init__(self, n):
        self._elements = [int(d) for d in str(n)]
        self._elements = sorted(self._elements)

    def add(self, e):
        self._elements.append(e)
        self._elements = sorted(self._elements)

    def getElements(self):
        return tuple(self._elements)

    _elements = []
    
def eu62():
    NUM_OF_CUBIC_PERMUTATIONS = 5

    n = 1

    while (1):
        e = multiset(n ** 3).getElements()
        if e in d:
            d[e].append(n)
            if len(d[e]) == NUM_OF_CUBIC_PERMUTATIONS:
                return  min(d[e])**3
                break
        else:
            d[e] = [n]
            
        n += 1

    return 0
d = {}
startTime = time.clock()
print (eu62())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
