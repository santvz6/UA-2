"""
Una empresa de marketing tiene un presupuesto de 15.000 € para
anunciarse en redes, televisión y prensa. Cada euro gastado en redes llega
a 40 personas, en televisión llega a 70 y en prensa a 50 personas. Por
políticas internas se requiere que:

● Al menos 25% del presupuesto debe destinarse a redes sociales.
● El gasto en televisión no debe superar al gasto en prensa escrita.
● No se puede gastar más de 5.000 euros en prensa escrita.
● Plantea un modelo de programación lineal para maximizar el alcance
publicitario de la empresa.
"""

presupuesto = 15_000

# Función coste
# f(x1, x2, x3) = 40x1 + 70x2 + 50x3

# Restricciones
# x1 + x2 + x3 <= presupuesto
# x1 >= presupuesto * 0.25
# x2 <= x3 -> x2 - x3 <= 0
# x3 <= 5_000

c = [-40, -70, -50] # hay que maximizar (cambio de signo)

A = [[1, 1, 1],
     [-1, 0, 0],
     [0, 1, -1],    
     [0, 0, 1]]

b = [presupuesto, -presupuesto * 0.25, 0, 5_000]


from scipy.optimize import linprog

resultado = linprog(c= c, A_ub= A, b_ub= b, bounds=(0, None))

print(f"""
Valor óptimo {resultado.fun}
Valores de las variables {resultado.x}
""")