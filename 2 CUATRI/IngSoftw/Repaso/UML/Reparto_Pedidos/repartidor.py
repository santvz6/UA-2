from paquete import Paquete

import logging


logger = logging.getLogger(__name__)

class Repartidor:
    def __init__(self, zona: int, carga_max: int):
        self.__zona = zona
        self.carga_max = carga_max

        self.__carga = 0

    def asignar_paquete(self, paquete: Paquete) -> None:
        carga_disponible = self.carga_max - self.__carga
        
        if paquete.peso <= carga_disponible:
            self.__carga += paquete.peso
        
        else:
            logger.error("El repartidor no dispone de más capacidad de carga.")
            raise ValueError("El repartidor no dispone de más capacidad de carga.")
