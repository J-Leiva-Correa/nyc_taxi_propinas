from src.dataset import load_data
from src.build_features import build_features

# Cargar los datos
df = load_data("data/raw/yellow_tripdata_2020-01.parquet")

# Construir features
X, y = build_features(df)

print(X.head())
print(y.head())
