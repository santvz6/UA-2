'''
 ' Código principal de la aplicación para la práctica 1 de RyRDC
 ' No puede ser modificado por los alumnos
 ' 
 ' Creado por Diego Viejo
 ' el 16/09/2024
 ' V 0.4
'''


import pygame
import time
import numpy as np
from robot import *
from segmento import *
from expertSystem import *
AppTitle = "RRDC P1 2024"

import csv
import pandas as pd


RADIUS = 8 # Radio de dibujo para los puntos objetivo


# pygame setup
pygame.init()
sizeY = 720 #Necesario para adaptar las coordenadas del entorno a las de la pantalla de pygame
screen = pygame.display.set_mode((1024, sizeY))
clock = pygame.time.Clock()
running = True
programQuit = False

robotIimage = pygame.image.load('robot1.png').convert_alpha();

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
    score = 500
    for pos in posiciones:
        if inTriangle(triangulo, pos[0:2]):
            score -= 1
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

######################################################################################
k_lineal = 0.75
k_angular = 0.05
retraso = 1.5

experto = ExpertSystem(k_lineal, k_angular, retraso)
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

dict_datos = {
    "k_lineal": [k_lineal],
    "k_angular": [k_angular],
    "retraso": [retraso],
    "puntuacion": [0],
    "s1": [0],
    "s2": [0],
    "s3": [0],
    "s4": [0],
    "s5": [0],
    "s6": [0],
}

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            programQuit = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for trajCont in range(len(objectiveSet)):
        path = objectiveSet[trajCont]
        drawObjective(path, trajCont==numPath)
    poseActual = miRobot.getPose()
    drawRobot(poseActual)
    trayectoria.append(poseActual)
    trayectoriaTotal.append(poseActual)

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

            match(numPath):
                case 0:
                    dict_datos["s1"] = [segmentScore[0]]
                case 1:
                    dict_datos["s2"] = [segmentScore[0]]
                case 2:
                    dict_datos["s3"] = [segmentScore[0]]
                case 3:
                    dict_datos["s4"] = [segmentScore[0]]
                case 4:
                    dict_datos["s5"] = [segmentScore[0]]
                case 5:
                    dict_datos["s6"] = [segmentScore[0]]
                    

            trayectoria.clear()
            totalScore += segmentScore[0]
            print(f'Puntuación del segmento: {segmentScore[0]}. Puntuación de distancia: {segmentScore[1]} en {segmentScore[2]} segundos')
            tinicio = time.time()
            numPath += 1
            if numPath<len(objectiveSet) and objectiveSet[numPath].getType()==2 and not optativo:
                numPath += 1
            if numPath<len(objectiveSet):
                experto.setObjetivo(objectiveSet[numPath])

    else:
        velocidades = experto.tomarDecision(miRobot.getPose())
        miRobot.setVel(velocidades)
    # flip() the display to put your work on screen
    pygame.display.flip()


print(f'Puntuación total: {totalScore}')
dict_datos["puntuacion"] = totalScore

trajCont = 1
while not programQuit:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(screen, "Recorrido.png")
            time.sleep(1)

            # Creación DataFrame
            try:
                df = pd.read_csv("datos.csv")
            except FileNotFoundError as e:
                df = pd.DataFrame(dict_datos)
                df.to_csv("datos.csv", index=False)
            else:
                df_nuevo = pd.DataFrame(dict_datos)
                df = pd.concat([df, df_nuevo], ignore_index=True)
                df.to_csv("datos.csv", index=False)

            programQuit = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")
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
    pygame.display.flip()

    timeLapse = clock.tick(60)  
    miRobot.updateDynamics(timeLapse)

# this is important, run this if the pygame window does not want to close
pygame.quit()
