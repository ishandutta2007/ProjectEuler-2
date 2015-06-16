# ------------------------------------------ Efficient exponentiation ----------------------------------------- #
#                                                                                                               #
#       The most naive way of computing n15 requires fourteen multiplications:                                  #
#                                                                                                               #
#                       n × n × ... × n = n^15                                                                  #
#                                                                                                               #
#       But using a "binary" method you can compute it in six multiplications:                                  #
#                                                                                                               #
#                       n       × n     = n^2                                                                   #
#                       n^2     × n^2   = n^4                                                                   #
#                       n^4     × n^4   = n^8                                                                   #
#                       n^8     × n^4   = n^12                                                                  #
#                       n^12    × n^2   = n^14                                                                  #
#                       n^14    × n     = n^15                                                                  #
#                                                                                                               #
#       However it is yet possible to compute it in only five multiplications:                                  #
#                                                                                                               #
#                       n       × n     = n^2                                                                   #
#                       n^2     × n     = n^3                                                                   #
#                       n^3     × n^3   = n^6                                                                   #
#                       n^6     × n^6   = n^12                                                                  #
#                       n^12    × n^3   = n^15                                                                  #
#                                                                                                               #
#       We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.  #
#                                                                                                               #
#       For 1 ≤ k ≤ 200, find ∑ m(k).                                                                           #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

class Node:
    def __init__(self, p):
        self.v = None
        self.parent = p
        #self.children = []

    def add(self, val):
        toAdd = Node(self)
        toAdd.v = val
        #self.children += [toAdd]

        return toAdd

    def __repr__(self):
        if (self.parent == None):
            s = "Parent: None\n"
        else:
            s = "Parent: " + str(self.parent.v) + '\n'

        s += "Value: " + str(self.v) + '\n' \
             + "Children: [ "
        
        for c in self.children:
            s += str(c.v) + ' '
        s += ']'
        
        return s

def calcTotDepth(TOP):
    remaining = [i for i in range(2, TOP + 1)]
    
    root = Node(None)
    root.v = 1
    
    l = [root]

    s = 0
    d = 0
    while (True):
        newL = []
        for n in l:
            p = n
            while (p != None):
                newV = (n.v + p.v)
                if newV in remaining:
                    s += d + 1
                    remaining.remove(newV)
                    if remaining == []:
                        return s
                if newV < TOP:
                    newL.extend([n.add(newV)])

                p = p.parent

        l = newL
        d += 1
        
def eu122():
    TOP = 200

    return calcTotDepth(TOP)
    
if __name__ == "__main__":
    startTime = time.clock()
    print (eu122())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
