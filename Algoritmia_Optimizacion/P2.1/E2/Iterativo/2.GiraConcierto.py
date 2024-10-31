import numpy as np

def planear_gira(C: int, R: int, entradas_dia: np.array, n):
    
    mem = np.zeros((n, C))

    for i in range(n):
        for j in range(C-1, -1, -1):

            # No podemos agarrar un concierto
            if j < 1:
                mem[i, j] = mem[i-1, j]
            
            # Podemos agarrar un concierto
            else:
                mem[i, j] = max(entradas_dia[i] + mem[i-1, j-R], mem[i-1, j])
                
                if mem[i, j] = entradas_dia[i] + mem[i-1, j-R]:
                    pass


        return mem
    

entradasDia = np.array([3000, 6000, 7000, 8000, 9000])
beneficios = planear_gira(3, 3, entradasDia, len(entradasDia))

print(beneficios)