"http://www.alpertron.com.ar/METHODS.HTM"
from .basics import gcd as _gcd, eea as _eea
from ..numbers import get_divisors as _get_divisors

def __is_perfect_square(n):
    if n < 0:
        return False
    
    s = int(n ** 0.5)

    return s ** 2 == n

def solve_diophantine_equation(A, B, C, D, E, F):
    """Solve the diophantine equation "Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0".

    """
    if A == 0 and B == 0 and C == 0: # Linear case
        return _solve_linear_case(D, E, F)

    elif A == 0 and C == 0 and B != 0: # Simple Hyperbolic case
        return _solve_simple_hyperbolic_case(B, D, E, F)

    elif (B * B - 4 * A * C) < 0: # Elliplical case
        return _solve_elliptical_case(A, B, C, D, E, F)

    elif (B * B - 4 * A * C) == 0: # Parabolic case
        return _solve_parabolic_case(A, B, C, D, E, F)

def _solve_linear_case(D, E, F):
    """Solve the diophantine equation "Dx + Ey + F = 0".

    """
    if D == 0 and E == 0:
        if F != 0:
            return

        x = 0
        while True:
            for y in range(x + 1):
                yield (x, y)

            x += 1

    elif D == 0 and E != 0:
        if F % E != 0: # No solution
            return

        y = -F // E
        x = 0
        while True:
            yield (x, y)

            x += 1

    elif D != 0 and E == 0:
        if F % D != 0: # No solution
            return

        x = -F // D
        y = 0
        while True:
            yield (x, y)

            y += 1

    else:
        g = _gcd(D, E)

        if F % g != 0: # No solution
            return

        x, y, g = _eea(D, E)
        d, e, f = D // g, E // g, F // g

        x *= f
        y *= f
        
        while True:
            yield (x, y)
            x += e
            y -= d

def _solve_simple_hyperbolic_case(B, D, E, F):
    """Solve the diophantine equation "Bxy + Dx + Ey + F = 0".

    Bxy + Dx + Ey + F = 0  -->  B^2xy + BDx + BEy = -BF
    B^2xy + BDx + BEy + DE = DE - BF  -->
    (Bx + E) * (By + D) = DE - BF
    """
    if D * E - B * F == 0: # Two lines parallel to x and y axes respectively
        flag1 = (E % B == 0)
        flag2 = (D % B == 0)

        if not flag1 and not flag2: # No solutions
            return
        
        x = -E // B
        y = -D // B

        t = 0
        while True:
            if flag1:
                yield (x, t)

            if flag2:
                yield (t, y)

            t += 1

    else: # a hyperbola whose asymptotes are parallel to x and y axes.
        divisors = _get_divisors(D * E - B * F, with_negative=True)

        for d in divisors:
            if (d - E) % B != 0:
                continue
            
            x = (d - E) // B
            y = ((D * E - B * F) // d - D) // B
            
            yield (x, y)

def _solve_elliptical_case(A, B, C, D, E, F):
    """Solve the diophantine equation "Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0" when "B^2 - 4AC < 0".

    Ellipse is a closed figure, only finite number of solutions.
    Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0  --> Cy^2 + (Bx + E)y + (Ax^2 + Dx + F) = 0
    y = {-(Bx + E) +- sqrt[(Bx + E)^2 - 4C(Ax^2 + Dx + F)]} / 2C

    In the left and right extremes, there is only one solution (y)  -->
    The discriminant equals to zero.
    (Bx + E)^2 - 4C(Ax^2 + Dx + F)] = 0  -->
    (B^2 - 4AC)x^2 + 2(BE - 2CD)x + (E^2 - 4CF) = 0
    """
    discriminant_x = (2*B*E - 4*C*D)**2 - 4 * (B*B - 4*A*C) * (E*E - 4*C*F)

    if discriminant_x < 0:
        return # No solutions

    x1 = int(((-2*B*E + 4*C*D) + discriminant_x**0.5) / (2 * (B*B - 4*A*C)))
    x2 = int(((-2*B*E + 4*C*D) - discriminant_x**0.5) / (2 * (B*B - 4*A*C)))

    for x in range(x1, x2 + 1):
        discriminant = (B*x + E)**2 - 4 * C * (A * x**2 + D*x + F)

        if not __is_perfect_square(discriminant):
            continue

        dis_sqrt = int(discriminant**0.5)
        b_minus = (-B * x - E)

        if (b_minus - dis_sqrt) % (2 * C) == 0:
            y = (b_minus - dis_sqrt) // (2 * C)

            yield (x, y)

        if (b_minus + dis_sqrt) % (2 * C) == 0:
            y = (b_minus + dis_sqrt) // (2 * C)

            yield (x, y)

def _solve_parabolic_case(A, B, C, D, E, F):
    """Solve the diophantine equation "Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0" when "B^2 - 4AC = 0".

    Ellipse is a closed figure, only finite number of solutions.
    Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0  --> Cy^2 + (Bx + E)y + (Ax^2 + Dx + F) = 0
    y = {-(Bx + E) +- sqrt[(Bx + E)^2 - 4C(Ax^2 + Dx + F)]} / 2C

    In the left and right extremes, there is only one solution (y)  -->
    The discriminant equals to zero.
    (Bx + E)^2 - 4C(Ax^2 + Dx + F)] = 0  -->
    (B^2 - 4AC)x^2 + 2(BE - 2CD)x + (E^2 - 4CF) = 0
    """
