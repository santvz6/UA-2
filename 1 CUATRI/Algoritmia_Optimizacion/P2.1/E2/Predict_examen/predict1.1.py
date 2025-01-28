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

    # Variables - Atributos
        self.n = len(costes)

        self.mem_memo = np.zeros((self.n, presupuesto+1)) - 1

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
    
    def formarEquipoMemoizacion(self, costes:list, valoraciones:list, presupuesto:int, n:int):
    
    # Caso memoizacion
        actual = self.mem_memo[n, presupuesto] 
        if actual != -1:
            return actual

    # Caso base
        if n < 0:
            return 0
    
    # Caso recursivo

        # No hay presupuesto
        if presupuesto < costes[n]:
            return self.formarEquipoMemoizacion(costes, valoraciones, presupuesto, n-1)
        # Hay presupuesto

        si = valoraciones[n] + self.formarEquipoMemoizacion(costes, valoraciones, presupuesto-costes[n], n-1)
        no = self.formarEquipoMemoizacion(costes, valoraciones, presupuesto, n-1)

        actual = max(si, no)
        return actual
    
    def formarEquipoIterativo(self, costes, valoraciones, presupuesto, n):

    # Creación memoria
        mem = np.zeros((n+1, presupuesto+1)) # Fila y columna extra de: 0 elementos (n) y presupuesto 0 (presupuesto)

        for i in range(1, n+1):
            for j in range(1, presupuesto+1):
            
            # No hay presupuesto
                if costes[i-1] > j:
                    mem[i, j] = mem[i-1, j] 
            # Hay presupuesto    
                else:
                    si = valoraciones[i-1] + mem[i-1, j-costes[i-1]]
                    no = mem[i-1, j] 
                    mem[i, j] = max(si, no)
        return mem
    
    def backtracking(self, mem, costes, valoraciones, presupuesto, n):

        i, p = n, presupuesto
        solucion = list()

        while i > 0 and p > 0:

            si = valoraciones[i-1] + mem[i-1, p-costes[i-1]]
            no = mem[i-1, p-1]

        # Anteriormente se eligió jugador
            if mem[i, p] == si:
                p -= costes[i-1]
                i -= 1
                solucion += [i]
        # Anteriormente no se eligió jugador
            else:
                i-=1

        return solucion

fortnite = Fortnite(nombres, costes, valoraciones, presupuesto)
print(fortnite)