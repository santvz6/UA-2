# Librerías
from PIL import Image
from torchvision import transforms, models
import numpy as np

# Módulos
from rendimiento import getTimeCPU, getTimeGPU

# Funciones
def cargarImagen(filePath, size: tuple):
    image = Image.open(filePath)
    # Redimensionar y convertimos la imagen a tensor
    transform = transforms.Compose([
        transforms.Resize(size),
        transforms.ToTensor()])
    input_tensor = transform(image).unsqueeze(0)

    return input_tensor

def main(ejecutar:str, sizes:list[int], NUM_IMG= 5) -> None:

    cputimes = gputimes = list()

    #####################
    # Carga del modelo
    model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
    model.eval() # Modo de evaluación

    #####################
    # Hay que separar las operaciones de CPU y GPU
    for i in range(NUM_IMG):
        input_tensor = cargarImagen(f"gfx/Foto facial {i+1}.jpg", (sizes[i], sizes[i]))

        if ejecutar == "CPU":
            cputimes.append(str(getTimeCPU(input_tensor, model)))
        
            #####################
            # Escritura de tiempos en ficheros de texto
            with open("cputime.txt", "w") as file:
                file.write(", ".join(cputimes))
                file.write("\n")
                file.write(", ".join(map(str, sizes)))
    
        elif ejecutar == "GPU":
            gputimes.append(str(getTimeGPU(input_tensor, model, primeraEjecucion=not(bool(i)))))

            #####################
            # Escritura de tiempos en ficheros de texto
            with open("gputime.txt", "w") as file:
                file.write(", ".join(gputimes))
                file.write("\n")
                file.write(", ".join(map(str, sizes)))

if __name__ == "__main__":
    NUM_IMG = 5
    #####################
    # Aplicamos un vector de tamaño para comparar distintos resultados
    sizes = np.linspace(start=256, stop=4096, num=NUM_IMG, dtype=int)
    print(f"TAMAÑOS GENERADOS: {sizes}")
    #####################
    # Para ejecutar cpu: "CPU"
    # Para ejecutar gpu: "GPU"
    main(ejecutar= "CPU", sizes= sizes, NUM_IMG= NUM_IMG)
    