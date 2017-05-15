# --------------------------------------------------------- Problem 601 ----------------------------------------------------------------------- #
#                                                                                                                                               #
#       For every positive number nn we define the function streak(n)=kstreak(n)=k as the smallest positive integer k such that n+k             #
#       is not divisible by k+1.                                                                                                                #
#       E.g:                                                                                                                                    #
#       13 is divisible by 1                                                                                                                    #
#       14 is divisible by 2                                                                                                                    #
#       15 is divisible by 3                                                                                                                    #
#       16 is divisible by 4                                                                                                                    # 
#       17 is NOT divisible by 5                                                                                                                #
#       So streak(13)=4.                                                                                                                        #
#       Similarly:                                                                                                                              #
#       120 is divisible by 1                                                                                                                   #
#       121 is NOT divisible by 2                                                                                                               #
#       So streak(120)=1streak(120)=1.                                                                                                          #
#                                                                                                                                               #
#       Define P(s,N) to be the number of integers nn, 1<n<N, for which streak(n)=s.                                                            #
#       So P(3,14)=1 and P(6,106)=14286.                                                                                                        #
#                                                                                                                                               #
#       Find the sum, as ii ranges from 1 to 31, of P(i,4**i).                                                                                  #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def gcd(a, b):
    if b > a:
        return gcd(b, a)
        
    if b == 0:
        return a
        
    return gcd(b, a % b)
    
def lcm(a, b):
    return a * b // gcd(a, b)
        
        
def eu601():
    TOP = 31

    l = 1
    s = 0
    
    for i in range(1, TOP + 1):
        l = lcm(l, i)
        s += (4 ** i - 2) // l - (4 ** i - 2) // lcm(l, i + 1)        
    
    return s

if __name__ == '__main__':
    startTime = time.clock()
    print (eu601())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
