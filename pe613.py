# --------------------------------------------------------- Problem 613 ----------------------------------------------------------------------- #
#                                                                                                                                               #
#       Dave is doing his homework on the balcony and, preparing a presentation about Pythagorean triangles, has just cut out a triangle		#
#	 	with side lengths 30cm, 40cm and 50cm from some cardboard, when a gust of wind blows the triangle down into the garden.					#
#       Another gust blows a small ant straight onto this triangle. The poor ant is completely disoriented and starts to crawl straight ahead	#
#		in random direction in order to get back into the grass.																				#
#                                                                                                                                               #
#       Assuming that all possible positions of the ant within the triangle and all possible directions of moving on are equiprobable, 			#
#		what is the probability that the ant leaves the triangle along its longest side?														#
#       Give your answer rounded to 10 digits after the decimal point.       																	#
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

import math
from scipy import integrate


def f(y, x):
	a_s = (x-3)**2 + y**2
	b_s = x**2 + (y-4)**2
	c_s = 25

	r = (a_s + b_s - c_s) / (2 * (a_s*b_s)**0.5)

	if r < -1 or r > 1:
		return 0

	return math.acos( r )  / (12 * math.pi)

def f1(y, x):
	return ((3 * math.pi / 2) - math.atan( (3-x) / y ) - math.atan( (4-y) / x )) / (12 * math.pi)

def eu613():
	print round(integrate.dblquad(f, 0, 3, lambda x: 0, lambda x: 4 - 4.0 * x / 3)[0], 10)
	#print round(integrate.dblquad(f1, 0, 3, lambda x: 0, lambda x: 4 - 4.0 * x / 3)[0], 10)

if __name__ == '__main__':
	startTime = time.clock()
    print (eu613())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")