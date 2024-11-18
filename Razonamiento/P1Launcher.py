'''
 ' Código principal de la aplicación para la práctica 1 de RyRDC
 ' No puede ser modificado por los alumnos
 ' 
 ' Creado por Diego Viejo
 ' el 16/09/2024
 ' V 0.5
'''

import math
import pygame
import time
import numpy as np
from robot import *
from segmento import *
from expertSystem import *
from fuzzyExpert import *
import sys

AppTitle = "RRDC P1 2024"



RADIUS = 8 # Radio de dibujo para los puntos objetivo

#Cambiar a True para usar el sistema experto difuso
useFuzzySystem = False

testeando:bool = False # True -> no ejecutará el dibujo del recorrido

# pygame setup
pygame.init()
sizeY = 720 #Necesario para adaptar las coordenadas del entorno a las de la pantalla de pygame
screen = pygame.display.set_mode((1024, sizeY))
clock = pygame.time.Clock()
running = True
programQuit = False

robotIimage = pygame.image.load('robot1.png').convert_alpha()


################################################################################################
def mostrar_texto(texto, pos_x, pos_y, tamaño=20, color=(255, 255, 255)):
    
    fuente = pygame.font.Font(None, tamaño)
    txt_surface = fuente.render(texto, True, color)  
    screen.blit(txt_surface, (pos_x, pos_y)) 
################################################################################################

def drawRobot(pose):
    #from Aleksandar haber
    # over here we rotate an image and create a copy of the rotated image 
    image1 = pygame.transform.rotate(robotIimage, pose[2])
    # then we return a rectangle corresponding to the rotated copy
    # the rectangle center is specified as an argument
    image1_rect = image1.get_rect(center=(10.0*pose[0], sizeY - 10.0*pose[1]))
    # then we plot the rotated image copy with boundaries specified by 
    # the rectangle
    screen.blit(image1, image1_rect)



def drawObjective(objetivo, activo=True):
    pInicio = (objetivo.getInicio()[0]*10.0, sizeY-objetivo.getInicio()[1]*10.0)
    pFin = (objetivo.getFin()[0]*10.0, sizeY-objetivo.getFin()[1]*10.0)
    if activo is True:
        colorInicio = "green"
        colorFin = "red"
        colorLinea = "darkgray"
        radio = RADIUS
    else:
        colorInicio = "lightgray"
        colorFin = "darkgray"
        colorLinea = "gray"
        radio = RADIUS * 0.8
    if objetivo.getType() == 1:
        pygame.draw.line(screen, colorLinea, pInicio, pFin, 5)
    else:
        pMedio = (objetivo.getMedio()[0]*10.0, sizeY-objetivo.getMedio()[1]*10.0)
        pygame.draw.polygon(screen, colorLinea, [pInicio, pFin, pMedio])
        pygame.draw.circle(screen, colorFin, pMedio, RADIUS)
    pygame.draw.circle(screen, colorInicio, pInicio, radio)
    pygame.draw.circle(screen, colorFin, pFin, radio)

def straightToPointDistance(p1, p2, p3):
    m1 = p2[1]-p1[1]
    m2 = p2[0]-p1[0]
    return m1*p3[0] - m2*p3[1] - p1[0]*m1 + p1[1]*m2

def straightToPointDistanceNorm(p1, p2, p3):
    m1 = p2[1]-p1[1]
    m2 = p2[0]-p1[0]
    norm = math.sqrt(m1*m1+m2*m2)
    return (m1*p3[0] - m2*p3[1] - p1[0]*m1 + p1[1]*m2)/norm

def inTriangle(triangulo, punto):
    inicio = np.array(triangulo.getInicio())
    medio = np.array(triangulo.getMedio())
    fin = np.array(triangulo.getFin())

    d1 =straightToPointDistance(inicio, medio, np.array(punto))
    d2 =straightToPointDistance(medio, fin, np.array(punto))
    d3 =straightToPointDistance(fin, inicio, np.array(punto))

    tieneNegativo =  d1<0 or d2<0 or d3<0
    tienePositivo = d1>0 or d2>0 or d3>0

    return not(tieneNegativo and tienePositivo)

    

def getSegmentScore(segmento, posiciones, tiempo=1):
    inicio = np.array(segmento.getInicio())
    fin = np.array(segmento.getFin())
    score = 0
    for pos in posiciones:
        dist = np.abs(straightToPointDistanceNorm(inicio, fin, np.array(pos[0:2])))
        if dist<3:
            if dist < 0.01:
                score += 100
            else:
                score += 1 / dist
    return (score/((1+tiempo)*(1+tiempo)*(1+tiempo)), score, tiempo)

def getTriangleScore(triangulo, posiciones, tiempo=1):
    inicio = np.array(triangulo.getInicio())
    medio = np.array(triangulo.getMedio())
    fin = np.array(triangulo.getFin())
    score = 500
    penalizacion = 0
    factor = -1
    altura = np.abs(straightToPointDistanceNorm(inicio, fin, medio))
    for pos in posiciones:
        if inTriangle(triangulo, pos[0:2]):
            penalizacion += 1
            #print("Triangulo")

        m1 = medio[0]-pos[0]
        m2 = medio[1]-pos[1]
        norm = math.sqrt(m1*m1+m2*m2)
        if factor<1 and norm<altura:
            factor = 1
    score = (score-penalizacion)*factor
    return (score/((1+tiempo)*(1+tiempo)), score, tiempo)

miRobot = Robot()

objectiveSet = []
segmento = Objetivo()
segmento.setInicio((12, 34))
segmento.setFin((85,62))
objectiveSet.append(segmento)
triangulo = Objetivo()
triangulo.setInicio((85, 62)) #(95, 62))
triangulo.setFin((98, 55))
triangulo.setMedio((96, 64))
objectiveSet.append(triangulo)
segmento = Objetivo()
segmento.setInicio((98, 55))
segmento.setFin((70,15))
objectiveSet.append(segmento)
triangulo = Objetivo()
triangulo.setInicio((70, 15)) #(95, 62))
triangulo.setFin((55, 7))
triangulo.setMedio((62, 7))
objectiveSet.append(triangulo)
segmento = Objetivo()
segmento.setInicio((55, 7))
segmento.setFin((15, 20))
objectiveSet.append(segmento)
triangulo = Objetivo()
triangulo.setInicio((15, 20)) #(95, 62))
triangulo.setFin((12, 34))
triangulo.setMedio((8, 26))
objectiveSet.append(triangulo)


numPath = 0

#####################################################################################
KR_lineal = float(sys.argv[1])
KR_angular = float(sys.argv[2])
KR_deteccion = float(sys.argv[3])

KT_lineal = float(sys.argv[4])
KT_angular = float(sys.argv[5])
KT_deteccion = float(sys.argv[6])


if useFuzzySystem:
    experto = FuzzySystem()
else:
    experto = ExpertSystem(KR_lineal, KR_angular, KR_deteccion,
                            KT_lineal, KT_angular, KT_deteccion)
    
experto.setObjetivo(objectiveSet[numPath])
optativo = experto.hayParteOptativa()
######################################################################################


miRobot.setPose((1,10,-10))

elapsedTime = 0
tinicio = time.time()
trayectoria = []
trayectoriaTotal = []
poseActual = ()
segmentScore = ()
totalScore = 0

timePerFrame = []

########################################################################################
puntuacionSegmento = (0,0,0)

dict_datos = {
    "puntuacion": f"{totalScore:.7f}",  
    
    "KR_Vl": f"{KR_lineal:.3f}",       
    "KR_Wa": f"{KR_angular:.3f}",
    "Dtc-": f"{KR_deteccion:.2f}",          
    "segm1": f"{0:.3f}",
    "segm3": f"{0:.3f}",
    "segm5": f"{0:.3f}",

    "KT_Vl": f"{KT_lineal:.3f}",
    "KT_Wa": f"{KT_angular:.3f}",
    "DtcΔ": f"{KT_deteccion:.2f}",
    "segm2": f"{0:.3f}",
    "segm4": f"{0:.3f}",
    "segm6": f"{0:.3f}"
}
########################################################################################


while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            programQuit = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray10")


    # RENDER YOUR GAME HERE
    for trajCont in range(len(objectiveSet)):
        path = objectiveSet[trajCont]
        drawObjective(path, trajCont==numPath)
    poseActual = miRobot.getPose()
    drawRobot(poseActual)
    trayectoria.append(poseActual)
    trayectoriaTotal.append(poseActual)

################################################################################################
    mostrar_texto(f"Segmento Actual: {numPath+1}", 10, 10)
    mostrar_texto(f"Puntuación Segmento {puntuacionSegmento[0]:.4f}", 10, 30, color=(0, 255, 0))
    mostrar_texto(f"Puntuación Total {totalScore}", 10, 50, color=(255, 0, 0))


    mostrar_texto(f"Posicion: ({poseActual[0]:.4f}, {poseActual[1]:4f})", 10, 90)
    mostrar_texto(f"Angulo: {poseActual[2]%360:.2f}", 10, 110)
    mostrar_texto(f"VLineal: {poseActual[3]:.2f}", 10, 130)
    mostrar_texto(f"WAngular: {poseActual[4]:.2f}", 10, 150)
    mostrar_texto(f"Tiempo Transcurrido: {(time.time() - tinicio):.2f}", 10, 170, color=(0,0,255))


    mostrar_texto(f"KR_V: {dict_datos["KR_Vl"]}", 920, 420, color=(255, 255, 0))
    mostrar_texto(f"KR_W: {dict_datos["KR_Wa"]}", 920, 440, color=(255, 255, 0))
    mostrar_texto(f"Detc-: {dict_datos["Dtc-"]}", 920, 460, color=(255, 255, 0))
    mostrar_texto(f"KT_V: {dict_datos["KT_Vl"]}", 920, 500, color=(255, 0, 255))
    mostrar_texto(f"KT_W: {dict_datos["KT_Wa"]}", 920, 520, color=(255, 0, 255))
    mostrar_texto(f"DtcΔ: {dict_datos["DtcΔ"]}", 920, 540, color=(255, 0, 255))


    mostrar_texto(f"Puntuación Segm1: {dict_datos["segm1"]}", 840, 580, color=(255, 255, 0))
    mostrar_texto(f"Puntuación Segm3: {dict_datos["segm3"]}", 840, 600, color=(255, 255, 0))
    mostrar_texto(f"Puntuación Segm5: {dict_datos["segm5"]}", 840, 620, color=(255, 255, 0))
    mostrar_texto(f"Puntuación Segm2: {dict_datos["segm2"]}", 840, 660, color=(255, 0, 255))
    mostrar_texto(f"Puntuación Segm4: {dict_datos["segm4"]}", 840, 680, color=(255, 0, 255))
    mostrar_texto(f"Puntuación Segm6: {dict_datos["segm6"]}", 840, 700, color=(255, 0, 255))
    
################################################################################################

    timeLapse = clock.tick(60)  
    miRobot.updateDynamics(timeLapse)
    timePerFrame.append(timeLapse)
    if experto.esObjetivoAlcanzado():
        elapsedTime = time.time() - tinicio
        if numPath>=len(objectiveSet):
            miRobot.setVel((0,0))
            running = False
        else:
            # Recta
            if objectiveSet[numPath].getType()==1:
                segmentScore = getSegmentScore(objectiveSet[numPath], trayectoria, elapsedTime)
            # Triángulo
            else:
                segmentScore = getTriangleScore(objectiveSet[numPath], trayectoria, elapsedTime)
            
########################################################################################
            if dict_datos["segm1"] != "None":
                puntSegm = f"{segmentScore[0]:.3f}"
                dict_datos["segm"+str(numPath+1)] = puntSegm
########################################################################################
         
            trayectoria.clear()
            totalScore += segmentScore[0]
            print(f'Puntuación del objetivo: {segmentScore[0]}. Puntuación de distancia: {segmentScore[1]} en {segmentScore[2]} segundos')
            tinicio = time.time()
            numPath += 1
            if numPath<len(objectiveSet) and objectiveSet[numPath].getType()==2 and not optativo:
                numPath += 1
            if numPath<len(objectiveSet):
                experto.setObjetivo(objectiveSet[numPath])

    else:
        velocidades = experto.tomarDecision(miRobot.getPose())
        miRobot.setVel(velocidades)
    
########################################################################################
        
        if objectiveSet[numPath].getType()==1:
            puntuacionSegmento = getSegmentScore(objectiveSet[numPath], trayectoria, time.time()-tinicio)
        else:
            puntuacionSegmento = getTriangleScore(objectiveSet[numPath], trayectoria, time.time()-tinicio)


        if time.time() - tinicio > 100: # 2 minutos
            for i in range(6):
                dict_datos["segm"+str(i+1)] = "None"
            
            numPath=len(objectiveSet)
            experto.setobjetivoAlcanzado()
            
########################################################################################

    # flip() the display to put your work on screen
    pygame.display.flip()

dict_datos["puntuacion"] = totalScore
print(f'Puntuación total: {totalScore}')


if testeando:
    sys.exit()


trajCont = 1
while not programQuit:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
########################################################################################
            # Creación/Edición del DataFrame
            experto.añadirFila(nueva_fila=dict_datos, nombre="datos.csv")
            # Creación Captura de Pantalla
            pygame.image.save(screen, "Recorridos/ID"+ str(experto.getmaxID(nombre="datos.csv")) + ".png")    
########################################################################################

            programQuit = True


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey15")

################################################################################################
    mostrar_texto(f"Segmento Actual: {numPath+1}", 10, 10)
    mostrar_texto(f"Puntuación Segmento {puntuacionSegmento[0]:.4f}", 10, 30, color=(0, 255, 0))
    mostrar_texto(f"Puntuación Total {totalScore}", 10, 50, color=(255, 0, 0))


    mostrar_texto(f"Posicion: ({poseActual[0]:.4f}, {poseActual[1]:4f})", 10, 90)
    mostrar_texto(f"Angulo: {poseActual[2]%360:.2f}", 10, 110)
    mostrar_texto(f"VLineal: {poseActual[3]:.2f}", 10, 130)
    mostrar_texto(f"WAngular: {poseActual[4]:.2f}", 10, 150)
    mostrar_texto(f"Tiempo Transcurrido: {elapsedTime:.2f}", 10, 170, color=(0,0,255))

    mostrar_texto(f"KR_V: {dict_datos["KR_Vl"]}", 920, 420, color=(255, 255, 0))
    mostrar_texto(f"KR_W: {dict_datos["KR_Wa"]}", 920, 440, color=(255, 255, 0))
    mostrar_texto(f"Detc-: {dict_datos["Dtc-"]}", 920, 460, color=(255, 255, 0))
    mostrar_texto(f"KT_V: {dict_datos["KT_Vl"]}", 920, 500, color=(255, 0, 255))
    mostrar_texto(f"KT_W: {dict_datos["KT_Wa"]}", 920, 520, color=(255, 0, 255))
    mostrar_texto(f"DtcΔ: {dict_datos["DtcΔ"]}", 920, 540, color=(255, 0, 255))

    mostrar_texto(f"Puntuación Segm1: {dict_datos["segm1"]}", 840, 580, color=(255, 255, 0))
    mostrar_texto(f"Puntuación Segm3: {dict_datos["segm3"]}", 840, 600, color=(255, 255, 0))
    mostrar_texto(f"Puntuación Segm5: {dict_datos["segm5"]}", 840, 620, color=(255, 255, 0))
    mostrar_texto(f"Puntuación Segm2: {dict_datos["segm2"]}", 840, 660, color=(255, 0, 255))
    mostrar_texto(f"Puntuación Segm4: {dict_datos["segm4"]}", 840, 680, color=(255, 0, 255))
    mostrar_texto(f"Puntuación Segm6: {dict_datos["segm6"]}", 840, 700, color=(255, 0, 255))
    
################################################################################################

    
    for cont in range(len(objectiveSet)):
        path = objectiveSet[cont]
        drawObjective(path, False)
    poseActual = miRobot.getPose()
    drawRobot(poseActual)

    if trajCont < len(trayectoriaTotal):
        for cont in range(1, trajCont):
            p1 = (trayectoriaTotal[cont-1][0]*10, sizeY-trayectoriaTotal[cont-1][1]*10)
            p2 = (trayectoriaTotal[cont][0]*10, sizeY-trayectoriaTotal[cont][1]*10)
            pygame.draw.line(screen, "red", p1, p2, 2)
        trajCont += 2
    else:
        for cont in range(1, len(trayectoriaTotal)):
            p1 = (trayectoriaTotal[cont-1][0]*10, sizeY-trayectoriaTotal[cont-1][1]*10)
            p2 = (trayectoriaTotal[cont][0]*10, sizeY-trayectoriaTotal[cont][1]*10)
            pygame.draw.line(screen, "red", p1, p2, 2)

        ########################################################################################   
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        ########################################################################################

    pygame.display.flip()
    timeLapse = clock.tick(60)  
    miRobot.updateDynamics(timeLapse)

# this is important, run this if the pygame window does not want to close
pygame.quit()
