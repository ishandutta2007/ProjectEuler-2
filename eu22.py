#------------------------------------------------------- Names scores ------------------------------------------------- #
#                                                                                                                       #
#       Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand       #
#       first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,#
#       multiply this value by its alphabetical position in the list to obtain a name score.                            #
#                                                                                                                       #
#       For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,  #
#       is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.                              #
#                                                                                                                       #
#       What is the total of all the name scores in the file?                                                           #
# --------------------------------------------------------------------------------------------------------------------- #
import time
import math

def scoreName(name):
    c = 0
    for i in range(len(name)):
        c += ord(name[i]) - ord('A') + 1

    return c
    
def eu22(names):
    total = 0
    for i in range(len(names)):
        total += (i + 1) * scoreName(names[i])
            
    return total
            

startTime = time.clock()
fsock = open("eu22.txt", "r")
names = fsock.readlines()
fsock.close()
names = [n.replace("\"", "") for n in names]
names = names[0].split(",")
names = sorted(names)
print (eu22(names))
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
