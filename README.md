# Proyecto Subgrupo 2 - Procesador de Datos de Canciones Spotify

**Actividad Día 4: Introducción a la Ciencia de Datos y Buenas Prácticas**
*Fecha de generación: 11 de abril de 2025*
*Ubicación: A Coruña, Galicia, España*

---
## 1. Descripción General

Este proyecto implementa el módulo de procesamiento de datos asignado al **Subgrupo 2**. Actúa como un servicio intermedio en una aplicación completa de análisis de datos de canciones de Spotify. Su función principal es consumir los datos brutos proporcionados por el Subgrupo 1, aplicar técnicas de Análisis Exploratorio de Datos (EDA) y limpieza, y finalmente exponer los datos procesados a través de una API REST para que el Subgrupo 3 pueda visualizarlos.

## 2. Contexto de la Aplicación

Esta aplicación se divide en tres componentes principales, simulando un flujo de trabajo real en ciencia de datos:

1.  **Subgrupo 1:** Lee un archivo CSV (`songs.csv`), lo carga en una base de datos SQLite y expone los datos crudos a través de un endpoint FastAPI (`http://127.0.0.1:8000/songs`).
2.  **Subgrupo 2 (Este proyecto):** Consume los datos del endpoint del Subgrupo 1, realiza EDA y limpieza (manejo de nulos, tipos de datos, duplicados, etc.), y expone los datos limpios a través de su propio endpoint FastAPI (`http://127.0.0.1:8001/cleaned_songs`).
3.  **Subgrupo 3:** Consume los datos limpios del endpoint del Subgrupo 2 y crea una interfaz web interactiva (usando Streamlit) para visualizar los datos y realizar análisis gráficos.

**Nota:** Debido a restricciones de red, todos los endpoints se ejecutan en `localhost` en diferentes puertos, requiriendo que toda la aplicación se ejecute en una única máquina para la integración completa.

## 3. Responsabilidades Específicas del Subgrupo 2

-   **Consumo de Datos:** Conectar al endpoint `http://127.0.0.1:8000/songs` para obtener el JSON con los datos de las canciones. Incluye manejo de errores de conexión.
-   **Análisis Exploratorio y Limpieza (EDA):**
    -   Cargar los datos en un DataFrame de Pandas.
    -   Inspeccionar la estructura, tipos de datos y valores faltantes.
    -   Aplicar pasos de limpieza como:
        -   Manejo de valores nulos (NaNs) en columnas críticas.
        -   Conversión y corrección de tipos de datos (ej. fechas, números).
        -   Identificación y eliminación de registros duplicados (basado en `Track ID`).
        -   (Opcional) Normalización de campos de texto.
        -   (Opcional) Conversión de unidades (ej. `Duration_ms` a segundos).
-   **Exposición de Datos Limpios:** Implementar un endpoint GET `/cleaned_songs` usando FastAPI en `http://127.0.0.1:8001` que devuelva un JSON con la lista de canciones procesadas.
-   **Buenas Prácticas:**
    -   Uso de `logging` para el registro de eventos (en lugar de `print`).
    -   Documentación de código mediante Docstrings (estilo Google).
    -   Adherencia al estilo de código PEP 8 (verificado con linters como Flake8).
    -   Estructuración del código siguiendo patrones básicos (ej. separación de lógica de obtención, procesamiento y exposición).

## 4. Pila Tecnológica (Tech Stack)

-   **Lenguaje:** Python 3.8+
-   **Framework API:** FastAPI
-   **Servidor ASGI:** Uvicorn
-   **Manipulación de Datos:** Pandas
-   **Peticiones HTTP:** Requests
-   **Registro:** Logging (módulo estándar de Python)

## 5. Estructura del Proyecto

```
proyecto_subgrupo2/
├── .gitignore             # Archivos y carpetas a ignorar por Git
├── README.md              # Este archivo de documentación
├── requirements.txt       # Dependencias del proyecto Python
├── data/                  # Carpeta para datos de prueba locales
│   └── short_songs.json   # Datos de ejemplo para desarrollo offline
├── main_subgrupo2.py      # Script principal con la aplicación FastAPI y la lógica EDA
└── venv/                  # Entorno virtual de Python (ignorado por Git)
```

## 6. Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

-   **Python:** Versión 3.8 o superior. Puedes verificarlo con `python --version`.
-   **pip:** El gestor de paquetes de Python (normalmente viene incluido con Python). Puedes verificarlo con `pip --version`.
-   **(Opcional) Git:** Para clonar el repositorio si está alojado en uno.

## 7. Instalación y Configuración

Sigue estos pasos para configurar el entorno de desarrollo local:

1.  **Clona el repositorio (si es necesario):**
    ```bash
    git clone <url-del-repositorio-si-existe>
    cd proyecto_subgrupo2
    ```
    Si no tienes un repositorio, simplemente crea la carpeta `proyecto_subgrupo2` y coloca los archivos dentro.

2.  **Crea un entorno virtual:** Es una buena práctica aislar las dependencias del proyecto.
    ```bash
    python -m venv venv
    ```

3.  **Activa el entorno virtual:**
    -   **Windows (cmd/powershell):**
        ```bash
        .\venv\Scripts\activate
        ```
    -   **macOS / Linux (bash/zsh):**
        ```bash
        source venv/bin/activate
        ```
    Deberías ver `(venv)` al principio de la línea de comandos, indicando que el entorno está activo.

4.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **(Opcional) Preparar Datos de Prueba Locales:**
    -   Asegúrate de que el archivo `short_songs.json` (o el archivo de datos completo `songs.json`) se encuentra en la carpeta `data/`. Este archivo debe contener el JSON esperado del Subgrupo 1.
    -   Para usar este archivo en lugar de intentar conectar con el endpoint del Subgrupo 1 (útil si el Subgrupo 1 no está listo o para pruebas aisladas), modifica la variable `SOURCE_DATA_URL` en el archivo `main_subgrupo2.py`:
        ```python
        # Comenta la URL real y descomenta la ruta al archivo local:
        # SOURCE_DATA_URL = "[http://127.0.0.1:8000/songs](http://127.0.0.1:8000/songs)"
        SOURCE_DATA_URL = "data/short_songs.json"
        ```
    -   **¡Importante!** Recuerda revertir este cambio cuando quieras conectar con el endpoint real del Subgrupo 1.

## 8. Ejecución de la Aplicación

Una vez instalado y configurado, puedes iniciar el servidor FastAPI. Asegúrate de que tu entorno virtual (`venv`) esté activado.

```bash
uvicorn main_subgrupo2:app --host 127.0.0.1 --port 8001 --reload
```

Explicación del comando:

uvicorn: Lanza el servidor ASGI.
main_subgrupo2:app: Le dice a Uvicorn que busque el objeto app (la instancia de FastAPI) dentro del archivo main_subgrupo2.py.
--host 127.0.0.1: Hace que el servidor solo sea accesible desde tu propia máquina (localhost).
--port 8001: Especifica el puerto en el que escuchará el servidor para este subgrupo.
--reload: Activa el modo de recarga automática. Uvicorn monitorizará los cambios en los archivos .py y reiniciará el servidor automáticamente, lo cual es muy útil durante el desarrollo.
El servidor estará funcionando y accesible en http://127.0.0.1:8001.

9. Uso y Endpoints de la API
La API expuesta por este servicio tiene los siguientes endpoints principales:

Endpoint de Datos Limpios:

URL: http://127.0.0.1:8001/cleaned_songs
Método: GET
Descripción: Devuelve una respuesta JSON que contiene la lista completa de canciones después de haber sido procesadas (limpieza de nulos, corrección de tipos, eliminación de duplicados, etc.). Este es el endpoint que el Subgrupo 3 consumirá.
Respuesta Exitosa (Código 200):

```json	
[
  {
    "Track Name": "Song Title 1",
    "Track Artist": "Artist Name",
    "Track Album Release Date": "YYYY-MM-DDTHH:MM:SS", // Formato ISO después de procesar
    "Energy": 0.85,
    "Tempo": 120.0,
    // ... resto de campos procesados ...
  },
  {
    "Track Name": "Song Title 2",
    // ...
  }
]
```

### Respuesta de Error
En caso de problemas (ej. no se puede conectar al Subgrupo 1, error interno de procesamiento), devolverá un código de estado HTTP de error (ej. 500, 503) con un detalle en JSON.

### Endpoints de Documentación Automática
FastAPI genera documentación interactiva automáticamente.

- **Swagger UI:** http://127.0.0.1:8001/docs
  Permite ver los endpoints disponibles, sus parámetros, descripciones y probarlos directamente desde el navegador.
- **ReDoc:** http://127.0.0.1:8001/redoc
  Ofrece una vista alternativa de la documentación de la API.

## 10. Resumen de Pasos de EDA y Limpieza Implementados
El script `main_subgrupo2.py` realiza las siguientes operaciones principales sobre los datos recibidos:

1. **Carga y Estructura:** Carga los datos JSON en un DataFrame de Pandas.
2. **Manejo de Nulos:** Identifica y elimina filas con valores nulos en columnas consideradas críticas (ej. Track ID, Track Album Release Date después de la conversión). Se registra la cantidad de filas eliminadas.
3. **Conversión de Tipos:** Convierte la columna Track Album Release Date a objetos datetime de Pandas. Maneja errores durante la conversión (valores no válidos resultan en NaT y se eliminan). Asegura que columnas numéricas (Energy, Tempo, Track Popularity, etc.) tengan tipos numéricos (float o int), intentando la conversión si llegan como texto.
4. **Eliminación de Duplicados:** Elimina filas duplicadas basándose en el identificador único Track ID, conservando la primera aparición de cada canción. Se registra la cantidad de duplicados eliminados.
5. **Logging:** Todas las operaciones importantes, advertencias y errores se registran usando el módulo logging para facilitar la depuración y el seguimiento.

(Nota: Se podrían añadir pasos adicionales como normalización de texto, imputación de valores faltantes en otras columnas, o creación de nuevas características si el análisis lo requiriera).

## 11. Pruebas (Testing)
Actualmente, este proyecto no incluye un conjunto formal de pruebas automatizadas (ej. usando pytest). Para un desarrollo más robusto, se recomienda añadir tests unitarios y/o de integración, especialmente para las funciones de limpieza de datos (`perform_eda_and_cleaning`) y para verificar la respuesta del endpoint usando librerías como `httpx`.

## 12. Contribuyentes
Subgrupo 2: [Aquí irían los nombres de los miembros del Subgrupo 2]
