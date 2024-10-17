from segmento import *
import math
import numpy as np
import time

class ExpertSystem:
    def __init__(self) -> None:
        self.objetivoAlcanzado = False
        self.segmentoObjetivo = None

        self.velocidad_actual = 0  # Velocidad lineal actual aproximada
        self.velocidad_inicial = 0
        self.ultimo_tiempo = time.time()  # Tiempo de la última actualización para calcular el tiempo transcurrido
        self.VACC = 1  # Aceleración máxima del robot (m/s^2)
        self.VMAX = 3  # Velocidad máxima del robot (m/s)
        self.inicioAlcanzado = False  # Variable para detectar el punto más cercano alcanzado

    def setObjetivo(self, segmento):
        self.inicioAlcanzado = False
        self.objetivoAlcanzado = False
        self.segmentoObjetivo = segmento

    def tomarDecision(self, poseRobot):

        # Calcular el tiempo transcurrido desde la última actualización
        actual = time.time()
        tiempo_transcurrido = actual - self.ultimo_tiempo
        self.ultimo_tiempo = actual

        # Coordenadas del robot
        xR, yR, theta = poseRobot


        # Si el robot ha alcanzado el punto más cercano, dirigirse al punto final del segmento
        if self.inicioAlcanzado:
            xObj, yObj = self.segmentoObjetivo.getFin()
            distancia_final = math.sqrt((xR - xObj) ** 2 + (yR - yObj) ** 2)

            if distancia_final < 0.2:  # Umbral para considerar que hemos alcanzado el punto final
                self.objetivoAlcanzado = True

        else:
            xObj, yObj = self.punto_cercano(poseRobot)    
            distancia_inicio = math.sqrt((xR - xObj) ** 2 + (yR - yObj) ** 2)

            if distancia_inicio < 0.2:  # Umbral para considerar que alcanzó el punto más cercano
                self.inicioAlcanzado = True  # Se considera el punto más cercano como alcanzado
                self.velocidad_actual = 0

        # Calcular el ángulo hacia el punto objetivo (punto más cercano o punto final)
        angulo_objetivo = math.degrees(math.atan2(yObj - yR, xObj - xR))
        angulo_robot = theta % 360

        # Calcular el error angular y ajustarlo al rango [-180, 180]
        error_angular = angulo_objetivo - angulo_robot
        if error_angular > 180:
            error_angular -= 360
        elif error_angular < -180:
            error_angular += 360

        

        if self.inicioAlcanzado and not self.objetivoAlcanzado:
            # Controlador proporcional para la velocidad angular
            k_angular = 0.1  # Aumentar la ganancia para ser más sensible a la orientación
            w_angular = k_angular * error_angular

            # Limitar la velocidad angular máxima
            w_angular = max(-2, min(2, w_angular))  # Evitar giros muy bruscos

        else:
            if abs(error_angular) > 80:
                w_angular = 3
            elif abs(error_angular) > 40:
                w_angular = 2
            elif abs(error_angular) > 20:
                w_angular = 1
            elif abs(error_angular) > 5:
                w_angular = 0.1
            else:
                w_angular = 0
            w_angular = -w_angular if error_angular <= 0 else w_angular

            if abs(error_angular) < 5:
                # VELOCIDAD ACTUAL -> v = v0 + at
                self.velocidad_actual = min(self.velocidad_inicial + self.VACC * tiempo_transcurrido, 3)
                self.velocidad_inicial = self.velocidad_actual

                # ACELERANDO
                v_lineal = self.velocidad_actual

            else:
                v_lineal = 0

        P = (self.velocidad_actual**2 ) / 2

        if math.sqrt((xR - xObj) ** 2 + (yR - yObj) ** 2)+1 < P:
            # Si está cerca de la línea, reducir la velocidad para mantener la precisión
            v_lineal = 0  # Velocidad baja para corrección   

        return (v_lineal, w_angular)

    def esObjetivoAlcanzado(self):
        return self.objetivoAlcanzado
    
    def calcularAngulo(self, xRobot, yRobot):
        xR, yR = xRobot, yRobot
        xObj, yObj = self.segmentoObjetivo.getFin() if self.inicioAlcanzado else self.segmentoObjetivo.getInicio()
        
        cateto1 = xObj - xR if xObj >= xR else xR - xObj
        cateto2 = yObj - yR if yObj >= yR else yR - yObj

        hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

        angulo = math.degrees(math.acos(cateto1 / hipotenusa))

        if xObj >= xR and yObj >= yR:
            return angulo
        elif xObj >= xR and yObj < yR:
            return 360 - angulo
        elif xObj < xR and yObj >= yR:
            return 180 - angulo
        elif xObj < xR and yObj < yR:
            return 180 + angulo

    def orientacionGiro(self, angRobot: float, angObj: float):
        giroNegativo = abs(angObj - angRobot) if angRobot > angObj else abs(360 - angObj + angRobot) 
        giroPositivo = abs(360 - angRobot + angObj) if angRobot > angObj else abs(angObj - angRobot)
        
        return True if giroNegativo >= giroPositivo else False
    
    def alcanzado(self, poseRobot, dist):
        objetivo = self.segmentoObjetivo.getFin() if self.inicioAlcanzado else self.punto_cercano(poseRobot)
        return objetivo[0] - dist < poseRobot[0] < objetivo[0] + dist and objetivo[1] - dist < poseRobot[1] < objetivo[1] + dist
    
    def punto_cercano(self, poseRobot):
        # Coordenadas del robot
        xR, yR = poseRobot[0], poseRobot[1]

        # Obtener los puntos inicial y final del segmento objetivo
        xA, yA = self.segmentoObjetivo.getInicio()
        xB, yB = self.segmentoObjetivo.getFin()

        # Vector del segmento (B - A)
        AB = np.array([xB - xA, yB - yA])
        AP = np.array([xR - xA, yR - yA])

        # Proyección de AP sobre AB
        t = np.dot(AP, AB) / np.dot(AB, AB)

        # Limitar t al rango [0, 1] para asegurar que el punto proyectado esté dentro del segmento
        t = max(0, min(1, t))

        # Calcular el punto más cercano en la línea
        punto_cercano = np.array([xA, yA]) + t * AB

        return (punto_cercano[0], punto_cercano[1])
