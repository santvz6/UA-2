import numpy as np


def salvar_princesa(mazmorra: np.array, max_daño = 0):
    """
    Inicio = (0, 0)
    Fin = (i, j)

    [ x |   |   |   ]     
    [   |   |   |   ] ->  [ x |   |   |   ] -> ... -> [ x ]
    [   |   |   |   ]     [   |   |   |   ]
    
    Movimientos Disponibles: Este, Sur
    Este: j+1 -> Quitar la columna 0
    Sur: i+1 -> Quitar la fila 0

    Cada camino tiene que tener ALGO que guarde la menor cantidad que llegó a obtener
    """
    mazmorra = np.atleast_2d(mazmorra)
    maximos_daño = list()

    # Mapa tamaño 1x1
    if np.shape(mazmorra) == (1, 1):
        if mazmorra[0, 0] + max_daño < max_daño:
            max_daño += mazmorra[0, 0] 
        return max_daño
    
    # Mapa tamaño ix1
    if np.shape(mazmorra)[1] == 1:
        # Limitado a moverse al Sur / Vector columna    
        if mazmorra[1, 0] + max_daño < max_daño:
            max_daño += mazmorra[1, 0]

        maximos_daño.append(salvar_princesa(mazmorra[1:, :]), max_daño)

    # Mapa tamaño 1xj
    elif np.shape(mazmorra)[0] == 1:
        # Limitado a moverse al Este / Vector fila
        if mazmorra[0, 1] + max_daño < max_daño:
            max_daño += mazmorra[0, 1]

        maximos_daño.append(mazmorra[0, 1] + salvar_princesa(mazmorra[:, 1:]), max_daño)

    # Mapa tamaño ixj
    else:
        # Probamos ir al Sur
        if mazmorra[1, 0] + max_daño < max_daño:
            max_daño += mazmorra[1, 0]
        maximos_daño.append(mazmorra[1, 0] +  salvar_princesa(mazmorra[1:, :]), max_daño)
        # Probamos ir al Este
        if mazmorra[0, 1] + max_daño < max_daño:
            max_daño += mazmorra[0, 1]
        maximos_daño.append(mazmorra[0, 1] + salvar_princesa(mazmorra[:, 1:]), max_daño)
    
    # el maximo daño -> menos daño haya recibido
    return max(maximos_daño)

mazmorra = np.array([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])

print(salvar_princesa(mazmorra))

"""
El problema es que max_daño no se tiene en cuenta en las siguientes iteraciones
"""