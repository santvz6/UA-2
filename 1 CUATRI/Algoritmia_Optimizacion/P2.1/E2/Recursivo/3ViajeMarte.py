import numpy as np

def viajar(costes: np.array, volumenes: np.array, n:int , S=10):

    if n == -1:
        """
        Obligatoriamente hay que completar la bodega.
        Si no se ha llenado entonces los costes son infinitos
        """
        return 0 if S == 0 else float('inf')

    costes_totales = list()

    # Agarramos el suministro
    if S - volumenes[n] >= 0:
        costes_totales.append(costes[n] + viajar(costes, volumenes, n-1, S-volumenes[n]))
    
    # Probamos no agarrar el suministro
    costes_totales.append(0 + viajar(costes, volumenes, n-1, S))    

    return min(costes_totales) 

costes = np.array([3, 2, 5, 4, 1])
volumenes = np.array([4, 3, 2, 5, 1])
print(viajar(costes, volumenes, len(costes)-1))
