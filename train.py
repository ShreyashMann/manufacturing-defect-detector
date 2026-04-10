from ultralytics import YOLO

model = YOLO('yolov8m.pt')  # medium — better accuracy, M4 handles this easily

results = model.train(
    data='data.yaml',
    epochs=30,
    imgsz=640,
    batch=16,
    name='steel_defects'
)

print("Training complete!")
