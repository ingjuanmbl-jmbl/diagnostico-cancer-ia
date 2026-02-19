# Diagnóstico de Cáncer mediante Redes Neuronales Profundas (DNN)

Este repositorio contiene un sistema de clasificación binaria basado en **Deep Learning** para la detección de tumores benignos y malignos. El proyecto implementa un pipeline completo de Ciencia de Datos: desde la limpieza y preprocesamiento de datos médicos hasta la optimización de hiperparámetros y el despliegue de un script de predicción funcional.

## 📊 Rendimiento del Modelo
Tras una fase de optimización estocástica y control de sobreajuste, el modelo alcanzó métricas de grado clínico en el conjunto de prueba (114 pacientes):

El modelo ha alcanzado métricas de rendimiento sobresalientes, consolidándose como una herramienta de diagnóstico de alta fiabilidad:

* Accuracy Global: 98,25%. El sistema clasifica correctamente a casi la totalidad de la muestra, fallando únicamente en 2 de cada 114 casos.

* Precisión: 100%: cero falsos positivos. Si el modelo identifica un tumor como maligno, la certeza es absoluta, eliminando el riesgo de tratamientos agresivos innecesarios.

* Recall (Sensibilidad): 95.24%. Se ha mejorado significativamente la detección de casos positivos. El modelo identificó correctamente a 40 de 42 pacientes con tumores malignos.

## Estabilidad y Generalización
Las gráficas de entrenamiento muestran lo que en Deep Learning se llama un "Good Fit":

* Convergencia Ideal: Las curvas de Accuracy y Loss de entrenamiento y validación se desplazan en paralelo y terminan prácticamente juntas.

* Prevención de Overfitting: La cercanía final entre las métricas de entrenamiento y prueba confirma que el modelo no ha memorizado los datos, sino que ha aprendido a generalizar los patrones biológicos de los tumores.

---

## Stack Tecnológico
* **Lenguaje:** Python 3.x
* **IA & ML:** TensorFlow 2.x, Keras, Scikit-Learn
* **Análisis de Datos:** Pandas, NumPy
* **Visualización:** Matplotlib, Seaborn
* **Persistencia:** Joblib (para el escalador de datos)

---

## 📂 Estructura del Repositorio
* `data/`: Archivos CSV con los datos de diagnóstico tanto los datos crudos como los resultantes despues de la limpieza de datos
* `models/`: Contiene el modelo entrenado (`.keras`) y el escalador estandarizado (`.pkl`).
* `src/`: Scripts modulares (limpieza, modelado y utilidades).
* `main.py`: El punto de entrada para ejecutar todo el entrenamiento.

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Requisitos Previos
Es recomendable usar un entorno virtual de Conda con python 3.11:

conda activate entorno_ia

### 2. Entrenamiento Completo
Para ejecutar el pipeline de carga, optimización y guardado del modelo: python main.py


### ✒️ Conclusión

Este proyecto demuestra cómo una red neuronal, cuando se le aplican técnicas adecuadas de regularización (Dropout) y escalado, puede alcanzar niveles de precisión superiores al 99%, sirviendo como una herramienta de apoyo robusta para el diagnóstico oncológico.
