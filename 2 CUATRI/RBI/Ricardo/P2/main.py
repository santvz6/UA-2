#############################
# Ejercicio 1
# Crea una función que admita como parámetros un número y las 
# cifras a redondear y devuelva el número introducido redondeado

def ejercicio1(num:float, cifras_redondeo:int) -> float:
    return float(round(number= num, ndigits= cifras_redondeo))

#############################
# Ejercicio 2
# Crea una función que admita dos números (verdadero y aproximado)
# y calcule el error absoluto.

def errorAbsoulto(num_verdadero:float, num_aproximado:float) -> float:
    return float(abs(num_verdadero - num_aproximado))

#############################
# Ejercicio 3
#  Crea una función que admita dos números (verdadero y aproximado)
#  y calcule el error relativo.

def errorRelativo(num_verdadero:float, num_aproximado:float) -> float:
    return float(abs((num_verdadero)-num_aproximado) / num_verdadero)

#############################
# Ejercicio 4
# Crea una función que admita dos vectores numéricos (verdadero y aproximado)
# y las cifras a redondear y calcule el error absoluto de la suma de los números.

def errorAbsolutoSuma(num_verdaderos:list[float], num_aproximados:list[float], cifras_redondeo:int) -> float:
    return float(round(number=abs(sum(num_verdaderos) - sum(num_aproximados)), ndigits= cifras_redondeo))

############################
# Ejercicio 5
# Añadele a la función anterior el código necesario 
# para que calcule tambien el error relativo.

def errorRelativoSuma(num_verdaderos:list[float], num_aproximados:list[float], cifras_redondeo:int) -> float:
    return float(round(number= abs((sum(num_verdaderos)-sum(num_aproximados)/sum(num_verdaderos)), ndigits= cifras_redondeo)))

############################
# Ejercicio 6
# Crea una función que admita dos vectores numéricos (verdadero y aproximado)
# y las cifras a redondear y calcule el error relativo del producto de los números.

def errorRelativoProducto(num_verdaderos:list[float], num_aproximados:list[float], cifras_redondeo:int) -> float:
    productoV = productoA = -1
    for verdadero, aproximado in zip(num_verdaderos, num_aproximados):
        productoV *= verdadero
        productoA *= aproximado
    return float(round(number= round(abs((productoV-productoA)/productoV)), ndigits= cifras_redondeo))

############################
# Ejercicio 7
# Crea una función que admita dos números y las cifras a
# redondear y cacule el error relativo del cociente.

def errorRelativoProducto(num1:float, num2:float, cifras_redondeo:int) -> float:
    cocienteV = num1/num2
    cocienteA = round(number=num1/num2, ndigits= cifras_redondeo)
    return float(abs((cocienteV-cocienteA)/cocienteV))

############################
# Ejercicio 8, (9)
# Una encuesta estima que el ingreso mensual promedio de una muestra de 100 personas es de 3000€
# con un error absoluto de 100€. Calcule el error relativo (en porcentaje) para las estimaciones de ingresos.

def errorRelativoPorcentaje(num_aproximado= 3000, error_abosulto= 100) -> float:
    # Valor absoluto = abs(valor real - valor aproximado)
    num_verdadero = num_aproximado + error_abosulto
    return float(error_abosulto/num_verdadero) * 100

############################
# Ejercicio 10
# Al realizar una conversión de unidades, un alumno escribe 10 millas es igual a 16,096 kilómetros. 
# Sin embargo, el valor aceptado es 16,093 kilómetros. ¿Cuál es el error relativo cometido por el alumno?
print(f"Ejercicio 10: {errorRelativo(num_verdadero= 16.093, num_aproximado=16.096)}")


############################
# Ejercicio 11
# A un chico se le pide que mida la altura de un árbol y acaba encontrando que la altura del árbol es de 10,02 pies. 
# La altura real del árbol es de 10,00 pies. Calcula el error relativo en la medición del chico.
print(f"Ejercicio 11: {errorRelativo(num_verdadero= 10.02, num_aproximado=10.00)}")

############################
# Ejercicio 12
# ¿Cuál es el error relativo cuando una chica escribe 1.000 atm es igual a 103,1 kPa 
# mientras que la conversión correcta es 1.000 atm = 101,3 kPa?
print(f"Ejercicio 12: {errorRelativo(num_verdadero= 101.3, num_aproximado=103.1)}")

############################
# Ejercicio 13
# Construye una función que calcule el error absoluto medio de un array numérico.

def errorAbsolutoArray(array:list[list]) -> float:
    sumaArray = sum(array)
    tamañoArray = len(array)
    for i in array:
        numerador += abs(sumaArray - i) / tamañoArray
    return float(numerador / tamañoArray)

############################
# Ejercicio 14
# Crea una función que admita un vector y una cota del error absoluto
# y devuelva el número de cifras exactas de cada número del vector.
import math

def cifrasExactas(vectorErroresAbsolutos, cota) -> list[int]:
    # La cota ha de ser mayor o igual al error relativo
    resultado = list()

    for i in range(len(vectorErroresAbsolutos)):
        errorActual = vectorErroresAbsolutos[i]
        error_absoluto = num_cifras = 0
        # Comprobación mejor resultado respecto la cota
        for j in range(len(str(errorActual))):
            redondeo = math.trunc(errorActual * (10**j))
            if redondeo >= error_absoluto and redondeo <= cota * (10**j):
                error_absoluto = redondeo / (10**j)
                num_cifras = j
        resultado.append(num_cifras)

    return resultado

print(cifrasExactas([0.1238, 0.1234, 0.124], 0.1235))

############################
# Ejercicio 15
def calcular_altura_arbol(L1, eL1, L2, eL2, L3, eL3):
    L = L1 * (L2 / L3)
    eL = L * ((eL1 / L1) + (eL2 / L2) + (eL3 / L3))
    return L, eL

############################
# Ejercicio 16
def error_absoluto_funcion(f, x, ex):
    return abs(f(x) * ex)

############################
# Ejercicio 17
def error_absoluto_dos_variables(f, x, y, ex, ey):
    return abs(f(x, y) * (ex / x + ey / y))

############################
# Ejercicio 18
def error_absoluto_tres_variables(f, x, y, z, ex, ey, ez):
    return abs(f(x, y, z) * (ex / x + ey / y + ez / z))