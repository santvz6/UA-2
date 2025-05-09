import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

############################
# Ejercicio 1
# Se lanzan dos dados y se considera la variable aleatoria que asocia a cada resultado el mayor de los números obtenidos.
# a) Función de probabilidad asociada
# b) Función de distribución asociada


# a) Función de probabilidad
def probabilidad():
    outcomes = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    max_values = [max(i, j) for i, j in outcomes]
    max_values_count = {i: max_values.count(i) for i in range(1, 7)}

    prob = {i: count / 36 for i, count in max_values_count.items()}
    return prob

# b) Función de distribución
def distribucion(prob):
    distrib = {}
    cumulative_prob = 0
    for i in range(1, 7):
        cumulative_prob += prob.get(i, 0)
        distrib[i] = cumulative_prob
    return distrib

# Calcular probabilidad y distribución
prob = probabilidad()
distrib = distribucion(prob)

# Resultados
print("Función de probabilidad:", prob)
print("Función de distribución:", distrib)

# Graficar función de distribución
plt.step(distrib.keys(), distrib.values(), where="post")
plt.title("Función de distribución acumulada")
plt.xlabel("Valor máximo obtenido")
plt.ylabel("Probabilidad acumulada")
plt.show()
############################


############################
# Ejercicio 2
# Hallar la media, varianza y desviación típica de la variable aleatoria

def estadisticas(prob):
    media = sum(i * p for i, p in prob.items())
    varianza = sum((i - media)**2 * p for i, p in prob.items())
    desviacion_tipica = np.sqrt(varianza)
    
    return media, varianza, desviacion_tipica

# Calcular estadísticos
media, varianza, desviacion_tipica = estadisticas(prob)

# Resultados
print("Media:", media)
print("Varianza:", varianza)
print("Desviación típica:", desviacion_tipica)
############################


############################
# Ejercicio 3
# Un jugador lanza tres monedas. Recibe 100 €, si salen tres caras; 25 €, si salen 2 caras; y nada si sale cualquier otra combinación.
# Calcular el precio de la apuesta para que el juego sea equitativo

def probabilidad_moneda():
    resultados = [
        ('C', 'C', 'C'), ('C', 'C', 'S'), ('C', 'S', 'C'), ('C', 'S', 'S'),
        ('S', 'C', 'C'), ('S', 'C', 'S'), ('S', 'S', 'C'), ('S', 'S', 'S')
    ]
    pagos = {('C', 'C', 'C'): 100, ('C', 'C', 'S'): 25, ('C', 'S', 'C'): 25,
             ('S', 'C', 'C'): 25, ('S', 'S', 'S'): 0, ('S', 'S', 'C'): 0,
             ('S', 'C', 'S'): 0, ('C', 'S', 'S'): 0}

    probabilidad_pagos = {}
    for resultado in resultados:
        probabilidad_pagos[resultado] = pagos.get(resultado, 0)

    # Calcular el valor esperado
    valor_esperado = sum(pagos.get(resultado, 0) / 8 for resultado in resultados)
    return valor_esperado

# Precio de la apuesta
precio_apuesta = probabilidad_moneda()

# Imprimir resultado
print("Precio de la apuesta:", precio_apuesta)
############################


############################
# Ejercicio 4
# Probabilidades de tener un número determinado de varones en una familia con seis hijos, considerando la probabilidad de que nazca niño sea 0,50

def probabilidad_varones():
    # Parámetros de la distribución binomial
    n = 6  # Número de ensayos
    p = 0.5  # Probabilidad de éxito (nacer niño)
    
    # a) Probabilidad de que todos sean varones
    prob_todos_varones = binom.pmf(6, n, p)
    
    # b) Probabilidad de al menos dos varones
    prob_al_menos_dos = 1 - binom.cdf(1, n, p)
    
    # c) Probabilidad de tres varones
    prob_tres_varones = binom.pmf(3, n, p)
    
    # d) Media y desviación típica
    media = n * p
    desviacion_tipica = np.sqrt(n * p * (1 - p))

    return prob_todos_varones, prob_al_menos_dos, prob_tres_varones, media, desviacion_tipica

# Calcular probabilidades y estadísticas
prob_todos_varones, prob_al_menos_dos, prob_tres_varones, media, desviacion_tipica = probabilidad_varones()

# Resultados
print("Probabilidad de todos varones:", prob_todos_varones)
print("Probabilidad de al menos dos varones:", prob_al_menos_dos)
print("Probabilidad de tres varones:", prob_tres_varones)
print("Media:", media)
print("Desviación típica:", desviacion_tipica)
############################


############################
# Ejercicio 5
# Una prueba de inteligencia está compuesta por 10 preguntas. Se pide: 
# a) Probabilidad de acertar exactamente 4 preguntas; 
# b) Probabilidad de no acertar ninguna pregunta; 
# c) Probabilidad de acertar al menos 3; 
# d) Probabilidad de acertar al menos m; 
# e) Probabilidad de acertar sólo 2.

from scipy.stats import binom

def probabilidad_aciertos(m=5):
    n = 10  # Número de preguntas
    p = 1 / 4  # Probabilidad de acertar una pregunta

    # a) Probabilidad de acertar exactamente 4 preguntas
    prob_4 = binom.pmf(4, n, p)
    
    # b) Probabilidad de no acertar ninguna pregunta
    prob_0 = binom.pmf(0, n, p)
    
    # c) Probabilidad de acertar al menos 3 preguntas
    prob_al_menos_3 = 1 - binom.cdf(2, n, p)

    # d) Probabilidad de acertar al menos m
    prob_al_menos_m = 1 - binom.cdf(m-1, n, p)

    # e) Probabilidad de acertar solo 2
    prob_2 = binom.pmf(2, n, p)
    
    return prob_4, prob_0, prob_al_menos_3, prob_al_menos_m, prob_2

# Calcular las probabilidades
m = 5
prob_4, prob_0, prob_al_menos_3, prob_al_menos_m, prob_2 = probabilidad_aciertos(m)

# Resultados
print("Probabilidad de acertar 4 preguntas:", prob_4)
print("Probabilidad de no acertar ninguna pregunta:", prob_0)
print("Probabilidad de acertar al menos 3 preguntas:", prob_al_menos_3)
print(f"Probabilidad de acertar al menos {m} preguntas:", prob_al_menos_m)
print("Probabilidad de acertar exactamente 2 preguntas:", prob_2)
############################


############################
# Ejercicio 6
# En el lanzamiento de tres dados, consideramos la variable aleatoria que cuenta cuántos múltiplos de 3 aparecen.
# a) Función de probabilidad
# b) Función de distribución
# c) Media y desviación típica

def probabilidad_multiplo_tres():
    # Posibles resultados de los dados (1 a 6)
    resultados = [(i, j, k) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)]
    # Número de múltiplos de tres que aparecen
    multiples_de_tres = [sum(1 for x in (i, j, k) if x % 3 == 0) for (i, j, k) in resultados]
    
    # Contar cuántos casos hay para cada cantidad de múltiplos de 3
    cuenta = {i: multiples_de_tres.count(i) for i in range(4)}
    prob = {i: cuenta[i] / 216 for i in cuenta}
    
    return prob

def distribucion_multiplo_tres(prob):
    distrib = {}
    acumulada = 0
    for i in range(4):
        acumulada += prob.get(i, 0)
        distrib[i] = acumulada
    return distrib

# a) Calcular la probabilidad
prob = probabilidad_multiplo_tres()

# b) Calcular la distribución
distrib = distribucion_multiplo_tres(prob)

# c) Media y desviación típica
media = sum(i * prob[i] for i in prob)
varianza = sum((i - media) ** 2 * prob[i] for i in prob)
desviacion_tipica = np.sqrt(varianza)

# Imprimir resultados
print("Función de probabilidad:", prob)
print("Función de distribución acumulada:", distrib)
print("Media:", media)
print("Desviación típica:", desviacion_tipica)

# Graficar la función de distribución
plt.step(distrib.keys(), distrib.values(), where="post")
plt.title("Función de distribución acumulada de múltiplos de 3")
plt.xlabel("Número de múltiplos de 3")
plt.ylabel("Probabilidad acumulada")
plt.show()
############################


############################
# Ejercicio 7
# El 30% de un pueblo ve un concurso. Se llama a 10 personas al azar. Calcular la probabilidad de que:
# a) Más de ocho personas están viendo el programa.
# b) Algunas de las diez personas.
# c) Calcular la media y desviación típica.

def probabilidad_concurso():
    # Parámetros de la distribución binomial
    n = 10  # Número de personas
    p = 0.3  # Probabilidad de ver el programa
    
    # a) Probabilidad de que más de ocho personas estén viendo el programa
    prob_mas_de_ocho = 1 - binom.cdf(8, n, p)
    
    # b) Probabilidad de que algunas de las 10 personas vean el programa
    prob_al_menos_1 = 1 - binom.pmf(0, n, p)
    
    # c) Media y desviación típica
    media = n * p
    desviacion_tipica = np.sqrt(n * p * (1 - p))

    return prob_mas_de_ocho, prob_al_menos_1, media, desviacion_tipica

# Calcular probabilidades y estadísticas
prob_mas_de_ocho, prob_al_menos_1, media, desviacion_tipica = probabilidad_concurso()

# Imprimir resultados
print("Probabilidad de que más de ocho personas vean el programa:", prob_mas_de_ocho)
print("Probabilidad de que algunas de las diez personas vean el programa:", prob_al_menos_1)
print("Media:", media)
print("Desviación típica:", desviacion_tipica)
############################


############################
# Ejercicio 8
# Una sucursal bancaria atiende, en promedio, a 6 clientes por día.
# a) Definir la variable aleatoria y distribución
# b) Calcular la probabilidad de que atienda exactamente a 4 clientes
# c) Calcular la probabilidad de que atienda al menos a 6 clientes
# d) Calcular la probabilidad de que reciba entre 6 y 8 clientes
# e) Obtener la mediana de la variable
# f) Generar una muestra de 10 valores aleatorios

from scipy.stats import poisson

def probabilidad_clientes():
    # Parámetro de la distribución de Poisson (media 6 clientes por día)
    lambda_ = 6
    
    # b) Probabilidad de que atienda exactamente 4 clientes
    prob_4 = poisson.pmf(4, lambda_)
    
    # c) Probabilidad de que atienda al menos 6 clientes
    prob_al_menos_6 = 1 - poisson.cdf(5, lambda_)
    
    # d) Probabilidad de que reciba entre 6 y 8 clientes
    prob_entre_6_8 = poisson.cdf(8, lambda_) - poisson.cdf(5, lambda_)
    
    # e) Mediana
    mediana = poisson.ppf(0.5, lambda_)
    
    # f) Generar una muestra de 10 valores aleatorios
    muestra = poisson.rvs(lambda_, size=10)
    
    return prob_4, prob_al_menos_6, prob_entre_6_8, mediana, muestra

# Calcular probabilidades, mediana y muestra
prob_4, prob_al_menos_6, prob_entre_6_8, mediana, muestra = probabilidad_clientes()

# Imprimir resultados
print("Probabilidad de atender exactamente 4 clientes:", prob_4)
print("Probabilidad de atender al menos 6 clientes:", prob_al_menos_6)
print("Probabilidad de atender entre 6 y 8 clientes:", prob_entre_6_8)
print("Mediana de la distribución:", mediana)
print("Muestra aleatoria de 10 valores:", muestra)
############################


############################
# Ejercicio 9
# Un estudiante tiene un peso normal de media 70 kg y desviación típica 3 kg. Calcular:
# a) La probabilidad de que el estudiante pese entre 60 kg y 75 kg.
# b) La probabilidad de que el estudiante pese más de 75 kg.
# c) La probabilidad de que el estudiante pese 64 kg o menos.
# d) El peso mínimo del 10% de los estudiantes que más pesan.
# e) Generar 12 pesos aleatorios siguiendo esta distribución.

from scipy.stats import norm

def probabilidad_peso():
    # Parámetros de la distribución normal
    mu = 70  # media
    sigma = 3  # desviación típica
    
    # a) Probabilidad de que el estudiante pese entre 60 kg y 75 kg
    prob_entre_60_75 = norm.cdf(75, mu, sigma) - norm.cdf(60, mu, sigma)
    
    # b) Probabilidad de que el estudiante pese más de 75 kg
    prob_mas_75 = 1 - norm.cdf(75, mu, sigma)
    
    # c) Probabilidad de que el estudiante pese 64 kg o menos
    prob_menos_64 = norm.cdf(64, mu, sigma)
    
    # d) Peso mínimo del 10% de los estudiantes que más pesan
    peso_min_10 = norm.ppf(0.9, mu, sigma)
    
    # e) Generar 12 pesos aleatorios
    muestra = norm.rvs(mu, sigma, size=12)
    
    return prob_entre_60_75, prob_mas_75, prob_menos_64, peso_min_10, muestra

# Calcular probabilidades, peso mínimo y muestra
prob_entre_60_75, prob_mas_75, prob_menos_64, peso_min_10, muestra = probabilidad_peso()

# Imprimir resultados
print("Probabilidad de que pese entre 60 y 75 kg:", prob_entre_60_75)
print("Probabilidad de que pese más de 75 kg:", prob_mas_75)
print("Probabilidad de que pese 64 kg o menos:", prob_menos_64)
print("Peso mínimo del 10% de los estudiantes que más pesan:", peso_min_10)
print("Muestra aleatoria de 12 pesos:", muestra)
############################


############################
# Ejercicio 10
# La glucosa en sangre sigue una distribución normal con media 106 mg/100 ml y desviación típica 8 mg/100 ml.
# a) Probabilidad de que el nivel de glucosa sea inferior a 120 mg/100 ml.
# b) ¿Qué porcentaje de diabéticos tienen niveles de glucosa entre 90 y 130 mg/100 ml?
# c) El valor que caracteriza el 25% de diabéticos con nivel inferior.
# d) Generar una muestra de tamaño 12 para esta distribución.

def probabilidad_glucosa():
    # Parámetros de la distribución normal
    mu = 106  # media
    sigma = 8  # desviación típica
    
    # a) Probabilidad de que el nivel de glucosa sea inferior a 120 mg/100 ml
    prob_inferior_120 = norm.cdf(120, mu, sigma)
    
    # b) Porcentaje de diabéticos con niveles de glucosa entre 90 y 130 mg/100 ml
    prob_entre_90_130 = norm.cdf(130, mu, sigma) - norm.cdf(90, mu, sigma)
    
    # c) Valor del 25% de diabéticos con nivel inferior
    valor_25 = norm.ppf(0.25, mu, sigma)
    
    # d) Generar una muestra de tamaño 12
    muestra = norm.rvs(mu, sigma, size=12)
    
    return prob_inferior_120, prob_entre_90_130, valor_25, muestra

# Calcular probabilidades y generar muestra
prob_inferior_120, prob_entre_90_130, valor_25, muestra = probabilidad_glucosa()

# Imprimir resultados
print("Probabilidad de que la glucosa sea inferior a 120 mg/100 ml:", prob_inferior_120)
print("Porcentaje de diabéticos entre 90 y 130 mg/100 ml:", prob_entre_90_130)
print("Valor del 25% de diabéticos con nivel inferior:", valor_25)
print("Muestra aleatoria de 12 valores de glucosa:", muestra)
############################
