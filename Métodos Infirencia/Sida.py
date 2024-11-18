import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

RED = (1, 0, 0)
GREEN = (0, 1, 0)
BLUE = (0, 0, 1)
GRAY =  (0.4, 0.4, 0.4)

    
class Persona:        

    cont_ID = 0

    def __init__(self) -> None:
        Persona.cont_ID += 1
        self.ID = Persona.cont_ID

        self.edad= np.random.normal(43, 1)
        self.Posx=np.random.rand()
        self.Posy=np.random.rand()
        self.sexo="hombre" if np.random.randint(0, 2) == 0 else "mujer"
                             #sano, infectado, inmune, muerto

        self.FACTOR_MOVIMIENTO = 0.5
        self.Vx=np.random.choice([0.01,-0.01]) * self.FACTOR_MOVIMIENTO
        self.Vy=np.random.choice([0.01,-0.01]) * self.FACTOR_MOVIMIENTO

        self.estado="sano"   
        self.color = ()
        self.tcont=0        # representa el instante cuando se ha inmune    


    def __str__ (self) -> str:
        return f"""
        ID= {self.ID}
        (x,y)= ({self.Posx}, {self.Posy})
        edad= {self.edad} 
        estado= {self.estado}
        """

    def setInfo(self, estado: str, color= tuple) -> None:
        self.estado = estado
        self.color = color
    
    def getInfo(self) -> tuple:
        return self.estado, self.color, (self.Posx, self.Posy)

    def move(self) -> None:
       self.Posx += self.Vx
       self.Posy += self.Vy       
       if self.Posx <= 0 or self.Posx >= 1:  # Colisión con borde izquierdo o derecho
           self.Vx *=-1
       if self.Posy <= 0 or self.Posy >= 1:  # Colisión con borde izquierdo o derecho
           self.Vy *=-1          
       


########################################################
#######    Agrupacion   Lista de personas con una misma característica. p.e. estar sano
########################################################                
           
class Agrupacion:    
    
    def __init__(self, n:int, sname:str, color:tuple) -> None:  
        self.caracter = sname   
        self.color = color

        self.Lpersonas = [Persona() for _ in range(n)]
        
    def setInfo(self, nuevo_estado: str, color: tuple) -> None:
        for persona in self.Lpersonas:
            persona.setInfo(estado= nuevo_estado, color= color)
        
    def move(self) -> None:
        for persona in self.Lpersonas:
            persona.move()
    
    def getLpersonas(self) -> list:
        return self.Lpersonas
    
########################################################
#######    Poblacion
########################################################                
class Poblacion: 

    iteracion=0    #instante en el que está viviendo. Cada vez que evoluciona, t incrementa
    
    def __init__(self,nombre:str ,nsanos:int ,ninfectados:int) -> None:    
        self.nombre = nombre
        self.contactos=0     # Debug -> cuántas proximidades se han producido

        self.AgrupSana = Agrupacion(n=nsanos, sname="Sanos", color= GREEN)
        self.AgrupSana.setInfo("sano", self.AgrupSana.color)

        self.AgrupInfectada = Agrupacion(n=ninfectados, sname="Infectados", color=RED)
        self.AgrupInfectada.setInfo("infectado", self.AgrupInfectada.color)
        
        self.AgrupInmune=Agrupacion(0, sname="Inmunes", color=BLUE)
        self.AgrupInmune.setInfo("inmune", self.AgrupInmune.color)
        
        self.AgrupFallecida=Agrupacion(0, sname="Fallecidos", color=GRAY)
        self.AgrupFallecida.setInfo("fallecido", self.AgrupFallecida.color)  
    
        self.dist_contagio=0.05
        self.prob_contagio=0.2
        self.prob_muerte=0.5
        self.tiempo_contagio=20


    def __str__ (self) -> str:   

        num_personas = self.lenAgrupaciones()

        return f"""
        Resumen de la población {self.nombre}
        Personas sanas: {num_personas[0]}
        Personas infectadas: {num_personas[1]}
        Personas inmunes: {num_personas[2]}
        Personas fallecidas: {num_personas[3]}
        """

    def move(self) -> None:
        self.AgrupSana.move()
        self.AgrupInmune.move()
        self.AgrupInfectada.move()
    
    def sano_a_Infectado(self) -> None:
        for infectado in self.AgrupInfectada.getLpersonas():           
            for sano in self.AgrupSana.getLpersonas():
                distancia = getDistancia(infectado,sano)

                if (distancia < self.dist_contagio) and (np.random.rand() < self.prob_contagio): #Se produce contacto y contagio

                    sano.tcont = self.iteracion   #Instante que se produce la infección
                    sano.setInfo(estado="infectado", color=RED)

                    self.AgrupSana.getLpersonas().remove(sano)
                    self.AgrupInfectada.getLpersonas().append(sano) 


                    self.contactos += 1  # ¿Contactos totales o infectados actuales?
    
    def infectado_a_Inmune(self) -> None:
        for infectado in self.AgrupInfectada.getLpersonas():
            if self.iteracion - infectado.tcont > self.tiempo_contagio:
                infectado.setInfo(estado="inmune", color=BLUE)

                self.AgrupInfectada.getLpersonas().remove(infectado)
                self.AgrupInmune.getLpersonas().append(infectado)


    def calcularFallecer(self, infectado: object):
        CTE_sexo = 0.5 if infectado.sexo == "hombre" else 0.5
        CTE_edad = getNormal(media=30, desviacion=18, X=infectado.edad)
        return self.prob_muerte * CTE_sexo * CTE_edad


    def infectado_a_Fallecido(self) -> None:
        for infectado in self.AgrupInfectada.getLpersonas():
            if np.random.rand() < self.calcularFallecer(infectado):
                infectado.setInfo(estado="fallecido", color=GRAY)
                self.AgrupInfectada.getLpersonas().remove(infectado)
                self.AgrupFallecida.getLpersonas().append(infectado)

    def evoluciona(self) -> None:  
       
        self.iteracion += 1
        self.move()

        self.sano_a_Infectado()
        self.infectado_a_Inmune()
        self.infectado_a_Fallecido()

        # ¿En cada iteración realizamos la aleatorización de muerte?
        # ¿O lo hacemos una vez cuando ya ha superado el tiempo de infectado?

    def positions(self) -> tuple:
        LP = list()
        colores = list()

        for persona in self.getPopulation():

            # estado, color, (Posx, Posy)
            informacion = persona.getInfo()

            LP.append(informacion[2])
            colores.append(informacion[1])
 
        return LP,colores
    
    def getPopulation(self) -> list:
        return self.AgrupInmune.getLpersonas() + self.AgrupInfectada.getLpersonas() + self.AgrupSana.getLpersonas() + self.AgrupFallecida.getLpersonas()

    def lenAgrupaciones(self) -> tuple:
        return len(self.AgrupSana.getLpersonas()), len(self.AgrupInfectada.getLpersonas()), len(self.AgrupInmune.getLpersonas()), len(self.AgrupFallecida.getLpersonas())

    # Este método no se utiliza
    def dist_total(self) -> tuple:
        S,Smin,Smax =0,100000000,0        
        for infectado in self.AgrupSana.getLpersonas():
            for sano in self.AgrupInfectada.getLpersonas():
                distancia = getDistancia(infectado, sano)
                S += distancia
                if distancia < Smin: Smin = distancia
                if distancia > Smax: Smax = distancia  

        return S,Smin,Smax


########################################################
#######    FUNCIONES        
######################################################## 

def getNormal(media, desviacion, X):
    coeficiente = 1 / (desviacion* np.sqrt(2 * np.pi))
    exponente = -0.5 * ((X - media) / desviacion) ** 2
    return coeficiente * np.exp(exponente)

def getDistancia(infectado: object, sano: object) -> float:
    return ((infectado.Posx-sano.Posx)**2+(infectado.Posy-sano.Posy)**2)**(0.5)

# Función de actualización para la animación
def update(frame):
    global positions, velocities,i,ax
    # Actualizar posiciones    
    i+=1
    #positions += v
    # Verificar colisiones con los bordes y cambiar dirección
    positions,colores = miPueblo1.positions()            
    print(i,"---> ",miPueblo1.lenAgrupaciones())   
    scat.set_offsets(positions) 
    scat.set_facecolors(colores)   
    miPueblo1.evoluciona() 


       
# Configuración inicial de los puntos: posiciones y velocidades
#np.random.seed(0)  # Para reproducibilidad

########################################################

########################################################
#######    Población
######################################################## 
NN=500           #Nº de individuos en la población
miPueblo1=Poblacion("Xixona",NN,1)
print(miPueblo1)

########################################################
#######    Draw
########################################################    

N = len(miPueblo1.getPopulation())

positions = np.random.rand(N, 2)               # Posiciones iniciales entre [0 y 1]
velocities = ((np.random.rand(N, 2)) * 2-1)/2  # Velocidades aleatorias en el rango [-1, 1]
nn = int(N/2)

colores=[]
#for i in range(N) : colores.append([255,0,0])  # Por si quiero poner colores aleatorios en la población

# Configurar la figura y los límites
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("Pandemia")
ax.color="Red"
scat = ax.scatter(positions[:, 0], positions[:, 1])
i=0    #Nº de frame que estoy actualizando. Inicializado a cero


# Crear animación
duracion_mp4 = 15
Nfps= 15                           # Nº de frames por segundo para visualizar el estado de la población
Nframes= Nfps * duracion_mp4        # Nº de pasos a dibujar en un ciclo completo

ani = FuncAnimation(fig, update, frames=Nframes)
ani.save("animation.mp4", writer="ffmpeg", fps=Nfps)


#########################################################
#   Este código genera un gráfico estático con la evolución de la población. 
#########################################################

miPueblo2 = Poblacion("Mutxamel",NN,1)
print(miPueblo2)

positions=[]
colores=[]

for i in range(Nframes):
    sanos,infect,contag,fallecidos = miPueblo2.lenAgrupaciones()

    miPueblo2.evoluciona()
    positions.append([i/Nframes,infect/NN])
    colores.append(RED)
    positions.append([i/Nframes,contag/NN])
    colores.append(BLUE)
    positions.append([i/Nframes,sanos/NN])
    colores.append(GREEN)
    positions.append([i/Nframes,fallecidos/NN])
    colores.append(GRAY)


scat.set_offsets(positions)    
scat.set_facecolors(colores) 

plt.savefig("imagen.png")

plt.show()

print("--------------------------------------")
print(miPueblo1)