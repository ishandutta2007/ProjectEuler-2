# ------------------------------------------------ Number Mind ------------------------------------------------ #
#                                                                                                               #
#       The game Number Mind is a variant of the well known game Master Mind.                                   #
#                                                                                                               #
#       Instead of coloured pegs, you have to guess a secret sequence of digits. After each guess you're only   #
#       told in how many places you've guessed the correct digit. So, if the sequence was 1234 and you          #
#       guessed 2036, you'd be told that you have one correct digit;                                            #
#       however, you would NOT be told that you also have another digit in the wrong place.                     #
#                                                                                                               #
#       For instance, given the following guesses for a 5-digit secret sequence,                                #
#                                                                                                               #
#               90342 ;2 correct                                                                                #
#               70794 ;0 correct                                                                                #
#               39458 ;2 correct                                                                                #
#               34109 ;1 correct                                                                                #
#               51545 ;2 correct                                                                                #
#               12531 ;1 correct                                                                                #
#                                                                                                               #
#       The correct sequence 39542 is unique.                                                                   #
#                                                                                                               #
#       Based on the following guesses,                                                                         #
#                                                                                                               #
#               5616185650518293 ;2 correct                                                                     #
#               3847439647293047 ;1 correct                                                                     #
#               5855462940810587 ;3 correct                                                                     #
#               9742855507068353 ;3 correct                                                                     #
#               4296849643607543 ;3 correct                                                                     #
#               3174248439465858 ;1 correct                                                                     #
#               4513559094146117 ;2 correct                                                                     #
#               7890971548908067 ;3 correct                                                                     #
#               8157356344118483 ;1 correct                                                                     #
#               2615250744386899 ;2 correct                                                                     #
#               8690095851526254 ;3 correct                                                                     #
#               6375711915077050 ;1 correct                                                                     #
#               6913859173121360 ;1 correct                                                                     #
#               6442889055042768 ;2 correct                                                                     #
#               2321386104303845 ;0 correct                                                                     #
#               2326509471271448 ;2 correct                                                                     #
#               5251583379644322 ;2 correct                                                                     #
#               1748270476758276 ;3 correct                                                                     #
#               4895722652190306 ;1 correct                                                                     #
#               3041631117224635 ;3 correct                                                                     #
#               1841236454324589 ;3 correct                                                                     #
#               2659862637316867 ;2 correct                                                                     #
#                                                                                                               #
#       Find the unique 16-digit secret sequence.                                                               #
# ------------------------------------------------------------------------------------------------------------- #
import time
from itertools import combinations
from copy import deepcopy

def findSecret(hints, secret_len):
    secret = [set(range(10)) for i in range(secret_len)]

    # Secret uniqness elimination
    for i in range(secret_len):
        p = set(range(10))

        for hint, correct in hints:
            d = (hint // (10 ** (secret_len - 1 - i))) % 10
            if (d in p):
                p.remove(d)
        
        if (len(p) >= 2):
            secret[i] -= p
                             
    return findSecretHelp(hints, secret_len, secret, 0)
    
def findSecretHelp(hints, secret_len, secret, depth):
    if (len(hints) == 0):
        flag = True
        s = 0
        
        for i in range(secret_len):
            if (len(secret[i]) != 1):
                flag = False
                break
            else:
                e = list(secret[i])
                s *= 10
                s += e[0]

        if (flag == True):
            return str(s)

        return False

    #ident = ""
    #for i in range(depth):
    #    ident += "    "
        
    cur_hint, correct = hints[0]
    #print(ident,"Current hint:", cur_hint, ", ", correct)
    empty_places = [i for i in range(secret_len) if (len(secret[i]) != 1)]
    #print(ident,"Empty places:", empty_places)
    #print(ident,"Possible:", secret)

    #i = (secret_len - 1)
    #m = 10 ** (secret_len - 1)
    cur_hint_tmp = cur_hint
    for i in range(secret_len - 1, -1, -1):
        d = (cur_hint_tmp % 10)
        if (len(secret[i]) == 1 and (d in secret[i])):
            correct -= 1
        cur_hint_tmp //= 10

    #print("corr: ", correct)
    if (correct < 0):
        return False

    if (len(empty_places) < correct):
        #print(hints, secret, correct, empty_places)
        return False
    
    """if (correct == 0):
        tmp_secret = deepcopy(secret)

        for i in range(secret_len):
            if (len(secret[i]) != 1 and int(cur_hint[i]) in tmp_secret[i]):
                tmp_secret[i].remove(int(cur_hint[i]))
                
        return findSecretHelp(hints[1:], secret_len, tmp_secret)"""

    tmp_secret = [set() for i in range(len(secret))]
    for p in combinations(empty_places, correct):
        #tmp_secret = deepcopy(secret)
        #print(ident,"Cur combination:", p)

        
        if (not(all([(cur_hint // (10 ** (secret_len - 1 - j)) % 10) in secret[j] for j in p]))): #if (not(all([int(cur_hint[j]) in secret[j] for j in p]))):
            #print("err")
            continue

        # Mask secret with hint
        for j in empty_places:
            d = (cur_hint // (10 ** (secret_len - 1 - j)) % 10)
            if (j in p):
                tmp_secret[j] = secret[j]
                secret[j] = {d}
            else:
                if (d in secret[j]): #if (int(cur_hint[j]) in tmp_secret[j]):
                    #print({int(cur_hint[j])})
                    tmp_secret[j] = {d}
                    secret[j].remove(d)

        ret = findSecretHelp(hints[1:], secret_len, secret, depth + 1)
        if (ret != False):
            return ret

        # Reverse mask
        for j in empty_places:
            if (j in p):
                secret[j] = tmp_secret[j]
                tmp_secret[j] = set()
            else:
                d = (cur_hint // (10 ** (secret_len - 1 - j)) % 10)
                if (d in tmp_secret[j]):
                    secret[j] = secret[j].union(tmp_secret[j])
                    tmp_secret[j] = set()

    return False
            
def eu185():
    SECRET_LEN = 16
    
    """hints = [(70794, 0), \
             (90342, 2), \
             (39458, 2), \
             (51545, 2), \
             (34109, 1), \
             (12531, 1)]"""
    hints = [(2321386104303845, 0), \

             (5855462940810587, 3), \
             (9742855507068353, 3), \
             (4296849643607543, 3), \
             (7890971548908067, 3), \
             (8690095851526254, 3), \
             (1748270476758276, 3), \
             (3041631117224635, 3), \
             (1841236454324589, 3), \

             (4513559094146117, 2), \
             (2615250744386899, 2), \
             (6442889055042768, 2), \
             (5616185650518293, 2), \
             (2326509471271448, 2), \
             (5251583379644322, 2), \
             (2659862637316867, 2), \
             
             (3174248439465858, 1), \
             (3847439647293047, 1), \
             (8157356344118483, 1), \
             (6375711915077050, 1), \
             (6375711915077050, 1), \
             (6913859173121360, 1), \
             (4895722652190306, 1)]
    
    secret = findSecret(hints, SECRET_LEN)

    return secret

if __name__ == "__main__":
    startTime = time.clock()
    print (eu185())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
