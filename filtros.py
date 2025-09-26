def filtro_1(df, year):
    """Filtro que selecciona los datos del año especificado."""
    # Buscar la columna que tiene los años
    year_column = [col for col in df.columns if 'año' in col.lower()]
    if not year_column:
        raise ValueError("No se encontró una columna que contenga 'año'.")
    return df[df[year_column[0]] == year]

def filtro_2(df):
    """Filtro que elimina filas con valores nulos en la columna 'Monto'."""
    # Buscar la columna que tiene los montos
    monto_column = [col for col in df.columns if 'monto' in col.lower()]
    if not monto_column:
        raise ValueError("No se encontró una columna que contenga 'monto'.")
    return df.dropna(subset=[monto_column[0]])

def filtro_3(df):
    """Filtro que agrega una columna 'Años de Contratación'."""
    # Buscar la columna que tiene los años
    year_column = [col for col in df.columns if 'año' in col.lower()]
    if not year_column:
        raise ValueError("No se encontró una columna que contenga 'año'.")
    df['Años de Contratación'] = 2025 - df[year_column[0]]
    return df

def filtro_4(df):
    """Filtro que filtra los registros cuyo 'Monto' sea mayor a 5000."""
    # Buscar la columna que tiene los montos
    monto_column = [col for col in df.columns if 'monto' in col.lower()]
    if not monto_column:
        raise ValueError("No se encontró una columna que contenga 'monto'.")
    return df[df[monto_column[0]] > 5000]

def filtro_5(df, output_file):
    """Guarda el DataFrame en un archivo Excel."""
    df.to_excel(output_file, index=False)

def aplicar_filtros(df, filtros_seleccionados, year, output_file):
    """Aplica los filtros seleccionados sobre el DataFrame."""
    if "Filtro 1" in filtros_seleccionados:
        df = filtro_1(df, year)
    if "Filtro 2" in filtros_seleccionados:
        df = filtro_2(df)
    if "Filtro 3" in filtros_seleccionados:
        df = filtro_3(df)
    if "Filtro 4" in filtros_seleccionados:
        df = filtro_4(df)
    filtro_5(df, output_file)  # Guarda el archivo
    return df
