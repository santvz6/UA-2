# Imagen base de Python 3.9
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos todo el código de la aplicación 
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

# Puerto en el que el servicio de inferencia estará disponible
EXPOSE 8001

# Comando para ejecutar el servicio de inferencia
CMD ["uvicorn", "inference.main:app", "--host", "0.0.0.0", "--port", "8001"]
