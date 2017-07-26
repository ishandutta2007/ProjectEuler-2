# --------------------------------------------------------- Problem 607 ----------------------------------------------------------------------- #
#                                                                                                                                               #
#       Frodo and Sam need to travel 100 leagues due East from point A to point B. On normal terrain, they can cover 10 leagues per day,        #
#       and so the journey would take 10 days. However, their path is crossed by a long marsh which runs exactly South-West to North-East,      #
#       and walking through the marsh will slow them down. The marsh is 50 leagues wide at all points, and the mid-point of AB is located       #
#       in the middle of the marsh. A map of the region is shown in the diagram below:                                                          #
#                                                                                                                                               #
#       The marsh consists of 5 distinct regions, each 10 leagues across, as shown by the shading in the map.                                   #
#       The strip closest to point A is relatively light marsh, and can be crossed at a speed of 9 leagues per day.                             #
#       However, each strip becomes progressively harder to navigate, the speeds going down to 8, 7, 6 and finally 5 leagues per day            #
#       for the final region of marsh, before it ends and the terrain becomes easier again, with the speed going back to 10 leagues per day.    #
#                                                                                                                                               #
#       If Frodo and Sam were to head directly East for point B, they would travel exactly 100 leagues, and the journey would                   #
#       take approximately 13.4738 days. However, this time can be shortened if they deviate from the direct path.                              #
#                                                                                                                                               #
#       Find the shortest possible time required to travel from point A to B, and give your answer in days, rounded to 10 decimal places.       #                                                                                  #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from scipy.optimize import fsolve
import math
from decimal import *
    
def lagrange_lambda(x):
    a = [(50 / (2**0.5)) - 25, 10, 10, 10, 10, 10, (50 / (2**0.5)) - 25]
    v = [10, 9, 8, 7, 6, 5, 10]
    v = [vv / 10.0 for vv in v]
    h = 100 / (2**0.5)

    t = 0 - h
    for i in range(7):
        t += (a[i] * x * v[i]) / ( (1 - (x**2 * v[i]**2))**0.5 )
    
    return t

def eu607():
    lambda0 = fsolve(lagrange_lambda, 0.8)
    T = Decimal(lambda0[0])
    getcontext().prec=100
    
    a = [ (50 / (2**0.5)) - 25, 10, 10, 10, 10, 10,  (50 / (2**0.5)) - 25]
    v = [1,0.9,0.8,0.7,0.6,0.5,1]
    phi = [math.asin(T * Decimal(vv)) for vv in v]
    
    t = []
    for i in range(len(v)):
        t.append(a[i] / (math.cos(phi[i])*10*v[i]))

    return sum(t)

if __name__ == '__main__':
    startTime = time.clock()
    print (eu607())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
