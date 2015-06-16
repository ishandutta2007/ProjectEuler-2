# --------------------------------------- Factorial trailing digits ------------------------------------------- #
#                                                                                                               #
#       For any N, let f(N) be the last five digits before the trailing zeroes in N!.                           #
#       For example,                                                                                            #
#                                                                                                               #
#                                           9! = 362880 so f(9)=36288                                           #
#                                           10! = 3628800 so f(10)=36288                                        #
#                                           20! = 2432902008176640000 so f(20)=17664                            #
#                                                                                                               #
#       Find f(1,000,000,000,000)                                                                               #
# ------------------------------------------------------------------------------------------------------------- #
import time

def count_factorial_factors(n, f):
    s = 0
    
    while (n):
        s += n // f
        n //= f

    return s

def factorial_factors_without_2_5(n, modulos):
    try:
        return factorial_factors_without_2_5.MEMORY[n]
    except KeyError:
        return (pow(factorial_factors_without_2_5.MEMORY[modulos], (n // modulos), modulos) * \
               factorial_factors_without_2_5.MEMORY[n % modulos]) % modulos
factorial_factors_without_2_5.MEMORY = { 0: 1 }

def f(n):
    b = pow(2, numOf2 - numOf5, MODULOS)

    a = 1
    for i in range(1, MODULOS, 2):
        if (i % 5 == 0):
            t = i
            while (t % 5 == 0):
                t //= 5

            a *= t

        else:
            a *= i

    a %= MODULOS
    print (a)
    a = pow(a, n // MODULOS, MODULOS)
    print(a)
    return (a * b) % MODULOS

def eu160():
    TARGET  = 10 ** 12
    MODULOS = 10 ** 5

    num_of_2 = count_factorial_factors(TARGET, 2)
    num_of_5 = count_factorial_factors(TARGET, 5)

    t = 1
    for i in range(1, min(TARGET + 1, MODULOS + 1)):
        if i % 2 != 0 and i % 5 != 0:
            t = (t * i) % MODULOS

        factorial_factors_without_2_5.MEMORY[i] = t
        
    trailing_digits = factorial_factors_without_2_5(TARGET, MODULOS)

    p = 2
    while (p <= TARGET):
        q = 1
        while (q <= TARGET // p):
            trailing_digits = (trailing_digits * factorial_factors_without_2_5(TARGET // (p * q), MODULOS)) % MODULOS
            q *= 5
        p *= 2

    q = 5
    while (q <= TARGET):
        trailing_digits = (trailing_digits * factorial_factors_without_2_5(TARGET // q, MODULOS)) % MODULOS
        q *= 5

    trailing_digits = (trailing_digits * pow(2, num_of_2 - num_of_5, MODULOS)) % MODULOS
    
    return trailing_digits

if __name__ == "__main__":
    startTime = time.clock()
    print (eu160())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
