"""
Una empresa necesita planificar los turnos de trabajo para cubrir sus operaciones du-
rante una semana. Hay tres turnos diarios: mañana, tarde y noche. Cada turno tiene dife-
rentes necesidades de personal, y el coste por hora de los empleados varía segun el turno.
Los requisitos de personal y los costes por turno son:

Turno                           Mañana Tarde Noche
Necesidad de personal por día   5       4       3
Coste por empleado (€/hora)     15      18      22

La empresa tiene una capacidad de producción diaria de 200 unidades y genera ingresos
de 1,000 euros diarios. Cada empleado puede trabajar un maximo de 40 horas por semana
y debe descansar al menos un día completo. La empresa tiene 10 empleados disponibles,
pero tres de ellos han solicitado no trabajar en turnos de noche. Ademas, cada empleado
debe trabajar al menos dos turnos de tarde durante la semana.
Plantea un modelo de programacion lineal para minimizar los costes de personal mien-
tras se cumplen los requisitos de los turnos y las restricciones de los empleados.
"""


# función coste
# f = 15*x1 + 18*x2 + 22*x3 -> solamente en un día

# Restricciones
# x1 >= 5
# x2 >= 4
# x3 >= 3

c = [15, 18, 22]
A = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
b = [-5, -4, -3]

from scipy.optimize import linprog

resultado = linprog(c= c, A_ub= A, b_ub= b, bounds=(0, None))

print(f"""
Valor óptimo {resultado.fun}
Valores de las variables {resultado.x}
""")