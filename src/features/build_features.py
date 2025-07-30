# src/build_features.py

def build_features(df):
    df = df.copy()

    # Crear duración del viaje en segundos
    df['trip_duration'] = (df['tpep_dropoff_datetime'] -
                           df['tpep_pickup_datetime']).dt.total_seconds()

    # Extraer hora y día de la semana del viaje
    df['hour'] = df['tpep_pickup_datetime'].dt.hour
    df['dayofweek'] = df['tpep_pickup_datetime'].dt.dayofweek

    # Seleccionar columnas para el modelo
    features = ['trip_distance', 'fare_amount',
                'passenger_count', 'trip_duration', 'hour', 'dayofweek']
    X = df[features]
    y = df['has_tip']

    return X, y
