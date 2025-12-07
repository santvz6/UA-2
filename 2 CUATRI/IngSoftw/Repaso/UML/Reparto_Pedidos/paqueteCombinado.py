from paquete import Paquete


class PaqueteCombinado(Paquete):
    def __init__(self, paquetes: list[Paquete]):
        self.paquetes = paquetes

    @property
    def direccion(self):
        direccion_total = ""
        for paquete in self.paquetes:
            direccion_total += paquete.direccion + " "
        return direccion_total
    
    @property
    def peso(self):
        peso_total = 0
        for paquete in self.paquetes:
            peso_total += paquete.peso
        return peso_total
