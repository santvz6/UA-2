# Imagen base de Python 3.9
FROM python:3.9-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copia las dependencias y las instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código fuente al contenedor
COPY . .

# Puerto en el que se ejecuta la aplicación
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
