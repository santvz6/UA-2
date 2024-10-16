'''
 ' Código principal de la aplicación para la práctica 1 de RyRDC
 ' No puede ser modificado por los alumnos
 ' 
 ' Creado por Diego Viejo
 ' el 16/09/2024
 ' V 0.3
'''


import pygame
import time
import numpy as np
from robot import *
from segmento import *
from expertSystem import *
AppTitle = "RRDC P1 2024"

RADIUS = 8 # Radio de dibujo para los puntos objetivo


# pygame setup
pygame.init()
sizeY = 720 #Necesario para adaptar las coordenadas del entorno a las de la pantalla de pygame
screen = pygame.display.set_mode((1280, sizeY))
clock = pygame.time.Clock()
running = True

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



def drawSegment(Inic, Fin, activo=True):
    pInicio = (Inic[0]*10.0, sizeY-Inic[1]*10.0)
    pFin = (Fin[0]*10.0, sizeY-Fin[1]*10.0)
    if activo is True:
        colorInicio = "green"
        colorFin = "red"
        colorLinea = "darkgray"
    else:
        colorInicio = "lightgray"
        colorFin = "darkgray"
        colorLinea = "gray"
    pygame.draw.line(screen, colorLinea, pInicio, pFin, 5)
    pygame.draw.circle(screen, colorInicio, pInicio, RADIUS)
    pygame.draw.circle(screen, colorFin, pFin, RADIUS)

def straightToPointDistance(p1, p2, p3):
    return np.linalg.norm(np.cross(p2-p1, p1-p3))/np.linalg.norm(p2-p1)

def getSegmentScore(segmento, posiciones, tiempo=1):
    inicio = np.array(segmento.getInicio())
    fin = np.array(segmento.getFin())
    score = 0
    for pos in posiciones:
        dist = np.abs(straightToPointDistance(inicio, fin, np.array(pos[0:2])))
        if dist<3:
            if dist < 0.01:
                score += 100
            else:
                score += 1 / dist
    return (score/(tiempo*tiempo*tiempo), score, tiempo)

miRobot = Robot()

pathSet = []
path1 = Objetivo()
path1.setInicio((22, 34))
path1.setFin((95,62))
pathSet.append(path1)
path2 = Objetivo()
path2.setInicio((108, 55))
path2.setFin((80,15))
pathSet.append(path2)
numPath = 0

experto = ExpertSystem()
experto.setObjetivo(pathSet[numPath])

miRobot.setPose((10,10,-10))

elapsedTime = 0
tinicio = time.time()
trayectoria = []
poseActual = ()
segmentScore = ()
totalScore = 0

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for cont in range(len(pathSet)):
        path = pathSet[cont]
        drawSegment(path.getInicio(), path.getFin(), cont==numPath)
    poseActual = miRobot.getPose()
    drawRobot(poseActual)
    trayectoria.append(poseActual)
    # flip() the display to put your work on screen
    pygame.display.flip()

    timeLapse = clock.tick(60)  
    miRobot.updateDynamics(timeLapse)
    if experto.esObjetivoAlcanzado():
        elapsedTime = time.time() - tinicio
        if numPath>=len(pathSet):
            miRobot.setVel((0,0))
        else:
            segmentScore = getSegmentScore(pathSet[numPath], trayectoria, elapsedTime)
            trayectoria.clear()
            totalScore += segmentScore[0]
            print(f'Puntuación del segmento: {segmentScore[0]}. Puntuación del segmento: {segmentScore[1]} en {segmentScore[2]} segundos')
            tinicio = time.time()
            numPath += 1
            if numPath<len(pathSet):
                experto.setObjetivo(pathSet[numPath])

    else:
        velocidades = experto.tomarDecision(miRobot.getPose())
        miRobot.setVel(velocidades)
        print(getSegmentScore(pathSet[numPath], trayectoria, elapsedTime+0.00000001)[1])
        


# this is important, run this if the pygame window does not want to close
pygame.quit()
print(f'Puntuación total: {totalScore}')
