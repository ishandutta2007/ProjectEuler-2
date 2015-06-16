# ------------------------------------------- Path sum: three ways -------------------------------------------- #
#                                                                                                               #
#       NOTE: This problem is a more challenging version of Problem 81.                                         #
#                                                                                                               #
#       The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column             #
#       and finishing in any cell in the right column, and only moving up, down, and right,                     #
#       is indicated in red and bold; the sum is equal to 994.                                                  #
#                                                                                                               #
#                                     131	673	234	103	18                                      #
#                                     201	96	342	965	150                                     #
#                                     630	803	746	422	111                                     #
#                                     537	699	497	121	956                                     #
#                                     805	732	524	37	331                                     #
#                                                                                                               #
#       Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'),                    #
#       a 31K text file containing a 80 by 80 matrix, from the left column to the right column.                 #
# ------------------------------------------------------------------------------------------------------------- #
import time

def calcMaxPath3Ways(matrix, start):
    l = len(matrix)
    d = [[-1 for i in range(l)] for i in range(l)]

    d[start][0] = matrix[start][0]
    reduced = [(start, 0)]

    for i in range(l * 2):
        for x,y in reduced:
            if (x > 0):
                if (d[x - 1][y] == -1):
                    reduced.append((x - 1, y))
                    d[x - 1][y] = d[x][y] + matrix[x - 1][y]
                else:
                    d[x - 1][y] = min(d[x - 1][y], d[x][y] + matrix[x - 1][y])
            if (x < l - 1):
                if (d[x + 1][y] == -1):
                    reduced.append((x + 1, y))
                    d[x + 1][y] = d[x][y] + matrix[x + 1][y]
                else:
                    d[x + 1][y] = min(d[x + 1][y], d[x][y] + matrix[x + 1][y])
            if (y < l - 1):
                if (d[x][y + 1] == -1):
                    reduced.append((x, y + 1))
                    d[x][y + 1] = d[x][y] + matrix[x][y + 1]
                else:
                    d[x][y + 1] = min(d[x][y + 1], d[x][y] + matrix[x][y + 1])

    m = d[0][l - 1]
    for i in range(1, l):
        if (d[i][l - 1] < m):
            m = d[i][l - 1]

    return m

def eu82(matrix):
    m = calcMaxPath3Ways(matrix, 0)

    for i in range(1, len(matrix)):
        t = calcMaxPath3Ways(matrix, i)
        if (t < m):
            m = t

    return m

if __name__ == "__main__":
    startTime = time.clock()
    fsock = open("eu82.txt", "r")
    matrix = fsock.readlines()
    fsock.close()
    matrix = [l.replace("\n", "") for l in matrix]
    matrix = [l.split(",") for l in matrix]
    matrix = [[int(n) for n in l] for l in matrix] 
    print (eu82(matrix))
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
