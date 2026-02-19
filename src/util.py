# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 17:15:54 2026

@author: JM
"""

import os
import pandas as pd


import os
import pickle
import pandas as pd


def guardar_archivo(obj, nombre_archivo, carpeta_principal, subcarpeta=None, formato="parquet"):
    """
    Guarda un objeto dentro de la estructura del proyecto.

    Parameters
    ----------
    obj : objeto
        Puede ser DataFrame, modelo, dict, etc.

    nombre_archivo : str
        Nombre sin extensión.

    carpeta_principal : str
        Carpeta raíz del proyecto ('data', 'models', 'reports', etc.)

    subcarpeta : str, optional
        Subnivel dentro de la carpeta principal.

    formato : str
        'csv', 'parquet', 'pkl'
    """

    # Ruta base del proyecto (un nivel arriba de src)
    ruta_base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Construcción dinámica de ruta
    if subcarpeta:
        ruta_carpeta = os.path.join(ruta_base, carpeta_principal, subcarpeta)
    else:
        ruta_carpeta = os.path.join(ruta_base, carpeta_principal)

    os.makedirs(ruta_carpeta, exist_ok=True)

    ruta_archivo = os.path.join(ruta_carpeta, f"{nombre_archivo}.{formato}")

    # Guardado según tipo
    if formato == "csv":
        obj.to_csv(ruta_archivo, index=False)

    elif formato == "parquet":
        obj.to_parquet(ruta_archivo, index=False)

    elif formato == "pkl":
        with open(ruta_archivo, "wb") as f:
            pickle.dump(obj, f)

    else:
        raise ValueError("Formato no soportado.")

    print(f"✅ Archivo guardado en: {ruta_archivo}")

    return ruta_archivo

def cargar_archivo(nombre_archivo, carpeta_principal, subcarpeta=None, formato="parquet"):
    """
    Carga un objeto desde la estructura del proyecto.

    Parameters
    ----------
    nombre_archivo : str
        Nombre del archivo sin extensión.

    carpeta_principal : str
        Carpeta raíz ('data', 'models', etc.)

    subcarpeta : str, optional
        Subnivel (ej: 'raw', 'processed').

    formato : str
        'csv', 'parquet', 'pkl'

    Returns
    -------
    obj : El objeto cargado (DataFrame, modelo, etc.)
    """
    
    # 1. Construir la ruta de forma dinámica (igual que en guardar)
    ruta_base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    if subcarpeta:
        ruta_archivo = os.path.join(ruta_base, carpeta_principal, subcarpeta, f"{nombre_archivo}.{formato}")
    else:
        ruta_archivo = os.path.join(ruta_base, carpeta_principal, f"{nombre_archivo}.{formato}")

    # 2. Verificar si el archivo existe antes de intentar abrirlo
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"❌ No se encontró el archivo en: {ruta_archivo}")

    # 3. Carga según formato
    if formato == "csv":
        obj = pd.read_csv(ruta_archivo)
    
    elif formato == "parquet":
        obj = pd.read_parquet(ruta_archivo, engine='pyarrow') # Forzamos pyarrow
    
    elif formato == "pkl":
        with open(ruta_archivo, "rb") as f:
            obj = pickle.load(f)
            
    else:
        raise ValueError("Formato no soportado.")

    print(f"✅ Archivo cargado desde: {ruta_archivo}")
    return obj