from ultralytics import YOLO

class GestureDetector:
    def __init__(self, weights_path="weights/best.pt", conf=0.4):
        self.model = YOLO(weights_path)
        self.confidence_threshold = conf

    def predict(self, image):
        results = self.model(image)[0]

        if len(results.boxes) == 0:
            return {"prediction": "undecided", "confidence": 0}

        # tomar detección más confiable
        best = results.boxes.conf.argmax()
        box = results.boxes[best]

        pred_class = results.names[int(box.cls)]
        conf = float(box.conf)

        if conf < self.confidence_threshold:
            return {"prediction": "undecided", "confidence": conf}

        bbox = box.xywh.tolist()[0]
        return {
            "prediction": pred_class,
            "confidence": conf,
            "bbox": bbox
        }
