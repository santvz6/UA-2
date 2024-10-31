import numpy as np

def viajar(costes: np.array, volumenes: np.array, n:int , S=10):
    mem = np.zeros((n, S+1))
    mem[:,1:] = np.inf
    for i in range(n):
        for j in range(S+1):
            if volumenes[i] > j:
                mem[i, j] = mem[i-1, j]
            else:
                mem[i, j] = min(mem[i-1, j], costes[i] + mem[i-1, j-volumenes[i]])    
    return mem

costes = np.array([3, 2, 5, 4, 1])
volumenes = np.array([4, 3, 2, 5, 1])
viaje = viajar(costes, volumenes, len(costes))
print(viaje)
