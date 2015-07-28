def gradient_descent(f, a, b):
    '''Return local minimum of 'f' a <= x <= b'''
    def f_derivative(x):
        return (f(x + e) - f(x)) / e
    
    e = 1e-10
    gamma = 1e-6

    x_old = 0
    x_new = (a + b) / 2

    while abs(x_new - x_old) > e:
        x_old = x_new
        x_new = x_old - f_derivative(x_old) * gamma

    return x_new

def Newton_Raphson(f, x_0, e):
    '''Return root of 'f' near x_0'''
    def f_derivative(x):
        epsilon = 1e-5
        
        return (f(x + epsilon) - f(x)) / epsilon
        
    x_n = x_0

    delta = f(x_n) / f_derivative(x_n)
    
    while abs(delta) >= e:
        x_n = x_n - delta
        delta = f(x_n) / f_derivative(x_n)

    return x_n 
