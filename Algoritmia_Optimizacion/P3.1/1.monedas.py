import numpy as np

def cambio_monedas(M:int, C :tuple):

    solucion = list()

    # C: Es un conjunto, no hay repetición de elementos 

    # 1. Ordenar de mayor a menor
    ordenado = sorted(C, reverse=True)

    S = np.zeros(len(ordenado), dtype=int)

    # 2. Comprobamos que monedas podemos elegir
    while True:
        # Miramos todas las posibles monedas
        for index, moneda in enumerate(ordenado):
            # Podemos agarrar dicha moneda
            if moneda <= M:
                M -= moneda
                solucion.append(moneda)
                S[index] += 1
                # Salimos del bucle for para volver a entrar
                # Podríamos optimizar el código haciendo que el nuevo bucle
                # for empiece desde el indice en el que hemos acabado
                break
        # Cuando ya no quede espacio salimos del bucle while
        if M < 1:
            break 

    return solucion, S

M = 169
C = (200, 100, 50, 20, 10, 5, 2, 1)
S = cambio_monedas(M, C)

print(f"""
Solución Monedas -> {S[0]}
Solución Cantidad -> {S[1]}
""")
