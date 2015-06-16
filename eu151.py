# ----------------------------- Paper sheets of standard sizes: an expected-value problem --------------------------------- #
#                                                                                                                           #
#       A printing shop runs 16 batches (jobs) every week and each batch requires a sheet of special                        #
#       colour-proofing paper of size A5.                                                                                   #
#                                                                                                                           #
#       Every Monday morning, the foreman opens a new envelope, containing a large sheet of the special                     #
#       paper with size A1.                                                                                                 #
#                                                                                                                           #
#       He proceeds to cut it in half, thus getting two sheets of size A2. Then he cuts one of them in half                 #
#       to get two sheets of size A3 and so on until he obtains the A5-size sheet needed for the first batch of the week.   #
#                                                                                                                           #
#       All the unused sheets are placed back in the envelope.                                                              #
#                                                                                                                           #
#                          .+:::::::::::::::::::::::::::::::::::::::::o:::::::::::::::::::::::::::::::::::::::::+           #
#                          -+                                         y                                         y           #
#                          -+                                         y                                         y           #
#                          -+                                         y                                         y           #
#                          -+                                         y                                         y           #
#                          -+                                         y                                         y           #
#                          -+                                         y                                         y           #
#                          -+                                         y                  /\                     y           #
#                          -+                                         y                 /__\                    y           #
#                          -+                                         y                /    \3                  y           #
#                          -+                                         y                                         y           #
#                          -+                                         y                                         y           #
#                          -+                                         y                                         y           #
#                          -+                                         y                                         y           #
#                 /\       -+                  /\                     y                                         y           #
#                /  \      -+                 /__\                    h::::::::::::::::::::/::::::::::::::::::::h           #
#               /____\     -+                /    \2                  y                    y                    y           #
#              /      \1   -+                                         y                    y                    y           #
#                          -+                                         y                    y        /\          y           #
#                          -+                                         y                    y       /__\         y           #
#                          -+                                         y                    y      /    \5       y           #
#                          -+                                         y                    y                    y           #
#                          -+                                         y       /\           y                    y           #
#                          -+                                         y      /__\          h::::::::::::::::::::h           #
#                          -+                                         y     /    \4        y                    y           #
#                          -+                                         y                    y                    y           #
#                          -+                                         y                    y        /\          y           #
#                          -+                                         y                    y       /__\         y           #
#                          -+                                         y                    y      /    \5       y           #
#                          -+                                         y                    y                    y           #
#                          -s:::::::::::::::::::::::::::::::::::::::::h::::::::::::::::::::h::::::::::::::::::::h           #                                                                                                 #
#                                                                                                                           #
#       At the beginning of each subsequent batch, he takes from the envelope one sheet of paper at random.                 #
#       If it is of size A5, he uses it. If it is larger, he repeats the 'cut-in-half' procedure until he has what          #
#       he needs and any remaining sheets are always placed back in the envelope.                                           #
#                                                                                                                           #
#       Excluding the first and last batch of the week, find the expected number of times (during each week) that the       #
#       foreman finds a single sheet of paper in the envelope.                                                              #
#                                                                                                                           #
#       Give your answer rounded to six decimal places using the format x.xxxxxx .                                          #
# ------------------------------------------------------------------------------------------------------------------------- #
import time
from fractions import Fraction

def find_expected_env(env, single_sheet_count=0, prob=Fraction(1)):
    sheet_count = sum(env.values())
        
    if sheet_count == env[5]:
        find_expected_env.PROB[single_sheet_count] += prob
        return    

    if sheet_count == 1:
        single_sheet_count += 1

    for s, c in env.items():
        if c == 0:
            continue
        
        new_env = env.copy()
        
        if s == 5: # Found A5
            new_env[5] -= 1
        else:
            new_env[s] -= 1
            for i in range(s + 1, 6):
                new_env[i] += 1

        find_expected_env(new_env, single_sheet_count, prob * Fraction(c, sheet_count))
find_expected_env.PROB = { 0: 0, 1: 0, 2: 0, 3: 0}

def eu151():
    env = { 1: 0, 2: 1, 3: 1, 4: 1, 5: 1}

    find_expected_env(env)
    
    assert(sum([p for v, p in find_expected_env.PROB.items()]) == 1) # Sanity check

    e = sum([v * p for v, p in find_expected_env.PROB.items()])

    return float(round(e, 6))

if __name__ == "__main__":
    startTime = time.clock()
    print (eu151())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
