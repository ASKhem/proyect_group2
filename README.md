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