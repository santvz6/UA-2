import numpy as np

def director_deportivo(valoraciones: np.array, fichas: np.array,  n: int, G=3000):
    mem = np.zeros((n+1, G+1))
    for i in range(1, n+1):
        for j in range(G+1):
            # Un fichaje vale más del espacio del que dispones
            # Este -1 no hace referencia al anterior sino al correspondiente de 1 a indice 0
            if fichas[i-1] > j:

                # Pasamos al siguiente
                mem[i, j] = mem[i-1, j]
            else:
                mem[i, j] = max(mem[i-1, j], valoraciones[i-1]+mem[i-1, j-fichas[i-1]])
    return mem


valoraciones = np.array([6, 1, 3, 8])
fichas = np.array([950, 2400, 500, 2000])
mem = director_deportivo(valoraciones, fichas, len(valoraciones))
print(mem)

def backtracking(mem, valoraciones, fichas, G, n):

    i, g = n, G
    solucion = list()
    
    while i > 0 and g > 0:

        # No agarré un jugador (por eso el i-1)
        a = mem[i-1, g] 

        # Agarré un jugador
        b = valoraciones[i-1] + mem[i-1, g-fichas[i-1]]

        if mem[i, g] == b:
            g -= fichas[i-1]
            i -= 1
            solucion += [i]

        else:
            i-=1
        
    return solucion

solucion = backtracking(mem, valoraciones, fichas, G=3000, n=len(valoraciones))
print(solucion)

