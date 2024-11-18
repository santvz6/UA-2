from segmento import *
import numpy as np
import pandas as pd
import math

class ExpertSystem:
    def __init__(self, KR_lineal:float, KR_angular:float, KR_deteccion:float,
                    KT_lineal:float, KT_angular:float, KT_deteccion:float) -> None:

        """
        Parámetros
        ----------

        KR_lineal: constante que determina la velocidad lineal en una recta
        KR_angular: constante que determina la velocidad angular en una recta
        KR_deteccion: determina a partir de que momento el robot detecta un objetivo como alcanzado en una recta

        KT_lineal: constante que determina la velocidad lineal en un triángulo
        KT_angular: constante que determina la velocidad angular en un triángulo
        KT_deteccion: determina a partir de que momento el robot detecta un objetivo como alcanzado en un triángulo

        """
        
        self.segmentoObjetivo = None    # Inicializamos valores en P1Launcher
        self.objetivoAlcanzado = False  # Final del segmento
        self.inicioAlcanzado = False    # Inicio del segmento (Punto cercano: Recta, PuntoMedio: Triángulo)

        self.tipoSegmento = "recta" # Como se inicializa el segmento 0

        self.KR_lineal = KR_lineal      
        self.KR_angular = KR_angular
        self.KR_deteccion = KR_deteccion

        self.KT_lineal = KT_lineal
        self.KT_angular = KT_angular
        self.KT_deteccion = KT_deteccion

    def setObjetivo(self, segmento: object) -> None:
        """
        Establece un nuevo segmento Objetivo y resetea los checkpoints
        """
        self.inicioAlcanzado = False
        self.objetivoAlcanzado = False
        self.segmentoObjetivo = segmento

        self.tipoSegmento: str = "recta" if self.segmentoObjetivo.getType() == 1 else "triangulo"



    def tomarDecision(self, poseRobot:tuple) -> tuple:
        """
        Determina que velocidad lineal y angular tiene el robot en el instante de 
        tiempo actual en función de las características del segmentoObjetivo.

        Return
        ------

        Devuelve una tupla con la velocidad lineal y velocidad angular.
        """
        if self.tipoSegmento == "recta":
            return self.decisionRecta(poseRobot)
        else:
            return self.decisionTriangulo(poseRobot)
        


    def calcularerrorAngular(self, poseRobot:tuple, objetivo:tuple) -> float:
        xR, yR, angR, vR, wR = poseRobot
        xObj, yObj = objetivo

        # Calcular el ángulo hacia el punto objetivo
        # tg(ang) = Copuesto / Ccontiguo = y/x
        angulo_objetivo = math.degrees(math.atan2(yObj - yR, xObj - xR))

        # Lo mantenemos en el rango [0, 360)
        angulo_robot = angR % 360 

        # Ángulo entre el Objetivo y el Robot
        error_angular = angulo_objetivo - angulo_robot
        if error_angular > 180:
            error_angular -= 360
        # Si tiene que dar más de media vuelta a la izquierda
        # Hacemos que vaya a la derecha sumando +360 (más corto)
        elif error_angular < -180:
            error_angular += 360
        
        return error_angular


    def decisionRecta(self, poseRobot:tuple) -> tuple:

    #### VARIABLES DEL MÉTODO

        # Información sobre el Robot
        xR, yR, angR, vR, wR = poseRobot

        # Primer Objetivo: Punto más cercano recta AB respecto al robot R
        # Siguientes Objetivos: Punto medio situado en AB entre el punto final B y el robot R
        objetivo = self.puntoCercano(poseRobot) if not self.inicioAlcanzado else self.puntoInterpolado(poseRobot, t=1/9)

        # Diferencia de angulos entre el angObjetivo y el angRobot
        error_angular = self.calcularerrorAngular(poseRobot, objetivo)

        
    #### DETECCIÓN OBJETIVO INICIAL (PUNTO CERCANO)
        distanciaObjetivo = math.sqrt(abs((xR - objetivo[0]) ** 2 + (yR - objetivo[1]) ** 2))

        # No es necesario utilizar 0.5 como distancia de detección
        if not self.inicioAlcanzado and distanciaObjetivo <= (vR**2 - self.KR_deteccion)/2:
            self.inicioAlcanzado = True 

    #### DETECCIÓN OBJETIVO FINAL
        xFinal, yFinal = self.segmentoObjetivo.getFin()
        distanciaFinal = math.sqrt((xR - xFinal) ** 2 + (yR - yFinal) ** 2)

        if distanciaFinal <= 0.5:
            self.setobjetivoAlcanzado()

        #self.debug("PC", distanciaObjetivo, objetivo)

    #### V_LINEAL

        try:
            # función de tipo: k / sqrt(x) (la inversa de la raíz cuadrada donde el numerador es una constante)
            # Determina la v_lineal que deberá llevar el Robot
            variable_ANGULAR = self.KR_lineal/math.sqrt(abs(error_angular)) # Rango: [aprox(0.75 -> k=10), inf]
        except (ZeroDivisionError, ValueError):
            variable_ANGULAR = 3

        v_lineal = variable_ANGULAR 


    #### W_ANGULAR

        # Usamos la función sqrt(x) * KR_angular
        # Donde la constante aumenta el crecimiento de la funcón raíz cuadrada
        # Se recomienda un valor menor a 1 para entrar en el rango de [0, 3]
        try:
            w_angular =  math.sqrt(error_angular) * self.KR_angular if error_angular >= 0 else -math.sqrt(-error_angular) * self.KR_angular 

        except (ZeroDivisionError, ValueError):
            w_angular = 0
  
        return v_lineal, w_angular


    def decisionTriangulo(self, poseRobot:tuple) -> tuple:

    #### VARIABLES DEL MÉTODO

        # Información sobre el Robot
        xR, yR, angR, vR, wR = poseRobot

        # Primer Objetivo: Punto Medio del triángulo
        # Segundo Objetivo: Fin del tríangulo
        objetivo = self.segmentoObjetivo.getMedio() if not self.inicioAlcanzado else self.segmentoObjetivo.getFin()
        
        # Diferencia de angulos entre el angObjetivo y el angRobot
        error_angular = self.calcularerrorAngular(poseRobot, objetivo)
        

    #### DETECCIÓN OBJETIVO INICIAL (PUNTO CERCANO)
        if not self.inicioAlcanzado:

            distanciaObjetivo = math.sqrt((xR - objetivo[0]) ** 2 + (yR - objetivo[1]) ** 2)

            # x = -vi**2 + v**2 / 2*aceleracion -> donde v = 0 (acabará frenado)
            # El retraso servirá como constante que ajusta la distancia de detección en función de la velocidad
            # Es por ello que lo restamos en el numerador

            #¡En un futuro podremos quitar el *vR de KT_Freando!
            if distanciaObjetivo < abs(vR**2 - self.KT_deteccion*vR)/2: 
                self.inicioAlcanzado = True

    #### DETECCIÓN OBJETIVO FINAL
        xFinal, yFinal = self.segmentoObjetivo.getFin()
        distanciaFinal = math.sqrt((xR - xFinal) ** 2 + (yR - yFinal) ** 2)

        if distanciaFinal <= 0.5:
            self.setobjetivoAlcanzado()

    #### V_LINEAL


        # La CTE_ANGULAR depende del error_angular (a mayor error, menor valor = menor velocidad)
        # Cuando el error es máximo la cte reduce a la mitad (1/2), cuando es menor tiende a infinito (máximo 3)
        CTE_ANGULAR = 1/abs(error_angular/90)       # He preferido dejarlo fijo y no como parámetro en el __init__
                                                    # Porque ya tenemos k_lineal como parámetro
        v_lineal = CTE_ANGULAR * self.KT_lineal
 

    #### W_ANGULAR
 
        # La velocidad angular depende del error_angular (a mayor error, mayor velocidad angular)
        # Nuestra constante servirá para regular este valor
        w_angular = self.KT_angular * error_angular



        return v_lineal, w_angular

#################################### objetivos ####################################

    def puntoCercano(self, poseRobot: tuple):
        xR, yR = poseRobot[0], poseRobot[1]
        xA, yA = self.segmentoObjetivo.getInicio()
        xB, yB = self.segmentoObjetivo.getFin()

        # Vectores (AB y AR)
        ABx, ABy = xB - xA, yB - yA
        ARx, ARy = xR - xA, yR - yA

        # Proyección de AR sobre AB 
        # AR * AB / |AB|**2
        AB_escalar = ABx**2 + ABy**2

        try:
            proyeccion = max(0, min(1, (ARx * ABx + ARy * ABy) / AB_escalar))
        except (ZeroDivisionError, ValueError):
            proyeccion = 0

        # Calcular el punto más cercano en la línea
        punto_cercano_x = xA + proyeccion * ABx
        punto_cercano_y = yA + proyeccion * ABy

        return (punto_cercano_x, punto_cercano_y)
        

    def puntoInterpolado(self, poseRobot: tuple, t: float):
        
        punto_cercano = self.puntoCercano(poseRobot)
        xB, yB = self.segmentoObjetivo.getFin()

        x_t = (1 - t) * punto_cercano[0] + t * xB
        y_t = (1 - t) * punto_cercano[1] + t * yB

        return (x_t, y_t)



#################################### set ####################################
    def setobjetivoAlcanzado(self) -> None:
        self.objetivoAlcanzado = True  

#################################### P1Launcher ####################################
    def hayParteOptativa(self) -> bool:
        return True
    
    def esObjetivoAlcanzado(self) -> bool:
        return self.objetivoAlcanzado
    
#################################### csv ####################################
    def añadirFila(self,nueva_fila: dict, nombre: str) -> None:
            df = pd.read_csv(nombre, index_col=0)
            df.loc[len(df)] = nueva_fila
            df.to_csv(nombre, index=True)
    
    def getmaxID(self, nombre:str) -> int:
        try:
            df = pd.read_csv(nombre, index_col=0)
        except:
            print("getDF(): No hemos podido abrir", nombre)
        else:
            return (max(df.index))
    
##################################### debug ####################################
    def debug(self, objetivo:str, distancia:int, coordenadas:tuple) -> None:
        print(f"{objetivo} -> Distancia: {distancia:.2f} | Coordenadas: {coordenadas}")