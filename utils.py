# utils.py
import pandas as pd

def cargar_datos(input_file):
    """Carga un archivo Excel en un DataFrame."""
    return pd.read_excel(input_file)