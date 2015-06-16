# -------------------------------------------- Cube digit pairs ----------------------------------------------- #
#                                                                                                               #
#       Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done          #
#       to a second cube. By placing the two cubes side-by-side in different positions we can form a            #
#       variety of 2-digit numbers.                                                                             #
#                                                                                                               #
#       For example, the square number 64 could be formed:                                                      #
#                                                                                                               #
#                                                       64                                                      #
#                                                                                                               #
#       In fact, by carefully choosing the digits on both cubes it is possible to display all of the            #
#       square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.                               #
#                                                                                                               #
#       For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube                  #
#       and {1, 2, 3, 4, 8, 9} on the other cube.                                                               #
#                                                                                                               #
#       However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement     #
#       like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed;      #
#       otherwise it would be impossible to obtain 09.                                                          #
#                                                                                                               #
#       In determining a distinct arrangement we are interested in the digits on each cube, not the order.      #
#                                                                                                               #
#               {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}                                          #
#               {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}                                          #
#                                                                                                               #
#       But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both      #
#       represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.            #
#                                                                                                               #
#       How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?    #
# ------------------------------------------------------------------------------------------------------------- #
import time
import itertools

def genCube():
    S = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for s in itertools.combinations(S, 6):
        yield s

def checkCubes(cA, cB):
    if (not((0 in cA and 1 in cB) or (1 in cA and 0 in cB))): #01
        return 0

    if (not((0 in cA and 4 in cB) or (4 in cA and 0 in cB))): #04
        return 0

    if (not((0 in cA and 6 in cB) or (6 in cA and 0 in cB) or
            (0 in cA and 9 in cB) or (9 in cA and 0 in cB))): #09
        return 0

    if (not((1 in cA and 6 in cB) or (6 in cA and 1 in cB) or
            (1 in cA and 9 in cB) or (9 in cA and 1 in cB))): #16
        return 0

    if (not((2 in cA and 5 in cB) or (5 in cA and 2 in cB))): #25
        return 0

    if (not((3 in cA and 6 in cB) or (6 in cA and 3 in cB) or
            (3 in cA and 9 in cB) or (9 in cA and 3 in cB))): #36
        return 0

    if (not((4 in cA and 6 in cB) or (6 in cA and 4 in cB) or
            (4 in cA and 9 in cB) or (9 in cA and 4 in cB))): #49
        return 0

    if (not((6 in cA and 4 in cB) or (4 in cA and 6 in cB) or
            (9 in cA and 4 in cB) or (4 in cA and 9 in cB))): #64
        return 0

    if (not((8 in cA and 1 in cB) or (1 in cA and 8 in cB))): #81
        return 0

    return 1  
    
def eu90():
    count = 0
    
    cubeA = genCube()

    for cA in cubeA:
        cubeB = genCube()

        for cB in cubeB:
            count += checkCubes(cA, cB)

    return count // 2 # Can replace cube positions, cubes can't be the same...

if __name__ == "__main__":
    startTime = time.clock()
    print (eu90())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
