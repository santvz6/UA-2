def colorear(ordenado, nodo, j):
    pass

def colorearGrafos(adjacencyArray):

    num_aristas = list()
    for fila in adjacencyArray:
       num_aristas.append(fila.count(1))
    
    # (Nodo, num_aristas)
    agrupado = zip(list(range(1, len(adjacencyArray)+1)), num_aristas)

    # Ordenamos con key = num_aristas y orden descendente
    # Resultado Ordenado: (nodo, num_aristas, color)
    ordenado = [(nodo, aristas, None) for nodo, aristas in sorted(agrupado, key=lambda x: x[1], reverse=True)]
    
    visitados = list()
    for nodo, aristas, color in ordenado:
        for j in range(len(ordenado)):
            mirando = array[nodo-1][j] # nodo - 1: porque empezamos en 1
            if  mirando == 1 and mirando not in visitados:
                colorear(ordenado, nodo, j)
                visitados.append(j)
                break   # siguiente nodo
            continue    # siguiente iteración

    return ordenado

array = [
 [0, 1, 0, 0, 1, 1, 0, 0, 0, 0], # 1
 [1, 0, 1, 0, 0, 0, 1, 0, 0, 0], # 2
 [1, 1, 0, 1, 0, 0, 0, 1, 0, 0], # 3
 [0, 0, 1, 0, 1, 0, 0, 0, 1, 0], # 4
 [1, 0, 0, 1, 0, 0, 0, 0, 0, 1], # 5
 [1, 0, 0, 0, 0, 0, 0, 1, 1, 0], # 6
 [0, 1, 0, 0, 0, 0, 0, 0, 1, 1], # 7
 [0, 0, 1, 0, 0, 1, 0, 0, 0, 1], # 8
 [0, 0, 0, 1, 0, 1, 1, 0, 0, 0], # 9
 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0]] # 10

solucion = colorearGrafos(array)

print(solucion)