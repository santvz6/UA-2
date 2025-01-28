"""
Van a poner algo del estilo Knapsack ya que dijeron que no sería tan "difícil"
como el de la princesa. Por tanto pondrán algo simple que hemos visto.
"""
import numpy as np

### EQUIPO GUISPLAY

nombres = ["Guisplay", "Manolo", "ElSensibilidades", "Alextini", "Conchoceratops", "Carlitos"]

costes = [6, 5, 6, 7, 2, 3]
valoraciones = [8, 8, 7, 9, 3, 5]
presupuesto:int =  14

# Empezamos con Recursividad + Memoización
class Fortnite:
    def __init__(self, nombres:list, costes:list, valoraciones:list, presupuesto:int) -> None:
        
        self.nombres = nombres
        self.costes = costes
        self.valoraciones = valoraciones
        self.presupuesto = presupuesto

        self.n = len(costes)

        self.mem_memoizacion = np.zeros((self.n, presupuesto+1)) - 1
        self.mem_memoizacion[:, 0] = 0 # Cuando el presupuesto es 0

        # Llamada a métodos
        self.m1 = self.formarEquipoMemoizacion(self.costes, self.valoraciones, self.presupuesto, self.n-1)
        self.m2 = self.formarEquipoIterativo(self.costes, self.valoraciones, self.presupuesto, self.n)
        self.m3 = self.backtracking(self.m2, self.costes, self.valoraciones, self.presupuesto, self.n)


    def __str__(self) -> str:
        return f"""
        formarEquipoMemoizacion -> {self.m1}
        formarEquipoIterativo -> Array \n{self.m2}
        backtracking -> {self.m3}
        EquipoFormado -> {[self.nombres[indx] for indx in self.m3]}
        """
        

    def formarEquipoMemoizacion(self, costes:list , valoraciones:list , presupuesto: int, n:int) -> int:
    
    # Memoizacion    
        actual = self.mem_memoizacion[n, presupuesto]
        if actual != - 1:
            return actual
        
    # Caso Base
        if n < 0:
            return 0
        
    # Caso recursivo

        # NO hay espacio
        if costes[n] > presupuesto:
            return self.formarEquipoMemoizacion(costes, valoraciones, presupuesto, n-1)
        
        # NO agarramos ningún jugador
        no = self.formarEquipoMemoizacion(costes, valoraciones, presupuesto, n-1)
        # SÍ agarramos algún jugador
        si = valoraciones[n] + self.formarEquipoMemoizacion(costes, valoraciones, presupuesto-costes[n], n-1)

        actual = max(si, no)
        return actual
    
    def formarEquipoIterativo(self, costes:list , valoraciones:list , presupuesto: int, n:int) -> np.array:

    # Creación memoria
        """
        Consideramo[0] y presupesto[0] como == 0 (por eso usamos np.zeros)
        Vamos a trabajar desde n[1] y presupuesto[1]
        """
        mem = np.zeros((self.n+1, presupuesto+1)) 

        for i in range(1, self.n+1):
            for j in range(1, presupuesto+1):
                
            # No hay espacio
                """Este "i-1" no hace referencia al anterior, hace referencia al indice correspondiente (es una lista, empieza en 0)"""
                if costes[i-1] > j:
                    """ Este "i-1" sí hace referencia a la "n" anterior de la lista"""
                    mem[i, j] = mem[i-1, j]
                
            # Hay espacio
                else:
                    no = mem[i-1, j]
                    si = mem[i-1, j-costes[i-1]] + valoraciones[i-1]
            
                    mem[i, j] = max(no, si)

        return mem

    def backtracking(self, mem:np.array, costes:list , valoraciones:list , presupuesto: int, n:int) -> list:

        i, p = n, presupuesto
        solucion = list()

        while i>0 and p>0:
            
            no = mem[i-1, p]
            si = mem[i-1, p-costes[i-1]] + valoraciones[i-1]

        # Actualmente venimos de SÍ haber agarrado anteriormente un jugador
            if mem[i, p] == si:
                """El orden de estas tres operaciones es bastante importante"""
                p -= costes[i-1]
                i -= 1 
                solucion += [i]

        # Actualmente venimos de NO haber agarrado anteriormente un jugador
            else:
                i -= 1

        return solucion

fortnite = Fortnite(nombres, costes, valoraciones, presupuesto)
print(fortnite)