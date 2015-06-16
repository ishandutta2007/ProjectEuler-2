# ------------------------------------------- Path sum: four ways --------------------------------------------- #
#                                                                                                               #
#       NOTE: This problem is a significantly more challenging version of Problem 81.                           #
#                                                                                                               #
#       In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,                 #
#       by moving left, right, up, and down, is indicated in bold red and is equal to 2297.                     #
#                                                                                                               #
#                                     131	673	234	103	18                                      #
#                                     201	96	342	965	150                                     #
#                                     630	803	746	422	111                                     #
#                                     537	699	497	121	956                                     #
#                                     805	732	524	37	331                                     #
#                                                                                                               #
#       Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'),                    #
#       a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right                     #
#       by moving left, right, up, and down.                                                                    #
# ------------------------------------------------------------------------------------------------------------- #
import time

def calcMaxPath4Ways(matrix):
    l = len(matrix)
    d = [[-1 for i in range(l)] for i in range(l)]

    d[0][0] = matrix[0][0]
    reduced = [(0, 0)]

    for i in range(l ** 2):
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
            if (y > 0):
                if (d[x][y - 1] == -1):
                    reduced.append((x, y - 1))
                    d[x][y - 1] = d[x][y] + matrix[x][y - 1]
                else:
                    d[x][y - 1] = min(d[x][y - 1], d[x][y] + matrix[x][y - 1])
            if (y < l - 1):
                if (d[x][y + 1] == -1):
                    reduced.append((x, y + 1))
                    d[x][y + 1] = d[x][y] + matrix[x][y + 1]
                else:
                    d[x][y + 1] = min(d[x][y + 1], d[x][y] + matrix[x][y + 1])

    return d[l - 1][l - 1]

def eu83(matrix):
    m = calcMaxPath4Ways(matrix)

    return m

if __name__ == "__main__":
    startTime = time.clock()
    fsock = open("eu83.txt", "r")
    matrix = fsock.readlines()
    fsock.close()
    matrix = [l.replace("\n", "") for l in matrix]
    matrix = [l.split(",") for l in matrix]
    matrix = [[int(n) for n in l] for l in matrix] 
    print (eu83(matrix))
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
