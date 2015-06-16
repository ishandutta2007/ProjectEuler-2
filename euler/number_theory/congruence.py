from .basics import eea as _eea
from operator import add as _add, mul as _mul
from functools import reduce as _reduce

def crt(R, N, view = 0):
    ''' Chinese remainder theorem
        Input: R = Vector of remainders
               N = Vector of modulos
        Output: x = Solution of the system
    '''
    n = _reduce(_mul, N)
        
    M = [int(n/t) for t in N]
    L = [_eea(N[i], M[i])[1] for i in range(0, len(R))]
    C = [R[i]*M[i]*L[i] for i in range(0, len(R))]

    x = _reduce(_add, C) % n
    
    if (view == 1):
        print('The modulo is: {0:10}'.format(n))
        print()
        print('{0:3} {1:15} {2:15} {3:15} {4:15}'.format('i'.rjust(3),'r[i]'.rjust(15),'m[i]'.rjust(15),'l[i]'.rjust(15),'x[i]'.rjust(15)))
        print('---------------------------------------------------------------------')
        for i in range(0, len(R)):
              print('{0:3} {1:15} {2:15} {3:15} {4:15}'.format(str((i + 1)).rjust(3),str(R[i]).rjust(15),str(M[i]).rjust(15),str(L[i]).rjust(15),str(C[i]).rjust(15)))

        print('x = sigma(x[i]) mod {0} = '.format(n))

        sigma = ''
        for i in range(0, len(C) - 1):
            sigma = sigma + str(C[i]) + ' + '

        sigma = sigma + str(C[len(C) - 1]) + ' = ' + str(x)
        print(sigma)
            
    return x

def legendre_symbol(a, p):
    if pow(a, (p - 1) // 2, p) == 1:
        return 1
    else:
        return -1

def Tonelli_Shanks(n, p):
    if legendre_symbol(n, p) != 1:
        return

    # check for immediate solution
    if p % 4 == 3:
        R = pow(n, (p + 1) // 4, p)
        
        return R, p - R
    
    S = 0
    p1 = p - 1
    while (p1 % 2 == 0):
        p1 //= 2
        S += 1
    Q = p1        

    z = 2
    while legendre_symbol(z, p) == 1:
        z += 1

    c = pow(z, Q, p)

    R = pow(n, (Q + 1) // 2, p)
    t = pow(n, Q, p)
    M = S
    
    while True:
        if t == 1:
            return R, p - R

        i = 1
        t_2_i = pow(t, 2, p)
        while (t_2_i != 1):
            i += 1
            t_2_i = pow(t_2_i, 2, p)

        b = pow(c, 2**(M - i - 1), p)
        R = (R * b) % p
        c = pow(b, 2, p)
        t = (t * c) % p
        M = i

