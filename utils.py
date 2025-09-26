# utils.py
import pandas as pd

def cargar_datos(input_file):
    """Carga un archivo Excel en un DataFrame."""
    return pd.read_excel(input_file)

def guardar_datos(df, output_file):
    """Guarda un DataFrame en un archivo Excel."""
    df.to_excel(output_file, index=False)
