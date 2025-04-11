"""
Aplicación FastAPI principal para servir datos procesados de canciones Spotify.
"""
import uvicorn
from fastapi import FastAPI, HTTPException
from typing import List, Dict, Union
import logging
import os
from app.processor import get_processed_data

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Inicializar aplicación FastAPI
app = FastAPI(
    title="Procesador de Datos de Canciones Spotify",
    description="API para acceder a datos procesados de canciones Spotify",
    version="1.0.0"
)

# Configuración
SOURCE_DATA = os.getenv('SOURCE_DATA_URL', 'data/short_songs.json')

@app.get("/", tags=["Health"])
async def root():
    """Endpoint raíz - Verificación de salud"""
    return {"status": "saludable", "message": "Servicio en ejecución"}

@app.get("/cleaned_songs", response_model=List[Dict[str, Union[str, float, int]]])
async def get_cleaned_songs():
    """
    Obtiene datos de canciones procesados y limpios.
    
    Returns:
        List[Dict]: Lista de diccionarios con datos de canciones limpios
    """
    try:
        data = get_processed_data(SOURCE_DATA)
        logger.info(f"Se recuperaron exitosamente {len(data)} canciones procesadas")
        return data
    except Exception as e:
        logger.error(f"Error al recuperar las canciones procesadas: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar los datos: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
