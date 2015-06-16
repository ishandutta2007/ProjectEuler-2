# -------------------------------------------- Special subset sums: optimum ------------------------------------------- #
#                                                                                                                       #
#       Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for            #
#       any two non-empty disjoint subsets, B and C, the following properties are true:                                 #
#                                                                                                                       #
#               i.  S(B) ≠ S(C); that is, sums of subsets cannot be equal.                                              #
#               ii. If B contains more elements than C then S(B) > S(C).                                                #
#       If S(A) is minimised for a given n, we shall call it an optimum special sum set.                                #
#       The first five optimum special sum sets are given below.                                                        #
#                                                                                                                       #
#               n = 1: {1}                                                                                              #
#               n = 2: {1, 2}                                                                                           #
#               n = 3: {2, 3, 4}                                                                                        #
#               n = 4: {3, 5, 6, 7}                                                                                     #
#               n = 5: {6, 9, 11, 12, 13}                                                                               #
#                                                                                                                       #
#       It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form              #
#       B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.                            #
#                                                                                                                       #
#       By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24},           #
#       with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a      #
#       near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and                #
#       corresponding set string: 111819202225.                                                                         #
#                                                                                                                       #
#       Given that A is an optimum special sum set for n = 7, find its set string.                                      #
#                                                                                                                       #
#       NOTE: This problem is related to Problem 105 and Problem 106.                                                   #
# --------------------------------------------------------------------------------------------------------------------- #
import time
import itertools

def check_special_subset_sum(S):
    if len(S) != len(set(S)):
        return False

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

def eu103():
    OPTIMAL_6 = [11, 18, 19, 20, 22, 25]

    interval = 3
    interval = tuple(range(-interval, interval + 1))

    near_optimal_7 = OPTIMAL_6[(len(OPTIMAL_6) - 1) // 2]
    near_optimal_7 = [near_optimal_7] + [near_optimal_7 + d for d in OPTIMAL_6]

    s = 500

    for v in itertools.product(interval, repeat=len(near_optimal_7)):
        optimal_7_candidate = [near_optimal_7[i] + v[i] for i in range(len(near_optimal_7))]

        if sum(optimal_7_candidate) >= s:
            continue

        if check_special_subset_sum(optimal_7_candidate):
            optimal_7 = optimal_7_candidate
            s = sum(optimal_7_candidate)
    
    return "".join([str(c) for c in optimal_7])
            
if __name__ == "__main__":
    startTime = time.clock()
    print (eu103())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
