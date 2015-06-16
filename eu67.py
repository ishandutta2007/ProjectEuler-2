# ------------------------------------------- Maximum path sum II --------------------------------------------- #
#                                                                                                               #
#       By starting at the top of the triangle below and moving to adjacent numbers on the row below,           #
#       the maximum total from top to bottom is 23.                                                             #
#                                                                                                               #
#                                                   3                                                           #
#                                               7       4                                                       #
#                                           2       4       6                                                   #
#                                       8       5       9       3                                               #
#                                                                                                               #
#       That is, 3 + 7 + 4 + 9 = 23.                                                                            #
#                                                                                                               #
#       Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),   #
#       a 15K text file containing a triangle with one-hundred rows.                                            #
#                                                                                                               #
#       NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to     #
#           solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes      #
#           every second it would take over twenty billion years to check them all.                             #
#           There is an efficient algorithm to solve it. ;o)                                                    #
# ------------------------------------------------------------------------------------------------------------- #
import time

def eu67(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 2):
            t = 0
            for k in range(j-1, j+1):
                if (k >= 0 and k <= i):
                    if (nums[i][k] > t):
                        t = nums[i][k]
            nums[i+1][j] += t

    #for i in range(len(nums)):
    #    print(nums[i])
        
    return max(nums[len(nums) - 1])
            

startTime = time.clock()
fsock = open("eu67.txt", "r")
nums = fsock.readlines()
fsock.close()
nums = [l.replace("\n", "") for l in nums]
nums = [l.split(" ") for l in nums]
nums = [[int(n) for n in l] for l in nums] 
print (eu67(nums))
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
