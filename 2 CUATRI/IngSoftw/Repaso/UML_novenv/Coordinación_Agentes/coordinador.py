from agentes import AgenteComercial, AgenteAsistencia, IAgente
from tarea import Tarea


class Coordinador:
    def __init__(self) -> None:
        self.__agentes: list[IAgente] = [
            AgenteComercial(), 
            AgenteAsistencia(),
            AgenteComercial(), 
            AgenteComercial(), 
            AgenteComercial(), 
            AgenteAsistencia(),
            AgenteComercial(), 
            AgenteAsistencia(),
            AgenteAsistencia()]
         
    def asignar_tarea(self, tarea: Tarea) -> None:
        
        for agente in self.__agentes:
            if agente.get_tipo() == tarea.tipo:

                if tarea.tipo == "ASISTENCIA":
                    if agente.estado == "LIBRE":
                        agente.ejecutar_tarea(tarea)
                        break

                else:
                    agente.ejecutar_tarea(tarea)
                    break
                    
            else:
                continue
  
  
    ########################### AÑADIDO POR MÍ PARA TESTS    
    @property
    def agentes(self):
        return self.__agentes.copy()

    def __len__(self):
        return len(self.__agentes)
    