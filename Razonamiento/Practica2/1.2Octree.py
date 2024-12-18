class OctreeNode:
    def __init__(self, limites: tuple, capacidad=4):
        """
        Un nodo del Octree que contiene una región del espacio.
        
        :param limites: Una tupla de 6 valores (xmin, xmax, ymin, ymax, zmin, zmax) que define el límite del nodo.
        :param capacidad: El número máximo de puntos que un nodo puede contener antes de subdividirse.
        """
        self.limites = limites  # Límite del cubo: (xmin, xmax, ymin, ymax, zmin, zmax)
        self.capacidad = capacidad  # Capacidad del nodo
        self.points = []  # Lista de puntos almacenados en este nodo
        self.children = []  # Los 8 subnodos (hijos)
        self.is_divided = False  # Indica si el nodo ya ha sido dividido

    def _subdivide(self):
        """Divide el nodo en 8 subnodos."""
        xmin, xmax, ymin, ymax, zmin, zmax = self.limites
        mx = (xmin + xmax) / 2
        my = (ymin + ymax) / 2
        mz = (zmin + zmax) / 2
        
        # Crear los 8 subnodos
        self.children = [
            OctreeNode((xmin, mx, ymin, my, zmin, mz), self.capacidad),
            OctreeNode((mx, xmax, ymin, my, zmin, mz), self.capacidad),
            OctreeNode((xmin, mx, my, ymax, zmin, mz), self.capacidad),
            OctreeNode((mx, xmax, my, ymax, zmin, mz), self.capacidad),
            OctreeNode((xmin, mx, ymin, my, mz, zmax), self.capacidad),
            OctreeNode((mx, xmax, ymin, my, mz, zmax), self.capacidad),
            OctreeNode((xmin, mx, my, ymax, mz, zmax), self.capacidad),
            OctreeNode((mx, xmax, my, ymax, mz, zmax), self.capacidad)
        ]
        self.is_divided = True

    def insert(self, point):
        """
        Inserta un punto en el Octree.
        
        :param point: El punto a insertar, una tupla (x, y, z).
        :return: True si el punto se insertó correctamente, False si no.
        """
        # Verificar si el punto está dentro del límite del nodo
        xmin, xmax, ymin, ymax, zmin, zmax = self.limites
        x, y, z = point
        if not (xmin <= x <= xmax and ymin <= y <= ymax and zmin <= z <= zmax):
            return False  # El punto está fuera del límite del nodo

        # Si el nodo no ha sido dividido y tiene espacio, insertamos el punto
        if len(self.points) < self.capacidad:
            self.points.append(point)
            return True
        
        # Si el nodo está lleno y no ha sido subdividido, lo subdividimos
        if not self.is_divided:
            self._subdivide()

        # Intentamos insertar el punto en los subnodos
        for child in self.children:
            if child.insert(point):
                return True
        
        return False

    def query(self, limites):
        """
        Devuelve una lista de puntos dentro de un límite especificado.

        :param limites: Un límite de búsqueda, una tupla (xmin, xmax, ymin, ymax, zmin, zmax).
        :return: Lista de puntos dentro del límite.
        """
        xmin, xmax, ymin, ymax, zmin, zmax = limites
        result = []

        # Verificar si el límite de búsqueda se cruza con este nodo
        x1, x2, y1, y2, z1, z2 = self.limites
        if xmax < x1 or xmin > x2 or ymax < y1 or ymin > y2 or zmax < z1 or zmin > z2:
            return result  # No hay intersección

        # Agregar puntos de este nodo si están dentro del límite
        for point in self.points:
            x, y, z = point
            if xmin <= x <= xmax and ymin <= y <= ymax and zmin <= z <= zmax:
                result.append(point)

        # Si el nodo está dividido, consultar los subnodos
        if self.is_divided:
            for child in self.children:
                result.extend(child.query(limites))

        return result


# Crear un Octree con un límite de espacio de (0, 100, 0, 100, 0, 100) y una capacidad de 4 puntos por nodo
octree = OctreeNode((0, 1, 0, 1, 0, 1), capacidad=4)

# Insertar algunos puntos
filename = "puntos.txt"
with open(filename, "r") as readfile:
    puntos = readfile.readlines()

for punto in puntos:
    punto = tuple(float(num) for num in punto.split(', '))
    octree.insert(punto)


# Consultar puntos dentro de un límite específico
limites_query = (0, 1, 0.2, 1, 0.4, 1)
points_in_range = octree.query(limites_query)

print(f"Puntos dentro de la consulta: {points_in_range}")
