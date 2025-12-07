from .iAgente import IAgente
from tarea import Tarea

import logging


logger = logging.getLogger(__name__)

class AgenteComercial(IAgente):

    def __init__(self) -> None:
        self.__tipo = "COMERCIAL"

    def get_tipo(self) -> str:
        return self.__tipo
    
    def ejecutar_tarea(self, tarea: Tarea) -> None:

        logger.info(f"Procesando Tarea: {tarea.descripcion}.")
        tarea.estado = "COMPLETADA"
        logger.info(f"Tarea Procesada.")
