def update(frame):
    global positions, velocities,ax

    print(miPueblo1.ciclo(iteracion= miPueblo1.iteracion + 1))
    

    positions,colores = miPueblo1.positions()            
    scat.set_offsets(positions) 
    scat.set_facecolors(colores)   
    miPueblo1.evoluciona() 

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