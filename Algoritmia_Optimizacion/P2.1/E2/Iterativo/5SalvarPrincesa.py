import numpy as np


def salvar_princesa(mazmorra: np.array):

    I, J = np.shape(mazmorra)

    # Nuestra memoria tiene que guardar la cantidad máxima de daño
    # recibido para llegar a un i, j concreto
    mem1 = np.zeros((I, J)) 
    # Creamos otra memoria para guardar la puntuacion actual
    # que llevamos en cada casilla i, j
    mem2 = np.zeros((I, J))

    for i in range(I):
        for j in range(J):
        
        #### DATOS MEM1 Y ACTUALIZACIÓN MEM2 ####

            # Mejor movimiento para recibir el mínimo daño (mayor cantidad positiva)
            # El primer movimiento nos da igual ya que mem1 esta a 0

            if i==0:    # viene del Oeste (obligatoriamente)
                daño_anterior = mem1[i, j-1] 
                
                punt_anterior = mem2[i, j-1]
                # Actualizamos nuestra memoria de puntuaciones
                mem2[i, j] = punt_anterior + mazmorra[i, j] 

            elif j==0:  # viene del Norte (obligatoriamente)
                daño_anterior = mem1[i-1, j]
                
                punt_anterior = mem2[i-1, j]
                # Actualizamos nuestra memoria de puntuaciones
                mem2[i, j] = punt_anterior + mazmorra[i, j]

            else:       # Puede venir de ambos lados
                daño_anterior = max(mem1[i-1, j], mem1[i, j-1])
                
                # En este caso la puntuación que agarramos se determina
                # a partir del max_daño que más nos beneficie
                punt_anterior = mem2[i-1, j] if daño_anterior == mem1[i-1, j] else mem2[i, j-1]
                # Actualizamos nuestra memoria de puntuaciones                
                mem2[i, j] = punt_anterior + mazmorra[i, j]
                
        #### ACTUALIZACIÓN MEM1 ####

            # max_daño ha aumentado (en negativo) [casilla negativa]
            if punt_anterior + mazmorra[i, j] < daño_anterior :
                mem1[i, j] =  punt_anterior + mazmorra[i, j]
            # max_daño ha disminuido (en negativo) [casilla positiva]
            else:
                # El valor que más me beneficie de las casillas anteriores a mí
                mem1[i, j] = daño_anterior

    return mem1, mem2


mazmorra = np.array([[-2, -3, 3], 
                     [-5, -10, 1], 
                     [10, 30, -5]])

print("Memoria - Máximo Daño")
print(salvar_princesa(mazmorra)[0],"\n")
print("Memoria - Puntuaciones")
print(salvar_princesa(mazmorra)[1],"\n")