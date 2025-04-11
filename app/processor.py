"""
Módulo EDA para procesar datos de canciones de Spotify.
Maneja la carga, limpieza y transformación de datos.
"""
import json
import logging
import pandas as pd
from datetime import datetime
import requests
from typing import Dict, List, Union

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DataProcessor:
    """Clase para manejar operaciones de procesamiento de datos de canciones Spotify."""
    
    def __init__(self, source_path: str):
        """Inicializa el DataProcessor.
        
        Args:
            source_path: URL o ruta al archivo de datos de canciones
        """
        self.source_path = source_path
        self.data = None
        
    def load_data(self) -> None:
        """Carga datos desde un endpoint API o archivo JSON local."""
        try:
            if self.source_path.startswith('http'):
                response = requests.get(self.source_path)
                response.raise_for_status()
                self.data = response.json()
            else:
                with open(self.source_path, 'r') as f:
                    self.data = json.load(f)
            logging.info(f"Datos cargados exitosamente desde {self.source_path}")
        except Exception as e:
            logging.error(f"Error al cargar los datos: {str(e)}")
            raise
            
    def process_data(self) -> pd.DataFrame:
        """Procesa y limpia los datos cargados.
        
        Returns:
            pd.DataFrame: DataFrame limpio de datos de canciones
        """
        if self.data is None:
            raise ValueError("No hay datos cargados. Llame a load_data() primero.")
            
        # Convertir a DataFrame
        df = pd.DataFrame(self.data)
        initial_rows = len(df)
        logging.info(f"Número inicial de filas: {initial_rows}")
        
        # Manejar conversión de fecha
        df['track_album_release_date'] = pd.to_datetime(
            df['track_album_release_date'], 
            errors='coerce'
        )
        
        # Eliminar filas con valores nulos críticos
        critical_columns = ['track_id', 'track_album_release_date']
        df = df.dropna(subset=critical_columns)
        logging.info(f"Se eliminaron {initial_rows - len(df)} filas con valores nulos en columnas críticas")
        
        # Convertir columnas numéricas
        numeric_columns = ['energy', 'tempo', 'track_popularity']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
                
        # Eliminar duplicados
        df = df.drop_duplicates(subset=['track_id'], keep='first')
        logging.info(f"Número final de filas después de la limpieza: {len(df)}")
        
        return df

def get_processed_data(source_path: str) -> List[Dict[str, Union[str, float, int]]]:
    """Función principal para procesar datos de canciones.
    
    Args:
        source_path: Ruta a la fuente de datos (URL o ruta de archivo)
        
    Returns:
        Lista de diccionarios que contienen datos procesados de canciones
    """
    processor = DataProcessor(source_path)
    processor.load_data()
    df = processor.process_data()
    
    # Convertir fechas a formato ISO string antes de convertir a diccionario
    df['track_album_release_date'] = df['track_album_release_date'].dt.strftime('%Y-%m-%d')
    
    return df.to_dict(orient='records')
