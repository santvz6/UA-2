def particion(n, pivote):
    izq = []
    der = []
    for i in range(1, len(n)):  # Comienzo desde el segundo elemento
        if n[i] <= pivote:
            izq.append(n[i])
        else:
            der.append(n[i])
    return izq, der

def quicksort(n):
    nl = len(n)
    if nl <= 1:
        return n
    
    pivote = n[0]  # Primer elemento como pivote
    izq, der = particion(n, pivote)
    
    # Llamadas recursivas a quicksort en los subarreglos
    return quicksort(izq) + [pivote] + quicksort(der)

# Ejemplo de uso
arreglo = [3, 6, 2, 8, 5]
resultado = quicksort(arreglo)
print(resultado)  # Debería imprimir [2, 3, 5, 6, 8]
