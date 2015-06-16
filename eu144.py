# --------------------------- Investigating multiple reflections of a laser beam -------------------------- #
#                                                                                                           #
#       In laser physics, a "white cell" is a mirror system that acts as a delay line for the laser beam.   #
#       The beam enters the cell, bounces around on the mirrors, and eventually works its way back out.     #
#                                                                                                           #
#       The specific white cell we will be considering is an ellipse with the equation 4x2 + y2 = 100       #
#                                                                                                           #
#       The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, allowing the light            #
#       to enter and exit through the hole.                                                                 #
#                                                                                                           #
#       The light beam in this problem starts at the point (0.0,10.1) just outside the white cell,          #
#       and the beam first impacts the mirror at (1.4,-9.6).                                                #
#                                                                                                           #
#       Each time the laser beam hits the surface of the ellipse, it follows the usual law of reflection    #
#       "angle of incidence equals angle of reflection." That is, both the incident and reflected beams     #
#       make the same angle with the normal line at the point of incidence.                                 #
#                                                                                                           #
#       In the figure on the left, the red line shows the first two points of contact between the laser     #
#       beam and the wall of the white cell; the blue line shows the line tangent to the ellipse at         #
#       the point of incidence of the first bounce.                                                         #
#                                                                                                           #
#       The slope m of the tangent line at any point (x,y) of the given ellipse is: m = −4x/y               #
#                                                                                                           #
#       The normal line is perpendicular to this tangent line at the point of incidence.                    #
#                                                                                                           #
#       The animation on the right shows the first 10 reflections of the beam.                              #
#                                                                                                           #
#       How many times does the beam hit the internal surface of the white cell before exiting?             #
# --------------------------------------------------------------------------------------------------------- #
import time
import math

# See eu144.doc for mathematical explanation
def eu144():
    r = 0

    x0, y0, x1, y1 = 0.0, 10.1, 1.4, -9.6
    eps = 0.01

    while True:
        mt = (-4 * x1) / y1
        mn = -1 / mt

        mi = (y1 - y0) / (x1 - x0)
        mr = (2 + mi * (mn + mt)) / (2 * mi - (mn + mt))

        x2 = (-2 * mr * y1 - x1 * (4 - mr ** 2)) / (4 + mr ** 2)
        y2 = (y1 * (4 - mr ** 2) - 8 * x1 * mr) / (4 + mr ** 2)

        x0, y0, x1, y1, r = x1, y1, x2, y2, r+1
        
        if -eps <= x2 <= eps and y2 > 0:
            return r
    
def eu144_visualization():
    import matplotlib.pyplot as plt
    from matplotlib.patches import Ellipse
    import numpy

    ellipse = Ellipse(xy=(0, 0), width=10, height=20, angle=0, color='red')

    fig = plt.figure()

    ax = fig.add_subplot(111, aspect='equal')

    ax.add_artist(ellipse)   

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    x0, y0, x1, y1 = 0.0, 10.1, 1.4, -9.6
    lines, = ax.plot([x0, x1], [y0,y1], color='black')

    fig.show()

    while True:
        mt = (-4 * x1) / y1
        mn = -1 / mt

        lines.set_xdata(numpy.append(lines.get_xdata(), x1))
        lines.set_ydata(numpy.append(lines.get_ydata(), y1))
        plt.draw()
        
        mi = (y1 - y0) / (x1 - x0)
        mr = (2 + mi * (mn + mt)) / (2 * mi - (mn + mt))

        x2 = (-2 * mr * y1 - x1 * (4 - mr ** 2)) / (4 + mr ** 2)
        y2 = (y1 * (4 - mr ** 2) - 8 * x1 * mr) / (4 + mr ** 2)

        x0, y0, x1, y1 = x1, y1, x2, y2
        
if __name__ == "__main__":
    startTime = time.clock()
    print (eu144())
    #print (eu144_visualization())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
