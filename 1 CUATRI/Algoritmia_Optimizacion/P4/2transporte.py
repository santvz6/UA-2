"""
Una empresa debe transportar productos desde tres almacenes a tres tiendas. Los alma-
cenes tienen disponibles 120, 180 y 200 unidades de producto, respectivamente, mientras
que las tiendas necesitan 100, 150 y 250 unidades, respectivamente. Los costes de transporte
por unidad son los siguientes:

          Tienda 1 Tienda 2 Tienda 3
Almacen 1 | 4       6       8
Almacen 2 | 5       3       7   
Almacen 3 | 6       4       5

Plantea un modelo de programacion lineal para minimizar el coste total de transporte,
asegurando que se satisfagan las necesidades de las tiendas y no se exceda la capacidad de
los almacenes.
"""


# función coste
# f = 4*x11 + 6*x12 + 8*x13
#   + 5*x21 + 3*x22 + 7*x23
#   + 6*x31 + 4*x32 + 5*x33

c = [4, 6, 8, 5, 3, 7, 6, 4, 5]


# Restricciones

# x11 + x12 + x13 = 120 -> Espacio Almacén 1
# x21 + x22 + x23 = 180 -> Espacio Almacén 2
# x31 + x32 + x33 = 200 -> Espacio Almacén 3


# x11 + x21 + x31 = 100 -> Espacio Tienda 1
# x12 + x22 + x32 = 150 -> Espacio Tienda 2
# x13 + x23 + x33 = 250 -> Espacio Tienda 3

A = [
[1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 1],
[1, 0, 0, 1, 0, 0, 1, 0, 0],
[0, 1, 0, 0, 1, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 1, 0, 0, 1]
]

b = [120, 180, 200, 100, 150, 250]

from scipy.optimize import linprog

resultado = linprog(c= c, A_eq= A, b_eq= b, bounds=(0, None))

print(f"""
Valor óptimo {resultado.fun}
Valores de las variables {resultado.x}
""")
