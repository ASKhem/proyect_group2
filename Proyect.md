# Documentación Técnica - Procesador de Datos de Canciones Spotify

## 1. Componentes Principales

### 1.1 Procesador de Datos (`app/processor.py`)

```python
class DataProcessor:
    # Maneja la carga y procesamiento de datos
    def load_data() -> None
    def process_data() -> pd.DataFrame
```

Funcionalidades:
- Carga de datos desde API o archivo JSON
- Conversión de tipos de datos
- Limpieza de valores nulos
- Eliminación de duplicados
- Logging de operaciones

### 1.2 API REST (`app/main.py`)

Endpoints:
- `GET /cleaned_songs` - Datos procesados
- `GET /` - Health check

Features:
- FastAPI con Swagger UI
- Manejo de errores HTTP
- Logging de requests
- Validación de datos

## 2. Flujo de Datos

1. **Entrada de Datos:**
   - API endpoint del Subgrupo 1 (`http://127.0.0.1:8000/songs`)
   - Archivo JSON local (`data/short_songs.json`)

2. **Procesamiento:**
   - Carga en DataFrame
   - Conversión de fechas
   - Limpieza de nulos
   - Conversión numérica
   - Eliminación de duplicados

3. **Exposición:**
   - Endpoint REST
   - Formato JSON
   - Documentación automática

## 3. Manejo de Errores

- **Carga de Datos:**
  ```python
  try:
      response = requests.get(source_path)
      response.raise_for_status()
  except Exception as e:
      logging.error(f"Error loading data: {str(e)}")
      raise
  ```

- **API:**
  ```python
  @app.get("/cleaned_songs")
  async def get_cleaned_songs():
      try:
          data = get_processed_data(SOURCE_DATA)
          return data
      except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))
  ```

## 4. Configuración

Variables de entorno:
- `SOURCE_DATA_URL`: Origen de datos
  - Default: `data/short_songs.json`
  - Alternativa: URL del endpoint del Subgrupo 1

## 5. Logging

- **Nivel:** INFO
- **Formato:** `%(asctime)s - %(levelname)s - %(message)s`
- **Eventos registrados:**
  - Carga de datos
  - Limpieza de datos
  - Operaciones de API
  - Errores y excepciones

## 6. Uso

```bash
# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Iniciar servidor
uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload

# Acceder a la documentación
# Abrir en navegador: http://127.0.0.1:8001/docs
