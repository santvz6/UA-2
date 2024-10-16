'''
 Sistema Experto para el guiado de un robot
 Esta clase contendrá el código creado por los alumnos de RyRDC para el control 
 y guiado de un robot móvil sobre un plano cartesiano pasando por un punto inicial
 y siguiendo una línea recta hasta un punto final

 Creado por: Diego Viejo
 el 26/09/2024
 Modificado por: 

'''

from segmento import *
import math
import numpy as np
import time
class ExpertSystem:
    def __init__(self) -> None:
        self.objetivoAlcanzado = False
        self.segmentoObjetivo = None
        self.segmentoObjetivo2 = None

        # Propios
        self.inicioAlcanzado = False
        #self.ang1 = np.linspace[0, 90, 100]

        self.inicio_truco = False
        self.ready_bro =  False


    # función setObjetivo
    #   Especifica un segmento como objetivo para el recorrido del robot
    #   Este método NO debería ser modificado
    def setObjetivo(self, segmento):
        self.inicioAlcanzado = False
        self.objetivoAlcanzado = False
        self.segmentoObjetivo = segmento


    # función tomarDecision. 
    #   Recibe una tupla de 3 valores con la pose del robot y un objeto
    #   de clase Segmento con la información del segmento a seguir
    #   
    #   Devuelve una tupla con la velocidad lineal y angular que se
    #   quiere dar al robot
    def tomarDecision(self, poseRobot):        
        
        # código del sistema experto. A completar por la alumna o alumno
        """if self.alcanzado(poseRobot, dist=3):
            self.objetivoAlcanzado = True if self.inicioAlcanzado else False
            self.inicioAlcanzado = True if not self.objetivoAlcanzado else False"""
        

        angObj = self.calcularAngulo(poseRobot[0], poseRobot[1])
        angRobot = poseRobot[2]%360 if poseRobot[2] < 0 else poseRobot[2]

        if self.alcanzado(poseRobot, dist=4.05) or self.ready_bro:
            v_lineal = 0
            w_angular = 0
            
            if self.alcanzado(poseRobot, dist=4.05):
                self.objetivoAlcanzado = True if self.inicioAlcanzado else False
                self.inicioAlcanzado = True if not self.objetivoAlcanzado else False
            
            if not self.inicio_truco:
                self.inicio_truco = time.time()
            if time.time() - self.inicio_truco > 5:
                self.ready_bro = False
            elif time.time() - self.inicio_truco > 1:
               w_angular = 1.4
               if abs(angObj - angRobot) < 5:
                   w_angular = 0
                   print(2)
            else:
                self.ready_bro = True
            
            


        elif abs(angObj - angRobot) > 45:
            v_lineal = 1
            w_angular = 1

        elif abs(angObj - angRobot) > 15:
            v_lineal = 2
            w_angular = 0.5
        
        elif abs(angObj - angRobot) > 5:
            v_lineal = 2.75
            w_angular = 0.2
        elif abs(angObj - angRobot) > 1:
            v_lineal = 3
            w_angular = 0.1
        else:
            v_lineal = 3
            w_angular = 0
        
        return (v_lineal,w_angular) if self.orientacionGiro(angRobot, angObj) else (v_lineal, -w_angular)

    
    # función esObjetivoAlcanzado 
    #   Devuelve True cuando el punto final del objetivo ha sido alcanzado. 
    #   Es responsabilidad de la alumna o alumno cambiar el valor de la 
    #   variable objetivoAlcanzado cuando se detecte que el robot ha llegado 
    #   a su objetivo. Esto se llevará a cabo en el método tomarDecision
    #   Este método NO debería ser modificado
    def esObjetivoAlcanzado(self):
        return self.objetivoAlcanzado
    
    def calcularAngulo(self, xRobot, yRobot):
        xR, yR = xRobot, yRobot
        xObj, yObj = self.segmentoObjetivo.getFin() if self.inicioAlcanzado else self.segmentoObjetivo.getInicio()
        
        cateto1 = xObj-xR if xObj >= xR else xR-xObj
        cateto2 = yObj-yR if yObj >= yR else yR-yObj

        hipotenusa = math.sqrt(cateto1**2+cateto2**2)

        angulo = math.degrees(math.acos(cateto1/hipotenusa))

        if xObj >= xR and yObj >= yR:
            return angulo # + 360
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
        objetivo = self.segmentoObjetivo.getFin() if self.inicioAlcanzado else self.segmentoObjetivo.getInicio()
        return objetivo[0]-dist<poseRobot[0]<objetivo[0]+dist and objetivo[1]-dist<poseRobot[1]<objetivo[1]+dist