def nim(N, M):
    """
    N: Cantidad que queda
    M: Máx. Cantidad

    """
    if N <= M:
        return True

    for i in range(1, M+1):
        # El rival no tiene jugada ganadora
        if not nim(N-i, M):
            return True
    return False

print(nim(9, 3))