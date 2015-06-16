def gen_sqrt_best_approximations(n):
    """Generate "best rational approximation" for sqrt(n).

    Iterating over the convergents and relevant semi-convergents.
    Each approximation is yielded by (x, y).
    """
    sqr = int(n ** 0.5)
    #s = decimal.Decimal(n).sqrt()
    
    a0 = sqr
    m0 = 0
    d0 = 1

    num0, num1 = 0, 1
    den0, den1 = 1, 0

    # The convergents are swinging below and number to be approximated
    # The first convergent is below the number, so |a - c[0]| = a - c[0]
    sign_correction = 1
    
    while (True):
        m = a0 * d0 - m0
        d = (n - (m ** 2)) // d0
        a = (sqr + m) // d
        
        num = (a0 * num1) + num0
        den = (a0 * den1) + den0

        yield (num, den)
        below = True

        a0, m0, d0 = a, m, d
        num0, num1 = num1, num
        den0, den1 = den1, den
        
        if (a % 2 == 0): # The "half-rule", see http://en.wikipedia.org/wiki/Continued_fraction#Best_rational_approximations
            semi_n = a // 2
            semi_con_num = (semi_n * num1) + num0
            semi_con_denum = (semi_n * den1) + den0

            # The last convergent is in a different side from the current semi convergent
            # |sqrt(n) - a/b| > |sqrt(n) - c/d| (a/b and c/d are in different sides    ---->
            # 4nb^2d^2 > (ad + bc)^2 if a/b < sqrt(n) AND
            # 4nb^2d^2 < (ad + bc)^2 if a/b > sqrt(n)
            # We can use sign correction for single inequality
            if (sign_correction * (4 * n * den**2 * semi_con_denum**2) >
                sign_correction * (num * semi_con_denum + den * semi_con_num)**2):
                yield semi_con_num, semi_con_denum

        for semi_n in range((a // 2) + 1, a):
            semi_con_num = (semi_n * num1) + num0
            semi_con_denum = (semi_n * den1) + den0

            yield semi_con_num, semi_con_denum

        sign_correction *= -1 # Change sign


if __name__ == "__main__":
    pass
                
