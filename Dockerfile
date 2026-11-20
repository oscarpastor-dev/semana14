FROM python:3.11-slim

WORKDIR /app

# Copiar e instalar dependencias primero (aprovecha cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar codigo fuente
COPY . .

# Ejecutar tests durante el build
RUN python -m unittest discover -s . -p "test_*.py" -v

# Puerto de la aplicacion
EXPOSE 5000

# Comando al iniciar el contenedor
CMD ["python", "app.py"]
