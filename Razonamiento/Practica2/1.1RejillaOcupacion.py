import numpy as np

class RejillaOcupacion:
    def __init__(self, filename= "puntos.txt") -> None:
        with open(filename, "r") as readfile:
            self.tamañoMapa = len(readfile.readlines())

        self.rejilla = np.full((self.tamañoMapa, self.tamañoMapa), -1)
    
    def  __str__(self) -> str:
        return str(self.rejilla)
    
    def actualizarCelda(self, x, y, probabilidad) -> None:
        self.rejilla[y, x] = probabilidad
        

if __name__ == "__main__":

    # Crear una rejilla de ocupación
    rejilla = RejillaOcupacion()

    # Actualizar algunas celdas con datos de sensores
    rejilla.actualizarCelda(1, 1, 1)    # ocupado
    rejilla.actualizarCelda(4, 5, 0)    # libre

    # Mostrar la rejilla
    print(rejilla)