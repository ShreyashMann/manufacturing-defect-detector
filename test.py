from ultralytics import YOLO

model = YOLO('runs/detect/steel_defects2/weights/best.pt')

results = model.predict(
    source='NEU-DET.v10i.yolov8/test/images',
    save=True,
    conf=0.25
)

print("Inference complete! Check runs/detect/ for output images.")
