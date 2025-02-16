import time, torch

def getTimeCPU(input_tensor, model) -> float:
    # Medir el tiempo en CPU
    start_cpu = time.time()
    with torch.no_grad():
        output_cpu = model(input_tensor)
    end_cpu = time.time()

    return end_cpu - start_cpu

def getTimeGPU(input_tensor, model, primeraEjecucion) -> float:
    # Verificar si CUDA está disponible
    if torch.cuda.is_available():
        # Mover el modelo a la GPU
        model = model.cuda()
        # Crear un tensor de ejemplo en la GPU (imagen de 224x224)
        input_tensor = input_tensor.cuda() # Imagen simulada en la GPU

        #######################################
        # La primera ejecución tiene que ejecutar cuda (tarda más)
        if primeraEjecucion:
            with torch.no_grad():
                output_gpu = model(input_tensor)
            # Sincronizar la GPU para garantizar que termine la ejecución
            torch.cuda.synchronize()
        #######################################  

        start_gpu = time.time()
        with torch.no_grad():
            output_gpu = model(input_tensor)
        torch.cuda.synchronize()
        end_gpu = time.time()

        return end_gpu - start_gpu

    else:
        return None