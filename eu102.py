# ------------------------------------------ Triangle containment --------------------------------------------- #
#                                                                                                               #
#       Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000,        #
#       such that a triangle is formed.                                                                         #
#                                                                                                               #
#                                  A(-340,495), B(-153,-910), C(835,-947)                                       #
#                                  X(-175,41), Y(-421,-714), Z(574,-645)                                        #
#                                                                                                               #
#       It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.                #
#                                                                                                               #
#       Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing              #
#       the co-ordinates of one thousand "random" triangles, find the number of triangles for which             #
#       the interior contains the origin.                                                                       #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceFrom(self, x, y):
        return math.sqrt( (self.x - x)**2 + (self.y - y)**2 )

def checkTriangle(A, B, C):
    t = abs((A.x * (B.y - C.y)) + (B.x * (C.y - A.y)) + (C.x * (A.y - B.y)))
    s1 = abs((A.x * (B.y)) + (B.x * (0 - A.y)))
    s2 = abs((A.x * (0 - C.y)) + (C.x * (A.y)))
    s3 = abs((B.x * (C.y)) + (C.x * (0 - B.y)))

    return (t == (s1 + s2 + s3))

def eu102(coordinates):
    count = 0
    for l in coordinates:
        A = Point(l[0],l[1])
        B = Point(l[2],l[3])
        C = Point(l[4],l[5])

        if (checkTriangle(A, B, C)):
            count += 1
            
    return count
            

startTime = time.clock()
fsock = open("eu102.txt", "r")
coordinates = fsock.readlines()
fsock.close()
coordinates = [l.replace("\n", "") for l in coordinates]
coordinates = [l.split(",") for l in coordinates]
coordinates = [[int(n) for n in l] for l in coordinates] 
print (eu102(coordinates))
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
