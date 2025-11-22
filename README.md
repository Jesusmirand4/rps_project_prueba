Este proyecto implementa un sistema de detección de gestos Piedra, Papel y Tijera utilizando YOLOv8, una API con FastAPI, y un contenedor Docker totalmente funcional.

Contenido del repositorio
rock-paper-scissors-eval/
│
├── data/                → Dataset desde Roboflow (YOLO format)
├── src/
│   ├── app/
│   │   ├── main.py      → API FastAPI
│   │   ├── utils.py     → Lógica del juego
│   │   └── model.py     → (opcional)
│   ├── inference/
│   │   └── predict.py   → Clase de inferencia
│   ├── train/
│   │   ├── train.py     → Script de entrenamiento YOLOv8
│   │   └── data.yaml    → Definición del dataset
│
├── weights/
│   └── best.pt          → Modelo entrenado
│
├── tests/
│   └── test_api.py
│
├── Dockerfile
├── requirements.txt
└── README.md

Instalación y ejecución local
1. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

2. Instalar dependencias
pip install -r requirements.txt

Entrenamiento del modelo YOLOv8

Asegúrate de que el dataset Roboflow esté en:

data/train/images
data/train/labels
data/valid/images
data/valid/labels


Ejecutar: python src/train/train.py


Los pesos entrenados aparecerán en: runs/detect/train/weights/best.pt


Cópiado a: weights/best.pt

Prueba de inferencia (opcional)
from ultralytics import YOLO
model = YOLO("weights/best.pt")
results = model("data/valid/images/ejemplo.jpg")
results[0].show()

Ejecución de la API FastAPI
uvicorn src.app.main:app --reload

Endpoints:

Swagger UI → http://localhost:8000/docs

POST /play → recibe player_a y player_b como archivos JPG/PNG

Ejemplo de respuesta:
{
  "player_a": {"prediction": "Piedra", "confidence": 0.92},
  "player_b": {"prediction": "Tijera", "confidence": 0.88},
  "winner": "player_a",
  "reason": "Piedra vence a Tijera"
}

Ejecutar con Docker
Construir imagen
docker build -t rps-api .

Ejecutar contenedor
docker run -p 8000:8000 rps-api


La API estará disponible en:

http://localhost:8000/docs

 Tests
pytest tests/test_api.py

Tecnologías utilizadas:

Python 3.10
FastAPI
YOLOv8 (Ultralytics)
OpenCV
Docker
Uvicorn