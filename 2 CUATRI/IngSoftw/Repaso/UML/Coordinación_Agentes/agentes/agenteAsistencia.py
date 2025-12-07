from .iAgente import IAgente
from tarea import Tarea

import logging


logger = logging.getLogger(__name__)

class AgenteAsistencia(IAgente):

    def __init__(self) -> None:
        self.__tipo = "ASISTENCIA"
        self.__estado = "LIBRE"

    @property
    def estado(self):
        return self.__estado

    def get_tipo(self) -> str:
        return self.__tipo
    
    def ejecutar_tarea(self, tarea: Tarea) -> None:
        self.__estado = "OCUPADO"  

        logger.info(f"Procesando Tarea: {tarea.descripcion}.")
        tarea.estado = "COMPLETADA"
        logger.info(f"Tarea Procesada.")

        self.__estado = "LIBRE"

    
    #################### AÑADIDO POR MÍ PARA TESTS
    def bloquear(self):
        self.__estado = "OCUPADO"
    