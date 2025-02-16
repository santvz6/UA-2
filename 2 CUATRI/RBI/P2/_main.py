def redondear_numero(numero, cifras):
    return round(numero, cifras)

def error_absoluto(verdadero, aproximado):
    return abs(verdadero - aproximado)

def error_relativo(verdadero, aproximado):
    if verdadero == 0:
        raise ValueError("El valor verdadero no puede ser cero.")
    return abs((verdadero - aproximado) / verdadero)

def error_absoluto_suma(verdadero, aproximado, cifras):
    return round(abs(sum(verdadero) - sum(aproximado)), cifras)

def error_relativo_suma(verdadero, aproximado, cifras):
    suma_verdadero = sum(verdadero)
    if suma_verdadero == 0:
        raise ValueError("La suma de los valores verdaderos no puede ser cero.")
    return round(abs((suma_verdadero - sum(aproximado)) / suma_verdadero), cifras)

def error_relativo_producto(verdadero, aproximado, cifras):
    prod_verdadero = 1
    prod_aproximado = 1
    for v, a in zip(verdadero, aproximado):
        prod_verdadero *= v
        prod_aproximado *= a
    if prod_verdadero == 0:
        raise ValueError("El producto de los valores verdaderos no puede ser cero.")
    return round(abs((prod_verdadero - prod_aproximado) / prod_verdadero), cifras)

error_relativo_producto

def error_relativo_cociente(verdadero, aproximado, cifras):
    if aproximado == 0:
        raise ValueError("El denominador no puede ser cero.")
    return round(abs((verdadero - aproximado) / verdadero), cifras)

def error_relativo_porcentaje(error_absoluto, valor_verdadero):
    return (error_absoluto / valor_verdadero) * 100

def error_absoluto_medio(array):
    return sum(abs(x - sum(array) / len(array)) for x in array) / len(array)

def cifras_exactas_vector(vector, cota_error):
    return [len(str(int(abs(v)))) for v in vector if abs(v) >= cota_error]

def calcular_altura_arbol(L1, eL1, L2, eL2, L3, eL3):
    L = L1 * (L2 / L3)
    eL = L * ((eL1 / L1) + (eL2 / L2) + (eL3 / L3))
    return L, eL

def error_absoluto_funcion(f, x, ex):
    return abs(f(x) * ex)

def error_absoluto_dos_variables(f, x, y, ex, ey):
    return abs(f(x, y) * (ex / x + ey / y))

def error_absoluto_tres_variables(f, x, y, z, ex, ey, ez):
    return abs(f(x, y, z) * (ex / x + ey / y + ez / z))
