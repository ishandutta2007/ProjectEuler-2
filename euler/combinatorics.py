def nCk(n, k):
    k = min(k, n - k)

    m = 1
    d = 1

    for i in range(k):
        d *= (i + 1)
        m *= (n - i)

    return m // d  
