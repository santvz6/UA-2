import subprocess
import pandas as pd
import numpy as np
import json

# Ruta completa del intérprete de Python dentro del entorno virtual
python_path = "/home/sant_vz6/Escritorio/UA-2/Razonamiento/.venv/bin/python"

################################ PARAMETROS ###############################################
NUM_P= 2

kR_lineal = np.linspace(0.700, 0.800, NUM_P) # [0.700, 0.750, 0.800] 
kR_angular = np.linspace(0.055, 0.065, NUM_P)  # [0.055, 0.060, 0.065]
retrasoR =  np.linspace(1.45, 1.55, NUM_P) # [1.45, 1.50, 1.55]

kT_lineal = np.linspace(0.950, 1.050, NUM_P) # [0.950, 1.000, 1.050]
kT_angular = np.linspace(0.015, 0.025, NUM_P) # [0.015, 0.020, 0.025]
retrasoT = np.linspace(0.90, 1.10, NUM_P) # [0.90, 1.00, 1.10]

wM = 2.00 # np.linspace(1.90, 2.10, 5)
hayTruco:bool = False

################################ FUNCIONES ###############################################

def existeFila(nombre:str, fila: list) -> bool:
    try:
        df = pd.read_csv(nombre, index_col=0)
    except:
        df = pd.DataFrame(columns=["puntuacion", "Truco", "kRe_V", "kRe_W", "Ret-", "segm1", "segm3", "segm5",
                                        "kTr_V", "kTr_W", "RetΔ", "segm2", "segm4", "segm6", "WMAX"])
        df.index.name = "ID" 
        df.to_csv(nombre, index=True)  
    else:
        for _, row in df.iterrows():
            if [row["kRe_V"], row["kRe_W"], row["Ret-"], row["kTr_V"], row["kTr_W"], row["RetΔ"], row["WMAX"]] == fila:
                return True
        return False
         

filas = list()
################################ MAIN ###############################################
for kRl in kR_lineal:
    for kRa in kR_angular:
        for retR in retrasoR:
            for kTl in kT_lineal:
                for kTa in kT_angular:
                    for retT in retrasoT:
                        fila = [kRl, kRa, retR, kTl, kTa, retT, wM]
                        if not existeFila("datos2.csv", fila):
                            filas.append(fila + [str(hayTruco)])
                        else:
                            print("Ya se ha ejecutado anteriormente:", fila)
                            continue


# Convertimos la lista de listas a JSON
filas_json = json.dumps(filas)
# Ejecuta el archivo .py que deseas ejecutar en bucle con parámetros
result = subprocess.run([python_path, "P1Launcher-MULTI.py", filas_json])