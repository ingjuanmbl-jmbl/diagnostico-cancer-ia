# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 17:00:37 2026

@author: JM
"""


from src.util import cargar_archivo
from src.limpieza import eliminar_columnas
from src.limpieza import renombrar_columnas
from src.feature import codificar_diagnostico
from src.util import guardar_archivo
from src.preprocesamiento import preparar_datos_entrenamiento
from src.modelado import optimizar_hiperparametros, guardar_modelo
from src.evaluacion import graficar_curvas_aprendizaje, evaluar_modelo_completo
def ejecutar_modelo():
    print("🚀 Iniciando sistema de diagnóstico...")
    
    
    #1. Cargar datos
    df_raw =cargar_archivo('raw_df_cancer','data','raw',formato='csv')
    
    #2.Limpieza de datos
    print("Inciando Limpieza de datos")
    
    #2.1 Eliminar columnas basura
    cols_drop = ['id','Unnamed: 32']
    df_raw = eliminar_columnas(df_raw, cols_drop)
    
    #2.2 Renombrar columnas en español
    df_raw = renombrar_columnas(df_raw)
    
    #2.2 Codificar variable diagnostico
    df_raw = codificar_diagnostico(df_raw)
    
    #2.3 Guardar el df limpio
    guardar_archivo(df_raw, "df_clean", carpeta_principal="data", subcarpeta="processed",formato="csv")
    
    #3. Preprocesamiento de datos
    print("Limpieza de datos Finalizada")
    print("---------------------------------------------------------------------")
    print("Inciando Preprocesamiento de datos")
    
    #3.1 Cargar archivo procesado
    df_clean = cargar_archivo('df_clean','data','processed',formato='csv')
    
    #3.2 Separar en entrenamiento y prueba
    X_train, X_test, y_train, y_test, mi_scaler = preparar_datos_entrenamiento(df_clean)
    print(f"Set de entrenamiento: {X_train.shape}")
    print(f"Set de prueba: {X_test.shape}")
    
    #4 Modelado
    print("Inciando Modelado ....")
    # Construccion de la red neuronal y optimización de hp
    modelo_final, historial, mejores_params = optimizar_hiperparametros(X_train, y_train)
    print("Modelado Completado")
    
    #5 Evaluación del modelo
    # 5.1 Con las curvas de aprendizaje se verifica el sobre ajuste
    graficar_curvas_aprendizaje(historial)

    # 5.2 analizar la Sensibilidad (Recall) y la Matriz de Confusión
    resumen = evaluar_modelo_completo(modelo_final, X_test, y_test)
    
    #2.3 Guardar el df limpio
    guardar_modelo(modelo_final)
    
    
   
    
    
    
    
    
    
    
    
