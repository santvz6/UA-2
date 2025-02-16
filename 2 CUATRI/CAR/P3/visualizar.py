import matplotlib.pyplot as plt

# Lectura de tiempos simulados
with open("cputime.txt", "r") as file:
    contenido = file.readlines()
cputime = list(map(float, contenido[0].strip().split(", ")))
cpusize = list(map(int, contenido[1].strip().split(", ")))

with open("gputime.txt", "r") as file:
    contenido = file.readlines()
gputime = list(map(float, contenido[0].strip().split(", ")))
gpusize = list(map(int, contenido[1].strip().split(", ")))

#####################
# Ordenamos las tuplas de (size, time)
cpu_data = sorted(zip(cpusize, cputime)) 
gpu_data = sorted(zip(gpusize, gputime))  

#####################
# Extraemos los valores ordenados
cpusize = [x[0] for x in cpu_data]
cputime = [x[1] for x in cpu_data]

gpusize = [x[0] for x in gpu_data]
gputime = [x[1] for x in gpu_data]

if __name__ == "__main__":
    #####################
    # Plot de los tiempos de CPU y GPU
    plt.plot(cpusize, cputime, label='CPU', marker='o')
    plt.plot(gpusize, gputime, label='GPU', marker='x')
    plt.legend()
    plt.xlabel('Tamaño de imagen')
    plt.ylabel('Tiempo (s)')
    plt.title('Comparación de tiempos CPU vs GPU')
    plt.savefig("rendimiento.png", bbox_inches='tight', dpi=300)
    plt.show()
    