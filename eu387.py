# -------------------------------------------------------------- Harshad Numbers -------------------------------------------------------------- #
#                                                                                                                                               #
#       A Harshad or Niven number is a number that is divisible by the sum of its digits.                                                       #
#       201 is a Harshad number because it is divisible by 3 (the sum of its digits.)                                                           #
#       When we truncate the last digit from 201, we get 20, which is a Harshad number.                                                         #
#       When we truncate the last digit from 20, we get 2, which is also a Harshad number.                                                      #
#       Let's call a Harshad number that, while recursively truncating the last digit, always results in a Harshad number                       #
#       a right truncatable Harshad number.                                                                                                     #

#       Also:                                                                                                                                   #
#       201/3=67 which is prime.                                                                                                                #
#       Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.                    #

#       Now take the number 2011 which is prime.                                                                                                #
#       When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable.                             #
#       Let's call such primes strong, right truncatable Harshad primes.                                                                        #

#       You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.                                    #

#       Find the sum of the strong, right truncatable Harshad primes less than 10^14.                                                           #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.primes import is_probable_prime

def get_right_truncatable_Harshad_numbers(l):
    harshad = [[(i, i) for i in range(1, 10)]]

    for le in range(1, l):
        harshad.append([])
        for h in harshad[le - 1]:
            for i in range(10):
                harshad_candidate = (10 * h[0] + i, h[1] + i)
                if harshad_candidate[0] % harshad_candidate[1] == 0:
                    harshad[le].append(harshad_candidate)                

    return harshad
    
def eu387():
    MAX_LEN = 14 - 1
    
    rt_harshad = get_right_truncatable_Harshad_numbers(MAX_LEN)
    rt_harshad = [i for l in rt_harshad for i in l]

    srt_harshad = [h for h in rt_harshad if ((h[0] // h[1] != 1) and is_probable_prime(h[0] // h[1]))]

    srt_harshad_primes = []
    for h in srt_harshad:
        for i in [1, 3, 7, 9]:
            srt_harshad_prime_candidate = h[0] * 10 + i
            if is_probable_prime(srt_harshad_prime_candidate):
                srt_harshad_primes.append(srt_harshad_prime_candidate)

    return sum(srt_harshad_primes)

if __name__ == "__main__":
    startTime = time.clock()
    print (eu387())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
