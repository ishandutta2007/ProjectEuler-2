import math
import random
import operator
import functools

def gcd(a, b, view = 0):
    if (view == 1):
            print('GCD({0:10}, {1:10})'.format(str(a).rjust(10),str(b).rjust(10)))
            
    if (b == 0):
        return a
    else:
        return gcd(b, a % b,view)

def eea(a, b, view = 0, returnConvergent = 0):
    ''' Extended Euclidean Algorithm

        Input: (a,b) - Integers
               view - 0 = No view, 1 = Table, 2 = Iterations
        Output: (d,x,y,c)
                 d   - GCD(a,b)
                 x,y - ax + by = d
                 c   - if (y < 0) = a - y 
    '''


    if (view == 1):
        print('{0:3} {1:20} {2:5} {3:20} {4:20}'.format('i'.rjust(3),'r[i]'.rjust(20),'q[i]'.rjust(5),'x[i]'.rjust(20),'y[i]'.rjust(20)))
        print('----------------------------------------------------------------------------------------')
        
    r = {-1:a, 0:b}
    x = {-1:1, 0:0}
    y = {-1:0, 0:1}
    q = {}
    
    i = 0

    if (view == 1):
        print('{0:3} {1:20} {2:5} {3:20} {4:20}'.format(-1,r[-1],'/'.rjust(5),x[-1],y[-1]))
        print('{0:3} {1:20} {2:5} {3:20} {4:20}'.format(0,r[0],'/'.rjust(5),x[0],y[0]))
        
    while (r[i] > 0):
        i += 1
        q[i] = int(r[i - 2] / r[i - 1])
        r[i] = r[i - 2] - q[i]*r[i - 1]
        x[i] = x[i - 2] - q[i]*x[i - 1]
        y[i] = y[i - 2] - q[i]*y[i - 1]

        if (view == 1):
            print('{0:3} {1:20} {2:5} {3:20} {4:20}'.format(i,r[i],q[i],x[i],y[i]))
        #elif (view == 2):
        #    print('{0:3} = {1:3} x {2:3} + {3:3}'.format(r[i - 2],r[i - 1],q[i],r[i]))

    #if (view == 2):
    #    while (i > 0):
    #        print('{0:3} = ({1:3} - {2:3}) x {3:3} + {4:3}'.format(r[i - 2],r[i - 3],r[i - 2],q[i],r[i]))
    #        i -= 1

    if (returnConvergent == 1):
        q = [y for (x,y) in q.items()]
        if (view == 1):
            print('The convergent is: <{0}; {1}>'.format(q[0],', '.join(map(str, q[1:]))))
        return q
    
    if (view == 1):
        xI = x[i]
        yI = y[i]
        
    d = r[i - 1]
    x = x[i - 1]
    y = y[i - 1]

    if (d == 1):
        if (i % 2 == 1):
            c = y
        else:
            c = y + a
    else:
        c = 0

    if (view == 1):
            print('{0:20} * {1:20} + {2:20} * {3:20} = {4:20}'.format(x,a,y,b,d))
            print('{0:20} * {1:20} + {2:20} * {3:20} = {4:20}'.format(xI,a,yI,b,0))
            
    return (d,x,y,c)

def crt(R, N, view = 0):
    ''' Chinese remainder theorem
        Input: R = Vector of remainders
               N = Vector of modulos
        Output: x = Solution of the system
    '''
    n = functools.reduce(operator.mul, N)
        
    M = [int(n/t) for t in N]
    L = [eea(N[i], M[i])[3] for i in range(0, len(R))]
    C = [R[i]*M[i]*L[i] for i in range(0, len(R))]

    x = functools.reduce(operator.add, C) % n
    
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

def DecToBinary(x, view = 0):
    ''' Translate decimal number into binary represantation
        Input: x = Decimal Number

        Output: e = Binary represantation of x
    '''

    e = ''
    i = 0
    if (view == 1):
        print('{0:3} {1:5} {2:10}'.format('i'.rjust(3),'x'.rjust(5),'x % 2'.rjust(10)))
        print('--------------------')
        print('{0:3} {1:5} {2:10}'.format('0'.rjust(3),str(x).rjust(5),str(x % 2).rjust(10)))
        
    while (True):
        e = str((x % 2)) + e
        x = int(x / 2)
        if (x == 0):
            break
        if (view == 1):
            i += 1
            print('{0:3} {1:5} {2:10}'.format(str(i).rjust(3),str(x).rjust(5),str(x % 2).rjust(10)))
            
    return e

def BinaryToDec(x, view = 0):
    ''' Translate binary number into decimal represantation
        Input: x = Binary Number

        Output: e = Decimal represantation of x
    '''

    x = str(x)
    e = 0
    if (view == 1):
        print('{0:3} {1:5} {2:10} {3:10} {4:10}'.format('i'.rjust(3),'x[i]'.rjust(5),'e'.rjust(10),'e * 2'.rjust(10),'e + 1'.rjust(10)))
        print('--------------------------------------------')
        print('{0:3} {1:5} {2:10} {3:10} {4:10}'.format('/'.rjust(3),'/'.rjust(5),'0'.rjust(10),'0'.rjust(10),'/'.rjust(10)))
    for i in range(0, len(x)):
        tmp = e
        e *= 2
        if (x[i] == '1'):
            e += 1
            if (view == 1):
                print('{0:3} {1:5} {2:10} {3:10} {4:10}'.format(str(len(x) - 1 - i).rjust(3),str(x[i]).rjust(5),str(tmp).rjust(10),str(tmp * 2).rjust(10),str(e).rjust(10)))
        else:
            if (view == 1):
                print('{0:3} {1:5} {2:10} {3:10} {4:10}'.format(str(len(x) - 1 - i).rjust(3),str(x[i]).rjust(5),str(tmp).rjust(10),str(tmp * 2).rjust(10),'/'.rjust(10)))
                

    return int(e)
    
def FastExpo(a, b, n, view = 0):
    ''' Fast exponention algorithm
        Input: a = Decinal number
               b = Decinal number
               n = Decinal number

        Output: e = a^b(mod n)
    '''
    
    z = 1
    b = DecToBinary(b)
    if (view == 1):
        print('{0:3} {1:5} {2:15} {3:15} {4:15}'.format('i'.rjust(3),'b[i]'.rjust(5),'z'.rjust(15),'z^2(mod n)'.rjust(15),'z * a(mod n)'.rjust(15)))
        print('----------------------------------------------------------')
        print('{0:3} {1:5} {2:15} {3:15} {4:15}'.format('/'.rjust(3),'/'.rjust(5),'1'.rjust(15),'/'.rjust(15),'/'.rjust(15)))
        
    for j in range (0, len(b)):
        t = n
        z = (z**2) % n
        if (b[j] == '1'):
            if (view == 1):
                print('{0:3} {1:5} {2:15} {3:15} {4:15}'.format(str(j).rjust(3),b[j].rjust(5),str(z).rjust(15),str((z**2) % n).rjust(15),str((a * z) % n).rjust(15)))
            z = (a * z) % n
        else:
            if (view == 1):
                print('{0:3} {1:5} {2:15} {3:15} {4:15}'.format(str(j).rjust(3),b[j].rjust(5),str(z).rjust(15),str((z**2) % n).rjust(15),'/'.rjust(15)))

    return z

def RSA_Encryption(x, n, b, view = 0):
    if (x >= n):
        return "Invalid data (must be element of Zn)"

    if (view == 1):
        print('Calculate y = {0:10} ^ {1:10} (mod {2:10})'.format(x, b, n))
        
    y = FastExpo(x, b, n, view)

    if (view == 1):
        print()
        print('The encrypted data is: {0:10}'.format(y))
        
    return y

def RSA_Decryption(y, p, q, b, view = 0):
    n = p * q
    if (y >= n):
        return "Invalid data (must be element of Zn)"

    phi = (p - 1) * (q - 1)

    if (view == 1):
        print('Phi(n) is: {0:10} * {1:10} = {2:10}'.format(p - 1, q - 1, phi))
        print('Calculate a = {0:10} ^ -1 (mod {1:10})'.format(b, phi))
        
    comb = EEA(phi, b, view)
    a = comb[3]
    
    if (view == 1):
        print('Private key is: {0:10}'.format(a))
        print()
        print('Calculate x = {0:10} ^ {1:10} (mod {2:10})'.format(y, a, n))
        
    x = FastExpo(y, a, n, view)

    if (view == 1):
        print()
        print('The decrypted data is: {0:10}'.format(x))
        
    return x

def PollardP_Minus_1FactoringAlgorithm(n, b, view = 0):
    ''' Pollard P-1 factoring algorithm (Attack on RSA)
        Input: n   = The modulo (n = pq)
               b   = Upper limit to the factors of p-1
               
        Output: d  = p
    '''
    
    a = 2
    if (view == 1):
        print('{0:3} {1:15} {2:15}'.format('j'.rjust(3),'a'.rjust(15),'a^j(mod n)'.rjust(15)))
        print('-------------------------------------')
        
    for j in range(2, b + 1):
        tmp = a
        a = FastExpo(a,j,n)
        if (view == 1):
              print('{0:3} {1:15} {2:15}'.format(str(j).rjust(3),str(tmp).rjust(15),str(a).rjust(15)))

    print()
    d = GCD(a-1,n,1)

    if (d < n):
        return d
    else:
        return "Failure"

def Weiners_Attack_RSA(n, b, view = 0):
    ''' Weiner's factoring algorithm (Attack on RSA)
        Input: n   = The modulo (n = pq)
               b   = The public key
               
        Output: d  = p
    '''

    if (view == 1):
        print('Calcutaing convergent to {0} / {1}'.format(b, n))
    convergent = EEA(b, n, view, 1)

    for i in range(1, len(convergent)):
        t, a = CalcConvergent(convergent, i)

        if (view == 1):
            print('Attempt #{0}:'.format(i))
            print('\tAssuming t/a = {0} / {1}'.format(t, a))
            
        if (a % 2 == 0):
            if (view == 1):
                print("\ta can't be even number")
            continue

        phi = int((a * b - 1) / t)
        A, B, C = 1, -(n - phi + 1), n

        if (view == 1):
            print("\tQuadratic is: X^2 - {0}X + {1} = 0".format(abs(B), C))
                
        if (B**2 - 4*A*C < 0):
            if (view == 1):
                print("\tFailure - No real roots...")
            continue
        
        x1, x2 = (-B) + math.sqrt(B**2 - 4*A*C), (-B) - math.sqrt(B**2 - 4*A*C)
        x1, x2 = x1 / 2*A, x2 / 2*A
        
        if (x1 * x2 == n):
            if (view == 1):
                print("\tSuccess!")
                print("{0} = {1} * {2}".format(n, int(x1), int(x2)))
            return int(x1), int(x2)
        else:
            if (view == 1):
                print("\tFailure - Roots aren't integers...")

    return "Attack didn't succeed"

def CalcConvergent(convergent, order):
    convergent = list(reversed(convergent[0 : order + 1]))

    num = convergent[0]
    denom = 1

    for i in range(0, order):
        num, denom = denom + num * convergent[i + 1], num
        
    return num, denom

def ElGamal_CreateEncryptionSystem(view = 0):
    isPrime = 0
            
    while (isPrime == 0):
        a = random.randint(1, 10**10)
        while (not Miller_Rabin_Primary_Test(a, 100)):
            a = random.randint(1, 10**10)
        
        p = a * 2 + 1

        isPrime = Miller_Rabin_Primary_Test(p, 100)

    g = Find_Primitive_Root(p, [2, a])

    a = random.randint(1, p - 1)
    b = FastExpo(g, a, p)

    print('Private key: {0}'.format(a))
    print('Public key: ({0},{1},{2})'.format(p, g, b))
    
def ElGamal_Encryption(x, p, g, b, view = 0):
    r = random.randint(1, p - 1)

    y1, y2 = FastExpo(g, r, p, view), (x * FastExpo(b, r, p, view)) % p

    return y1, y2

def ElGamal_Decryption(y, p, a, view = 0):
    y1 = y[0]
    y2 = y[1]

    y1 = FastExpo(y1, a, p)

    comb = EEA(p, y1, view)
    y1 = comb[3]

    x = (y1 * y2) % p

    return x

def Find_Primitive_Root(p, pMinus1Factors):
    while (1):
        g = random.randint(2, p - 2)
        flag = 1
        for q in pMinus1Factors:
            if (FastExpo(g, int((p - 1) / q), p) == 1):
                flag = 0
                break

        if (flag == 1):
            return g
        
def Miller_Rabin_Primary_Test(n, r):
    # Write n as 1 + 2^t * m
    tmp = n - 1

    t = 0

    while (tmp % 2 == 0):
        tmp /= 2
        t += 1

    m = tmp

    while (r > 0):
        a = random.randint(2, n - 2)
        x = FastExpo(a, m, n)
        if (x == 1):
            r -= 1
        else:
            flag = 0
            for j in range(0, t):
                if (x == (n - 1)):
                    flag = 1
                    break
                else:
                    x = (x * x) % n

            if (flag == 0):
                return 0
            else:
                r -= 1

    return 1
    
def ShiftEncryption(key, p, reverse = False):
    ''' Enccrypt with Affine Encryption

        Input: (key)   = Shift size 
               p       = Original text
               reverse = False = Encrypt, True = Decrypt

        Output: e    = Encrypted text

    '''

    ret = [0]*len(p)
    
    for i in range(0, len(p)):
        if (reverse == False):
            ret[i] = chr(((ord(p[i]) - ord('a')) + key) % 26 + ord('a'))
        elif (reverse == True):
            ret[i] = chr(((ord(p[i]) - ord('a')) - key) % 26 + ord('a'))   

    return ''.join(ret)
    
def AffineEncryption(key, p, reverse = False):
    ''' Enccrypt with Affine Encryption

        Input: key = (a,b) (GCD(a,26) = 1)
               p     = Original text
               reverse = False = Encrypt, True = Decrypt

        Output: e    = Encrypted text

    '''

    ret = [0]*len(p)

    if (reverse == False):
        for i in range(0, len(p)):
            ret[i] = chr((key[0]*(ord(p[i]) - ord('a')) + key[1]) % 26 + ord('a'))
            
    elif (reverse == True):
        if (GCD(key[0],26) != 1):
            return 'Error, can''t decrypt with a={0}'.format(key[0])
        else:
            aInv = EEA(26, key[0])[3]
            for i in range(0, len(p)):
                ret[i] = chr(aInv*((ord(p[i]) - ord('a')) - key[1]) % 26 + ord('a'))

    return ''.join(ret)
