# ----------------------------------------------- Su Doku ------------------------------------------------- #
#                                                                                                           #
#       Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.              #
#       Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar,      #
#       and much more difficult, puzzle idea called Latin Squares.                                          #
#       The objective of Su Doku puzzles, however, is to replace the blanks (or zeros)                      #
#       in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9.  #
#       Below is an example of a typical starting puzzle grid and its solution grid.                        #
#                                                                                                           #
#                   0 0 3 | 0 2 0 | 6 0 0                       4 8 3 | 9 2 1 | 6 5 7                       #
#                   9 0 0 | 3 0 5 | 0 0 1                       9 6 7 | 3 4 5 | 8 2 1                       #
#                   0 0 1 | 0 2 0 | 6 0 0                       2 5 1 | 8 7 6 | 4 9 3                       #
#                   ---------------------                       ---------------------                       #
#                   0 0 8 | 1 0 2 | 9 0 0                       5 4 8 | 1 3 2 | 9 7 6                       #
#                   7 0 0 | 0 0 0 | 0 0 8                       7 2 9 | 5 6 4 | 1 3 8                       #
#                   0 0 6 | 7 0 8 | 2 0 0                       1 3 6 | 7 9 8 | 2 4 5                       #
#                   ---------------------                       ---------------------                       #
#                   0 0 2 | 6 0 9 | 5 0 0                       3 7 2 | 6 8 9 | 5 1 4                       #
#                   8 0 0 | 2 0 3 | 0 0 9                       8 1 4 | 2 5 3 | 7 6 9                       #
#                   0 0 5 | 0 1 0 | 3 0 0                       6 9 5 | 4 1 7 | 3 8 2                       #
#                                                                                                           #
#       A well constructed Su Doku puzzle has a unique solution and can be solved by logic,                 #
#       although it may be necessary to employ "guess and test" methods in order to eliminate options       #
#       (there is much contested opinion over this).                                                        #
#       The complexity of the search determines the difficulty of the puzzle;                               #
#       the example above is considered easy because it can be solved by straight forward direct deduction. #
#                                                                                                           #
#       The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different   #
#       Su Doku puzzles ranging in difficulty, but all with unique solutions                                #
#       (the first puzzle in the file is the example above).                                                #
#                                                                                                           #
#       By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left              #
#       corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner   #
#       of the solution grid above.                                                                         #
# --------------------------------------------------------------------------------------------------------- #
import time
import math
import copy
import operator
import functools
import itertools

class Sudoku:
    """ Sudoku Puzzle """
    def __init__(self, l):
        if (l != ""):
            self._name = str(l[0]).replace("\n", "")
            self._board = [s.replace("\n", "") for s in l[1:]]
            self._board = [list(s) for s in self._board]
            self._board = [[int(d) for d in r] for r in self._board]

    def copy(self):
        ret = Sudoku("")

        ret._name = self._name
        ret._board = [self._board[i][:] for i in range(len(self._board))]

        return ret
    
    def cell(self, i, j):
        return self._board[i][j]

    def draw(self, withHeader = True, fsock = None):
        """ Draws the Sudoku """
        if withHeader == True:
            print (self._name)
            if (fsock != None):
                print (self._name, file = fsock)
        for i in range(9):
            if i % 3 == 0:
                print ("-------------------------")
                if (fsock != None):
                    print ("-------------------------", file = fsock)
            l = "| "
            for j in range(9):
                l += str(self.cell(i, j)) + " "
                if j % 3 == 2:
                    l += "| "
            print (l)
            if (fsock != None):
                 print (l, file = fsock)
        print ("-------------------------")
        if (fsock != None):
            print ("-------------------------", file = fsock)
                
    def solve(self):
        p = set(range(1, 10))
        self._candidates = [[copy.deepcopy(p) for i in range(9)] for j in range(9)]
        
        while (True):
            if (self.isSolved() == True):
                return self

            if (not self.isSolvable()):
                break
            
            for i in range(9):
                for j in range(9):
                    if self.cell(i, j) != 0:
                        self._candidates[i][j] = None
            
            for i in range(9):
                for j in range(9): 
                    self.eliminateWith(i, j)

            if (self.checkForFilling() == True):
                continue

            # guess fill
            r, c = self.getOptCandidate()
            if (self._candidates[r][c] == None):
                return self
            
            for d in self._candidates[r][c]:
                dup = self.copy()
                dup._board[r][c] = d
                
                ret = dup.solve()
                
                if ret != None and ret.isSolved():
                    return ret
                

            break

    def eliminateWith(self, r, c):
        if r < 0 or r >= 9:
            return

        if c < 0 or c >= 9:
            return

        d = self.cell(r, c)
        if d == 0:
            return
        
        for t in range(9):
            if self._candidates[r][t] != None:
                self._candidates[r][t].discard(d)

            if self._candidates[t][c] != None:
                self._candidates[t][c].discard(d)

        a = r // 3
        b = c // 3

        for i in range(3):
            for j in range(3):
                if self._candidates[a*3 + i][b*3 + j] != None:
                    self._candidates[a*3 + i][b*3 + j].discard(d)

    def checkForFilling(self):
        flag = False

        for i in range(9):
            for j in range(9):
                if self._candidates[i][j] != None:
                    if len(self._candidates[i][j]) == 1:
                        self._board[i][j] = self._candidates[i][j].pop()
                        self._candidates[i][j] = None
                        flag = True

        return flag

    def checkForSingleton(self):
        flag = False

        # Check rows
        for i in range(9):
            for num in range(1, 10):
                count = 0
                for j in range(9):
                    if self._candidates[i][j] != None:
                        if num in self._candidates[i][j]:
                            count += 1
                            index = j
                if count == 1:
                    self._board[i][index] = num
                    self._candidates[i][index] = None
                    self.eliminateWith(i, index)
                    flag = True

        # Check columns
        for j in range(9):
            for num in range(1, 10):
                count = 0
                for i in range(9):
                    if self._candidates[i][j] != None:
                        if num in self._candidates[i][j]:
                            count += 1
                            index = i
                if count == 1:
                    self._board[index][j] = num
                    self._candidates[index][j] = None
                    self.eliminateWith(index, j)
                    flag = True

        return flag

        # Check squares
        for a in range(3):
            for b in range(3):
                for num in range(1, 10):
                    count = 0
                    for i in range(3):
                        for j in range(3):
                            if self._candidates[a*3 + i][b*3 + j] != None:
                                if num in self._candidates[a*3 + i][b*3 + j]:
                                    count += 1
                                    index = (i, j)
                    if count == 1:
                        self._board[a*3 + index[0]][b*3 + index[1]] = num
                        self._candidates[a*3 + index[0]][b*3 + index[1]] = None
                        self.eliminateWith(a*3 + index[0], b*3 + index[1])
                        flag = True

        return flag

    def getOptCandidate(self):
        m = 10
        best_r = 0
        best_c = 0

        for r, c in itertools.product(range(9), repeat=2):
            tmp = self._candidates[r][c]
            if (tmp != None and len(tmp) < m):
                best_r = r
                best_c = c
                m = len(tmp)

        return best_r, best_c
    
    def isSolved(self):
        for r in range(9):
            if not all ([d in self._board[r] for d in range(1, 10)]):
                return False

        for c in range(9):
            if not all ([d in [self._board[r][c] for r in range(9)] for d in range(1, 10)]):
                return False

        return True

    def isSolvable(self):
        for r in range(9):
            for d in range(1, 10):
                if d not in self._board[r]:
                    flag = False
                    for c in range(9):
                        if self._candidates[r][c] != None and d in self._candidates[r][c]:
                            flag = True
                            break

                    if flag == False:
                        return False

        return True

    @property
    def result(self):
        a = self._board[0][0]
        b = self._board[0][1]
        c = self._board[0][2]

        if a == 0 or b == 0 or c == 0:
            return -1
        else:
            return 100*a + 10*b + c
        
    @property
    def name(self):
        return self._name
    
    _name = ""
    _board = []
    _candidates = []
        
def eu96():
    NUM_OF_PUZZLES = 50
    fsock = open("eu96.txt", "r")
    puzzles = fsock.readlines()
    fsock.close()
    foutsock = open("eu96_solved.txt", "w")
    totRes = 0
    totSolved = 0
    for curPuzzle in range(1, NUM_OF_PUZZLES + 1):
        s = Sudoku(puzzles[(curPuzzle-1) * 10 : curPuzzle * 10])
        s = s.solve()

        if s.isSolved() == True:
            print (s.name, " - Solved")
            print (s.name, " - Solved", file = foutsock)
            s.draw(False, foutsock)
            print ("Result:", s.result)
            print ("Result:", s.result, file = foutsock)
            totRes += s.result
            totSolved += 1
        else:
            print (s.name, " - Wasn't solved")
            print (s.name, " - Wasn't solved", file = foutsock)
            s.draw(False, foutsock)
            print ("Result:", s.result)
            print ("Result:", s.result, file = foutsock)

    print ("Total solved:", totSolved, "Puzzles")
    print ("Total solved:", totSolved, "Puzzles", file = foutsock)
    print ("Total result:", totRes)
    print ("Total result:", totRes, file = foutsock)

    foutsock.close()
    return totRes

if __name__ == "__main__":
    startTime = time.clock()
    ret = eu96()
    #print ()
    print (ret)
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
