from repartidor import Repartidor
from paquete import Paquete

import logging


logger = logging.getLogger(__name__)

class Equipo:
    def __init__(self, repartidores: list[Repartidor]):
        self.repartidores = repartidores

    def asignar_paquete(self, paquete: Paquete) -> None:
        for i, repartidor in enumerate(self.repartidores):
            try:
                repartidor.asignar_paquete(paquete)
            except ValueError:
                logger.info(f"Excepción: El repartidor {i} no dispone de más capacidad de carga.")
                continue
            else:
                logger.info(f"Paquete {paquete.direccion} asignado al repartidor {i}.")
                break