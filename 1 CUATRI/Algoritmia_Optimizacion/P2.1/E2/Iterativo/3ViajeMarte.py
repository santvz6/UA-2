import numpy as np

def viajar(costes: np.array, volumenes: np.array, n:int , S=10):
    mem = np.zeros((n+1, S+1))
    mem[:,1:] = np.inf

    for i in range(1, n+1):
        for j in range(S+1):
            # i-2 NO hace referencia al volumen anterior
            if volumenes[i-1] > j:

                mem[i, j] = mem[i-1, j]
            else:
                # costes [i-1] TAMPOCO HACE REFERENCIA al anterior
                mem[i, j] = min(mem[i-1, j], costes[i-1] + mem[i-1, j-volumenes[i-1]])    
    return mem


costes = np.array([3, 2, 5, 4, 1])
volumenes = np.array([4, 3, 2, 5, 1])
viaje = viajar(costes, volumenes, len(costes))
print(viaje)

def backtracking(mem, costes, volumenes, n, S=10):
    i, s = n, S
    solucion = list()

    while i>0 and S>0:

        a = mem[i-1, s]
        b = costes[i-1] + mem[i-1, s-volumenes[i-1]]

        if b == mem[i, s]:
            solucion += [i]         
            i -= 1
            s -= volumenes[i-1]
            
        
        else:
            i-=1
    
    return solucion

solcuion = backtracking(viaje, costes, volumenes, len(costes))
print(solcuion)
