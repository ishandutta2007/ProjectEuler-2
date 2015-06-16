# ----------------------------------------------------------- Arithmetic expressions ---------------------------------------------------------- #
#                                                                                                                                               #
#       By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /)     #
#       and brackets/parentheses, it is possible to form different positive integer targets.                                                    #
#                                                                                                                                               #
#       For example,                                                                                                                            #
#                                                                                                                                               #
#                       8 = (4 * (1 + 3)) / 2                                                                                                   #
#                       14 = 4 * (3 + 1 / 2)                                                                                                    #
#                       19 = 4 * (2 + 3) − 1                                                                                                    #
#                       36 = 3 * 4 * (2 + 1)                                                                                                    #
#                                                                                                                                               #
#       Note that concatenations of the digits, like 12 + 34, are not allowed.                                                                  #
#                                                                                                                                               #
#       Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum,                   #
#       and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.                                   #
#                                                                                                                                               #
#       Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers,                        #
#       1 to n, can be obtained, giving your answer as a string: abcd.                                                                          #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import itertools
import operator

def getArithmeticExpressions(s):
    ret = []
    per = list(itertools.permutations(s))
    
    for p in per:
        for o in getArithmeticExpressions.OPERATORS_SET:
            try: # e1: _ _ _ _ . . .
                e = o[2](p[0],o[1](p[1],o[0](p[2],p[3])))
                if (e == int(e) and e > 0):
                    ret.extend([e])
            except ZeroDivisionError:
                pass

            try: # e2: _ _ . _ . _ .
                e = o[2](o[1](o[0](p[0],p[1]),p[2]),p[3])
                if (e == int(e) and e > 0):
                    ret.extend([e])
            except ZeroDivisionError:
                pass

            try: # e3: _ _ _ . _ . .
                e = o[2](p[0],o[1](o[0](p[1],p[2]),p[3]))
                if (e == int(e) and e > 0):
                    ret.extend([e])
            except ZeroDivisionError:
                pass

            try: # e4: _ _ _ . . _ .
                e = o[2](o[1](p[0], o[0](p[1],p[2])),p[3])
                if (e == int(e) and e > 0):
                    ret.extend([e])
            except ZeroDivisionError:
                pass

            try: # e5: _ _ . _ _ . .
                e = o[2](o[0](p[0],p[1]), o[1](p[2],p[3]))
                if (e == int(e) and e > 0):
                    ret.extend([e])
            except ZeroDivisionError:
                pass

    ret = list(set(ret))
    for i in range(len(ret)):
        if (ret[i] != i + 1):
            break

    return i
getArithmeticExpressions.OPERATORS = [operator.add, operator.sub, operator.mul, operator.truediv]
getArithmeticExpressions.OPERATORS_SET = [(o1, o2, o3) for o1 in getArithmeticExpressions.OPERATORS
                                                       for o2 in getArithmeticExpressions.OPERATORS
                                                       for o3 in getArithmeticExpressions.OPERATORS]

def eu93():
    m = 0
    abcd = 0

    for digits in itertools.combinations([i for i in range(1, 10)], 4):
        s = getArithmeticExpressions(digits)
        if (s > m):
            m = s
            abcd = "".join([str(d) for d in digits])
    
    return abcd

if __name__ == "__main__":
    startTime = time.clock()
    print (eu93())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
