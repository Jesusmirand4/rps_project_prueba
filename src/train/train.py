from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")  # versión ligera para rapidez

    model.train(
        data="src/train/data.yaml",
        epochs=20,
        imgsz=320,
        batch=16,
        patience=10
    )

    model.export(format="onnx")  # opcional

if __name__ == "__main__":
    main()
