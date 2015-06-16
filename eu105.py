# -------------------------------------------- Special subset sums: testing ------------------------------------------- #
#                                                                                                                       #
#       Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two    #
#       non-empty disjoint subsets, B and C, the following properties are true:                                         #
#                                                                                                                       #
#       i.  S(B) ≠ S(C); that is, sums of subsets cannot be equal.                                                      #
#       ii. If B contains more elements than C then S(B) > S(C).                                                        #
#                                                                                                                       #
#       For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84,     #
#       whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair          #
#       combinations and S(A) = 1286.                                                                                   #
#                                                                                                                       #
#       Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing      #
#       seven to twelve elements (the two examples given above are the first two sets in the file),                     #
#       identify all the special sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).          #
#                                                                                                                       #
#       NOTE: This problem is related to problems 103 and 106.                                                          #
# --------------------------------------------------------------------------------------------------------------------- #
import time
import itertools

def check_special_subset_sum(S):
    S = sorted(S)

    l = (len(S) + 1) // 2
    r = l - 1

    if sum(S[:l]) <= sum(S[-r:]):
        return False

    sums = []
    for i in range(1, len(S) + 1):
        sums += list(itertools.combinations(S, i))
    sums = [sum(s) for s in sums]
    
    if len(sums) != len(set(sums)):
        return False

    return True

def eu105(sets):
    total = 0
    for s in sets:
        if check_special_subset_sum(s):
            total += sum(s)
            
    return total
            
if __name__ == "__main__":
    startTime = time.clock()
    fsock = open("eu105.txt", "r")
    sets = fsock.readlines()
    fsock.close()
    sets = [l.replace("\n", "") for l in sets]
    sets = [l.split(",") for l in sets]
    sets = [[int(n) for n in l] for l in sets]
    print (eu105(sets))
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
