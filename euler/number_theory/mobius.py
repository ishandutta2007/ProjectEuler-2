def mobius_sieve(n):
    sqrt = int(n ** 0.5)

    mobius = [1] * (n + 1)
    mobius[0] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if mobius[i] == 1:
            for j in range(i, n + 1, i):
                mobius[j] *= -i
            for j in range(i * i, n + 1, i * i):
                mobius[j] = 0

    for i in range(2, n + 1):
        if mobius[i] == i:
            mobius[i] = 1
        elif mobius[i] == -i:
            mobius[i] = -1
        elif mobius[i] < 0:
            mobius[i] = 1
        elif mobius[i] > 0:
            mobius[i] = -1

    return mobius
