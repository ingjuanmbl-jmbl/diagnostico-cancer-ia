# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 10:42:53 2026

@author: JM
"""

import pandas as pd
import numpy as np

def eliminar_columnas(dataframe,lista_columnas):
    """
    

    Parameters
    ----------
    dataframe : df
        Se debe ingresar la variable en la cual esta el data frame a eliminar las columnas
    lista_columnas : lista
        Listado de columnas que se quieren eliminar

    Returns
    -------
    data frame con las columnas eliminadas

    """
    
    #Fltrar unicamente las columnas que realmente existen en el df
    columnas_reales = [c for c in lista_columnas if c in dataframe.columns]
    
    if not columnas_reales:
        print("Advertencia: Ninguna de las columnas especificadas existe en el DataFrame.")
        return dataframe
    
    return dataframe.drop(columns=columnas_reales)


def renombrar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    
    """
    

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    DataGrame con las columnas traducidas

    """
    
    #Definimos el mapeo de nombres
    
    mapeo = {
    'diagnosis': 'diagnostico',
    'radius_mean': 'radio_promedio',
    'texture_mean': 'textura_promedio',
    'perimeter_mean': 'perimetro_promedio',
    'area_mean': 'area_promedio',
    'smoothness_mean': 'suavidad_promedio',
    'compactness_mean': 'compactacion_promedio',
    'concavity_mean': 'concavidad_promedio',
    'concave points_mean': 'puntos_de_concavidad_promedio',
    'symmetry_mean': 'simetria_promedio',
    'fractal_dimension_mean': 'dimension_fractal_promedio',

    'radius_se': 'radio_error_estandar',
    'texture_se': 'textura_error_estandar',
    'perimeter_se': 'perimetro_error_estandar',
    'area_se': 'area_error_estandar',
    'smoothness_se': 'suavidad_error_estandar',
    'compactness_se': 'compactacion_error_estandar',
    'concavity_se': 'concavidad_error_estandar',
    'concave points_se': 'puntos_de_concavidad_error_estandar',
    'symmetry_se': 'simetria_error_estandar',
    'fractal_dimension_se': 'dimension_fractal_error_estandar',

    'radius_worst': 'radio_maximo',
    'texture_worst': 'textura_maxima',
    'perimeter_worst': 'perimetro_maximo',
    'area_worst': 'area_maxima',
    'smoothness_worst': 'suavidad_maxima',
    'compactness_worst': 'compactacion_maxima',
    'concavity_worst': 'concavidad_maxima',
    'concave points_worst': 'puntos_de_concavidad_maximos',
    'symmetry_worst': 'simetria_maxima',
    'fractal_dimension_worst': 'dimension_fractal_maxima'
}
    return df.rename(columns = mapeo)

