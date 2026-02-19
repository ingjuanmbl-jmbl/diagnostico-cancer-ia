# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 17:01:23 2026

@author: JM
"""

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import keras_tuner as kt
from tensorflow.keras.callbacks import EarlyStopping

def build_model(hp):
    """
    Define el 'espacio de búsqueda' de la red neuronal.
    """
    model = Sequential()
    
    # Probamos diferentes números de neuronas en la primera capa
    model.add(Dense(
        units=hp.Int('units_input', min_value=8, max_value=64, step=8),
        activation='relu',
        input_shape=(30,)
    ))
    
    # Probamos si el Dropout ayuda (evita que la red memorice)
    if hp.Boolean("dropout"):
       model.add(Dropout(rate=hp.Float('dropout_rate', 0.2, 0.5, step=0.1)))
       
    # Segunda capa oculta con rango dinámico
    model.add(Dense(
        units=hp.Int('units_hidden', min_value=4, max_value=32, step=4),
        activation='relu'
    ))

    model.add(Dense(1, activation='sigmoid'))

    # Probamos diferentes velocidades de aprendizaje
    lr = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])

    model.compile(
        optimizer=Adam(learning_rate=lr),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model

def optimizar_hiperparametros(X_train, y_train, max_trials=10):
    tuner = kt.RandomSearch(
        build_model,
        objective='val_accuracy',
        max_trials=max_trials,
        directory='tuning_results',
        project_name='cancer_nn',
        overwrite=True
    )

    # Definimos el freno de mano
    early_stop = EarlyStopping(
        monitor='val_loss', 
        patience=8,          
        restore_best_weights=True 
    )

    # 1. Búsqueda de los mejores parámetros
    tuner.search(
        X_train, y_train, 
        epochs=100, 
        validation_split=0.2, 
        callbacks=[early_stop], 
        verbose=1
    )
    
    best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
    
    # 2. Re-entrenamos el modelo ganador para capturar el historial limpio
    model = tuner.hypermodel.build(best_hps)
    
    # IMPORTANTE: Aquí usamos 'early_stop' para que el historial 
    # no muestre la curva naranja subiendo otra vez.
    history = model.fit(
        X_train, y_train, 
        epochs=100, 
        validation_split=0.2,   
        callbacks=[early_stop], # <--- Corregido el nombre aquí
        verbose=0   
    )
    
    return model, history, best_hps


import os

def guardar_modelo(model, nombre_archivo='modelo_cancer_perfecto.keras'):
    """
    Guarda el modelo en la carpeta 'models' ubicada en la raíz del proyecto.
    """
    # Obtenemos la ruta del directorio donde está este archivo (src/)
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Subimos un nivel para llegar a la raíz del proyecto
    raiz_proyecto = os.path.dirname(directorio_actual)
    
    # Definimos la carpeta models en la raíz
    ruta_models = os.path.join(raiz_proyecto, 'models')
    
    if not os.path.exists(ruta_models):
        os.makedirs(ruta_models)
    
    ruta_final = os.path.join(ruta_models, nombre_archivo)
    model.save(ruta_final)
    print(f"✅ Modelo guardado correctamente en la raíz: {ruta_final}")