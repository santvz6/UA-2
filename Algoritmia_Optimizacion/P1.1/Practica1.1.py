"""

"""
import time
import random
import numpy as np
import matplotlib.pyplot as plt


def getTiempo(alg, arr):
    inicio = time.time()
    alg(arr)
    fin = time.time()
    return fin - inicio

def ordenacion_uno(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

NUM_EJECUCIONES = 10
SIZES = np.linspace(2, 100, 50, dtype=int)

mejor1 = np.zeros(len(SIZES))
peor1 = np.zeros(len(SIZES))
normal1 = np.zeros(len(SIZES))

for _ in range(NUM_EJECUCIONES):
    for i, size in enumerate(SIZES):
        array_mejor = np.sort(np.random.randint(1, size*2, size=size))
        array_peor = np.sort(np.random.randint(1, size*2, size=size))[::-1]
        array_normal = np.random.randint(1, size*2, size=size)
        
        mejor1[i] = getTiempo(ordenacion_uno, array_mejor)
        peor1[i] = getTiempo(ordenacion_uno, array_peor)
        normal1[i] = getTiempo(ordenacion_uno, array_normal)

mejor1 /= NUM_EJECUCIONES
peor1 /= NUM_EJECUCIONES
normal1 /= NUM_EJECUCIONES

plt.plot(SIZES, mejor1, color="green", label="Mejor")
plt.plot(SIZES, peor1, color="red", label="Peor")
plt.plot(SIZES, normal1, color="blue", label="Normal")

FACTOR = 10**(-8)
n = np.linspace(2, 100, max(SIZES), dtype=int)

plt.plot(n, n ** 2 * FACTOR, color="purple")
plt.plot(n, n ** 2 / 2 * FACTOR, color="pink")
plt.plot(n, 2 * n ** 2 * FACTOR , color="orange")

plt.legend()
plt.savefig("P1.1/E1_1.png")
plt.show()