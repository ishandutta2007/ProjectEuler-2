# ------------------------------------------------------------- Digital root clocks ----------------------------------------------------------- #
#                                                                                                                                               #
#                                               See https://projecteuler.net/problem=315 for images                                             #
#                                                                                                                                               #
#       Sam and Max are asked to transform two digital clocks into two "digital root" clocks.                                                   #
#       A digital root clock is a digital clock that calculates digital roots step by step.                                                     #
#                                                                                                                                               #
#       When a clock is fed a number, it will show it and then it will start the calculation,                                                   #
#       showing all the intermediate values until it gets to the result.                                                                        #
#       For example, if the clock is fed the number 137, it will show: "137" → "11" → "2" and then it will go black,                            #
#       waiting for the next number.                                                                                                            #
#                                                                                                                                               #
#       Every digital number consists of some light segments: three horizontal (top, middle, bottom) and four vertical                          #
#       (top-left, top-right, bottom-left, bottom-right).                                                                                       #
#       Number "1" is made of vertical top-right and bottom-right, number "4" is made by middle horizontal and vertical top-left,               #
#       top-right and bottom-right. Number "8" lights them all.                                                                                 #
#                                                                                                                                               #
#       The clocks consume energy only when segments are turned on/off.                                                                         #
#       To turn on a "2" will cost 5 transitions, while a "7" will cost only 4 transitions.                                                     #
#                                                                                                                                               #
#       Sam and Max built two different clocks.                                                                                                 #
#                                                                                                                                               #
#       Sam's clock is fed e.g. number 137: the clock shows "137", then the panel is turned off, then the next number ("11") is turned on,      #
#       then the panel is turned off again and finally the last number ("2") is turned on and, after some time, off.                            #
#       For the example, with number 137, Sam's clock requires:                                                                                 #
#       "137"	:	(2 + 5 + 4) × 2 = 22 transitions ("137" on/off).                                                                        #
#       "11"	:	(2 + 2) × 2 = 8 transitions ("11" on/off).                                                                              #
#       "2"	:	(5) × 2 = 10 transitions ("2" on/off).                                                                                  #
#       For a grand total of 40 transitions.                                                                                                    #
#                                                                                                                                               #
#       Max's clock works differently. Instead of turning off the whole panel,                                                                  #
#       it is smart enough to turn off only those segments that won't be needed for the next number.                                            #
#       For number 137, Max's clock requires:                                                                                                   #
#       "137"   :   2 + 5 + 4 = 11 transitions ("137" on)                                                                                       #
#                   7 transitions (to turn off the segments that are not needed for number "11").                                               #
#       "11"    :   0 transitions (number "11" is already turned on correctly)                                                                  #
#                   3 transitions (to turn off the first "1" and the bottom part of the second "1";                                             #
#                   the top part is common with number "2").                                                                                    #
#       "2"     :   4 transitions (to turn on the remaining segments in order to get a "2")                                                     #
#                   5 transitions (to turn off number "2").                                                                                     #
#       For a grand total of 30 transitions.                                                                                                    #
#                                                                                                                                               #
#       Of course, Max's clock consumes less power than Sam's one.                                                                              #
#       The two clocks are fed all the prime numbers between A = 10^7 and B = 2×10^7.                                                           #
#       Find the difference between the total number of transitions needed by Sam's clock and that needed by Max's one.                         #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.primes import prime_sieve
from euler.numbers import digital_root_consecutive

def Sam_number_cost(segments, n):
    digits = [int(d) for d in str(n)]

    return 2 * sum([len(segments[d]) for d in digits])

def Max_number_cost(segments, n1, n2):    
    digits = [int(d) for d in str(n1)]
    
    intersecting_count = 0
    if n2 != None:
        assert (n2 < n1) # Sanity check
        while n2 != 0:
            intersecting_count += len(segments[n1 % 10] & segments[n2 % 10])
            n1 //= 10
            n2 //= 10

    return 2 * (sum([len(segments[d]) for d in digits]) - intersecting_count)

def eu315():
    A = 10 ** 7
    B = 2 * (10 ** 7)

    primes = [p for p in prime_sieve(B) if p > A]
    segments = { 0: frozenset([1, 2, 3, 4, 5, 6]),
                 1: frozenset([2, 3]),
                 2: frozenset([1, 2, 4, 5, 7]),
                 3: frozenset([1, 2, 3, 4, 7]),
                 4: frozenset([2, 3, 6, 7]),
                 5: frozenset([1, 3, 4, 6, 7]),
                 6: frozenset([1, 3, 4, 5, 6, 7]),
                 7: frozenset([1, 2, 3, 6]),
                 8: frozenset([1, 2, 3, 4, 5, 6, 7]),
                 9: frozenset([1, 2, 3, 4, 6, 7]) }

    max_digital_sum = (len(str(B)) - 1) * 9 + (int(str(B)[0]) if str(B)[-1] != '0' else (int(str(B)[0]) - 1))

    sam_c = [0 for i in range(max_digital_sum + 1)]
    max_c = [0 for i in range(max_digital_sum + 1)]

    for i in range(1, 10):
        sam_c[i] = Sam_number_cost(segments, i)
        max_c[i] = Max_number_cost(segments, i, None)

    for i in range(10, max_digital_sum + 1):
        sam_c[i] = Sam_number_cost(segments, i) + sam_c[digital_root_consecutive(i)]
        max_c[i] = Max_number_cost(segments, i, digital_root_consecutive(i)) + max_c[digital_root_consecutive(i)]

    diff = 0
    for p in primes:
        diff += (Sam_number_cost(segments, p) + sam_c[digital_root_consecutive(p)]) - \
                (Max_number_cost(segments, p, digital_root_consecutive(p)) + max_c[digital_root_consecutive(p)])
        
    return diff
        
if __name__ == "__main__":
    startTime = time.clock()
    print (eu315())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
