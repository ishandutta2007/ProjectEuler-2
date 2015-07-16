# ------------------------------------------------------------- Maximix Arrangements ---------------------------------------------------------- #
#                                                                                                                                               #
#       A train is used to transport four carriages in the order: ABCD.                                                                         #
#       However, sometimes when the train arrives to collect the carriages they are not in the correct order.                                   #
#       To rearrange the carriages they are all shunted on to a large rotating turntable. After the carriages are uncoupled at a specific point #
#       the train moves off the turntable pulling the carriages still attached with it. The remaining carriages are rotated 180 degrees.        #
#       All of the carriages are then rejoined and this process is repeated as often as necessary in order to obtain the least number           #
#       of uses of the turntable.                                                                                                               #
#       Some arrangements, such as ADCB, can be solved easily: the carriages are separated between A and D, and after DCB are rotated           #
#       the correct order has been achieved.                                                                                                    #
#                                                                                                                                               #
#       However, Simple Simon, the train driver, is not known for his efficiency, so he always solves the problem by initially getting          #
#       carriage A in the correct place, then carriage B, and so on.                                                                            #
#                                                                                                                                               #
#       Using four carriages, the worst possible arrangements for Simon, which we shall call maximix arrangements,                              #
#       are DACB and DBAC; each requiring him five rotations (although, using the most efficient approach, they could be solved                 #
#       using just three rotations). The process he uses for DACB is shown below.                                                               #
#                                                                                                                                               #
#                                                                   D|ABC                                                                       #
#                                                                   |DBCA                                                                       #
#                                                                   AC|BD                                                                       #
#                                                                   A|CDB                                                                       #
#                                                                   AB|DC                                                                       #
#                                                                   ABCD                                                                        #
#                                                                                                                                               #
#       It can be verified that there are 24 maximix arrangements for six carriages, of which the tenth lexicographic                           #
#       maximix arrangement is DFAECB.                                                                                                          #
#                                                                                                                                               #
#       Find the 2011th lexicographic maximix arrangement for eleven carriages.                                                                 #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from itertools import permutations

class Train(object):
    def __init__(self, l):
        self.arrangement = l
        self.size = len(l)

    def __str__(self):
        return "".join([chr(ord('A') + c) for c in self.arrangement])

    def __len__(self):
        a = list(self.arrangement)

        l = 0
        for c in range(self.size - 1):
            if a[c] == c:
                continue

            i = a.index(c)
            
            if i != self.size - 1:
                l += 1
                a[i:] = reversed(a[i:])

            l += 1
            a[c:] = reversed(a[c:])

        return l

    def is_max_size(self):
        a = list(self.arrangement)

        for c in range(self.size - 2):
            if a[c] == c:
                return False

            i = a.index(c)

            if i == self.size - 1:
                return False

            a[i:] = reversed(a[i:])
            a[c:] = reversed(a[c:])

        return (a[self.size - 2] != self.size - 2)
        
    def solve(self):
        l = 0
        print('#{}: {}'.format(l, self))
        
        for c in range(len(self.arrangement) - 1):
            if self.arrangement[c] == c:
                continue

            i = self.arrangement.index(c)
            
            if i != self.size - 1:
                l += 1
                self.arrangement[i:] = reversed(self.arrangement[i:])
                print('#{}: {}'.format(l, self))

            l += 1
            self.arrangement[c:] = reversed(self.arrangement[c:])
            print('#{}: {}'.format(l, self))
        
def eu336():
    NUM_OF_CARRIAGES = 11
    TARGET_MAXIMIX_ELEMENT = 2011

    i = 0

    for p in permutations(range(NUM_OF_CARRIAGES)):
        train = Train(p)

        if train.is_max_size():
            i += 1
    
        if i == TARGET_MAXIMIX_ELEMENT:
            return train
        
if __name__ == "__main__":
    startTime = time.clock()
    print (eu336())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
