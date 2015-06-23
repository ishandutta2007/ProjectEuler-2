# ---------------------------------------------------- Polynomials of Fibonacci numbers ------------------------------------------------------- #
#                                                                                                                                               #
#       The Fibonacci numbers {f_n, n ≥ 0} are defined recursively as f_n = f_n-1 + f_n-2 with base cases f_0 = 0 and f_1 = 1.                  #
#                                                                                                                                               #
#       Define the polynomials {F_n, n ≥ 0} as Fn(x) = ∑f_i*x^i for 0 ≤ i ≤ n.                                                                  #
#                                                                                                                                               #
#       For example, F_7(x) = x + x^2 + 2x^3 + 3x^4 + 5x^5 + 8x^6 + 13x^7, and F_7(11) = 268357683.                                             #
#                                                                                                                                               #
#       Let n = 10^15. Find the sum [∑0≤x≤100 F_n(x)] mod 1307674368000 (= 15!).                                                                #
# --------------------------------------------------------------------------------------------------------------------------------------------- #
import time

def mat_pow_mod(A, e, m):
    def identity_mat():
        C = [[0 for j in range(l)] for i in range(l)]

        for i in range(l):
            C[i][i] = 1

        return C
        
    def mat_mult_mod(A, B, m):
        C = [[0 for j in range(l)] for i in range(l)]

        for i in range(l):
            for j in range(l):
                for k in range(l):
                    C[i][j] += A[i][k] * B[k][j]

                C[i][j] %= m
        return C

    l = len(A)
    i = identity_mat()
    
    while e:
        if e % 2 == 1:
            i = mat_mult_mod(A, i, m)

        e //= 2
        A = mat_mult_mod(A, A, m)

    return i

def Fib_mod(n, m):
    if n == 0:
        return 0
    
    return mat_pow_mod([[1, 1], [1, 0]], n - 1, m)[0][0]

def F(n, x, m):
    # bla bla
    D = x * x + x - 1
    N = (Fib_mod(n, m * D) * pow(x, n + 2, m * D) + Fib_mod(n + 1, m * D) * pow(x, n + 1, m * D) - x) % (m * D)

    return (N // D)
    
def eu435():
    # Look problem 137.
    # F_n(x) = [f_n*x^(n+2) + f_n+1*x^(n+1) - x] / (x^2 + x - 1)

    TOP = 100
    N = 10 ** 15
    MODULO = 1307674368000
    
    return sum([F(N, i, MODULO) for i in range(TOP + 1)]) % MODULO

if __name__ == '__main__':
    startTime = time.clock()
    print (eu435())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
