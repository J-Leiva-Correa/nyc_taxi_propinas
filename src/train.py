# src/train.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import joblib


def train_model(X, y, model_path='models/modelo_random_forest.pkl'):
    # Dividir en entrenamiento y validación
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Crear y entrenar modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluar el modelo
    y_pred = model.predict(X_val)
    f1 = f1_score(y_val, y_pred)
    print(f"F1-score en validación: {f1:.4f}")

    # Guardar el modelo
    joblib.dump(model, model_path)
    print(f"Modelo guardado en: {model_path}")

    return model
