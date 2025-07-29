# src/predict.py

import joblib
from sklearn.metrics import f1_score


def evaluate(model_path, X_test, y_test):
    # Cargar modelo entrenado
    model = joblib.load(model_path)

    # Predecir
    y_pred = model.predict(X_test)

    # Calcular F1-score
    f1 = f1_score(y_test, y_pred)

    return f1
