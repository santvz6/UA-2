def greedy_laberinto_solver_strict(laberinto):
    
    n, m = len(laberinto), len(laberinto[0])
    x, y = 0, 0
    camino = [(x, y)]
    
    objetivo = (n - 1, m - 1)

    def es_valido(nx, ny):
        return 0 <= nx < n and 0 <= ny < m and laberinto[nx][ny] == 1

    def heuristic(nx, ny):
        return abs(nx - objetivo[0]) + abs(ny - objetivo[1])

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izquierda, derecha

    while (x, y) != objetivo:
        best_move = None
        best_heuristic = float('inf')

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if es_valido(nx, ny):
                h = heuristic(nx, ny)
                if h < best_heuristic:
                    best_move = (nx, ny)
                    best_heuristic = h

        if best_move:
            x, y = best_move
            camino.append((x, y))
            laberinto[x][y] = 0  # Marca como visitado para no volver
        else:
            return None  # No hay camino disponible

    return camino


# Ejemplo de uso
laberinto = [
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 1]
]

camino = greedy_laberinto_solver_strict(laberinto)
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino.")
