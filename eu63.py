# ----------------------------------------- Powerful digit counts --------------------------------------------- #
#                                                                                                               #
#       The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9,     #
#       is a ninth power.                                                                                       #
#                                                                                                               #
#       How many n-digit positive integers exist which are also an nth power?                                   #
# ------------------------------------------------------------------------------------------------------------- #
import time
import math

# 10^(n-1)=x^n => 0.1*10^n=x^n => log(0.1)+n*log(10)=n*log(x) 
# => log(10)=n*(log(10)-log(x)) => n=log(10)/(log(10)-log(x))
def eu63():
    s = 0

    for i in range(1, 10): # x^n < 10^n => x < 10
        s += math.floor(math.log(10)/(math.log(10)-math.log(i)))
        
    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu63())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
