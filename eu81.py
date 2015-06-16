# -------------------------------------------- Path sum: two ways --------------------------------------------- #
#                                                                                                               #
#       In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,                 #
#       by only moving to the right and down, is indicated in bold red and is equal to 2427.                    #
#                                                                                                               #
#                                     131	673	234	103	18                                      #
#                                     201	96	342	965	150                                     #
#                                     630	803	746	422	111                                     #
#                                     537	699	497	121	956                                     #
#                                     805	732	524	37	331                                     #
#                                                                                                               #
#       Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'),                    #
#       a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right                     #
#       by only moving right and down.                                                                          #
# ------------------------------------------------------------------------------------------------------------- #
import time

def eu81(matrix):
    l = len(matrix)
    d = [[0 for i in range(l)] for i in range(l)]

    d[0][0] = matrix[0][0]
    for i in range(1, l):
        d[0][i] = matrix[0][i] + d[0][i - 1]
        d[i][0] = matrix[i][0] + d[i - 1][0]

    for i in range(1, l):
        for j in range(1, l):
            d[i][j] = min(d[i - 1][j], d[i][j - 1]) + matrix[i][j]
            
    return d[l - 1][l - 1]       

if __name__ == "__main__":
    startTime = time.clock()
    fsock = open("eu81.txt", "r")
    matrix = fsock.readlines()
    fsock.close()
    matrix = [l.replace("\n", "") for l in matrix]
    matrix = [l.split(",") for l in matrix]
    matrix = [[int(n) for n in l] for l in matrix] 
    print (eu81(matrix))
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
