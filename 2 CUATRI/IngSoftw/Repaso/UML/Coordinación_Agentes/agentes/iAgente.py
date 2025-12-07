from abc import ABC, abstractmethod
from tarea import Tarea

class IAgente(ABC):

    @abstractmethod
    def get_tipo(self) -> str: # pragma: no cover
        pass

    @abstractmethod
    def ejecutar_tarea(self, tarea: Tarea) -> None: # pragma: no cover
        pass
