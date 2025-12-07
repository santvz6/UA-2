import numpy as np
import time

class RejjillaOcupacion:
    def __init__(self, tam_celda, limites):
        self.tam_celda = tam_celda
        self.limites = limites  # (xmin, xmax, ymin, ymax, zmin, zmax)
        self.rejilla = {}
        self.inicializarCeldas()

    def getCelda(self, x, y, z):
        # Índice de celda correspondiente a (x, y, z)
        return (
            int(x // self.tam_celda),
            int(y // self.tam_celda),
            int(z // self.tam_celda)
        )

    def inicializarCeldas(self):
        # Genera todas las celdas posibles dentro de los límites
        xmin, xmax, ymin, ymax, zmin, zmax = self.limites
        # arange permite iterar usando float
        for x in np.arange(xmin, xmax, self.tam_celda):
            for y in np.arange(ymin, ymax, self.tam_celda):
                for z in np.arange(zmin, zmax, self.tam_celda):
                    celda = self.getCelda(x, y, z)
                    # Guardamos la suma en vez de la media de los puntos en esa celda
                    # Para calcular la media -> suma / numero
                    self.rejilla[celda] = {"numero": 0, "suma": np.zeros(3)} 

    
    def setPunto(self, x, y, z):
        celda = self.getCelda(x, y, z)

        if celda in self.rejilla:
            self.rejilla[celda]["numero"] += 1
            self.rejilla[celda]["suma"] += np.array([x, y, z])

    def analisis(self):
        celdas_vacias = 0
        celdas_ocupadas = 0
        media_puntos = 0

        for datos in self.rejilla.values():
            if datos["numero"] == 0:
                celdas_vacias += 1
            else:
                celdas_ocupadas += 1
                media_puntos += datos["numero"]
    
        return {
            "num_celdas": len(self.rejilla),
            "celdas_vacias": celdas_vacias,
            "celdas_ocupadas": celdas_ocupadas,
            "media_puntos": media_puntos / celdas_ocupadas
        }


class OcTree:
    def __init__(self, limites, profundidad=0, max_profundidad=10):
        self.limites = limites  # Límite del cubo: (xmin, xmax, ymin, ymax, zmin, zmax)
        self.profundidad = profundidad
        self.max_profundidad = max_profundidad
        self.puntos = []  # Puntos almacenados en este nodo
        # Para calcular la media -> sum(puntos) / len(puntos)
        self.hijos = None  # Los 8 subnodos (hijos)

    def expandir(self):
        """ Dividimos el nodo en 8 subnodos"""
        x_min, x_max, y_min, y_max, z_min, z_max = self.limites
        x_mid = (x_min + x_max) / 2
        y_mid = (y_min + y_max) / 2
        z_mid = (z_min + z_max) / 2

        # Creamos los 8 subnodos
        self.hijos = [
            OcTree((x_min, x_mid, y_min, y_mid, z_min, z_mid), self.profundidad + 1, self.max_profundidad),
            OcTree((x_mid, x_max, y_min, y_mid, z_min, z_mid), self.profundidad + 1, self.max_profundidad),
            OcTree((x_min, x_mid, y_mid, y_max, z_min, z_mid), self.profundidad + 1, self.max_profundidad),
            OcTree((x_mid, x_max, y_mid, y_max, z_min, z_mid), self.profundidad + 1, self.max_profundidad),
            OcTree((x_min, x_mid, y_min, y_mid, z_mid, z_max), self.profundidad + 1, self.max_profundidad),
            OcTree((x_mid, x_max, y_min, y_mid, z_mid, z_max), self.profundidad + 1, self.max_profundidad),
            OcTree((x_min, x_mid, y_mid, y_max, z_mid, z_max), self.profundidad + 1, self.max_profundidad),
            OcTree((x_mid, x_max, y_mid, y_max, z_mid, z_max), self.profundidad + 1, self.max_profundidad)
        ]

    def setPunto(self, punto):
        if self.profundidad == self.max_profundidad or not self.hijos:
            self.puntos.append(punto)
            if len(self.puntos) > 8 and self.profundidad < self.max_profundidad:
                self.expandir()
                while self.puntos:
                    pt = self.puntos.pop()
                    for child in self.hijos:
                        if child.contiene(pt):
                            child.setPunto(pt)
                            break
        else:
            for child in self.hijos:
                if child.contiene(punto):
                    child.setPunto(punto)
                    break

    def contiene(self, punto) -> bool:
        x_min, x_max, y_min, y_max, z_min, z_max = self.limites
        x, y, z = punto
        return x_min <= x < x_max and y_min <= y < y_max and z_min <= z < z_max

    def analisis(self):
        if not self.hijos:
            return {
                "num_celdas": 1,
                "num_puntos": len(self.puntos)
            }
        else:
            analisis = {"num_celdas": 0, "num_puntos": 0}
            for child in self.hijos:
                child_analisis = child.analisis()
                analisis["num_celdas"] += child_analisis["num_celdas"]
                analisis["num_puntos"] += child_analisis["num_puntos"]
            return analisis


def cargar_datos_pcd(filePath):
    puntos = []
    with open(filePath, 'r') as archivo:
        leer_datos = False
        for linea in archivo:
            if leer_datos:
                valores = linea.strip().split()
                if len(valores) >= 3:
                    x, y, z = map(float, valores[:3])
                    puntos.append((x, y, z))
            elif linea.startswith("DATA ascii"):
                leer_datos = True
    return puntos

path = "Datos/"
ciencias000 = cargar_datos_pcd(path + "ciencias000.pcd")
ciencias001 = cargar_datos_pcd(path + "ciencias001.pcd")
museo000 = cargar_datos_pcd(path + "museo000.pcd")
poli000 = cargar_datos_pcd(path + "poli000.pcd")
poli001 = cargar_datos_pcd(path + "poli001.pcd")
scan000 = cargar_datos_pcd(path + "scan000.pcd")

datos = [ciencias000, ciencias001, museo000, poli000, poli001, scan000]
t_inicio = 0
tam_celda = 0.9

for i, puntos in enumerate(datos):
    t_inicio = time.time()
    min_x = min(p[0] for p in puntos)
    max_x = max(p[0] for p in puntos)
    min_y = min(p[1] for p in puntos)
    max_y = max(p[1] for p in puntos)
    min_z = min(p[2] for p in puntos)
    max_z = max(p[2] for p in puntos)
    limites = (min_x, max_x, min_y, max_y, min_z, max_z)

    rejilla = RejjillaOcupacion(tam_celda=tam_celda, limites=limites)
    octree = OcTree(limites=limites, max_profundidad=8)

    # Insertar puntos en las estructuras
    for x, y, z in puntos:
        rejilla.setPunto(x, y, z)
        octree.setPunto((x, y, z))

    # Obtener análisis
    analisis_rejilla = rejilla.analisis()
    analisis_octree = octree.analisis()
    analisis_octree = {"num_celdas": analisis_octree["num_celdas"], 
                       "media_puntos": analisis_octree["num_puntos"] / analisis_octree["num_celdas"]}

    # Mostrar resultados
    print(
    f"""
    ------------- {i+1} ----------------
    Tamaño Celda -> {tam_celda}

    Rejilla -> {analisis_rejilla}

    OcTree -> {analisis_octree}

    TiempoEjecución -> {time.time()-t_inicio}
    """
    )