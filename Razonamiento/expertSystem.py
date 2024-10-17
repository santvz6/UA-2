from segmento import *
import math
import numpy as np
import time

class ExpertSystem:
    def __init__(self, k_lineal, k_angular, retraso) -> None:
        self.segmentoObjetivo = None

        self.objetivoAlcanzado = False
        self.inicioAlcanzado = False  # Variable para detectar el punto más cercano alcanzado

        self.k_lineal = k_lineal
        self.k_angular = k_angular
        self.retraso = retraso

    def setObjetivo(self, segmento):
        self.inicioAlcanzado = False
        self.objetivoAlcanzado = False
        self.segmentoObjetivo = segmento

    def tomarDecision(self, poseRobot):
        # Coordenadas del robot
        xR, yR, angR, vR, wR = poseRobot

        retraso = 1.2 * vR
        # Si el robot ha alcanzado el punto más cercano, dirigirse al punto final del segmento
        if self.inicioAlcanzado:
            xObj, yObj = self.segmentoObjetivo.getFin()
            distancia_final = math.sqrt((xR - xObj) ** 2 + (yR - yObj) ** 2)

            
            if distancia_final < (vR**2 - retraso)/2:  # Umbral para considerar que hemos alcanzado el punto final
                self.objetivoAlcanzado = True

        else:
            xObj, yObj = self.punto_cercano(poseRobot)    
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

        k_angular = 0.045
        w_angular = k_angular * error_angular
        # Limitar la velocidad angular máxima
        w_angular = max(-2, min(2, w_angular))  # Evitar giros muy bruscos

        k_lineal = 0.70  # Aumentar la ganancia para ser más sensible a la orientación
        v_lineal = 1/abs(error_angular/90) * k_lineal
        # Limitar la velocidad angular máxima
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