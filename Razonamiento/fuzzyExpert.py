'''
 Sistema Experto Difuso para el guiado de un robot
 Esta clase controla y guía a un robot móvil sobre un plano cartesiano para recorrer diferentes 
 objetivos utilizando un esquema de sistema experto difuso.
 
 Implementado con la librería fuzzy_expert.
 
 Creado por: Diego Viejo
 el 24/10/2024
 Modificado por: Diego Viejo. 
'''

import numpy as np
import math

from fuzzy_expert.variable import FuzzyVariable
from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.inference import DecompositionalInference

from segmento import *

class FuzzySystem:
    def __init__(self) -> None:
        self.objetivoAlcanzado = False
        self.segmentoObjetivo = None
        
        # Definición de las variables difusas
        self.definir_variables_difusas()

    def definir_variables_difusas(self):
        # Variable difusa para la distancia al objetivo
        self.distancia = FuzzyVariable(
            universe_range=(0, 100),
            terms={
                "cerca": [(0, 1), (10, 1), (20, 0)],
                "media": [(10, 0), (20, 1), (30, 1), (50, 0)],
                "lejos": [(30, 0), (50, 1), (100, 1)]
            }
        )

        # Variable difusa para el error angular
        self.error_angular = FuzzyVariable(
            universe_range=(-180, 180),
            terms={
                "alineado": [(-10, 0), (0, 1), (10, 0)],
                "izquierda": [(-180, 1), (-90, 1), (-10, 0)],
                "derecha": [(10, 0), (90, 1), (180, 1)]
            }
        )

        # Variable difusa para la velocidad lineal (V)
        self.velocidad_lineal = FuzzyVariable(
            universe_range=(0, 10),
            terms={
                "baja": [(0, 1), (2, 1), (4, 0)],
                "media": [(3, 0), (5, 1), (7, 0)],
                "alta": [(6, 0), (8, 1), (10, 1)]
            }
        )

        # Variable difusa para la velocidad angular (W)
        self.velocidad_angular = FuzzyVariable(
            universe_range=(-5, 5),
            terms={
                "giro_izquierda": [(-5, 1), (-3, 1), (-1, 0)],
                "sin_giro": [(-1, 0), (0, 1), (1, 0)],
                "giro_derecha": [(1, 0), (3, 1), (5, 1)]
            }
        )

        # Definición de las reglas difusas
        self.reglas = [
            # Reglas para velocidad lineal
            FuzzyRule(
                premise=[(self.distancia, "lejos"), (self.error_angular, "alineado")],
                consequence=(self.velocidad_lineal, "alta")
            ),
            FuzzyRule(
                premise=[(self.distancia, "media"), (self.error_angular, "alineado")],
                consequence=(self.velocidad_lineal, "media")
            ),
            FuzzyRule(
                premise=[(self.distancia, "cerca")],
                consequence=(self.velocidad_lineal, "baja")
            ),
            
            # Reglas para velocidad angular
            FuzzyRule(
                premise=[(self.error_angular, "izquierda")],
                consequence=(self.velocidad_angular, "giro_izquierda")
            ),
            FuzzyRule(
                premise=[(self.error_angular, "derecha")],
                consequence=(self.velocidad_angular, "giro_derecha")
            ),
            FuzzyRule(
                premise=[(self.error_angular, "alineado")],
                consequence=(self.velocidad_angular, "sin_giro")
            )
        ]

        # Creación del sistema de inferencia difusa
        self.inferencia = DecompositionalInference(
            and_operator=min,
            or_operator=max,
            implication_operator=min,
            composition_operator=max,
            production_link=min,
            defuzzification_operator="centroid"  # Usamos "centroid" como un string si es soportado
        )

    def setObjetivo(self, obj):
        self.objetivoAlcanzado = False
        self.segmentoObjetivo = obj

    def tomarDecision(self, poseRobot):
        xR, yR, angR, _, _ = poseRobot
        xObj, yObj = self.segmentoObjetivo.getFin()

        # Calcular distancia al objetivo
        distancia = math.sqrt((xR - xObj) ** 2 + (yR - yObj) ** 2)

        # Calcular error angular
        angulo_objetivo = math.degrees(math.atan2(yObj - yR, xObj - xR))
        error_angular = angulo_objetivo - (angR % 360)
        if error_angular > 180:
            error_angular -= 360
        elif error_angular < -180:
            error_angular += 360

        # Calcular el grado de membresía de la distancia
        membresia_distancia = {
            "cerca": self.distancia.membership("cerca", distancia),
            "media": self.distancia.membership("media", distancia),
            "lejos": self.distancia.membership("lejos", distancia)
        }

        # Calcular el grado de membresía del error angular
        membresia_error_angular = {
            "alineado": self.error_angular.membership("alineado", error_angular),
            "izquierda": self.error_angular.membership("izquierda", error_angular),
            "derecha": self.error_angular.membership("derecha", error_angular)
        }

        # Inferir valores difusos para V y W usando las membresías calculadas
        V = self.inferencia(
            rules=self.reglas,
            variables={
                self.distancia: membresia_distancia,  # Usamos las membresías
                self.error_angular: membresia_error_angular
            }
        ).get(self.velocidad_lineal, 0)

        W = self.inferencia(
            rules=self.reglas,
            variables={
                self.error_angular: membresia_error_angular  # Solo para velocidad angular
            }
        ).get(self.velocidad_angular, 0)

        # Detectar si el objetivo ha sido alcanzado
        if distancia <= 0.5:  # Umbral de cercanía para considerar que el objetivo se ha alcanzado
            self.objetivoAlcanzado = True

        return V, W

    def esObjetivoAlcanzado(self):
        return self.objetivoAlcanzado

    def hayParteOptativa(self):
        # Cambiar a True si se implementa la lógica difusa para objetivos triangulares
        return False
