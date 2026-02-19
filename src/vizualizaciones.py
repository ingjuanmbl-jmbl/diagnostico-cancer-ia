# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 14:52:43 2026

@author: JM
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



def plot_boxplots(df: pd.DataFrame, features, target, figsize=(8, 5)) -> pd.DataFrame:
    """
    Genera boxplots de múltiples variables contra una variable objetivo.
    
    Parámetros:
    - df: DataFrame
    - features: lista de columnas numéricas
    - target: variable objetivo (categoría)
    - figsize: tamaño base de cada figura
    """
    
    for feature in features:
        plt.figure(figsize=figsize)
        sns.boxplot(x=target, y=feature, data=df)
        plt.title(f'Boxplot de {feature} vs {target}')
        plt.tight_layout()
        plt.show()


def plot_histograms(df, features, target=None, bins=30, figsize=(8, 5)):
    """
    Genera histogramas o KDE plots.
    
    Parámetros:
    - df: DataFrame
    - features: lista de columnas
    - target: si se especifica, separa por clase
    - bins: número de bins
    - figsize: tamaño figura
    """
    
    for feature in features:
        plt.figure(figsize=figsize)
        
        if target:
            sns.histplot(data=df, x=feature, hue=target,
                         bins=bins, kde=True, element="step")
        else:
            sns.histplot(df[feature], bins=bins, kde=True)
        
        plt.title(f'Histograma de {feature} Maligno (1) - Benigno (0)')
        plt.tight_layout()
        plt.show()

    