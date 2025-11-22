from fastapi import FastAPI, UploadFile
from src.inference.predict import GestureDetector
from src.app.utils import rps_winner
import cv2
import numpy as np

app = FastAPI()
model = GestureDetector()

def read_image(file):
    content = file.file.read()
    img = np.frombuffer(content, np.uint8)
    return cv2.imdecode(img, cv2.IMREAD_COLOR)

@app.post("/play")
async def play(player_a: UploadFile, player_b: UploadFile):
    img_a = read_image(player_a)
    img_b = read_image(player_b)

    pred_a = model.predict(img_a)
    pred_b = model.predict(img_b)

    winner, reason = rps_winner(pred_a["prediction"], pred_b["prediction"])

    return {
        "player_a": pred_a,
        "player_b": pred_b,
        "winner": winner,
        "reason": reason
    }
