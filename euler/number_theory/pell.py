from heapq import heappush as __heappush, heappop as __heappop

def __is_perfect_square(n):
    if n < 0:
        return False
    
    s = int(n ** 0.5)

    return s ** 2 == n

def __PQA(p, q, D):
    """Lagrange algorithm
    
    Gives the expansion as a continued fraction of a
    quadratic number (p+√D)/q, with u, v, D integers, D not a square.
    """
    assert((p * p - D) % q == 0) # Works only if p^2 = D (mod q)
    A = (0, 1)
    B = (1, 0)

    while True:
        a = int(p + D ** 0.5) // q
        A = (A[1], a * A[1] + A[0])
        B = (B[1], a * B[1] + B[0])

        p = a * q - p
        q = (D - p * p) // q

        yield (A[1], B[1])    

def solve_pell_equation(D, N):
    """Solve the diophantine equation: x^2 - Dy^2 = N

    This method generating all the solutions (x, y) x >= 0, y >= 0
    to the equation.
    """
    if N == 0: 
        if D == 0: # There is only 1 solution
            yield 0, 0
            return
        elif D < 0 or not __is_perfect_square(D): # No solutions
            return
        else:
            t = 0
            while True:
                yield d * t, t # Inifinite number of solutions (dt, t) for t e N
                t += 1

    elif N == 1:
        if D < 0: # No solutions
            return
        else:
            trivial_solution = (1, 0)
        
            if __is_perfect_square(D): # There is only 1 primitive solution
                yield trivial_solution
                return

            g = __PQA(0, 1, D)
            c = next(g)

            while c[0]**2 - D * c[1]**2 != N:
                c = next(g)
            fundemental_solution = c
            
            while True:
                yield trivial_solution
                trivial_solution = (trivial_solution[0] * fundemental_solution[0] + trivial_solution[1] * fundemental_solution[1] * D,
                                    trivial_solution[0] * fundemental_solution[1] + trivial_solution[1] * fundemental_solution[0])

    elif N == -1:
        if D <= 0: # No solutions
            return
        else:
            g = __PQA(0, 1, D)
            c = next(g)

            i = 1
            while c[0]**2 - D * c[1]**2 not in [1, -1]:
                c = next(g)
                i += 1

            if i % 2 == 0:
                return # No solutions
            
            fundemental_solution = c
            corresponding_solution = (c[0] * c[0] + c[1] * c[1] * D,
                                      2 * c[0] * c[1])
            while True:
                yield fundemental_solution
                fundemental_solution = (fundemental_solution[0] * corresponding_solution[0] + fundemental_solution[1] * corresponding_solution[1] * D,
                                        fundemental_solution[0] * corresponding_solution[1] + fundemental_solution[1] * corresponding_solution[0])

    # Generalized Pell equation
    elif N > 0:
        if D == 0:
            if __is_perfect_square(N):
                n == int(N ** 0.5)
                x = n
                y = 0
                while True:
                    yield x, y
                    y += 1
            else:
                return # No solutions

        if D < 0:
            # Only finite number of solutions:
            #         x^2 + |D|y^2 = N
            y_bound = int((N // abs(D)) ** 0.5)

            x_square = N
            for y in range(y_bound + 1):
                if __is_perfect_square(x_square):
                    x = int(x_square ** 0.5)
                    yield (x, y)
                x_square += D * (2 * y + 1)

        else:            
            g = __PQA(0, 1, D)
            c = next(g)

            while c[0]**2 - D * c[1]**2 != 1:
                c = next(g)
            corresponding_solution = c

            primitive_solutions = []

            x_bound = int((((corresponding_solution[0] + 1) * abs(N)) / 2) ** 0.5)
            y_bound = int(corresponding_solution[1] * (abs(N) / (2 * (corresponding_solution[0] + 1))) ** 0.5)

            if x_bound < y_bound:
                for x in range(x_bound + 1):
                    d_y_square = x * x - N
                    if (d_y_square % D == 0):
                        y_square = d_y_square // D
                        if __is_perfect_square(y_square):
                            y = int(y_square ** 0.5)
                            primitive_solutions.extend([(x, y), (-x, y)])
            else:
                for y in range(y_bound + 1):
                    x_square = N + D * y * y
                    if __is_perfect_square(x_square):
                        x = int(x_square ** 0.5)
                        primitive_solutions.extend([(x, y), (-x, y)])

            if not primitive_solutions:
                return # No solutions

            # Normalize solutions
            for i in range(len(primitive_solutions)):
                x, y = primitive_solutions[i]
                if x < 0:
                    x, y = (-x, -y)
                if y < 0:
                    x, y = (x * corresponding_solution[0] + y * corresponding_solution[1] * D,
                            x * corresponding_solution[1] + y * corresponding_solution[0])
                if x < 0:
                    x, y = (-x, -y)
                primitive_solutions[i] = (x, y)
            primitive_solutions = list(set(primitive_solutions))
        
            # Remove equivalent solutions
            tmp_primitive_solutions = []
            for i in range(len(primitive_solutions)):
                x1, y1 = primitive_solutions[i]
                for j in range(i + 1, len(primitive_solutions)):
                    x2, y2 = primitive_solutions[j]
                    if (x1 * x2 - y1 * y2 * D) % N == 0 and \
                       (x1 * y2 - x2 * y1) % N == 0:
                        break
                else:
                    __heappush(tmp_primitive_solutions, (x1, y1))

            primitive_solutions = tmp_primitive_solutions

            while True:
                x, y = __heappop(primitive_solutions)
                yield (x, y)
                __heappush(primitive_solutions, (x * corresponding_solution[0] + y * corresponding_solution[1] * D,
                                                 x * corresponding_solution[1] + y * corresponding_solution[0]))

    elif N < 0:
        if D <= 0: # No solutions
            return

        else:
            g = __PQA(0, 1, D)
            c = next(g)

            while c[0]**2 - D * c[1]**2 != 1:
                c = next(g)
            corresponding_solution = c

            primitive_solutions = []

            x_bound = int((((corresponding_solution[0] + 1) * abs(N)) / 2) ** 0.5)
            y_bound = int(corresponding_solution[1] * (abs(N) / (2 * (corresponding_solution[0] + 1))) ** 0.5)

            if x_bound < y_bound:
                for x in range(x_bound + 1):
                    d_y_square = x * x - N
                    if (d_y_square % D == 0):
                        y_square = d_y_square // D
                        if __is_perfect_square(y_square):
                            y = int(y_square ** 0.5)
                            primitive_solutions.extend([(x, y), (-x, y)])
            else:
                for y in range(y_bound + 1):
                    x_square = N + D * y * y
                    if __is_perfect_square(x_square):
                        x = int(x_square ** 0.5)
                        primitive_solutions.extend([(x, y), (-x, y)])

            if not primitive_solutions:
                return # No solutions

            # Normalize solutions
            for i in range(len(primitive_solutions)):
                x, y = primitive_solutions[i]
                if x < 0:
                    x, y = (-x, -y)
                if y < 0:
                    x, y = (x * corresponding_solution[0] + y * corresponding_solution[1] * D,
                            x * corresponding_solution[1] + y * corresponding_solution[0])
                if x < 0:
                    x, y = (-x, -y)
                primitive_solutions[i] = (x, y)
            primitive_solutions = list(set(primitive_solutions))
        
            # Remove equivalent solutions
            tmp_primitive_solutions = []
            for i in range(len(primitive_solutions)):
                x1, y1 = primitive_solutions[i]
                for j in range(i + 1, len(primitive_solutions)):
                    x2, y2 = primitive_solutions[j]
                    if (x1 * x2 - y1 * y2 * D) % N == 0 and \
                       (x1 * y2 - x2 * y1) % N == 0:
                        break
                else:
                    __heappush(tmp_primitive_solutions, (x1, y1))

            primitive_solutions = tmp_primitive_solutions

            twin = False
            twin_fundemental_equation = solve_pell_equation(D, -1)
            try:
                twin = True
                twin_equation_primitive_solution = next(twin_fundemental_equation)
            except StopIteration:
                pass

            if twin == True:
                twin_equation = solve_pell_equation(D, -N)
            
            while True:
                x, y = __heappop(primitive_solutions)
                __heappush(primitive_solutions, (x * corresponding_solution[0] + y * corresponding_solution[1] * D,
                                                 x * corresponding_solution[1] + y * corresponding_solution[0]))

                x_t, y_t = next(twin_equation)
                x2, y2 = (x_t * twin_equation_primitive_solution[0] + y_t * twin_equation_primitive_solution[1] * D,
                          x_t * twin_equation_primitive_solution[1] + y_t * twin_equation_primitive_solution[0])

                while x < x2:
                    yield (x, y)
                    x, y = __heappop(primitive_solutions)
                    __heappush(primitive_solutions, (x * corresponding_solution[0] + y * corresponding_solution[1] * D,
                                                     x * corresponding_solution[1] + y * corresponding_solution[0]))

                yield (x2, y2)


if __name__ == "__main__":
    import random

    for i in range(3):
        D = random.randint(-500, 500)
        N = random.randint(-20, 20)

        g = solve_pell_equation(D, N)

        print ("x ^ 2 {0} {1:<3} * y ^ 2 == {2}".format(("+" if (D < 0) else "-"), abs(D), N))
        print ("=" * 30)
        try:
            for j in range(10):
                x, y = next(g)
                assert(x * x - D * y * y == N)
                print("({0:<10}, {1:<10})    {0:<3} ^ 2 {2} {3:<3} * {1:<3} ^ 2 == {4}".format(x, y, ("+" if (D < 0) else "-"), abs(D), N))
        except StopIteration:
            print("No more solutions!")
        except AssertionError:
            print("{0:<3} ^ 2 {1} {2:<3} * {3:<3} ^ 2 == {4}  -   Failed".format(x, ("+" if (D < 0) else "-"), abs(D), y, (x * x - D * y * y)))
        finally:
            print()
                
