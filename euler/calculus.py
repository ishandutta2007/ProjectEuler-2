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
