# -------------------------------------------------------- Perfect right-angled triangles ----------------------------------------------------- #
#                                                                                                                                               #
#       Consider the right angled triangle with sides a=7, b=24 and c=25. The area of this triangle is 84,                                      #
#       which is divisible by the perfect numbers 6 and 28.                                                                                     #
#       Moreover it is a primitive right angled triangle as gcd(a,b)=1 and gcd(b,c)=1.                                                          #
#       Also c is a perfect square.                                                                                                             #
#                                                                                                                                               #
#       We will call a right angled triangle perfect if                                                                                         #
#       -it is a primitive right angled triangle                                                                                                #
#       -its hypotenuse is a perfect square                                                                                                     #
#                                                                                                                                               #
#       We will call a right angled triangle super-perfect if                                                                                   #
#       -it is a perfect right angled triangle and                                                                                              #
#       -its area is a multiple of the perfect numbers 6 and 28.                                                                                #
#                                                                                                                                               #
#       How many perfect right-angled triangles with c≤1016 exist that are not super-perfect?                                                   #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def eu218():
    # https://luckytoilet.wordpress.com/2010/06/20/on-some-number-theoretic-properties-of-right-triangles-project-euler-218/
    # Mathematical proof
    return 0

if __name__ == '__main__':
    startTime = time.clock()
    print (eu218())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
