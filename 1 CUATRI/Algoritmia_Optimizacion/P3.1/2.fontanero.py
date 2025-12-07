"""
Un fontanero necesita hacer n reparaciones urgentes y sabe de antemano el tiempo
que le va a llevar cada una de ellas: en la tarea i-ésima tardará ti minutos. Como en su
empresa le pagan dependiendo de la satisfaccíon del cliente, necesita decidir el orden en el
que atenderá los avisos para minimizar el tiempo medio de espera de los clientes.
En otras palabras, si llamamos Ei a lo que espera el cliente i-ésimo hasta ver reparada
su avería por completo, necesita minimizar la expresíon.
"""

def fontanero(t: tuple):
    
    # 1. Ordenamos de menor a mayor
    ordenado = sorted(t, reverse=False)

    sumatorio = 0
    espera_acumulada = 0


    for elem in ordenado:
        espera_acumulada += elem
        sumatorio += espera_acumulada
    
    return sumatorio / len(ordenado)

t = (1, 2, 8, 2, 5)
solucion = fontanero(t)

print(solucion)