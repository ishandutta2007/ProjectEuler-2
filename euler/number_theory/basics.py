def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b

    return a
	
def eea(a, b):
    """Extended Euclidean Algorithm.

    Input: (a, b) - Integers
    Output: (x, y, g)
        x,y - ax + by = g
        g   - GCD(a, b)
    """
    r = {-1:a, 0:b}
    x = {-1:1, 0:0}
    y = {-1:0, 0:1}
    q = {}
    
    i = 0

    while (r[i] > 0):
        i += 1
        q[i] = int(r[i - 2] / r[i - 1])
        r[i] = r[i - 2] - q[i]*r[i - 1]
        x[i] = x[i - 2] - q[i]*x[i - 1]
        y[i] = y[i - 2] - q[i]*y[i - 1]
        
    g = r[i - 1]
    x = x[i - 1]
    y = y[i - 1]

    return (x, y, g)

def modular_multiplicative_inverse(a, p):
    x, y, g = eea(a, p)
    if g == 1:
        return x
    else:
        return 0
