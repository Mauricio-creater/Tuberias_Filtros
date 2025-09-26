
from filtros import aplicar_filtros
from utils import cargar_datos
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def seleccionar_archivo(tipo_archivo="input"):
    """Abre un cuadro de diálogo para seleccionar un archivo."""
    root = tk.Tk()
    root.withdraw()  

    if tipo_archivo == "input":
        # Seleccionar archivo de entrada
        archivo = filedialog.askopenfilename(
            title="Selecciona un archivo de entrada",
            filetypes=[("Archivos Excel", "*.xlsx;*.xls")]
        )
    else:
        # Seleccionar archivo de salida
        archivo = filedialog.asksaveasfilename(
            title="Selecciona la ubicación para guardar el archivo de salida",
            defaultextension=".xlsx",
            filetypes=[("Archivos Excel", "*.xlsx;*.xls")]
        )

    return archivo

def main():
    # Selección del archivo de entrada
    input_file = seleccionar_archivo("input")
    if not input_file:
        messagebox.showerror("Error", "No se seleccionó un archivo de entrada. El programa se cerrará.")
        return
    
    # Selección del archivo de salida
    output_file = seleccionar_archivo("output")
    if not output_file:
        messagebox.showerror("Error", "No se seleccionó un archivo de salida. El programa se cerrará.")
        return

    year = 2023  # Año para filtrar las contrataciones
    
    # Fuente de datos archivo .xlsx de entrada
    df = cargar_datos(input_file)
    

    # Filtros seleccionados (esto puede ser dinámico, dependiendo de la UI o parámetros)
    filtros_seleccionados = ["Filtro 1", "Filtro 2", "Filtro 3", "Filtro 4"]

    # Aplicar los filtros y guardar los resultados
    resultados = aplicar_filtros(df, filtros_seleccionados, year, output_file)  # Bomba

    # Mostrar las primeras filas del DataFrame resultante
    print(resultados.head())

if __name__ == '__main__':
    main()
