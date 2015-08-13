# ------------------------------------------------------ Exploring Pascal's triangle ---------------------------------------------------------- #
#                                                                                                                                               #
#       We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:                          #
#                                                                                                                                               #
#                                                                1                                                                              #
#        	 	 	 	 	         1	 	 1                                                                      #
#        	 	                         1	 	 2	 	 1                                                              #
#        	 	 	        1	 	 3	 	 3	 	 1                                                      #
#        	 	         1	 	 4	 	 6	 	 4	 	 1                                              #
#        	        1	 	5	 	10	 	10	 	 5	 	 1                                      #
#               1	 	 6	 	15	 	20	 	15	 	 6	 	 1                              #
#                                                                                                                                               #
#       However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.                #
#                                                                                                                                               #
#       Find the number of entries which are not divisible by 7 in the first one billion (109) rows of Pascal's triangle.                       #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.numbers import to_base
    
def eu148():
    TOP = 10 ** 9

    f = sum([(i + 1) for i in range(7)])

    b = to_base(TOP, 7)
    c = 1
    s = 0
    
    for i in range(len(b)):
        d = int(b[i])
        r = sum([(t + 1) for t in range(d)])

        s += c * r * (f ** (10 - i))
        c *= (d + 1)
        
    return s

if __name__ == '__main__':
    startTime = time.clock()
    print (eu148())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
