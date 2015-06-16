# --------------------------------- Number letter counts ---------------------------------- #
#                                                                                           #
#       If the numbers 1 to 5 are written out in words: one, two, three, four, five,        #
#           then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.                    #
#       If all the numbers from 1 to 1000 (one thousand) inclusive were written out         #
#           in words, how many letters would be used?                                       #
#                                                                                           #
#       NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)#
#           contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.      #
#           The use of "and" when writing out numbers is in compliance with British usage.  #
# ----------------------------------------------------------------------------------------- #
import time
import math

def eu17():
    d = { 0: 0,
          1: 3,
          2: 3,
          3: 5,
          4: 4,
          5: 4,
          6: 3,
          7: 5,
          8: 5,
          9: 4,
          10: 3,
          11: 6,
          12: 6,
          13: 8,
          14: 8,
          15: 7,
          16: 7,
          17: 9,
          18: 8,
          19: 8,
          20: 6,
          30: 6,
          40: 5,
          50: 5,
          60: 5,
          70: 7,
          80: 6,
          90: 6,
          100: 7,
          1000: 8}
    
    c = 0
    for n in range(1, 1000 + 1):
        n_org = n
        d4 = n_org % 10
        n_org //= 10
        d3 = n_org % 10
        n_org //= 10
        d2 = n_org % 10
        n_org //= 10
        d1 = n_org % 10

        t = 0
        t += d[d1] + d[1000] if d1 != 0 else 0
        t += d[d2] + d[100] if d2 != 0 else 0
        t += 3 if d2 != 0 and (d3 + d4 != 0) else 0 # for the word "and"
        t += d[d3 * 10 + d4] if d3 == 1 else d[d3 * 10] + d[d4]

        c += t

    return c
        

startTime = time.clock()
print (eu17())
elapsedTime = time.clock() - startTime
print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
