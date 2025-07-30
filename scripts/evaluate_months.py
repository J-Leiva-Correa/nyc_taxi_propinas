import sys
import os

# ✅ Forzar incluir la carpeta raíz del proyecto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

print("📂 Ruta añadida al sys.path:", project_root)

# ✅ Importaciones después del path
from src.data.dataset import load_data
from src.features.build_features import build_features
from src.modeling.predict import evaluate


def evaluate_model_on_months(months, base_path, model_path):
    resultados = []

    for month in months:
        print(f"\n📅 Evaluando mes: {month}")
        filename = f"yellow_tripdata_{month}.parquet"
        file_path = os.path.join(base_path, filename)

        try:
            df = load_data(file_path).sample(10000, random_state=42)
            X, y = build_features(df)
            f1 = evaluate(model_path, X, y)
            resultados.append({'mes': month, 'f1_score': round(f1, 4), 'n_ejemplos': len(df)})

        except FileNotFoundError:
            print(f"❌ Archivo no encontrado: {file_path}")
        except Exception as e:
            print(f"⚠️ Error al evaluar {month}: {e}")

    return resultados

if __name__ == "__main__":
    meses = ["2020-01", "2020-02", "2020-04"]

    resultados = evaluate_model_on_months(
        months=meses,
        base_path="data/raw",
        model_path="models/modelo_random_forest.pkl"
    )

    print("\n📊 Resultados por mes:")
    for r in resultados:
        print(f"Mes: {r['mes']} - F1: {r['f1_score']} - Ejemplos: {r['n_ejemplos']}")
