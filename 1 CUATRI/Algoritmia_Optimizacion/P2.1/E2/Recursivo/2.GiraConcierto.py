import numpy as np

def planear_gira(C: int, R: int, entradas_dia: np.array, n):
    
    if n < 0:
        return 0
    
    max_beneficios = list()

    # Todavía puedo agarrar un concierto
    if C > 0:

        # Agarro el concierto
        max_beneficios.append(entradas_dia[n] + planear_gira(C-1, R, entradas_dia, n-R))

    # No agarro el concierto
    max_beneficios.append(planear_gira(C, R, entradas_dia, n-1))
    
    return max(max_beneficios)
    

entradasDia = np.array([3000, 6000, 7000, 8000, 9000])
beneficios = planear_gira(3, 3, entradasDia, len(entradasDia)-1)

print(beneficios)