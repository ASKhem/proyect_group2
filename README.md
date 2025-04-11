# Proyecto Subgrupo 2 - Procesador de Datos de Canciones Spotify

**Actividad Día 4: Introducción a la Ciencia de Datos y Buenas Prácticas**
*Fecha de generación: 11 de abril de 2025*
*Ubicación: A Coruña, Galicia, España*

## Estructura del Proyecto

```
proyect_group2/
├── app/                    # Código principal
│   ├── __init__.py        # Inicialización del módulo
│   ├── main.py            # API endpoints
│   └── processor.py       # Procesamiento de datos
├── data/                  # Datos
│   └── short_songs.json   # Datos de ejemplo
├── README.md             # Documentación principal
└── requirements.txt      # Dependencias
```

## Instalación

1. **Crear y activar entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
.\venv\Scripts\activate  # Windows
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

## Uso

### Iniciar el servidor:
```bash
uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload
```

### Acceder a los endpoints:
- **API Documentation:** http://127.0.0.1:8001/docs
- **Cleaned Songs Data:** http://127.0.0.1:8001/cleaned_songs
- **Health Check:** http://127.0.0.1:8001/

## Características

- **Procesamiento de datos:**
  - Limpieza de datos
  - Manejo de valores nulos
  - Conversión de tipos
  - Eliminación de duplicados

- **API REST:**
  - Documentación automática con Swagger
  - Endpoints para datos procesados
  - Manejo de errores
  - Logging completo

## Variables de Entorno

- `SOURCE_DATA_URL`: URL del endpoint de datos o ruta al archivo JSON local
  - Default: 'data/short_songs.json'

## Desarrollo

El proyecto sigue las mejores prácticas de Python:
- PEP 8 para estilo de código
- Logging para registro de eventos
- Docstrings estilo Google
- Manejo de errores robusto

## Contribuidores
Subgrupo 2: [Nombres de los miembros]
