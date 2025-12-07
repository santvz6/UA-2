import time
import matplotlib.pyplot as plt
import numpy as np

def returnTiempo(array, n, target):
    inicio = time.time()
    busqueda_binaria(array, n, target)
    fin = time.time()
    return fin - inicio

def busqueda_binaria (arr , n, target):
    L = 0
    R = n - 1
    while L <= R:
        m = round(( L + R ) / 2)
        if arr[m] < target:
            L = m + 1
        elif arr[m] > target:
            R = m - 1
        else:
            return m
    return False

NUM_EJECUCIONES = 10
TAMAÑOS = np.linspace(3, 100, 50, dtype=int)

caso_normal = np.zeros(len(TAMAÑOS))
caso_bueno = np.zeros(len(TAMAÑOS))
caso_malo = np.zeros(len(TAMAÑOS))

for _ in range(NUM_EJECUCIONES):
    for i, tam in enumerate(TAMAÑOS):
        array = np.random.randint(1, tam*2, size=(tam))
        caso_normal[i] += returnTiempo(array, len(array), np.random.randint(1, tam*2))
        caso_bueno[i] += returnTiempo(array, len(array), array[len(array)//2])
        caso_malo[i] += returnTiempo(array, len(array), -1)
        

caso_normal /= NUM_EJECUCIONES
caso_bueno /= NUM_EJECUCIONES
caso_malo /= NUM_EJECUCIONES

plt.plot(TAMAÑOS, caso_normal, color="red", label="Caso Normal")
plt.plot(TAMAÑOS, caso_bueno, color="blue", label="Caso Bueno")
plt.plot(TAMAÑOS, caso_malo, color="green", label="Caso Malo")
plt.legend()

plt.savefig("P1.2/E4.png")
plt.show()