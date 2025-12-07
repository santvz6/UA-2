"""
Un nutricionista quiere diseñar una dieta utilizando dos alimentos:
avena y manzanas. Cada ración de avena cuesta 2 euros y cada ración
de manzanas 3 euros. Cada ración de avena aporta 3 unidades de
proteína y 4 unidades de fibra, mientras que cada ración de manzanas
aporta 2 unidades de proteína y 5 unidades de fibra. Se desea cubrir al
menos 18 unidades de proteína y 20 unidades de fibra con el menor
coste posible.
"""

# f(x1, x2) = 2x1 + 3x2
# 3x1 + 2x2 >= 18 -> Proteínas
# 4x1 + 5x2 >= 20 -> Fibra

from scipy.optimize import linprog

# Hay que minimizar -> z = c1*x1 + c2*x2

# Ax <= b -> linprog utiliza una restricción de <= (hay que cambiar signos)

c = [2, 3] # Cómo hay que minimizar no cambiamos signos

A = [[-3, -2], 
     [-4, -5]]
b = [-18, -20]

resultado = linprog(c= c, A_ub= A, b_ub= b, bounds=(0, None))

print(f"""
Valor óptimo {resultado.fun}
Valores de las variables {resultado.x}
""")