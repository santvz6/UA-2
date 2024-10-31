import numpy as np

def director_deportivo(valoraciones: np.array, fichas: np.array,  n: int, G=3000):
    if G == 0 or n == -1:
        return 0
    
    valoracion_final = list()

    # Si hay espacio agarro el objeto
    if G - fichas[n] >= 0:
        valoracion_final.append(valoraciones[n] + director_deportivo(valoraciones, fichas, n-1, G-fichas[n]))

    # Probamos la opción de no agarrar
    valoracion_final.append(0 + director_deportivo(valoraciones, fichas, n-1, G))

    return max(valoracion_final)

valoraciones = np.array([6, 1, 3, 8])
fichas = np.array([950, 2400, 500, 2000])
print(director_deportivo(valoraciones, fichas, len(valoraciones)-1))