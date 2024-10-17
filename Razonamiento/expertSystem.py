from segmento import *
import math
import numpy as np
import time

class ExpertSystem:
    def __init__(self) -> None:
        self.objetivoAlcanzado = False
        self.segmentoObjetivo = None
        self.velocidad_actual = 0  # Velocidad lineal actual aproximada
        self.last_update_time = time.time()  # Tiempo de la última actualización para calcular el tiempo transcurrido
        self.VACC = 1  # Aceleración máxima del robot (m/s^2)
        self.VMAX = 3  # Velocidad máxima del robot (m/s)
        self.puntoCercano = False  # Variable para detectar el punto más cercano alcanzado

    def setObjetivo(self, segmento):
        self.puntoCercano = False
        self.objetivoAlcanzado = False
        self.segmentoObjetivo = segmento

    def tomarDecision(self, poseRobot):
        """
        Controla el movimiento del robot para acercarse a la línea objetivo
        y seguir hasta el final una vez alcanzado el punto más cercano.
        """
        # Calcular el tiempo transcurrido desde la última actualización
        current_time = time.time()
        time_elapsed = current_time - self.last_update_time
        self.last_update_time = current_time

        # Coordenadas del robot
        xR, yR, theta = poseRobot

        # Calcular el punto más cercano en la trayectoria al robot
        punto_mas_cercano = self.punto_cercano(poseRobot)
        xC, yC = punto_mas_cercano

        # Calcular la distancia al punto más cercano
        distancia_a_punto_mas_cercano = math.sqrt((xR - xC) ** 2 + (yR - yC) ** 2)

        # Si el robot ha alcanzado el punto más cercano, dirigirse al punto final del segmento
        if self.puntoCercano:
            punto_final = self.segmentoObjetivo.getFin()
            distancia_a_final = math.sqrt((xR - punto_final[0]) ** 2 + (yR - punto_final[1]) ** 2)

            if distancia_a_final < 0.2:  # Umbral para considerar que hemos alcanzado el punto final
                self.objetivoAlcanzado = True
                print("Objetivo alcanzado, el robot ha llegado al punto final.")
                return (0, 0)  # Parar el robot cuando alcance el punto final

            # Actualizar el objetivo a seguir al punto final del segmento
            xC, yC = punto_final
        else:
            # Si aún no ha alcanzado el punto más cercano, seguir dirigiéndose hacia él
            if distancia_a_punto_mas_cercano < 0.2:  # Umbral para considerar que alcanzó el punto más cercano
                self.puntoCercano = True  # Se considera el punto más cercano como alcanzado
                print("Punto más cercano alcanzado, dirigiéndose al punto final.")

        # Calcular el ángulo hacia el punto objetivo (punto más cercano o punto final)
        angulo_objetivo = math.degrees(math.atan2(yC - yR, xC - xR))
        angulo_robot = theta % 360

        # Calcular el error angular y ajustarlo al rango [-180, 180]
        error_angular = angulo_objetivo - angulo_robot
        if error_angular > 180:
            error_angular -= 360
        elif error_angular < -180:
            error_angular += 360

        # Controlador proporcional para la velocidad angular
        k_angular = 0.1  # Aumentar la ganancia para ser más sensible a la orientación
        w_angular = k_angular * error_angular

        # Limitar la velocidad angular máxima
        w_angular = max(-2, min(2, w_angular))  # Evitar giros muy bruscos

        # Actualizar la velocidad actual del robot usando la aceleración conocida
        if self.velocidad_actual < self.VMAX:
            self.velocidad_actual += self.VACC * time_elapsed
            self.velocidad_actual = min(self.velocidad_actual, self.VMAX)

        # Calcular la distancia de frenado utilizando la velocidad estimada
        distancia_frenado = (self.velocidad_actual ** 2) / (2 * self.VACC)

        # Fase de aproximación con reducción gradual de velocidad
        distancia_actual = math.sqrt((xR - xC) ** 2 + (yR - yC) ** 2)

        # Siempre mantener el robot a menos de 0.001 de la línea
        if distancia_a_punto_mas_cercano > 0.001: 
            v_lineal = min(self.VMAX, 1.5)  # Velocidad alta para acercarse rápidamente
        else:
            # Si está cerca de la línea, reducir la velocidad para mantener la precisión
            v_lineal = 0.5  # Velocidad baja para corrección

        return (v_lineal, w_angular)

    def esObjetivoAlcanzado(self):
        return self.objetivoAlcanzado
    
    def calcularAngulo(self, xRobot, yRobot):
        xR, yR = xRobot, yRobot
        xObj, yObj = self.segmentoObjetivo.getFin() if self.puntoCercano else self.segmentoObjetivo.getInicio()
        
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
        objetivo = self.segmentoObjetivo.getFin() if self.puntoCercano else self.punto_cercano(poseRobot)
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
