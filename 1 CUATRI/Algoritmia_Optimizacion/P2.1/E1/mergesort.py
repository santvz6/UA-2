def mezclar(v_i, v_d):
    i = d = 0
    resultado = list()

    while i < len(v_i) and d < len(v_d):
        if v_i[i] <= v_d[d]:
            resultado.append(v_i[i]) # podriamos hacer += [v_i[1]]
            i+=1
        else:
            resultado.append(v_d[d])
            d+=1

    # Añadimos lo restante
    resultado += v_i[i:]
    resultado += v_d[d:]

    return resultado

def mergesort(v):
    vl = len(v)
    if vl <= 1:
        return v
    
    mitad = vl // 2
    v_i = mergesort(v[:mitad])
    v_d = mergesort(v[mitad:])
    
    return mezclar(v_i, v_d)


print(mergesort([5,4,1,7,2,9,4,1]))