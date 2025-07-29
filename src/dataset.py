# src/dataset.py

import pandas as pd


def load_data(file_path):
    # Leer el archivo Parquet
    df = pd.read_parquet(file_path)

    # Eliminar filas sin valor de propina
    df = df[df['tip_amount'].notnull()]

    # Crear columna binaria: 1 si hubo propina, 0 si no
    df['has_tip'] = (df['tip_amount'] > 0).astype(int)

    return df
