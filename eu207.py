# ------------------------------------------------------- Integer partition equations --------------------------------------------------------- #
#                                                                                                                                               #
#       For some positive integers k, there exists an integer partition of the form   4^t = 2^t + k,                                            #
#       where 4^t, 2^t, and k are all positive integers and t is a real number.                                                                 #
#                                                                                                                                               #
#       The first two such partitions are 4^1 = 2^1 + 2 and 4^1.5849625... = 2^1.5849625... + 6.                                                #
#                                                                                                                                               #
#       Partitions where t is also an integer are called perfect.                                                                               #
#       For any m ≥ 1 let P(m) be the proportion of such partitions that are perfect with k ≤ m.                                                #
#       Thus P(6) = 1/2.                                                                                                                        #
#                                                                                                                                               #
#       In the following table are listed some values of P(m)                                                                                   #
#                                                                                                                                               #
#          P(5) = 1/1                                                                                                                           #
#          P(10) = 1/2                                                                                                                          #
#          P(15) = 2/3                                                                                                                          #
#          P(20) = 1/2                                                                                                                          #
#          P(25) = 1/2                                                                                                                          #
#          P(30) = 2/5                                                                                                                          #
#          ...                                                                                                                                  #
#          P(180) = 1/4                                                                                                                         #
#          P(185) = 3/13                                                                                                                        #
#                                                                                                                                               #
#       Find the smallest m for which P(m) < 1/12345                                                                                            #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time
import math

def P(m):
    m = (-1 + int((1 + 4 * m) ** 0.5)) // 2
   
    return int(math.log(m + 1, 2)) / m

def eu207():
    THRESHOLD = 1 / 12345

    m_plus_1 = 4

    while P(m_plus_1 - 1) >= THRESHOLD:
       m_plus_1 *= 2

    a = m_plus_1 // 2 + 1
    b = m_plus_1 - 1

    while a != b and (a + 1) != b:
       if P((a + b) // 2) >= THRESHOLD:
          a = (a + b) // 2
       else:
          b = (a + b) // 2          

    if P(a) < THRESHOLD:
        return a
    else:
        return a + 1

if __name__ == '__main__':
    startTime = time.clock()
    print (eu207())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
