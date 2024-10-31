import numpy as np

def director_deportivo(valoraciones: np.array, fichas: np.array,  n: int, G=3000):
    mem = np.zeros((n, G))
    for i in range(n):
        for j in range(G):
            # Un fichaje vale más del espacio del que dispones
            if fichas[i] > j:
                # Pasamos al siguiente
                mem[i, j] = mem[i-1, j]
            else:
                mem[i, j] = max(mem[i-1, j], valoraciones[i]+mem[i-1, j-fichas[i]])
    return mem


valoraciones = np.array([6, 1, 3, 8])
fichas = np.array([950, 2400, 500, 2000])
print(np.max(director_deportivo(valoraciones, fichas, len(valoraciones))))
