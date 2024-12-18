# Función coste
# f = 5xa + 8xb + 3xc

# Restricciones

produccion = 500
# xa >= produccion * 0.3
# xb == produccion * 0.2 ¿? Lo voy a hacer como un >=
# xc <= produccion * 0.5

# xa <= 300
# xb <= 200
# xc <= 400

# xa + xb + xc == produccion ¿? Lo voy a hacer como un >=

c = [5, 8, 3]
A = [
[-1, 0, 0],
[0, -1, 0],
[0, 0, 1],
[1, 0, 0],
[0, 1, 0],
[0, 0, 1],
[-1, -1, -1]
]
b = [-produccion*0.3, -produccion*0.2, produccion*0.5, 300, 200, 400, -500]

from scipy.optimize import linprog

resultado = linprog(c= c, A_ub= A, b_ub= b, bounds=(0, None))

print(f"""
Valor óptimo {resultado.fun}
Valores de las variables {resultado.x}
""")