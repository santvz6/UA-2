import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

import numpy as np
import pandas as pd
from scipy.stats import t, f
import os

from Epidemia import Poblacion

SEGUNDOS = 5
FPS = 50
NFRAMES = FPS * SEGUNDOS


xlim, ylim = 2, 2
numDivisiones = 1

p1 = Poblacion("P1", nsanos= 1000, ninfectados= 1, limitePoblacion= (xlim, ylim), numDivisiones= numDivisiones)


positions, colors = p1.positions()
fig, ax = plt.subplots()
ax.set_xlim(0, xlim)
ax.set_ylim(0, ylim)
ax.set_title('Pandemy')
ax.color='Red'

scat = ax.scatter(positions[:][0], positions[:][1])
i=0    #Nº de frame que estoy actualizando. Inicializado a cero
# Función de actualización para la animación
def update(frame):
    global positions, velocities,i,ax
    # Actualizar posiciones    
    i+=1
    #positions += v
    # Verificar colisiones con los bordes y cambiar dirección
    positions,colors=p1.positions()            
    print(p1)    #util para depurar
    scat.set_offsets(positions) 
    scat.set_facecolors(colors)   
    p1.evoluciona()  #Mueve las personas y actualiza contagios.

# Crear animación
ani = FuncAnimation(fig, update, frames=NFRAMES)
ani.save('animation.mp4', writer='ffmpeg', fps=FPS);