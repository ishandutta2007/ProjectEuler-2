# --------------------------------------------------------------- Primonacci ------------------------------------------------------------------ #
#                                                                                                                                               #
#       For any positive integer n the function next_prime(n) returns the smallest prime p                                                      #
#       such that p>n.                                                                                                                          #
#                                                                                                                                               #
#       The sequence a(n) is defined by:                                                                                                        #
#       a(1)=next_prime(10^14) and a(n)=next_prime(a(n-1)) for n>1.                                                                             #
#                                                                                                                                               #
#       The fibonacci sequence f(n) is defined by: f(0)=0, f(1)=1 and f(n)=f(n-1)+f(n-2) for n>1.                                               #
#                                                                                                                                               #
#       The sequence b(n) is defined as f(a(n)).                                                                                                #
#                                                                                                                                               #
#       Find ∑b(n) for 1≤n≤100 000. Give your answer mod 1234567891011.                                                                         #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

from euler.primes import next_prime

def fib_mod(n, mod):
    def mat_mul_mod(mat_a, mat_b, mod):
        mat_c = [[0 for _ in range(len(mat_a))] for _ in range(len(mat_b[0]))]

        for i in range(len(mat_a)):
            for j in range(len(mat_b[0])):
                s = 0
                for k in range(len(mat_a[0])):
                    s += mat_a[i][k] * mat_b[k][j]
                mat_c[i][j] = s % mod

        return mat_c
    
    def mat_exp_mod(mat, e, mod):
        ret = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(ret)):
            ret[i][i] = 1

        while e:
            if e % 2 == 1:
                ret = mat_mul_mod(ret, mat, mod)

            mat = mat_mul_mod(mat, mat, mod)
            e //= 2
            
        return ret

    m = [[1, 1], [1, 0]]
        
    return mat_exp_mod(m, n, mod)[1][0]
    
def eu304():
    START = 10 ** 14
    MODULO = 1234567891011

    primes = [next_prime(START)]
    for i in range(100000 - 1):
        primes.append(next_prime(primes[-1]))

    s = 0

    fib_l = fib_mod(START, MODULO)
    fib_n = fib_mod(START + 1, MODULO)
    i = START + 1
    
    for p in primes:
        while i < p:
            fib_l, fib_n = fib_n, (fib_l + fib_n) % MODULO
            i += 1

        s += fib_n
        
    return s % MODULO

if __name__ == '__main__':
    startTime = time.clock()
    print (eu304())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
