# Day 1 Tasks — April 9, 2026
## Goal: Get YOLO training on the NEU steel defects dataset

---

## Checklist

- [ ] Step 1: Extract dataset into data/ folder
- [ ] Step 2: Create data.yaml
- [ ] Step 3: Create train.py
- [ ] Step 4: Run training (python train.py)
- [ ] Step 5: Run inference with test.py

---

## Step 1: Check / Extract Dataset
Extract the Roboflow ZIP into your project so structure looks like:
```
data/
├── train/
│   ├── images/
│   └── labels/
└── val/
    ├── images/
    └── labels/
```

## Step 2: Create data.yaml
File goes in project root. Content:
```yaml
path: /Users/shreyashmann/Robotics-project-sprint/data
train: train/images
val: val/images

nc: 6
names: ['crazing', 'inclusion', 'patches', 'pitted_surface', 'rolled-in_scale', 'scratches']
```

## Step 3: Create train.py
```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # nano — fastest to train

results = model.train(
    data='data.yaml',
    epochs=30,
    imgsz=640,
    batch=8,
    name='steel_defects'
)

print("Training complete!")
```

## Step 4: Run Training
```bash
python train.py
```
Watch the loss numbers decrease. Normal to take 30-60 min.

## Step 5: Create test.py and run inference
```python
from ultralytics import YOLO

model = YOLO('runs/detect/steel_defects/weights/best.pt')

# Test on an image from val set
results = model('data/val/images/', save=True)
```
```bash
python test.py
```

---
## Notes / Errors
(paste errors here as you go)
