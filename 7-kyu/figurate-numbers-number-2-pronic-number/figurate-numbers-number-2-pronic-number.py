def is_pronic(n):
    n = abs(n)
    for i in range(int(n/2) + 1):
        if i * (i + 1) == n:
            return True
    return False