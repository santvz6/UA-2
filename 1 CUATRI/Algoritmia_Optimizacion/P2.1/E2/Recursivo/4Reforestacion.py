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

def plantar(arr, nivel = 0):
    print("Nivel:", nivel, "\nArray actual:\n", arr)  # Imprime el estado actual del array y el nivel
    arr = np.atleast_2d(arr) # lo transforma en un array bidimensional siempre (1, j)
    if np.shape(arr) == (1, 1):
        print(f"Llegada a la posición final en nivel {nivel}")  # Mensaje cuando se llega a la meta
        return 0
    
    # Vector Columna (i, 1) (Solo tiene una columna)
    # Vector fila (1, j) (Solo tiene una fila)
    

    i = 0
    j = np.shape(arr)[1] - 1
    puntuacion = [np.inf]

    # Vector fila: No se puede mover al Sur ni Diag
    if np.shape(arr)[0] == 1:
        if arr[i, j-1] == 0:
            print(f"Moviendo Oeste en nivel {nivel}")  # Mensaje al moverse al Oeste
            puntuacion.append(1+plantar(arr[:, :j], nivel+1))

        
    # Vector columna: No se puede mover al Oeste ni Diag
    elif np.shape(arr)[1] == 1:
        if arr[i+1, j] == 0:
            print(f"Moviendo Sur en nivel {nivel}")  # Mensaje al moverse al Sur
            puntuacion.append(1+plantar(arr[1:, :], nivel+1))
    
    else:
        # Mov. Oeste
        if arr[i, j-1] == 0:
            print(f"Intentando mover Oeste en nivel {nivel}")  # Intento de mover al Oeste
            puntuacion.append(1+plantar(arr[:, :j], nivel+1))
        # Mov. Sur
        if arr[i+1, j] == 0:
            print(f"Intentando mover Sur en nivel {nivel}")  # Intento de mover al Sur
            puntuacion.append(1+plantar(arr[1:, :], nivel+1))
        # Mov. Diag
        if arr[i+1, j-1] == 0:
            print(f"Intentando mover Diagonal en nivel {nivel}")  # Intento de mover Diagonal
            puntuacion.append(1+plantar(arr[1:, :j], nivel+1))
    
    mejor_ruta = min(puntuacion)
    print(f"Mejor ruta encontrada en nivel {nivel} es de {mejor_ruta} pasos")  # Resultado del nivel actual
    return mejor_ruta
    

array = np.array([[0, 0, 0, 0],[0, 1, 1, 0], [0, 1, 0, 0]])

res = plantar(array)
print("Número mínimo de pasos:", res)
