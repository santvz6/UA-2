import numpy as np

def planear_gira(C: int, R: int, entradas_dia: np.array, n):
    
    mem = np.zeros((n+1, C+1))

    for i in range(1, n+1):
        for j in range(C+1):

            # No podemos agarrar un concierto
            if j < 1:
                mem[i, j] = mem[i-1, j]
            
            # Podemos agarrar un concierto
            else:
                anterior = mem[i-R, j-1] if i-R > 0 else 0
                mem[i, j] = max(entradas_dia[i-1] + anterior, mem[i-1, j])
                 
    return mem
    

entradasDia = np.array([3000, 6000, 7000, 8000, 9000])
beneficios = planear_gira(3, 3, entradasDia, len(entradasDia))

print(beneficios)


def backtracking(mem, n, C, R, entradas_dia):
    solucion = list()
    i, c = n, C
    while i > 0 and c > 0:
        anterior = mem[i - R, c - 1] if i-R > 0 else 0
        
        a = entradas_dia[i-1] + anterior
        b = mem[i-1][c]
        
        # Se realiza concierto
        if mem[i, c] == a:     
            i -= R
            c -= 1
            solucion += [i]

        # No se realiza concierto
        else:
            i -= 1
        
    return solucion

solucion = backtracking(mem= beneficios, n=len(entradasDia)-1, C=3, R=3, entradas_dia=entradasDia)
print(f"Solcuión: {solucion}")