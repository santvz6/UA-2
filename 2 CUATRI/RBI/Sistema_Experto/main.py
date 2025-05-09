import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Definir las variables de entrada y salida
edad = ctrl.Antecedent(np.arange(0, 101, 1), 'edad')
dolor_pecho = ctrl.Antecedent(np.arange(0, 11, 1), 'dolor_pecho')  # Escala de 0 a 10
presion_arterial = ctrl.Antecedent(np.arange(80, 201, 1), 'presion_arterial')
colesterol = ctrl.Antecedent(np.arange(100, 301, 1), 'colesterol')
azucar_sangre = ctrl.Antecedent(np.arange(0, 201, 1), 'azucar_sangre') # Añadir azúcar en sangre
ecg = ctrl.Antecedent(np.arange(0, 3, 1), 'ecg') #Valores  0, 1, 2
max_ritmo_cardiaco = ctrl.Antecedent(np.arange(60, 221, 1), 'max_ritmo_cardiaco')
angina_ejercicio = ctrl.Antecedent(np.arange(0, 2, 1), 'angina_ejercicio') # 0 o 1
riesgo_cardiovascular = ctrl.Consequent(np.arange(0, 101, 1), 'riesgo_cardiovascular')


# 2. Definir las funciones de membresía (fuzzy sets)
edad['joven'] = fuzz.trapmf(edad.universe, [0, 0, 30, 40])
edad['mediana_edad'] = fuzz.trapmf(edad.universe, [30, 40, 50, 60])
edad['mayor'] = fuzz.trapmf(edad.universe, [50, 60, 100, 100])

dolor_pecho['leve'] = fuzz.trapmf(dolor_pecho.universe, [0, 0, 3, 5])
dolor_pecho['moderado'] = fuzz.trapmf(dolor_pecho.universe, [3, 5, 7, 9])
dolor_pecho['severo'] = fuzz.trapmf(dolor_pecho.universe, [7, 9, 10, 10])

presion_arterial['baja'] = fuzz.trapmf(presion_arterial.universe, [80, 80, 120, 140])
presion_arterial['normal'] = fuzz.trapmf(presion_arterial.universe, [120, 140, 160, 180])
presion_arterial['alta'] = fuzz.trapmf(presion_arterial.universe, [160, 180, 200, 200])

colesterol['bajo'] = fuzz.trapmf(colesterol.universe, [100, 100, 150, 200])
colesterol['normal'] = fuzz.trapmf(colesterol.universe, [150, 200, 250, 300])
colesterol['alto'] = fuzz.trapmf(colesterol.universe, [250, 300, 300, 300])

azucar_sangre['normal'] = fuzz.trapmf(azucar_sangre.universe, [0, 0, 100, 140])
azucar_sangre['alta'] = fuzz.trapmf(azucar_sangre.universe, [100, 140, 200, 200])

ecg['normal'] = fuzz.trimf(ecg.universe, [0, 0, 1])
ecg['anormal'] = fuzz.trimf(ecg.universe, [1, 2, 2])


max_ritmo_cardiaco['bajo'] = fuzz.trapmf(max_ritmo_cardiaco.universe, [60, 60, 100, 140])
max_ritmo_cardiaco['moderado'] = fuzz.trapmf(max_ritmo_cardiaco.universe, [100, 140, 180, 200])
max_ritmo_cardiaco['alto'] = fuzz.trapmf(max_ritmo_cardiaco.universe, [180, 200, 220, 220])

angina_ejercicio['no'] = fuzz.trimf(angina_ejercicio.universe, [0, 0, 1])
angina_ejercicio['si'] = fuzz.trimf(angina_ejercicio.universe, [0, 1, 1])


riesgo_cardiovascular['bajo'] = fuzz.trapmf(riesgo_cardiovascular.universe, [0, 0, 20, 40])
riesgo_cardiovascular['medio'] = fuzz.trapmf(riesgo_cardiovascular.universe, [20, 40, 60, 80])
riesgo_cardiovascular['alto'] = fuzz.trapmf(riesgo_cardiovascular.universe, [60, 80, 100, 100])


# 3. Definir las reglas
regla1 = ctrl.Rule(edad['mayor'] | dolor_pecho['severo'] | presion_arterial['alta'] | colesterol['alto'] | azucar_sangre['alta'], riesgo_cardiovascular['alto'])
regla2 = ctrl.Rule(edad['mediana_edad'] & dolor_pecho['moderado'] & presion_arterial['normal'] & colesterol['normal'], riesgo_cardiovascular['medio'])
regla3 = ctrl.Rule(edad['joven'] & dolor_pecho['leve'] & presion_arterial['baja'] & colesterol['bajo'] & azucar_sangre['normal'], riesgo_cardiovascular['bajo'])
# Añadir más reglas según sea necesario... (incluyendo ecg, max_ritmo_cardiaco, angina_ejercicio)


# 4. Crear el sistema de control
riesgo_ctrl = ctrl.ControlSystem([regla1, regla2, regla3]) # añadir el resto de reglas
riesgo_sim = ctrl.ControlSystemSimulation(riesgo_ctrl)


# 5. Simular el sistema
riesgo_sim.input['edad'] = 65
riesgo_sim.input['dolor_pecho'] = 8
riesgo_sim.input['presion_arterial'] = 180
riesgo_sim.input['colesterol'] = 280
riesgo_sim.input['azucar_sangre'] = 160 # Ejemplo
riesgo_sim.input['ecg'] = 1 # Ejemplo
riesgo_sim.input['max_ritmo_cardiaco'] = 190 # Ejemplo
riesgo_sim.input['angina_ejercicio'] = 1 # Ejemplo


riesgo_sim.compute()

print(riesgo_sim.output['riesgo_cardiovascular'])
riesgo_cardiovascular.view(sim=riesgo_sim)