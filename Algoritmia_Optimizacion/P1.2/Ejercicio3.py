import numpy as np
import time
import matplotlib.pyplot as plt

def producto_matrices_cuadradas (A , B ):
    n = np.shape(A)[0]
    C = np.zeros((n, n))
    for i in range(n - 1):
        for j in range(n - 1):
            suma = 0
            for k in range(n - 1):
                suma += A[i][k] * B[k][j]
            C[i][j] = suma

    return C

def devolverTiempo(A, B):
    inicio = time.time()
    print(producto_matrices_cuadradas(A, B))
    fin = time.time()

    return fin - inicio

TAMAÑOS = np.linspace(2, 60, 50, dtype=int)
NUM_EJECUCIONES = 8


caso_promedio = np.zeros((len(TAMAÑOS)))
# [SIZE1, SIZE2, SIZE3, ...]

#mejor_caso = 0 
#peor_casdo = 0

# No hay mejor ni peor caso
for _ in range(NUM_EJECUCIONES):
    for i, tam in enumerate(TAMAÑOS):
        A = np.random.randint(2, tam*2, size=(tam, tam))
        B = np.random.randint(2, tam*2, size=(tam, tam))
        caso_promedio[i] += devolverTiempo(A, B)

caso_promedio /= NUM_EJECUCIONES

FACTOR = 10**(-4.6)
a = np.linspace(2, np.max(TAMAÑOS), 50)

plt.plot(TAMAÑOS, caso_promedio)
plt.plot(a, a**2 * FACTOR, color='red')
plt.savefig("P1.2/E3.png")
plt.show()

