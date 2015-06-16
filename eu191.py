# ------------------------------------------------ Prize Strings ---------------------------------------------- #
#                                                                                                               #
#       A particular school offers cash rewards to children with good attendance and punctuality.               #
#       If they are absent for three consecutive days or late on more than one occasion then they               #
#       forfeit their prize.                                                                                    #
#                                                                                                               #
#       During an n-day period a trinary string is formed for each child consisting of L's (late),              #
#       O's (on time), and A's (absent).                                                                        #
#                                                                                                               #
#       Although there are eighty-one trinary strings for a 4-day period that can be formed,                    #
#       exactly forty-three strings would lead to a prize:                                                      #
#                                                                                                               #
#                               OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA                               #
#                               OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO                               #
#                               AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL                               #
#                               AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA                               #
#                               LAOO LAOA LAAO                                                                  #
#                                                                                                               #
#       How many "prize" strings exist over a 30-day period?                                                    #
# ------------------------------------------------------------------------------------------------------------- #
import time
from math import pow

def F(n):
    if (n <= 0):
        return 1
    
    if (not n in F.MEMORY):
        F.MEMORY[n] = F(n - 1) + F(n - 2) + F(n - 3)
    
    return F.MEMORY[n]
F.MEMORY = {1: 2, 2: 4, 3: 7}

def eu191():
    PERIOD = 30

    c = F(PERIOD)

    for i in range(PERIOD):
        c += F(i) * F(PERIOD - 1 - i)

    return c

if __name__ == "__main__":
    startTime = time.clock()
    print (eu191())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
