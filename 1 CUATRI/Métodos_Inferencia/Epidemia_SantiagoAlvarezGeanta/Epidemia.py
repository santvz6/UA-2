import numpy as np

import pandas as pd
from scipy.stats import t, f

import os


RED = (1, 0, 0)
GREEN = (0, 1, 0)
BLUE = (0, 0, 1)
GRAY =  (0.4, 0.4, 0.4)

    
class Persona:        

    cont_ID = 0

    def __init__(self, limitePoblacion: tuple, numDivisiones: int, barrio: int) -> None:
        Persona.cont_ID += 1
        self.ID = Persona.cont_ID

        edad = np.abs(np.random.normal(38, 10))
        self.edad= edad if edad > 0 else 0
  
        # El límite en X varía
        self.limInicialx, self.limFinalx = (barrio * limitePoblacion[0])/(numDivisiones+1), (barrio+1) * limitePoblacion[0]/(numDivisiones+1)
        # El límite en Y nunca varía
        self.limInicialy, self.limFinaly = 0, limitePoblacion[1]

        self.Posx= np.random.rand() * limitePoblacion[0]/(numDivisiones+1) + (barrio*limitePoblacion[0])/(numDivisiones+1) if numDivisiones > 0 else np.random.rand() * self.limFinalx
        self.Posy= np.random.rand() * self.limFinaly
        self.sexo= "hombre" if np.random.binomial(1, 0.55) == 0 else "mujer"

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
       if self.Posx <= self.limInicialx or self.Posx >= self.limFinalx:  # Colisión con borde izquierdo o derecho
           self.Vx *= -1
       if self.Posy <= self.limInicialy or self.Posy >= self.limFinaly:  # Colisión con borde izquierdo o derecho
           self.Vy *= -1
       


########################################################
#######    Agrupacion   Lista de personas con una misma característica. p.e. estar sano
########################################################                
           
class Agrupacion:    
    
    def __init__(self, n:int, sname:str, color:tuple, numDivisiones:int, limitePoblacion:tuple) -> None:  
        self.caracter = sname   
        self.color = color
        self.Lpersonas = list()

        for _ in range(n):
            
            aleatorio = np.random.randint(0, numDivisiones+1)
            self.Lpersonas.append(Persona(limitePoblacion= limitePoblacion, numDivisiones= numDivisiones, barrio= aleatorio))
        
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


    def __init__(self,nombre:str ,nsanos:int ,ninfectados:int, numDivisiones= 0, limitePoblacion= (1, 1)) -> None:    
        self.nombre = nombre
        self.limite = limitePoblacion
        self.contactos=0     # Debug -> cuántas proximidades se han producido

        self.AgrupSana = Agrupacion(n=nsanos, sname="Sanos", color= GREEN, numDivisiones= numDivisiones, limitePoblacion= limitePoblacion)
        self.AgrupSana.setInfo("sano", self.AgrupSana.color)

        self.AgrupInfectada = Agrupacion(n=ninfectados, sname="Infectados", color=RED, numDivisiones= numDivisiones, limitePoblacion= limitePoblacion)
        self.AgrupInfectada.setInfo("infectado", self.AgrupInfectada.color)
        
        self.AgrupInmune=Agrupacion(0, sname="Inmunes", color=BLUE, numDivisiones= numDivisiones, limitePoblacion= limitePoblacion)
        self.AgrupInmune.setInfo("inmune", self.AgrupInmune.color)
        
        self.AgrupFallecida=Agrupacion(0, sname="Fallecidos", color=GRAY, numDivisiones= numDivisiones, limitePoblacion= limitePoblacion)
        self.AgrupFallecida.setInfo("fallecido", self.AgrupFallecida.color)  
    

        self.dist_contagio=0.05
        self.prob_muerte=0.005
        self.tiempo_contagio=20

        self.iteracion = 0    

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

                if sano.sexo == "hombre":
                    self.prob_contagio = (0.05 if sano.edad < 31
                                        else 0.08 if sano.edad < 61
                                        else 0.09)
                elif sano.sexo == "mujer":
                    self.prob_contagio = (0.06 if sano.edad < 31
                                        else 0.1 if sano.edad < 61
                                        else 0.13)

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

    def calcularFallecer(self, infectado: object) -> float:
        CTE_sexo = 1 # No se ha especificado quién tiene más probabilidad de fallecer
        CTE_edad = 1 # Tampoco se ha especificado
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
    
    def ciclo(self, maxIteraciones=1000) -> list:

        for _ in range(maxIteraciones):
            # Quedan personas Infectadas
            if not len(self.AgrupInfectada.getLpersonas()) == 0:
                self.evoluciona()
            # No hay personas infectadas
            else:
                return self.lenAgrupaciones()
            
            print(f"P{self.nombre} - I{self.iteracion} -> {self.lenAgrupaciones()}")

        return self.lenAgrupaciones()
        



########################################################
#######    FUNCIONES        
######################################################## 

def getInvNormal(media, desviacion, X):
    return (1 / (desviacion * np.sqrt(2 * np.pi))) * np.exp(-((X - media)**2) / (2 * desviacion**2))

def getDistancia(infectado: object, sano: object) -> float:
    return ((infectado.Posx-sano.Posx)**2+(infectado.Posy-sano.Posy)**2)**(0.5)

def getIntervaloConfianza(muestra: list[int], confianza=0.93) -> tuple:
 
    alfa = 1 - confianza 
    n = len(muestra)
    mediaPoblacional = sum(muestra) / n


    numeradorVarianza = 0
    for valor in muestra:
        numeradorVarianza += (valor - mediaPoblacional) ** 2
    varianzaPoblacional = numeradorVarianza / (n - 1)


    # Intervalo conociendo la desviacionPoblacional 
    tStudent = t.ppf(1 - alfa/2, n-1) 
    I1 = mediaPoblacional - (tStudent * np.sqrt(varianzaPoblacional) / np.sqrt(n))
    I2 = mediaPoblacional + (tStudent * np.sqrt(varianzaPoblacional) / np.sqrt(n))
    return float(I1), float(I2)

def getContrasteVarianza(n1, n2, S1, S2, alfa= 0.05) -> bool:
    
    # Valor P
    valorP = S1 / S2

    # Valor Alfa

    # HE CAMBIADO EL ORDEN DE 1-ALFA/2 EN DERECHA E IZQUIERDA
    valorAlfaDer = f.ppf(1-alfa/2, n1-1, n2-1) # F-snedecor (valor crítico -> ppf)
    valorAlfaIzq = f.ppf(alfa/2, n1-1, n2-1)
    
    print(valorAlfaIzq, valorP, valorAlfaDer)

    return not(valorAlfaIzq < valorP < valorAlfaDer)

def getContrasteMedia(muestra1: list[int], muestra2: list[int], alfa= 0.05) -> tuple[bool, bool]:
    
# Desconocemos las varianzas

    n1 = len(muestra1)
    X1 = sum(muestra1) / n1

    n2 = len(muestra2)
    X2 = sum(muestra2) / n2

    numeradorVarianza1 = numeradorVarianza2 = 0
    for valor1, valor2 in zip(muestra1, muestra2):
        numeradorVarianza1 += (valor1 - X1) ** 2
        numeradorVarianza2 += (valor2 - X2) ** 2

    S1 = numeradorVarianza1 / (n1 - 1) # S^2
    S2 = numeradorVarianza2 / (n2 - 1) # S^2

    mismaVarianza = getContrasteVarianza(n1= n1, n2= n2, 
                                         S1= S1, S2 = S2,
                                         alfa= alfa)
    
    if mismaVarianza:

        # Valor P
        numeradorP = X1 - X2

        Sd = ((n1-1)*S1 + (n2-1)*S2) / (n1+n2-2) # Sd^2
        denominadorP = (Sd**0.5) * (((1/n1) + (1/n2))**0.5)

        # Valor Alfa
        valorAlfa = t.ppf(alfa/2, n1+n2-2) # Distribución T-Student

    else:
        # Valor P
        numeradorP = X1 - X2
        denominadorP = ((S1/n1) + (S2/n2)) ** 0.5

        # Valor Alfa
        delta =  ((n2-1)*(S2**0.5) - (n1-1)*(S1**0.5))**2 / ((n2-1)*S2 + (n1-1)*S1)
        g = n1 + n2 - 2 - int(delta)
        valorAlfa = t.ppf(alfa/2, g) # Distribución T-Student

    return not(abs(numeradorP / denominadorP) > abs(valorAlfa)), mismaVarianza



def crearCSV(filePath):
    columns = ["pueblo", "sano", "infectado", "inmune", "fallecido"]
    df = pd.DataFrame(columns=columns)
    df.to_csv(filePath, index=False)

def añadirCSV(filePath, pueblo, sano, infectado, inmune, fallecido):
    fila = [[pueblo, sano, infectado, inmune, fallecido]]
    df2 = pd.DataFrame(fila, columns=["pueblo", "sano", "infectado", "inmune", "fallecido"])

    try:
        open(filePath) 
    except FileNotFoundError:
        crearCSV(filePath)
    
    df1 = pd.read_csv(filePath) 
    df = pd.concat([df1, df2], ignore_index=True)
    df.to_csv(filePath, index=False)

def getColumnaCSV(filePath, columna: str):
    try:
        df = pd.read_csv(filePath)
    except FileNotFoundError:
        crearCSV(filePath)
        return list()
    else:
        columna = df[str(columna)]
        return columna

# Configuración inicial de los puntos: posiciones y velocidades
#np.random.seed(0)  # Para reproducibilidad

########################################################

########################################################
#######    Población
######################################################## 

NN=1000          #Nº de individuos en la población
NUM_EJECUCIONES = 200
LIMITE = (1, 1)
DIVISIONES = 0
confianza = 0.93

fileCSV = "PrimeraEntrega.csv"
CSV_ACTIVO = True if len(getColumnaCSV(filePath=fileCSV, columna="pueblo")) >= NUM_EJECUCIONES else False


if not CSV_ACTIVO:

    # Borramos si ya existe uno a la mitad
    if os.path.exists(fileCSV):
        os.remove(fileCSV)

    for i in range(NUM_EJECUCIONES):
        miPueblo = Poblacion(str(i), nsanos= NN, ninfectados= 1, limitePoblacion= LIMITE, numDivisiones= DIVISIONES)
        sanos, infectados, inmunes, fallecidos = miPueblo.ciclo(maxIteraciones= 1000)

        # Añadimos los nuevos datos
        añadirCSV(filePath= fileCSV, pueblo= miPueblo.nombre,
                sano=sanos, infectado=infectados, inmune=inmunes, fallecido=fallecidos)
    


############################################## entrega 1
def primeraEntrega():
    # 1. 915 Individuos
    print(f"Número de individuos: {NN}")

    # 2. Edad -> distribución N(38, 10)
    edad = np.random.normal(38, 10)

    # 3. La proporción de mujeres en dicha población es de un 55%
    sexo = "hombre" if np.random.binomial(1, 0.55) == 0 else "mujer"

    # 4. La probabilidad de que una mujer contagie a otra persona de una determinada enfermedad viene dada por los valores 6%,10%,13%
    # según esté en el intervalo de edad menor de 30 años, entre 31 y 60 ó mayor de 60.
    # En un hombre, las probabilidades vienen dadas por 5%,8%,9%.

    """ Línea 148 -> sano_a_Infectado()"""

    # 5. Inicializa la población con un infectado. Elabora un método (ciclo)

    # miPueblo = Poblacion(str(i), nsanos= NN, ninfectados= 1) # línea 333
    # miPueblo.ciclo() # línea 235

    # 6. Repite dicho método 200 veces y obtén un intervalo de confianza al 93%  para cada uno de los valores devueltos por el método ciclo.       
    for columna in ["sano", "infectado", "inmune", "fallecido"]:
        muestra = getColumnaCSV(filePath=fileCSV, columna= columna)
        intervalo = getIntervaloConfianza(muestra= muestra, confianza= confianza)
        print(f"Intervalo de Confianza {confianza*100}% | {columna}: {intervalo}")


############################################## entrega 2
def segundaEntrega():

    muestraOriginal = getColumnaCSV(filePath="PrimeraEntrega.csv", columna= "fallecido")

    muestraSinDividir = getColumnaCSV(filePath="SinDividir.csv", columna= "fallecido")
    mismaMedia1, mismaVarianza1 = getContrasteMedia(muestra1= muestraOriginal,muestra2= muestraSinDividir)

    muestraDividida = getColumnaCSV(filePath="Dividida.csv", columna= "fallecido")
    mismaMedia2, mismaVarianza2 = getContrasteMedia(muestra1= muestraSinDividir,muestra2= muestraDividida)

    print(f"""
Muestra 1 -> Original - SinDividir
Misma media: {mismaMedia1} | Misma varianza: {mismaVarianza1}

Muestra 2 -> Dividida - SinDividir
Misma media: {mismaMedia2} | Misma varianza: {mismaVarianza2}

""")

    
segundaEntrega()