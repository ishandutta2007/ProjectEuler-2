from copy import deepcopy as __deepcopy

def hungarian_algorithm(m):
    """Using the "Hungarian Algorithm" to solve the "Assignment Problem"."""
    
    def one():
        nonlocal step, cost
        
        for r in range(L):
            min_r = min(cost[r])
            cost[r] = [c - min_r for c in cost[r]]

        step = 2

    def two():
        nonlocal step, mask, row_cover, col_cover
        
        for r in range(L):
            for c in range(L):
                if cost[r][c] == 0 and row_cover[r] == 0 and col_cover[c] == 0:
                    mask[r][c] = 1
                    row_cover[r] = 1
                    col_cover[c] = 1
                
        row_cover = [0 for i in range(L)]
        col_cover = [0 for i in range(L)]

        step = 3

    def three():
        nonlocal step, mask, col_cover
        
        for r in range(L):
            for c in range(L):
                if mask[r][c] == 1:
                    col_cover[c] = 1

        if sum(col_cover) == L:
            step = 7
        else:
            step = 4

    def four():
        nonlocal step, mask, row_cover, col_cover, zero_r, zero_c
        
        def find_a_zero():
            for r in range(L):
                for c in range(L):
                    if cost[r][c] == 0 and row_cover[r] == 0 and col_cover[c] == 0:
                        return r, c

            return (-1, -1)

        def star_in_row(r):
            for c in range(L):
                if mask[r][c] == 1:
                    return True

            return False

        def find_star_in_row(r):
            for c in range(L):
                if mask[r][c] == 1:
                    return c

            return -1
    
        while True:
            r, c = find_a_zero()
            if r == -1:
                step = 6

                return
            else:
                mask[r][c] = 2
                if (star_in_row(r)):
                    c = find_star_in_row(r)
                    row_cover[r] = 1
                    col_cover[c] = 0
                else:
                    step = 5

                    zero_r = r
                    zero_c = c

                    return

    def five():
        nonlocal step, mask, row_cover, col_cover, zero_r, zero_c
        
        def find_star_in_col(c):
            for r in range(L):
                if mask[r][c] == 1:
                    return r

            return -1

        def find_prime_in_row(r):
            for c in range(L):
                if mask[r][c] == 2:
                    return c

        def augment_path():
            nonlocal mask
            
            for p in range(path_count):
                if mask[path[p][0]][path[p][1]] == 1:
                    mask[path[p][0]][path[p][1]] = 0
                else:
                    mask[path[p][0]][path[p][1]] = 1

        def clear_covers():
            nonlocal row_cover, col_cover
            
            row_cover = [0 for i in range(L)]
            col_cover = [0 for i in range(L)]

        def erase_primes():
            nonlocal mask
            
            for r in range(L):
                for c in range(L):
                    if mask[r][c] == 2:
                        mask[r][c] = 0
                    
        path_count = 1
        path = [[zero_r, zero_c]]

        done = False
        while not done:
            r = find_star_in_col(path[path_count - 1][1])
            if r > -1:
                path_count += 1
                path.append([r, path[path_count - 2][1]])
            else:
                done = True

            if not done:
                c = find_prime_in_row(path[path_count - 1][0])
                path_count += 1
                path.append([path[path_count - 2][0], c])

        augment_path()
        clear_covers()
        erase_primes()
    
        step = 3

    def six():
        nonlocal step, cost
        
        def find_smallest():
            return min([cost[r][c] for c in range(L) for r in range(L) if row_cover[r] == 0 and col_cover[c] == 0])

        minval = find_smallest()

        for r in range(L):
            for c in range(L):
                if row_cover[r] == 1:
                    cost[r][c] += minval
                if col_cover[c] == 0:
                    cost[r][c] -= minval

        step = 4
    
    L = len(m)

    cost = __deepcopy(m)
    mask = [[0 for i in range(L)] for j in range(L)]
    
    row_cover = [0 for i in range(L)]
    col_cover = [0 for i in range(L)]

    zero_r = -1
    zero_c = -1
    
    step = 1
    while True:
        if step == 1:
            one()
        elif step == 2:
            two()
        elif step == 3:
            three()
        elif step == 4:
            four()
        elif step == 5:
            five()
        elif step == 6:
            six()
        elif step == 7:
            return mask

if __name__ == "__main__":
    def pretty_print_matrix(m):
        s = [[str(e) for e in row] for row in m]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print ('\n'.join(table))
    
    import random

    L = random.randint(3, 10)
    cost_mat = [[random.randint(1, 10 * L) for j in range(L)] for i in range(L)]
    mask_mat = hungarian_algorithm(cost_mat)
    min_assignment = sum([cost_mat[i][j] for j in range(L) for i in range(L) if mask_mat[i][j] == 1])
    
    print ('Cost Matrix:')
    pretty_print_matrix(cost_mat)

    print ('\nMask Matrix:')
    pretty_print_matrix(mask_mat)
    
    print ('\nMinimun Assignment: {0}'.format(min_assignment))
