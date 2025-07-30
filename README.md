# 🗽 Clasificación de Propinas en Taxis de NYC (2020)

Este proyecto corresponde a la **Tarea 1 del ramo Desarrollo de Productos de Datos** del Magíster en Data Science – UDD.  
Consiste en construir un clasificador que prediga si un viaje en taxi incluirá propina (`tip_amount > 0`) utilizando datos abiertos del NYC Taxi & Limousine Commission.

---

## 📁 Estructura del proyecto


```
nyc_taxi_propinas/
├── data/
│   └── raw/                          ← Archivos .parquet (no incluidos)
├── models/
│   └── modelo_random_forest.pkl      ← Modelo entrenado serializado
├── notebooks/
│   └── 00_nyc_taxi_model.ipynb       ← Notebook con proceso unificado y conclusiones
├── scripts/
│   ├── evaluate_months.py            ← Evalúa el modelo en distintos meses
│   └── plot_resultados.py            ← Genera gráfico de F1-score por mes
├── src/
│   ├── config.py                     ← Parámetros generales y rutas
│   ├── data/
│   │   └── dataset.py                ← Carga y preparación de datos
│   ├── features/
│   │   └── build_features.py         ← Ingeniería de variables
│   ├── modeling/
│   │   ├── train.py                  ← Entrenamiento del modelo
│   │   └── predict.py                ← Predicción y evaluación
│   └── visualization/
│       └── plots.py                 ← Visualización de métricas
├── probar_dataset.py                 ← Script principal para prueba unificada
├── requirements.txt                  ← Requisitos del entorno
└── README.md                         ← Descripción del proyecto y guía de uso
```

## ⚙️ Requisitos del proyecto

- Python 3.8
- pandas 1.3
- scikit-learn 1.0
- joblib 1.1
- matplotlib 3.4


## Instrucciones para ejecutar el proyecto.

1) Entrenar el modelo:

python probar_dataset.py

2) Evaluar por mes:

python scripts/evaluate_months.py

Imprime F1-score para:

Enero
Febrero
Abril

3) Visualizar F1 por mes.

python scripts/plot_resultados.py

4) Resultados del modelo

Mes	F1-Score	Ejemplos
Enero	0.9593	10.000
Febrero	0.8238	10.000
Abril	0.6606	10.000

5) Comentarios y conclusiones.


- El modelo Random Forest clasifica correctamente si hay propina en el mes de entrenamiento (enero).
- Su rendimiento cae en febrero y más aún en abril.

Esto muestra falta de generalización en el tiempo, posiblemente por:

- Cambios en comportamiento de pasajeros
- Pandemia

- Ausencia de features temporales como día/semana/feriado

Se recomienda:

- Entrenar con datos más variados (múltiples meses)
- Incorporar más features temporales/contextuales
- Probar validación temporal cruzada

6) Datos utilizados

Los datos fueron descargados desde NYC TLC:

- yellow_tripdata_2020-01.parquet

- yellow_tripdata_2020-02.parquet

- yellow_tripdata_2020-04.parquet

7) Autor

Joaquín Leiva Correa
Magíster en Data Science – Universidad del Desarrollo
Repositorio: https://github.com/J-Leiva-Correa/nyc_taxi_propinas