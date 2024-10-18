# API de Tareas con FastAPI

Esta es una API de tareas simple desarrollada con FastAPI. La API permite crear, actualizar, eliminar y obtener tareas. También se proporcionan instrucciones para ejecutar las pruebas unitarias con cobertura del 100%.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- **Python 3.7+**: Asegúrate de tener Python instalado. Puedes verificarlo ejecutando:
  
  python --version

## Instalación de dependencias

1. Clona el repositorio o descarga los archivos.

2. Crea un entorno virtual (opcional, pero recomendado):

   python -m venv venv

3. Activa el entorno virtual:

   - En Windows:
     venv\Scripts\activate

   - En macOS/Linux:
     source venv/bin/activate

4. Instala las dependencias necesarias ejecutando el siguiente comando:

   pip install -r requirements.txt

## Ejecución de la aplicación

Sigue estos pasos para ejecutar la aplicación FastAPI en tu máquina local:

1. Asegúrate de estar en el entorno virtual (si lo estás usando) y en el directorio del proyecto.

2. Inicia el servidor FastAPI usando `uvicorn`:

   uvicorn main:app --reload

3. La API estará disponible en http://127.0.0.1:8000. Para ver la documentación interactiva de Swagger, navega a:

   http://127.0.0.1:8000/docs

   También puedes ver la documentación en formato OpenAPI en:

   http://127.0.0.1:8000/redoc

## Ejecución de pruebas unitarias

Sigue estos pasos para ejecutar las pruebas unitarias y verificar la cobertura de código:

1. Asegúrate de estar en el entorno virtual y en el directorio del proyecto.

2. Ejecuta el siguiente comando para ejecutar todas las pruebas unitarias:

   pytest

3. Para ejecutar las pruebas unitarias con un reporte de cobertura de código, ejecuta:

   pytest --cov=main --cov-report=term-missing

   Esto mostrará un reporte de cobertura en la terminal, incluyendo las líneas de código que no han sido cubiertas por las pruebas.

4. Si deseas generar un reporte de cobertura en formato HTML, ejecuta el siguiente comando:

   pytest --cov=main --cov-report=html

5. Después de ejecutar el comando anterior, abre el archivo `index.html` dentro de la carpeta `htmlcov` en tu navegador para ver el reporte de cobertura en formato visual.
