import random
from scipy.special import comb

############################
# Ejercicio 1
# Determinar por enumeración el espacio muestral del lanzamiento triple de un dado.

def espacio_muestral_dado():
    posibles = {1, 2, 3, 4, 5, 6}
    espacio_muestral = set()
    for tiro1 in posibles:
        for tiro2 in posibles:
            for tiro3 in posibles:
                salida = (tiro1, tiro2, tiro3)
                espacio_muestral.add(salida)
    return espacio_muestral


############################
# Ejercicio 2
# Probabilidad de elegir una carta roja en una baraja de 52 cartas.
    
def probabilidad_carta_roja():
    num_cartas = 52
    num_cartas_rojas = num_cartas / 2
    return num_cartas_rojas / num_cartas

############################
# Ejercicio 3
# Probabilidad de sacar el as de picas dos veces seguidas.

def probabilidad_as_picas_doble():
    return (1/52) * (1/52)

############################
# Ejercicio 4
# Hallar la probabilidad de que un alumno suspenda en el examen de Matemáticas.

def probabilidad_suspender_matematicas():
    prob_aprobar = 0.67
    prob_suspender_economia = 0.10
    prob_suspender_valenciano = 0.09
    return 1 - (prob_aprobar + prob_suspender_economia + prob_suspender_valenciano)

############################
# Ejercicio 5
# Probabilidad de volver a sacar la misma carta tras barajar.

def probabilidad_misma_carta():
    return 1/52

############################
# Ejercicio 6
# Probabilidad de que la suma de dos bolas sacadas con reposición sea impar.

def probabilidad_suma_impar_reposicion():
    numeros = [1, 2, 3, 4, 5]
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 == 1]
    return (len(pares)/5) * (len(impares)/5) + (len(impares)/5) * (len(pares)/5)

############################
# Ejercicio 7
# Probabilidad de que la suma de dos bolas sin reposición sea impar.

def probabilidad_suma_impar_sin_reposicion():
    numeros = [1, 2, 3, 4, 5]
    casos_totales = 0
    casos_favorables = 0

    for i in range(len(numeros)):
        for j in range(len(numeros)):
            if i != j:  # Que no se repitan (sin reposición)
                casos_totales += 1
                if (numeros[i] + numeros[j]) % 2 == 1:  # Suma impar
                    casos_favorables += 1

    return casos_favorables / casos_totales


############################
# Ejercicio 8
# Probabilidad de sacar tres caras en cinco lanzamientos de moneda usando combinatoria.

def probabilidad_tres_caras():
    return comb(5, 3) * (0.5**5)

############################
# Ejercicio 9
# Simulación de extracción de 5 bolas con reemplazo y cálculo de probabilidades.

def simulacion_extraccion_bolas():
    colores = ['blanca'] * 10 + ['roja'] * 20 + ['verde'] * 30
    resultados = {'3_blancas_2_rojas': 0, 'mismo_color': 0}
    for _ in range(1000):
        extraccion = random.choices(colores, k=5)
        if extraccion.count('blanca') == 3 and extraccion.count('roja') == 2:
            resultados['3_blancas_2_rojas'] += 1
        if len(set(extraccion)) == 1:
            resultados['mismo_color'] += 1
    return {key: value/1000 for key, value in resultados.items()}

############################
# Ejercicio 10
# Función para calcular probabilidades en cinco lanzamientos de moneda.

def probabilidad_lanzamientos():
    return {k: comb(5, k) * (0.5**5) for k in range(6)}

############################
# Ejercicio 11
# Hallar la probabilidad de que ocurra el suceso Y.

def probabilidad_suceso_y():
    p_x = 0.4
    p_union = 0.6
    return (p_union - p_x) / (1 - p_x)

############################
# Ejercicio 12
# Probabilidad de que la bola roja haya sido extraída de la urna A usando Bayes.

def probabilidad_bola_roja_urna_A():
    prob_urna_A = prob_urna_B = prob_urna_C = 1/3
    prob_roja_dado_A = 3/8
    prob_roja_dado_B = 2/3
    prob_roja_dado_C = 2/5

    prob_bola_roja = (prob_urna_A * prob_roja_dado_A) + (prob_urna_B * prob_roja_dado_B) + (prob_urna_C * prob_roja_dado_C)
    
    return (prob_urna_A * prob_roja_dado_A) / prob_bola_roja

############################
# Ejercicio 13
# Probabilidad de que una puerta elegida al azar sea defectuosa.

def probabilidad_puerta_defectuosa():
    total_puertas = 380 + 270 + 350
    prob_grupo_A = 380 / total_puertas
    prob_grupo_B = 270 / total_puertas
    prob_grupo_C = 350 / total_puertas

    prob_defectuosa_A = 0.04
    prob_defectuosa_B = 0.03
    prob_defectuosa_C = 0.06

    return (prob_grupo_A * prob_defectuosa_A) + (prob_grupo_B * prob_defectuosa_B) + (prob_grupo_C * prob_defectuosa_C)

############################
# Ejercicio 14
# Probabilidad de que una papa de rechazo provenga del segundo proveedor usando Bayes.

def probabilidad_papa_rechazo_proveedor2():
    prob_proveedor_1 = 5/6
    prob_proveedor_2 = 1/6
    prob_rechazo_dado_1 = 0.2
    prob_rechazo_dado_2 = 0.1

    prob_papa_rechazo = (prob_proveedor_1 * prob_rechazo_dado_1) + (prob_proveedor_2 * prob_rechazo_dado_2)
    
    return (prob_proveedor_2 * prob_rechazo_dado_2) / prob_papa_rechazo
