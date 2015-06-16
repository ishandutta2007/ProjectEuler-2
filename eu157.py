# ---------------------------------- Solving the diophantine equation 1/a + 1/b = p/10^n ---------------------------------- #
#                                                                                                                           #
#       Consider the diophantine equation 1/a+1/b= p/10n with a, b, p, n positive integers and a ≤ b.                       #
#       For n=1 this equation has 20 solutions that are listed below:                                                       #
#                                                                                                                           #
#       1/1+1/1=20/10	    1/1+1/2=15/10	1/1+1/5=12/10	    1/1+1/10=11/10	1/2+1/2=10/10                       #
#       1/2+1/5=7/10	    1/2+1/10=6/10	1/3+1/6=5/10	    1/3+1/15=4/10	1/4+1/4=5/10                        #
#       1/4+1/20=3/10	    1/5+1/5=4/10	1/5+1/10=3/10	    1/6+1/30=2/10	1/10+1/10=2/10                      #
#       1/11+1/110=1/10	    1/12+1/60=1/10	1/14+1/35=1/10	    1/15+1/30=1/10	1/20+1/20=1/10                      #
#                                                                                                                           #
#       How many solutions has this equation for 1 ≤ n ≤ 9?                                                                 #
# ------------------------------------------------------------------------------------------------------------------------- #
import time
from fractions import gcd
from euler.numbers import get_divisors

def sol(n):
    # Check for primitive solutions
    # 1/a + 1/b = 1/10^n
    # 10^n*a + 10^n*b = ab
    # a * (10^n - b) = -10^n*b
    # a = (10^n * b) / (b - 10^n)
    # k => b - 10^n ==> b = k + 10^n
    # a = 10^n + 10^2n / k
    # a<=b ==> k>=10^n AND k|10^2n

    max_num_of_2 = 2 * n
    max_num_of_5 = 2 * n

    k = []
    p2 = 1
    
    for i in range(max_num_of_2 + 1):
        t = p2

        for j in range(max_num_of_5 + 1):
            if t >= pow(10, n):
                k.append(t)

            t *= 5

        p2 *= 2

    k = sorted(k)
    a = [pow(10, n) + pow(10, 2*n) // i for i in k]
    b = [pow(10, n) + i for i in k]

    # Each primitive solution can generate more solutions my multiplication
    g = [gcd(a[i], b[i]) for i in range(len(k))]

    # Num of solutions
    d = [len(get_divisors(g[i])) for i in range(len(g))]
    
    return sum(d)
    
def eu157():
    TOP = 9
    s = 0
    
    for n in range(1, TOP + 1):
        s += sol(n)

    return s

if __name__ == "__main__":
    startTime = time.clock()
    print (eu157())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
