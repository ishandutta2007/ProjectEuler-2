# --------------------------------------------- Special isosceles triangles ------------------------------------------- #
#                                                                                                                       #
#   Consider the isosceles triangle with base length, b = 16, and legs, L = 17.                                         #
#                                                                                                                       #
#   By using the Pythagorean theorem it can be seen that the height of the triangle, h = √(17^2 − 8^2) = 15,            #
#   which is one less than the base length.                                                                             #
#                                                                                                                       #
#   With b = 272 and L = 305, we get h = 273, which is one more than the base length, and this is the second            #
#   smallest isosceles triangle with the property that h = b ± 1.                                                       #
#                                                                                                                       #
#   Find ∑L for the twelve smallest isosceles triangles for which h = b ± 1 and b, L are positive integers.             #
# --------------------------------------------------------------------------------------------------------------------- #
import time
from euler.number_theory.pell import solve_pell_equation

def genSpecialIsoscelesTrianges():
    # x = b / 2
    # h = 2x +- 1
    # 5x^2 +- 4x + 1 = b^2
    # 25x^2 +- 20x + 5 = 5b^2
    # (5x +- 2)^2 - 5b^2 = -1 -> Pell equation

    p = solve_pell_equation(5, -1)
    n = next(p)
    n = next(p) # Skip the n=0 solution
        
    while True:
        if n[0] % 5 == 2: # First type
            b_half = (n[0] - 2) // 5
            h = b_half * 2 + 1
            L = int((b_half * b_half + h * h) ** 0.5) # Calculate the hypotenuse
            yield L
        elif n[0] % 5 == 3: #-2 - Second type
            b_half = (n[0] + 2) // 5
            h = b_half * 2 - 1
            L = int((b_half * b_half + h * h) ** 0.5) # Calculate the hypotenuse
            yield L
            
        n = next(p)

def eu138():
    N = 12

    s = 0
    g = genSpecialIsoscelesTrianges()
    for i in range(N):
        s += next(g)

    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu138())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
