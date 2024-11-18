import numpy as np

G = 3000
valoraciones = np.array([6, 1, 3, 8])
fichas = np.array([950, 2400, 500, 2000])

mem = np.zeros((len(valoraciones), G+1)) - 1

def director_deportivo(valoraciones: np.array, fichas: np.array,  n: int, G=3000):
    global mem

    if mem[n, G] != -1:
        return mem[n, G]
    
    if G == 0 or n == -1:
        return 0
    
    valoracion_final = list()

    # Si hay espacio agarro el objeto
    if G - fichas[n] >= 0:
        valoracion_final.append(valoraciones[n] + director_deportivo(valoraciones, fichas, n-1, G-fichas[n]))

    # Probamos la opción de no agarrar
    valoracion_final.append(0 + director_deportivo(valoraciones, fichas, n-1, G))

    mem[n, G] = max(valoracion_final)
    return mem[n, G]



print(director_deportivo(valoraciones, fichas, len(valoraciones)-1, G))


print(mem)