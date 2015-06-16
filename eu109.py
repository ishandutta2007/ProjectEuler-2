# -------------------------------------------------------------------- Darts ------------------------------------------------------------------ #
#                                                                                                                                               #
#       In the game of darts a player throws three darts at a target board which is split into twenty equal sized sections numbered             #
#       one to twenty.                                                                                                                          #
#                                                                                                                                               #
#       The score of a dart is determined by the number of the region that the dart lands in. A dart landing outside the red/green outer        #
#       ring scores zero. The black and cream regions inside this ring represent single scores. However, the red/green outer ring               #
#       and middle ring score double and treble scores respectively.                                                                            #
#                                                                                                                                               #
#       At the centre of the board are two concentric circles called the bull region, or bulls-eye. The outer bull is worth 25 points           #
#       and the inner bull is a double, worth 50 points.                                                                                        #
#                                                                                                                                               #
#       There are many variations of rules but in the most popular game the players will begin with a score 301 or 501 and the first player     #
#       to reduce their running total to zero is a winner. However, it is normal to play a "doubles out" system, which means that the player    #
#       must land a double (including the double bulls-eye at the centre of the board) on their final dart to win; any other dart that would    #
#       reduce their running total to one or lower means the score for that set of three darts is "bust".                                       #
#                                                                                                                                               #
#       When a player is able to finish on their current score it is called a "checkout" and the highest checkout is 170:                       #
#       T20 T20 D25 (two treble 20s and double bull).                                                                                           #
#                                                                                                                                               #
#       There are exactly eleven distinct ways to checkout on a score of 6:                                                                     #
#                                                                                                                                               #
#                           D3	 	                                                                                                        #
#                           D1	        D2	                                                                                                #
#                           S2	        D2	                                                                                                #
#                           D2	        D1	                                                                                                #
#                           S4	        D1	                                                                                                #
#                           S1	        S1	        D2                                                                                      #
#                           S1	        T1	        D1                                                                                      #
#                           S1	        S3	        D1                                                                                      #
#                           D1	        D1	        D1                                                                                      #
#                           D1	        S2	        D1                                                                                      #
#                           S2	        S2	        D1                                                                                      #
#                                                                                                                                               #
#       Note that D1 D2 is considered different to D2 D1 as they finish on different doubles. However, the combination S1 T1 D1 is considered   #
#       the same as T1 S1 D1.                                                                                                                   #
#                                                                                                                                               #
#       In addition we shall not include misses in considering combinations; for example, D3 is the same as 0 D3 and 0 0 D3.                    #
#                                                                                                                                               #
#       Incredibly there are 42336 distinct ways of checking out in total.                                                                      #
#                                                                                                                                               #
#       How many distinct ways can a player checkout with a score less than 100?                                                                #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

MtoS = {1: 'S', 2: 'D', 3: 'T'}

def checkoutScore3(n):
    m = []
    count = 0

    if (n >= 50):
        m += [('D25', 50)]
        
    for i in range(min(20, n // 2), 0, -1):
        m += [('D' + str(i), i * 2)] 

    # 1 dart checkouts
    for d1 in m:
        if (d1[1] == n):
            count += 1
            #print(d1[0])

    # 2 darts checkouts
    for d2 in m:
        for d1 in checkoutScore1(n - d2[1]):
            count += 1
            #print(d1[0] + ' ' + d2[0])

    # 3 darts checkouts
    for d3 in m:
        for d12 in checkoutScore2(n - d3[1]):
            count += 1
            #print(d12[0][0] + ' ' + d12[1][0] + ' ' + d3[0])
    
    return count

def checkoutScore2(n):
    m = []
    d12 = []
       
    for i in range(min(20, n // 3), 0, -1):
        m += [('T' + str(i), i * 3)]

    if (n >= 50):
        m += [('D25', 50)]
        
    for i in range(min(20, n // 2), 0, -1):
        m += [('D' + str(i), i * 2)]

    if (n >= 25):
        m += [('S25', 25)]
        
    for i in range(min(20, n), 0, -1):
        m += [('S' + str(i), i)]

    for d2 in m:
        d = checkoutScore1(n - d2[1])

        for d1 in d:
            if ((d1, d2) not in d12):
                d12 += ((d2, d1),)
            
    return d12

def checkoutScore1(n):
    m = []

    for i in range(1, 2 + 1):
        if (n == 25 * i):
            m += [(MtoS[i] + '25', 25 * i)]

    for i in range(1, 3 + 1):
       for j in range(1, 20 + 1):
            if (n == j * i):
                m += [(MtoS[i] + str(j), j * i)]

    return m
    
def eu109():
    count = 0

    for i in range(1, 100):
        count += checkoutScore3(i)
        
    return count

if __name__ == "__main__":
    startTime = time.clock()
    print (eu109())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
