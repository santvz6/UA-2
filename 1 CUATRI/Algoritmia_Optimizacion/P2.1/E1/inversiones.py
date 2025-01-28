def contar_inversiones(v_izq, v_der):
    i = d = 0
    count = 0
    result = []
    
    while i < len(v_izq) and d < len(v_der):
        if v_izq[i] <= v_der[d]:
            result.append(v_izq[i])
            i += 1

        # v[i] > v[j] and i < j
        else:
            """Todos los elementos restantes en v_izq son mayores que v_der[d]

            [4, 5, 5] [1, 2, 3, 5] -> todos los elementos de [4, 5, 5] son mayores que [1]
            siempre que v[i] > v[j]
            """
            count += len(v_izq) - i  # Todas las posiciones restantes de v_izq forman una inversión
            result.append(v_der[d])
            d += 1
    
    # Agregar el resto de los elementos
    result += v_izq[i:]
    result += v_der[d:]
    
    return result, count


def inversiones(v):
    """
    Usaremos el esqueleto de Merge Sort para la recursividad
    y tendremos una función para contar las inversiones
    """

    # le llega un vector 
    if len(v) <= 1:
        return v, 0
    
    mitad = len(v)//2
    v_izq, ci = inversiones(v[:mitad])
    v_der, cd = inversiones(v[mitad:])

    v, cm = contar_inversiones(v_izq, v_der)

    return (v, ci + cd + cm)

# Obtenemos la lista ordenada y las inversiones

v = [4,3,7,0]
print(inversiones(v))