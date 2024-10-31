"""
Objetivo:

Llegar de Inicio a Fin en el menor num. pasos.

Posicion Inicial (0, j-1)
Posicion Final (i-1, 0)

Mov. Oeste (j-=1)
Mov. Sur (i+=1)
Mov. Diag (i+=1, j-=1)

Caso Base: Mapa 1x1 (llegar a la posicion final return 0)
Caso Fácil 1: mapa 2x2

"""
import numpy as np

def plantar(arr:np.array):
    
    I, J = np.shape(arr)
    mem = np.zeros((I+1, J+1)) + np.inf # la memoria cotniene una fila y columna extra
    mem[0, J-1] = mem[1, J] = -1        # Primeros dos posibles movimientos 

    for i in range(1, I+1):
        for j in range(J-1, -1, -1):
            if arr[i-1, j] == 0:
                mem[i, j] = min(1 + mem[i-1, j], 1 + mem[i, j+1])

    return mem
    

array = np.array([[0, 0, 0, 0],
                  [0, 1, 1, 0],
                  [0, 1, 0, 0]])

res = plantar(array)
print(res)
