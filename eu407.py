# ------------------------------------------------ Idempotents ------------------------------------------------ #
#                                                                                                               #
#       If we calculate a^2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.                                            #
#                                                                                                               #
#       The largest value of a such that a^2 ≡ a mod 6 is 4.                                                    #
#       Let's call M(n) the largest value of a < n such that a^2 ≡ a (mod n).                                   #
#       So M(6) = 4.                                                                                            #
#                                                                                                               #
#       Find ∑M(n) for 1 ≤ n ≤ 10^7.                                                                            #
# ------------------------------------------------------------------------------------------------------------- #
import time

def max_idempotent(n):
    for i in range(n - 1, -1, -1):
        if i*i % n == i:
            return i

def eu407():
    for p in range(1, 100):
        print (p, max_idempotent(p))

    return

if __name__ == "__main__":
    startTime = time.clock() 
    print (eu407())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
