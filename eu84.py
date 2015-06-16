# ---------------------------------------------------------------- Monopoly odds -------------------------------------------------------------- #
#                                                                                                                                               #
#       In the game, Monopoly, the standard board is set up in the following way:                                                               #
#                                                                                                                                               #
#                           GO	  A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL                                    #
#                           H2	 	                                                                C1                                      #
#                           T2	 	                                                                U1                                      #
#                           H1	 	                                                                C2                                      #
#                           CH3	 	                                                                C3                                      #
#                           R4	 	                                                                R2                                      #
#                           G3	 	                                                                D1                                      #
#                           CC3	 	                                                                CC2                                     #
#                           G2	 	                                                                D2                                      #
#                           G1	 	                                                                D3                                      #
#                           G2J	  F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP                                      #
#                                                                                                                                               #
#       A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a           #
#       clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However,              #
#       landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.                                           #
#                                                                                                                                               #
#       In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls               #
#       three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.                     #
#                                                                                                                                               #
#       At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the               #
#       top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards     #
#       in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned #
#       with movement will be ignored and the player will remain on the CC/CH square.                                                           #
#                                                                                                                                               #
#       Community Chest (2/16 cards):                                                                                                           #
#           1) Advance to GO                                                                                                                    #
#           2) Go to JAIL                                                                                                                       #
#       Chance (10/16 cards):                                                                                                                   #
#           1) Advance to GO                                                                                                                    #
#           2) Go to JAIL                                                                                                                       #
#           3) Go to C1                                                                                                                         #
#           4) Go to E3                                                                                                                         #
#           5) Go to H2                                                                                                                         #
#           6) Go to R1                                                                                                                         #
#           7) Go to next R (railway company)                                                                                                   #
#           8) Go to next R                                                                                                                     #
#           9) Go to next U (utility company)                                                                                                   #
#           10) Go back 3 squares.                                                                                                              #
#                                                                                                                                               #
#       The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at             #
#       that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing     #
#       on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final      #
#       square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting"         #
#       and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to      #
#       get out on their next turn.                                                                                                             #
#                                                                                                                                               #
#       By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings    #
#       that correspond with sets of squares.                                                                                                   #
#                                                                                                                                               #
#       Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24,      #
#       and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.                  #
#                                                                                                                                               #
#       If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.                                      #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from random import randint, shuffle

def rollDice():
    a = randint(1, 4)
    b = randint(1, 4)

    if (a == b):
        rollDice.DoubleCount += 1
    else:
        rollDice.DoubleCount = 0
        
    return (a, b)
rollDice.DoubleCount = 0

class Board:
    def __init__(self):
        self.Player = 0
        self.Squares = [0 for i in range(40)]
        self.Probabilities = []
        self.MovesCount = 0

        self.CommunityChestCards = [i for i in range(1, 16 + 1)]
        self.CommunityChestPtr = 0
        shuffle(self.CommunityChestCards)

        self.ChanceCards = [i for i in range(1, 16 + 1)]
        self.ChancePtr = 0
        shuffle(self.ChanceCards)

    def CommunityChest(self):
        if (self.CommunityChestCards[self.CommunityChestPtr] == 1):
            self.Player = 0 # Advance to GO
        elif (self.CommunityChestCards[self.CommunityChestPtr] == 2):
            self.Player = 10 # Go to JAIL

        self.CommunityChestPtr = (self.CommunityChestPtr + 1) % len(self.CommunityChestCards)

    def Chance(self):
        if (self.ChanceCards[self.ChancePtr] == 1):
            self.Player = 0 # Advance to GO
        elif (self.ChanceCards[self.ChancePtr] == 2):
            self.Player = 10 # Go to JAIL
        elif (self.ChanceCards[self.ChancePtr] == 3):
            self.Player = 11 # Go to C1
        elif (self.ChanceCards[self.ChancePtr] == 4):
            self.Player = 24 # Go to E3
        elif (self.ChanceCards[self.ChancePtr] == 5):
            self.Player = 39 # Go to H2
        elif (self.ChanceCards[self.ChancePtr] == 6):
            self.Player = 5 # Go to R1
        elif (self.ChanceCards[self.ChancePtr] == 7 or
              self.ChanceCards[self.ChancePtr] == 8):
            # Go to next R (railway company)
            if (self.Player == 7):
                self.Player = 15
            elif (self.Player == 22):
                self.Player = 25
            elif (self.Player == 36):
                self.Player = 5
        elif (self.ChanceCards[self.ChancePtr] == 9):
            # Go to next U (utility company)
            if (self.Player == 7):
                self.Player = 12
            elif (self.Player == 22):
                self.Player = 28
            elif (self.Player == 36):
                self.Player = 12
        elif (self.ChanceCards[self.ChancePtr] == 10):
            self.Player = (self.Player - 3) % 40 # Go back 3 squares.
            
        self.ChancePtr = (self.ChancePtr + 1) % len(self.ChanceCards)
    
    def Move(self):
        d = rollDice()
        self.Player = (self.Player + sum(d)) % 40

        if (rollDice.DoubleCount >= 3):
            self.Player = 10 # Three consecutive doubles - Go to JAIL
        elif (self.Player == 30): #G2J
            self.Player = 10
        elif (self.Player == 2 or self.Player == 17 or self.Player == 33):
            self.CommunityChest() # Community chest
        elif (self.Player == 7 or self.Player == 22 or self.Player == 36):
            self.Chance() # Chance
            
        self.Squares[self.Player] += 1.0
        self.MovesCount += 1

    def CalcStatistics(self):
        if (self.MovesCount == 0):
            return
        
        for i in range(40):
            self.Probabilities += [(self.Squares[i] / self.MovesCount * 100, i)]

        self.Probabilities = sorted(self.Probabilities, reverse = True)
        
    def PrintStatistics(self):
        if (self.MovesCount == 0):
            print("No iterations made")
            return
        
        for i in range(40):
            print(str(self.Probabilities[i][1]) + '\t' + str(self.Probabilities[i][0]))
    
Board.Player = 0
Board.Squares = [0 for i in range(40)]

def eu84():
    NumOfIterations = 500000

    b = Board()

    for i in range(NumOfIterations):
        b.Move()

    b.CalcStatistics()
    #b.PrintStatistics()

    return str(b.Probabilities[0][1]) + str(b.Probabilities[1][1]) + str(b.Probabilities[2][1])
    
if __name__ == "__main__":
    startTime = time.clock()
    print (eu84())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
