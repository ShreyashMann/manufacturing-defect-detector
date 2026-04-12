# Manufacturing Defect Detection

YOLOv8m trained on NEU-DET steel surface defect dataset. Detects 6 defect classes in real time via a Streamlit web app.

## Results

| Metric | Value |
|--------|-------|
| Model | YOLOv8m |
| Dataset | NEU-DET (1,800 images, 6 classes) |
| Epochs | 30 |
| mAP50 | **70.8%** |

| Class | mAP50 |
|-------|-------|
| scratches | 92.7% |
| pitted_surface | 90.9% |
| patches | 85.4% |
| inclusion | 69.3% |
| rolled-in_scale | 41.8% |
| crazing | 34.2% |

## How to Run

1. Clone the repo
   ```bash
   git clone https://github.com/ShreyashMann/manufacturing-defect-detector
   cd manufacturing-defect-detector
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   pip install streamlit
   ```

4. Train the model (runs overnight, ~12 hrs on CPU)
   ```bash
   python train.py
   ```

5. Launch the app
   ```bash
   streamlit run app.py
   ```

## Project Structure

```
├── data/train/       # NEU-DET training images (not tracked in git)
├── data/val/         # Validation images (not tracked in git)
├── app.py            # Streamlit web dashboard
├── train.py          # YOLOv8m training script
├── requirements.txt
└── README.md
```

## Tech Stack

- [Ultralytics YOLOv8](https://docs.ultralytics.com)
- [Streamlit](https://streamlit.io)
- [OpenCV](https://opencv.org)
- [NEU-DET Dataset](https://www.kaggle.com/datasets/fantacher/neu-metal-surface-defects-data)

## Roadmap

- [x] Train YOLOv8m on NEU-DET (mAP50: 70.8%)
- [x] Streamlit dashboard with image upload + webcam
- [ ] Add GC10-DET real-world images for webcam detection
- [ ] Deploy on Raspberry Pi (edge inference)

---

*Part of a 30-day Robotics + AI portfolio sprint — April–May 2026*
