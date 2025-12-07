import logging
from paquete import Paquete
from paqueteCombinado import PaqueteCombinado
from repartidor import Repartidor
from equipo import Equipo


logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="logs/app.log"
)

if __name__ == "__main__":
    

    paquetes = [
        Paquete("Calle A", zona=1, peso=3),
        Paquete("Calle B", zona=1, peso=2),
        Paquete("Calle C", zona=2, peso=4),
        Paquete("Calle D", zona=2, peso=6),
        Paquete("Calle E", zona=1, peso=1),
    ]

    
    paquete_combinado = PaqueteCombinado([
        Paquete("Calle F", zona=3, peso=7), 
        Paquete("Calle G", zona=3, peso=2)])

    repartidores = [
        Repartidor(zona=1, carga_max=5),
        Repartidor(zona=2, carga_max=10),
        Repartidor(zona=1, carga_max=8),
        Repartidor(zona=3, carga_max=9),
    ]

  
    equipo = Equipo(repartidores)

    
    for paquete in paquetes + [paquete_combinado] + [Paquete("Calle H", zona=1, peso=7)]:
        equipo.asignar_paquete(paquete)
        