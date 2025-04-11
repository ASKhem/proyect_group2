"""
Aplicación Procesadora de Datos de Canciones Spotify.
"""

from app.processor import get_processed_data
from app.main import app

__version__ = "1.0.0"
__all__ = ["app", "get_processed_data"]
