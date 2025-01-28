import numpy as np
import time
import matplotlib.pyplot as plt

def ordena(arr):    
        
    n = len(arr)
    izq = list()
    der = list()

    if n <= 1:
        return arr
    else:
        pivote = arr[0]
        for x in arr[1:]:
            if x <= pivote:
                izq.append(x)       
            if x > pivote:
                der.append(x)   
        return ordena(izq) + [pivote] + ordena(der)

def getTiempo(arr):
    inicio = time.time()
    ordena(arr)
    fin = time.time()
    return fin - inicio

def mejorArray(size):
    """ M_mejor = np.random.randint(1, size, size=(2))
    for _ in range(size - 2):
        media = np.mean(M_mejor)
        M_mejor = np.co[::-1]ncatenate(([media], M_mejor))"""
    M_mejor = np.random.randint(1, size*2, size=(size))
    for i in range(size-1):
        M_mejor[i] = np.mean(M_mejor[i+1:])
    
    return M_mejor

NUM_EJECUCIONES = 100
SIZES = np.linspace(4, 100, 200, dtype=int)
T_mejor = np.zeros(len(SIZES))
T_normal = np.zeros(len(SIZES))
T_peor = np.zeros(len(SIZES))

for _ in range(NUM_EJECUCIONES):
    for i, size in enumerate(SIZES):

        M_mejor = mejorArray(size)
        M_normal = np.linspace(1, size*2, size)
        M_peor =  np.sort(np.linspace(1, size*2, size))
        
        T_mejor[i] += getTiempo(M_mejor)
        T_normal[i] += getTiempo(M_normal)
        T_peor[i] += getTiempo(M_peor)

T_mejor /= NUM_EJECUCIONES
T_normal /= NUM_EJECUCIONES
T_peor /= NUM_EJECUCIONES


plt.plot(SIZES, T_mejor, color="red", label="Mejor Caso")
plt.plot(SIZES, T_normal, color="green", label="Caso Normal")
plt.plot(SIZES, T_peor, color="blue", label="Peor Caso")

FACTOR = 10**(-7)

x = np.linspace(1, 100, 200, dtype=int)
plt.plot(x, x * np.log2(x) * FACTOR, color="orange", label="nlog(n)")
plt.plot(x, x ** 2 * FACTOR, color="purple", label="n**2")


plt.legend()
plt.savefig("P1.3/E2.png")
plt.show()