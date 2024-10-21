from segmento import *
import math
import numpy as np
import pandas as pd

class ExpertSystem:
    def __init__(self, kR_lineal:float, kR_angular:float, retrasoR:float,
                    kT_lineal:float, kT_angular:float, retrasoT:float, 
                    WMAX: float, hayTruco:bool) -> None:

        """
        Parámetros
        ----------

        kR_lineal: constante que determina la velocidad lineal en una recta
        kR_angular: constante que determina la velocidad angular en una recta
        retrasoR: determina a partir de que momento el robot detecta un objetivo como alcanzado en una recta

        kT_lineal: constante que determina la velocidad lineal en un triángulo
        kT_angular: constante que determina la velocidad angular en un triángulo
        retrasoT: determina a partir de que momento el robot detecta un objetivo como alcanzado en un triángulo

        WMAX: establece la velocida angular máxima dentro del rango [-3, 3]
        hayTruco: determina si el robot recorrerá el triángulo por la zona inferior
        """
        
        self.segmentoObjetivo = None    # Inicializamos valores en P1Launcher
        self.objetivoAlcanzado = False  # Final del segmento
        self.inicioAlcanzado = False    # Inicio del segmento (Punto cercano: Recta, PuntoMedio: Triángulo)

        self.tipoSegmento = "triangulo" # Como se inicializa el segmento 0

        self.kR_lineal = kR_lineal      
        self.kR_angular = kR_angular
        self.retrasoR = retrasoR

        self.kT_lineal = kT_lineal
        self.kT_angular = kT_angular
        self.retrasoT = retrasoT

        self.WMAX = WMAX
        self.hayTruco = hayTruco

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

        # Valores de información sobre el robot
        xR, yR, angR, vR, wR = poseRobot
        
        # Determinamos el tipo de Retraso en función del tipo de segmento objetivo
        tipoRetraso = self.retrasoR if self.tipoSegmento == "recta" or self.hayTruco else self.retrasoT
        # En función de la velocidad que lleve el Robot el retraso será mayor o menor. 
        retraso = tipoRetraso * vR
    
        if self.inicioAlcanzado:
            # El final siempre será el mismo indep. de si es Triángulo o Recta 
            xObj, yObj = self.segmentoObjetivo.getFin()
            # Cálculo de distancia -> sqrt((x1-x2)**2 + (y1-y2)**2)
            distancia_final = math.sqrt((xR - xObj) ** 2 + (yR - yObj) ** 2)
            
            # x = -vi**2 + v**2 / 2*aceleracion -> donde v = 0 (acabará frenado)
            # Como la aceleración es negativa porque estamos frenando, cambiamos signos en denominador y numerador
            
            # El retraso servirá como constante que ajusta la distancia de detección en función de la velocidad
            # Es por ello que lo restamos en el numerador
            if distancia_final < abs(vR**2 - retraso)/2: 
                self.objetivoAlcanzado = True

        else:
            # El punto inicial se determina en función del tipo de segmento objetivo
            xObj, yObj = self.punto_cercano(poseRobot) if self.tipoSegmento == "recta" or self.hayTruco else self.segmentoObjetivo.getMedio() 
            distancia_inicio = math.sqrt((xR - xObj) ** 2 + (yR - yObj) ** 2)

            if distancia_inicio < (vR**2 - retraso)/2:  
                self.inicioAlcanzado = True  

        # Calcular el ángulo hacia el punto objetivo (punto más cercano o punto final)
        # tg(ang) = Copuesto / Ccontiguo = y/x
        angulo_objetivo = math.degrees(math.atan2(yObj - yR, xObj - xR))
        # Lo mantenemos en el rango [0, 360)
        angulo_robot = angR % 360 

        # Ángulo entre el Objetivo y el Robot
        error_angular = angulo_objetivo - angulo_robot

        # Si tiene que dar más de media vuelta a la derecha
        # Hacemos que vaya a la izquierda restando -360 (más corto)
        if error_angular > 180:
            error_angular -= 360
        # Si tiene que dar más de media vuelta a la izquierda
        # Hacemos que vaya a la derecha sumando +360 (más corto)
        elif error_angular < -180:
            error_angular += 360

        k_angular = self.kR_angular if self.tipoSegmento == "recta" or self.hayTruco else self.kT_angular
        # La velocidad angular depende del error_angular (a mayor error, mayor velocidad)
        # Depende también de la constante introducida como parámetro
        w_angular = k_angular * error_angular
        # Para evitar giros bruscos establecemos una WMAX dentro del rango [-3, 3]
        w_angular = max(-self.WMAX, min(self.WMAX, w_angular))  

        k_lineal = self.kR_lineal  if self.tipoSegmento == "recta" or self.hayTruco else self.kT_lineal
        # La CTE_ANGULAR depende del error_angular (a mayor error, menor valor = menor velocidad)
        # Cuando el error es máximo la cte reduce a la mitad (1/2), cuando es menor tiende a infinito (máximo 3)
        CTE_ANGULAR = 1/abs(error_angular/90)   # He preferido dejarlo fijo y no como parámetro en el __init__
        v_lineal = CTE_ANGULAR * k_lineal       # Porque ya tenemos k_lineal como parámetro
        # No queremos velocidades lineales negativas 
        v_lineal = max(0, v_lineal) 

        return (v_lineal, w_angular)

    def esObjetivoAlcanzado(self):
        return self.objetivoAlcanzado

    def punto_cercano(self, poseRobot):
        # Coordenadas del robot
        xR, yR = poseRobot[0], poseRobot[1]

        # Obtener los puntos inicial y final del segmento objetivo
        xA, yA = self.segmentoObjetivo.getInicio()
        xB, yB = self.segmentoObjetivo.getFin()

        # Vector del segmento (B - A)
        AB = np.array([xB - xA, yB - yA])
        AR = np.array([xR - xA, yR - yA])

        # Proyección de AP sobre AB
        t = np.dot(AR, AB) / np.dot(AB, AB)

        # Limitar t al rango [0, 1] para asegurar que el punto proyectado esté dentro del segmento
        t = max(0, min(1, t))

        # Calcular el punto más cercano en la línea
        punto_cercano = np.array([xA, yA]) + t * AB

        return (punto_cercano[0], punto_cercano[1])

    def hayParteOptativa(self):
        return True
    
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
    
    def objetivoAlcanzadoTrue(self):
        self.objetivoAlcanzado = True

 
            