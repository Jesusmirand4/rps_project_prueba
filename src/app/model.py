from src.inference.predict import GestureDetector


# Cargar el modelo una sola vez (optimiza latencia)
model = GestureDetector()