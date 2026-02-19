# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 13:33:20 2026

@author: JM
"""
import joblib
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preparar_datos_entrenamiento(df: pd.DataFrame, target: str = 'diagnostico'):
    """
    

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame correspondiente al que se limpio previamente.
    target : str, optional
        DESCRIPTION. The default is 'diagnostico'.

    Returns
    -------
    Divide los datos en entrenamiento y prueba y los escala
    """
    
    #1. Separar X (Caracteristicas) de y (Objetivo)
    X = df.drop(columns=[target])
    y = df[target]
    
    #2. Dividir 80% para entrenar y 20% para evaluar el modelo final
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2,random_state=42,stratify=y
        )
    
    #Escalar con StandardScaler (resta la media y divide por la desviación estándar)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test) # Usamos el mismo escalador del train
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler
    


def guardar_escalador(scaler, nombre_archivo='scaler.pkl'):
    """
    Guarda el objeto StandardScaler en la carpeta 'models' en la raíz.
    """
    # Localizar la raíz (subiendo un nivel desde src/)
    raiz_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_models = os.path.join(raiz_proyecto, 'models')

    # Crear la carpeta si no existe
    if not os.path.exists(ruta_models):
        os.makedirs(ruta_models)

    ruta_final = os.path.join(ruta_models, nombre_archivo)
    
    # Guardar el archivo físico
    joblib.dump(scaler, ruta_final)
    print(f"✅ Escalador guardado correctamente en: {ruta_final}")