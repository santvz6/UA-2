from segmento import *
import math
import numpy as np
import time

class ExpertSystem:
    def __init__(self, kR_lineal, kR_angular, retrasoR, kT_lineal, kT_angular, retrasoT, hayTruco) -> None:
        self.segmentoObjetivo = None
        self.objetivoAlcanzado = False
        self.inicioAlcanzado = False

        self.tipoSegmento = None
        self.kR_lineal = kR_lineal
        self.kR_angular = kR_angular
        self.retrasoR = retrasoR

        self.kT_lineal = kT_lineal
        self.kT_angular = kT_angular
        self.retrasoT = retrasoT
        
        self.hayTruco = hayTruco

    def setObjetivo(self, segmento):
        self.inicioAlcanzado = False
        self.objetivoAlcanzado = False
        self.segmentoObjetivo = segmento

        self.tipoSegmento: str = "recta" if self.segmentoObjetivo.getType() == 1 else "triangulo"

        print(self.tipoSegmento, self.segmentoObjetivo.getMedio())

    def tomarDecision(self, poseRobot):
        # Coordenadas del robot
        xR, yR, angR, vR, wR = poseRobot
        
        tipoRetraso = self.retrasoR if self.tipoSegmento == "recta" or self.hayTruco else self.retrasoT
        retraso = tipoRetraso * vR
    
        if self.inicioAlcanzado:    
            xObj, yObj = self.segmentoObjetivo.getFin()
            distancia_final = math.sqrt((xR - xObj) ** 2 + (yR - yObj) ** 2)
            
            if distancia_final < (vR**2 - retraso)/2:  # Umbral para considerar que hemos alcanzado el punto final
                self.objetivoAlcanzado = True

        else:
            xObj, yObj = self.punto_cercano(poseRobot) if self.tipoSegmento == "recta" or self.hayTruco else self.segmentoObjetivo.getMedio() 
            distancia_inicio = math.sqrt((xR - xObj) ** 2 + (yR - yObj) ** 2)

            if distancia_inicio < (vR**2 - retraso)/2:  # Umbral para considerar que alcanzó el punto más cercano
                self.inicioAlcanzado = True  # Se considera el punto más cercano como alcanzado

        # Calcular el ángulo hacia el punto objetivo (punto más cercano o punto final)
        angulo_objetivo = math.degrees(math.atan2(yObj - yR, xObj - xR))
        angulo_robot = angR % 360

        # Calcular el error angular y ajustarlo al rango [-180, 180]
        error_angular = angulo_objetivo - angulo_robot
        if error_angular > 180:
            error_angular -= 360
        elif error_angular < -180:
            error_angular += 360

        k_angular = self.kR_angular if self.tipoSegmento == "recta" or self.hayTruco else self.kT_angular
        w_angular = k_angular * error_angular
        w_angular = max(-2, min(2, w_angular))  # Evitar giros muy bruscos

        k_lineal = self.kR_lineal  if self.tipoSegmento == "recta" or self.hayTruco else self.kT_lineal
        v_lineal = 1/abs(error_angular/90) * k_lineal
        v_lineal = max(0, min(3, v_lineal))  # Evitar giros muy bruscos
    
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
    