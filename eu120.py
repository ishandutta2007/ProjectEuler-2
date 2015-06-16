# -------------------------------------------------------------- Square remainders ------------------------------------------------------------ #
#                                                                                                                                               #
#       Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.                                                                        #
#                                                                                                                                               #
#       For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49. And as n varies, so too will r,                              #
#       but for a = 7 it turns out that rmax = 42.                                                                                              #                                                                                                                                            #
#                                                                                                                                               #
#       For 3 ≤ a ≤ 1000, find ∑ rmax.                                                                                                          #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

# [(a−1)^n + (a+1)^n] % a^2 =
#   for even n: 2
#   for odd n: 2an % a^2
# max remainder is when n = (a-1)//2 --> remainder = a^2-a
def get_max_remainder(a):
    return 2*a*((a-1) // 2)
  
def eu120():
    TOP = 1000

    s = 0
    for a in range(3, TOP + 1):
        s += get_max_remainder(a)

    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu120())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
