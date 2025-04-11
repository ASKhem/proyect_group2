# Objetivo Principal

- **Consumir datos**: Conectaros al endpoint del Subgrupo 1 (http://127.0.0.1:8000/songs) para obtener el JSON con los datos de las canciones.
- **Analizar y Limpiar (EDA)**: Aplicar técnicas de EDA sobre estos datos. Esto implica entenderlos, limpiarlos (manejar nulos, corregir tipos, etc.) y posiblemente transformarlos para que sean más útiles.
- **Exponer datos limpios**: Crear vuestro propio endpoint (http://127.0.0.1:8001/cleaned_songs) usando FastAPI para servir un JSON que contenga el dataset ya procesado y limpio.

## Pasos Detallados

### Configuración del Entorno

1. Aseguraos de tener Python instalado.
2. Cread un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Instalad las librerías necesarias:
   ```bash
   pip install fastapi uvicorn requests pandas python-dotenv logging
   # Opcional pero recomendado para desarrollo:
   pip install flake8 pylance
   ```

### Obtención de Datos (Conexión al Subgrupo 1)

- Utilizad la librería `requests` para hacer una petición GET al endpoint del Subgrupo 1 (http://127.0.0.1:8000/songs).
- Manejad posibles errores (ej. si el endpoint del Subgrupo 1 no está disponible, errores de red).
- Para pruebas iniciales: Podéis usar los ficheros `songs.json` o `short_songs.json`. Leed este fichero y cargad su contenido en una estructura de datos Python (una lista de diccionarios).

### Análisis Exploratorio de Datos (EDA) y Limpieza

1. **Carga en Pandas**: Convertid la lista de diccionarios (obtenida del JSON) en un DataFrame de Pandas.

   ```python
   import pandas as pd
   df = pd.DataFrame(data_json)
   ```

2. **Comprensión Inicial**:
   - `df.head()`: Ver las primeras filas.
   - `df.info()`: Comprobar tipos de datos y valores no nulos por columna.
   - `df.describe()`: Estadísticas descriptivas para columnas numéricas.
   - `df.shape`: Dimensiones del DataFrame.
   - `df.columns`: Listar los nombres de las columnas.

3. **Limpieza**:
   - **Valores Nulos**: Identificadlos (`df.isnull().sum()`). Decidid cómo tratarlos.
   - **Tipos de Datos**: Corregid tipos si es necesario.
   - **Duplicados**: Buscad filas duplicadas, especialmente basándoos en Track ID.
   - **Consistencia de Texto**: Revisad columnas categóricas por posibles inconsistencias.
   - **Outliers** (Opcional Avanzado): Identificar valores extremos en columnas numéricas.

4. **Transformación/Ingeniería de Características** (Opcional):
   - Convertir `Duration_ms` a segundos o minutos.
   - Crear categorías a partir de variables numéricas.
   - Eliminar columnas irrelevantes si es necesario.

### Preparación del JSON de Salida

Una vez tengáis el DataFrame limpio y procesado (`df_cleaned`), convertidlo de nuevo a formato JSON:

```python
cleaned_data_json = df_cleaned.to_dict(orient='records')
```

### Creación del Endpoint con FastAPI

1. Cread un archivo Python (ej., `main_subgrupo2.py`).
2. Importad FastAPI y otras librerías necesarias.
3. Configurad el logging.
4. Cread una instancia de FastAPI.
5. Definid una función asíncrona para el endpoint `/cleaned_songs`.
6. Usad uvicorn para lanzar vuestra aplicación:
   ```bash
   uvicorn main_subgrupo2:app --host 127.0.0.1 --port 8001 --reload
   ```

### Requisitos Específicos y Buenas Prácticas

- Usad FastAPI para el endpoint `/cleaned_songs`.
- Documentad vuestras funciones con docstrings (Google Style).
- Seguid el patrón de diseño de Servicio (Service Layer).
- Usad un linter como Flake8 para seguir PEP 8.
- Utilizad logging en lugar de print para un mejor seguimiento.

### Coordinación

- **Con Subgrupo 1**: Asegurad la estructura del JSON que recibiréis.
- **Con Subgrupo 3**: Informad sobre la estructura final del JSON que expondréis en `/cleaned_songs`.

### JSON en crudo:

```json
[
  {
    "track_id": "2plbrEY59IikOBgBGLjaoe",
    "track_name": "Die With A Smile",
    "track_artist": "Lady Gaga, Bruno Mars",
    "track_album_name": "Die With A Smile",
    "track_album_release_date": "2024-08-16",
    "playlist_genre": "pop",
    "playlist_subgenre": "mainstream",
    "energy": 0.592,
    "danceability": 0.521,
    "tempo": 157.969,
    "valence": 0.535,
    "acousticness": 0.308,
    "instrumentalness": 0,
    "speechiness": 0.0304,
    "liveness": 0.122,
    "loudness": -7.777,
    "track_popularity": 100,
    "duration_ms": 251668,
    "mode": 0,
    "key": 6,
    "time_signature": 3
  },
  {
    "track_id": "6dOtVTDdiauQNBQEDOtlAB",
    "track_name": "BIRDS OF A FEATHER",
    "track_artist": "Billie Eilish",
    "track_album_name": "HIT ME HARD AND SOFT",
    "track_album_release_date": "2024-05-17",
    "playlist_genre": "pop",
    "playlist_subgenre": "mainstream",
    "energy": 0.507,
    "danceability": 0.747,
    "tempo": 104.978,
    "valence": 0.438,
    "acousticness": 0.2,
    "instrumentalness": 0.0608,
    "speechiness": 0.0358,
    "liveness": 0.117,
    "loudness": -10.171,
    "track_popularity": 97,
    "duration_ms": 210373,
    "mode": 1,
    "key": 2,
    "time_signature": 4
  },
  {
    "track_id": "7ne4VBA60CxGM75vw0EYad",
    "track_name": "That’s So True",
    "track_artist": "Gracie Abrams",
    "track_album_name": "The Secret of Us (Deluxe)",
    "track_album_release_date": "2024-10-18",
    "playlist_genre": "pop",
    "playlist_subgenre": "mainstream",
    "energy": 0.808,
    "danceability": 0.554,
    "tempo": 108.548,
    "valence": 0.372,
    "acousticness": 0.214,
    "instrumentalness": 0,
    "speechiness": 0.0368,
    "liveness": 0.159,
    "loudness": -4.169,
    "track_popularity": 93,
    "duration_ms": 166300,
    "mode": 1,
    "key": 1,
    "time_signature": 4
  },

  ```