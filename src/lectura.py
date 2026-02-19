# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 16:40:09 2026

@author: JM
"""
import pandas as pd
import os

def cargar_datos_crudos(nombre_archivo):
    """
    

    Parameters
    ----------
    nombre_archivo : CSV
    Localiza el carga un archivo csv almacenado en la carpeta data/raw

    Returns
    -------
    Archivo debidamente cargado en formato DataFrame

    """
    
    #Realizar busqueda en la carpeta raiz del proyecto (un nivel arriva de src)
    ruta_base = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
    ruta_archivo = os.path.join(ruta_base, 'data', 'raw', nombre_archivo)
    
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No se encontro archivo en: {ruta_archivo}")
        
    df = pd.read_csv(ruta_archivo)
    print(f"✅ Archivo cargado exitosamente. Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
    return df
