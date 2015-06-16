# ---------------------------------------------------- An amazing Prime-generating Automaton -------------------------------------------------- #
#                                                                                                                                               #
#       A program written in the programming language Fractran consists of a list of fractions.                                                 #
#                                                                                                                                               #
#       The internal state of the Fractran Virtual Machine is a positive integer, which is initially set to a seed value.                       #
#       Each iteration of a Fractran program multiplies the state integer by the first fraction in the list which will leave it an integer.     #
#                                                                                                                                               #
#       For example, one of the Fractran programs that John Horton Conway wrote for prime-generation consists of the following 14 fractions:    #
#                                                                                                                                               #
#                       17/91, 78/85, 19/51, 23/38, 29/33, 77/29, 95/23, 77/19, 11/17, 11/13, 13/11, 15/2, 1/7, 55/1                            #
#                                                                                                                                               #
#       Starting with the seed integer 2, successive iterations of the program produce the sequence:                                            #
#                                                                                                                                               #
#                       15, 825, 725, 1925, 2275, 425, ..., 68, 4, 30, ..., 136, 8, 60, ..., 544, 32, 240, ...                                  #
#                                                                                                                                               #
#       The powers of 2 that appear in this sequence are 2^2, 2^3, 2^5, ...                                                                     #
#       It can be shown that all the powers of 2 in this sequence have prime exponents and that all the primes appear as exponents              #
#       of powers of 2, in proper order!                                                                                                        #
#                                                                                                                                               #
#       If someone uses the above Fractran program to solve Project Euler Problem 7 (find the 10001st prime), how many iterations would be      #
#       needed until the program produces 2^10001st prime ?                                                                                     #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from fractions import gcd

def gen_Fractran(seed):
    n = seed

    while True:
        i = 0
        while n % gen_Fractran.list[i][1] != 0:
            i += 1

        n = (n * gen_Fractran.list[i][0]) // gen_Fractran.list[i][1]
        yield n
gen_Fractran.list = [(17, 91), (78, 85), (19, 51), (23, 38), (29, 33), (77, 29), (95, 23), \
                     (77, 19), (1, 17), (11,13), (13, 11), (15, 2), (1, 7), (55, 1)]

def eu308():
    TARGET = 10001
    
    s = 1
    v2 = 1
    v3 = v5 = v7 = 0

    t = 0
    p = 0
    
    while True:
        if s == 1: # A
            t += 3 * v2 + v7 + 2 # Jump over state B
            t += 1 # Jump to state D
            
            v7 = v2 - 1
            v3 = 0
            v5 += v2 + 1

            v2 = 0
            
            s = 4 # D

            continue
        
        elif s == 3: # C
            if v7 == 0:
                t += (2 * v3) + 2
                v7 = v3
                v3 = 0
                
            v7 -= 1
            t += 1

            s = 4 # D
            continue

        elif s == 4: # D
            # Skip over C
            if v5 > 0:
                if v7 >= v5 or v7 < 0:
                    v7 -= v5
                    v2 += v5
                    v3 += v5
                    t += 2 * v5
                    v5 = 0
                    
                    continue
                elif v5 > v7 and v7 > 0:
                    v5 -= v7 + 1
                    v2 += v7 + 1
                    v3 += v7 + 1
                    t += 2 * v7 + 2 * v3 + 4
                    v7 = v3 - 1
                    v3 = 0

                    continue
                else: # v7 == 0
                    v5 -= 1
                    v2 += 1
                    v3 += 1
                
                    s = 3 # C
                    t += 1
            elif v3 > 0:
                v3 -= 1

                # Jump over state E and B to C
                t += (2 * v2) + (2 * v3) + 1 + 1
                v5 += v2
                v2 = 0
                v7 += v3 + 1
                v3 = 0
                
                s = 3 # C
                t += 1

            else:
                s = 1 # A
                if (v7 == 0):
                    p += 1
                    #print (v2, v3, v5, v7, t + 1, "S=", s)

                    if p == TARGET:
                        return t + 1
                t += 1

            continue                

"""    # Original "state chart"
    while True:
        if s == 1: # A
            if v2 > 0:
                t += v2
                v3 += v2
                v5 += v2
                v2 = 0

            if v7 > 0:
                t += v7
                v7 = 0               

            v5 += 1
            t += 1
    
            s = 2 # B
            continue

        elif s == 2: # B
            if v3 > 0:
                v7 += v3
                t += (2 * v3)
                v3 = 0

            t += 1
            
            s = 3 # C
            continue
        
        elif s == 3: # C
            if v7 > 0:
                v7 -= 1

                s = 4 # D
                
            else:
                s = 2 # B

            t += 1
            
            continue

        elif s == 4: # D
            if v5 > 0:
                v5 -= 1
                v2 += 1
                v3 += 1
                
                s = 3 # C
            elif v3 > 0:
                v3 -= 1
                
                s = 5 # E

            else:
                s = 1 # A
                if (v7 == 0):
                    print (v2, v3, v5, v7, t + 1, "S=", s)

            t += 1
            continue

        elif s == 5: # E
            if v2 > 0:
                v5 += v2
                t += (2 * v2)
                v2 = 0

            v7 += 1
            t += 1

            s = 2 # B
            continue"""
        
if __name__ == "__main__":
    startTime = time.clock()
    print (eu308())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
