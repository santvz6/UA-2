import time 
import numpy as np
import matplotlib.pyplot as plt

class Algoritmo1:
    def __init__(self, NUM_EJECUCIONES: int):
        
        self.NUM_EJECUCIONES = NUM_EJECUCIONES
        self.SIZES = np.linspace(5, 1_000, 50)
        self.BLOQUEO = 0
        self.obtenerCasos()

    def g(self, n: int):
        if n == 1:
            self.BLOQUEO = 0
            return n
        
        self.BLOQUEO += 1
        if self.BLOQUEO < 990:
            return self.g(n -1) 
        else:
            self.BLOQUEO = 0
            return -1
    

        

    def getTiempo(self, n):
        inicio = time.time()
        self.g(n)
        fin = time.time()
        return fin - inicio
    
    def obtenerCasos(self):
        """
        Mejor caso: n==1
        Peor caso: n < 1 o número muy alto
        Caso normal: Número entre [1, infinito]
        """
        
        T_normal = np.zeros((len(self.SIZES)))
        T_peor = np.zeros((len(self.SIZES))) 
        T_mejor =  np.zeros((len(self.SIZES))) 


        for _ in range(self.NUM_EJECUCIONES):
            for i, size in enumerate(self.SIZES):
                T_normal[i] += self.getTiempo(np.random.randint(1, size))
                T_peor[i] += self.getTiempo(0)
                T_mejor[i] += self.getTiempo(1)
        
        self.dibujarGrafico((T_normal/self.NUM_EJECUCIONES, T_peor/self.NUM_EJECUCIONES, T_mejor/self.NUM_EJECUCIONES))
    
    def dibujarGrafico(self, Y: tuple):
        print(Y)
        colores = {0: "red", 1:"green", 2: "blue"}
        leyenda = {0: "Caso normal", 1:"Peor caso", 2: "Mejor caso"}
        for i, y in enumerate(Y):
            plt.plot(self.SIZES, y, color = colores[i], label = leyenda[i])
        
        # Media peor caso
        plt.plot(self.SIZES, np.zeros((len(self.SIZES))) + np.mean(Y[1]), color="yellow", linestyle="--")
        
        # Función n (Complejidad teórica)
        FACTOR = 10**(-6.65) # Máx cifra en Tiempo (4) -> 0.000x
        # Tamaños puede tener 1, 2, 3 o 4 cifras (5, 48, 712, 1000) -> digamos que de normal 2.65 -> 4 + 2.65 = 6.65

        plt.plot(self.SIZES, self.SIZES * FACTOR, color="orange")

        plt.legend()  
        plt.savefig("P1.3/E1.png")
        plt.show()


# Instancia del Alg1
alg1 = Algoritmo1(100)