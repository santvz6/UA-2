"""
Una fabrica produce dos tipos de camisetas: deportivas y casuales. Cada camiseta de-
portiva genera una ganancia de 5 euros y cada camiseta casual una ganancia de 4 euros.
Para fabricar una camiseta deportiva se necesitan 2 horas de trabajo y 1 metro de tela,
mientras que una camiseta casual requiere 1 hora de trabajo y 2 metros de tela. La fabrica
dispone de 100 horas de trabajo y 120 metros de tela.
Plantea un modelo de programacion lineal para maximizar las ganancias de la fabrica
cumpliendo las restricciones.
"""

# Función coste
# f(x1, x2) = 5x1 + 4x2

# Restricciones

# 2*x1 + 1*x2 <= 100 -> Número de Horas
# 1*x1 + 2*x2 <= 120 -> Metros de tela

c = [-5, -4]
A = [[2, 1], [1, 2]]
b = [100, 120]


from scipy.optimize import linprog

resultado = linprog(c= c, A_ub= A, b_ub= b, bounds=(0, None))

print(f"""
Valor óptimo {-resultado.fun}
Valores de las variables {resultado.x}
""")
