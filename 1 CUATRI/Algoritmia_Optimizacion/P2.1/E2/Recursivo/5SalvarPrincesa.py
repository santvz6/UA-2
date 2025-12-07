import numpy as np


def salvar_princesa(mazmorra: np.array, max_daño = 0, puntos_obtenidos = 0):
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

    maxdaño_E_S = list()

    mazmorra = np.atleast_2d(mazmorra)

    # get MAX DAÑO recibido hasta el momento
    if puntos_obtenidos + mazmorra[0, 0] < max_daño:
        max_daño = puntos_obtenidos + mazmorra[0, 0]
    # get puntuación actual del PATH
    puntos_obtenidos += mazmorra[0, 0]

    # Mapa tamaño 1x1
    if np.shape(mazmorra) == (1, 1):   
        # -1: porque el rey no puede llegar a 0 de vida, mínimo 1
        return max_daño-1
    
    # Mapa tamaño ix1
    if np.shape(mazmorra)[1] == 1:
        # Limitado a moverse al Sur / Vector columna    
        return salvar_princesa(mazmorra[1:, :], max_daño, puntos_obtenidos)

    # Mapa tamaño 1xj
    elif np.shape(mazmorra)[0] == 1:
        # Limitado a moverse al Este / Vector fila
        return salvar_princesa(mazmorra[:, 1:], max_daño, puntos_obtenidos)

    

    # Mapa tamaño ixj
    else:
        """
        En los casos de mapa ixj podemos ir al Sur o al Este
        Dependiendo de donde vayamos obtendremos un resultado u otro
        Por eso utilizaremos una lista para luego hacer max sobre ella
        """
        # Probamos ir al Sur
        maxdaño_E_S.append(salvar_princesa(mazmorra[1:, :], max_daño, puntos_obtenidos))
        # Probamos ir al Este
        maxdaño_E_S.append(salvar_princesa(mazmorra[:, 1:], max_daño, puntos_obtenidos))
    
    # el maximo daño -> menos daño haya recibido
    return max(maxdaño_E_S)

mazmorra = np.array([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])

print(salvar_princesa(mazmorra))

"""
El problema es que max_daño no se tiene en cuenta en las siguientes iteraciones
"""