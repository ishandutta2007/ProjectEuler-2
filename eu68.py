# -------------------------------------------- Magic 5-gon ring ----------------------------------------------- #
#                                                                                                               #
#       Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.#
#                                                                                                               #
#                                       4                                                                       #
#                                                                                                               #
#                                              3                                                                #
#                                                                                                               #
#                                           1       2       6                                                   #
#                                                                                                               #
#                                         5                                                                     #
#                                                                                                               #
#       Working clockwise, and starting from the group of three with the numerically lowest external node       #
#       (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can   #
#       be described by the set: 4,3,2; 6,2,1; 5,1,3.                                                           #
#                                                                                                               #
#       It is possible to complete the ring with four different totals: 9, 10, 11, and 12.                      #
#       There are eight solutions in total.                                                                     #
#                                                                                                               #
#               Total	Solution Set                                                                            #
#               9	4,2,3; 5,3,1; 6,1,2                                                                     #
#               9	4,3,2; 6,2,1; 5,1,3                                                                     #
#               10	2,3,5; 4,5,1; 6,1,3                                                                     #
#               10	2,5,3; 6,3,1; 4,1,5                                                                     #
#               11	1,4,6; 3,6,2; 5,2,4                                                                     #
#               11	1,6,4; 5,4,2; 3,2,6                                                                     #
#               12	1,5,6; 2,6,4; 3,4,5                                                                     #
#               12	1,6,5; 3,5,4; 2,4,6                                                                     #
#                                                                                                               #
#       By concatenating each group it is possible to form 9-digit strings; the maximum string for a            #
#       3-gon ring is 432621513.                                                                                #
#                                                                                                               #
#       Using the numbers 1 to 10, and depending on arrangements, it is possible to form                        #
#       16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?                 #
# ------------------------------------------------------------------------------------------------------------- #
import time
import itertools    

def printSolutionSet(r):
    m = 0

    for i in range(1, len(r)):
        if (r[i][0] < r[m][0]):
            m = i
            
    s = ""
    
    for i in range(len(r)):
        s += str(r[(i + m) % len(r)][0]) + ',' + str(r[(i + m) % len(r)][1]) + ',' + str(r[(i + m) % len(r)][2]) + '; '
        
    l = str(sum(r[0])) + '\t' + s[:-2]

    print(l)
    
def getRingVal(r):
    m = 0

    for i in range(1, len(r)):
        if (r[i][0] < r[m][0]):
            m = i

    s = ""
    for i in range(len(r)):
        s += str(r[(i + m) % len(r)][0]) + str(r[(i + m) % len(r)][1]) + str(r[(i + m) % len(r)][2])

    return int(s)
    
def getRingsSum(RING_SIZE, N, i):
    inner = [c for c in itertools.combinations(N, RING_SIZE) if sum(c) == ((i * RING_SIZE) - sum(N))]
    vals = []
    
    r = [[0, 0, 0] for j in range(RING_SIZE)]

    for c in inner:
        r[0][1] = c[0]
        p = itertools.permutations(c[1:])
        for p in p:
            for j in range(len(p)):
                r[j + 1][1] = p[j]

            for j in range(RING_SIZE):
                r[j][2] = r[(j + 1) % RING_SIZE][1]

            for j in range(RING_SIZE):
                r[j][0] = i - sum(r[j][1:])

            t = []
            
            for j in range(RING_SIZE):
                t += [r[j][0], r[j][1]]

            if (list(sorted(t)) == N):
                printSolutionSet(r)
                vals += [getRingVal(r)]

    return vals
    
def eu68():
    RING_SIZE = 5
    vals = []
    
    N = list(range(1, 2 * RING_SIZE + 1))

    min_sum = (sum(N) + sum(N[:RING_SIZE])) // RING_SIZE
    max_sum = (sum(N) + sum(N[RING_SIZE:])) // RING_SIZE

    print('Total' + '\t' + 'Solution Set')
          
    for i in range(min_sum, max_sum + 1):
        vals += getRingsSum(RING_SIZE, N, i)
        
    vals = list(reversed(sorted(vals)))
    vals = [v for v in vals if (len(str(v)) == 16)]
    
    return (vals[0])

if __name__ == "__main__":
    startTime = time.clock()
    print (eu68())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
