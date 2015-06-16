# ----------------------------------------------------------------- The Chase ----------------------------------------------------------------- #
#                                                                                                                                               #
#       "The Chase" is a game played with two dice and an even number of players.                                                               #
#                                                                                                                                               #
#       The players sit around a table; the game begins with two opposite players having one die each. On each turn,                            #
#       the two players with a die roll it.                                                                                                     #
#       If a player rolls a 1, he passes the die to his neighbour on the left; if he rolls a 6, he passes the die to his neighbour on the right;#
#       otherwise, he keeps the die for the next turn.                                                                                          #
#       The game ends when one player has both dice after they have been rolled and passed; that player has then lost.                          #
#                                                                                                                                               #
#       In a game with 100 players, what is the expected number of turns the game lasts?                                                        #
#                                                                                                                                               #
#       Give your answer rounded to ten significant digits.                                                                                     #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from numpy import linalg

def eu227():
    LEN = 100
    mat = [ [0 for i in range(LEN - 1)] for i in range(LEN - 1)]

    for i in range(LEN - 1):
        mat[i][i] = 1 / 2

        if (i > 0):
            mat[i][i - 1] = 2 / 9
            mat[i - 1][i] = 2 / 9

        if (i > 1):
            mat[i][i - 2] = 1 / 36
            mat[i - 2][i] = 1 / 36

        if (i < LEN - 2):
            mat[i][i + 1] = 2 / 9
            mat[i + 1][i] = 2 / 9

        if (i < LEN - 3):
            mat[i][i + 2] = 1 / 36
            mat[i + 2][i] = 1 / 36

        mat[0][LEN - 2] = 1 / 36
        mat[LEN - 2][0] = 1 / 36

    for i in range(LEN - 1):
        for j in range(LEN - 1):
            if i == j:
                mat[i][j] = 1 - mat[i][j]
            else:
                mat[i][j] = 0 - mat[i][j]
        
    inv = linalg.inv(mat)

    return (sum(inv[LEN // 2 - 1]).round(6))
    
if __name__ == "__main__":
    startTime = time.clock()
    print (eu227())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
