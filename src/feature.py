# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 14:10:39 2026

@author: JM
"""

import pandas as pd

def codificar_diagnostico(df: pd.DataFrame, target_col = 'diagnostico') -> pd.DataFrame:
    """
    Codifica la variable Objetivo para el modelko de Cancer

    Parameters
    ----------
    df : pd.DataFrame
        El DataFrame en la columna diagnostico

    Returns
    -------
    pd.DataFrame: El DataFrame Codificado con Valores 1 (Malino), 0 (Benigno)

    """
    df = df.copy() #evitamos modificar el df original por error
    
    if target_col in df.columns:
        #Se usa mapeo explicito para tener un control total
        mapping = {'M': 1, 'B': 0}
        df[target_col] = df[target_col].map(mapping)
        #Asegurar que la conversión devuelva un entero
        df[target_col] = df[target_col].astype(int)
        
        print(f"Variable '{target_col}' codificada correctamente")
    else:
        print(f"La Variable '{target_col}' no se encontró en el df")
    return df

    