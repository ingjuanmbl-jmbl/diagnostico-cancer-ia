# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 14:24:19 2026

@author: JM
"""

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, recall_score, precision_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def graficar_curvas_aprendizaje(history):
    plt.figure(figsize=(12, 4))

    # Gráfica de Precisión (Accuracy)
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Entrenamiento')
    plt.plot(history.history['val_accuracy'], label='Validación')
    plt.title('Precisión del Modelo')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    # Gráfica de Pérdida (Loss)
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Entrenamiento')
    plt.plot(history.history['val_loss'], label='Validación')
    plt.title('Pérdida del Modelo')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    
    plt.show()

def evaluar_modelo_completo(model, X_test, y_test):
    """
    Genera un análisis integral: Matriz de Confusión y Métricas Detalladas.
    """
    # 1. Predicciones
    y_pred_prob = model.predict(X_test)
    y_pred = (y_pred_prob > 0.5).astype(int)

    # 2. Cálculo de métricas individuales
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # 3. Mostrar Resumen de Métricas en Tabla
    print("\n" + "="*30)
    print("   RESUMEN DE MÉTRICAS")
    print("="*30)
    metrics_df = pd.DataFrame({
        'Métrica': ['Accuracy', 'Precision', 'Recall (Sensibilidad)', 'F1-Score'],
        'Valor': [f"{accuracy:.4f}", f"{precision:.4f}", f"{recall:.4f}", f"{f1:.4f}"]
    })
    print(metrics_df.to_string(index=False))
    print("="*30)

    # 4. Reporte detallado por clase
    print("\nDetalle por Clase (0: Benigno, 1: Maligno):")
    print(classification_report(y_test, y_pred))

    # 5. Visualización de la Matriz de Confusión
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(7, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', 
                xticklabels=['Pred. Benigno', 'Pred. Maligno'],
                yticklabels=['Real Benigno', 'Real Maligno'])
    plt.title('Matriz de Confusión: Diagnóstico de Cáncer')
    plt.ylabel('Realidad')
    plt.xlabel('Predicción de la Red')
    plt.show()

    return metrics_df