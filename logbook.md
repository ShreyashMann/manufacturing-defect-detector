# Logbook — Manufacturing Defect Detection Sprint

**Sprint:** April 9 – May 8, 2026
**Goal:** YOLO + OpenCV defect detection system with Streamlit dashboard

---

## [Apr 9–10, 2026] — Day 1

**What we did:**
- Fixed `data.yaml` with absolute paths pointing to NEU-DET dataset
- Created `train.py` — YOLOv8m, 30 epochs, batch 16
- Created `test.py` — inference on 180 test images
- Trained overnight using `caffeinate` (12.35 hours on M4 CPU)
- Ran inference, output saved to `runs/detect/predict`

**What you learned:**
- What `data.yaml` is and why YOLO needs it
- What training loss means (box_loss, cls_loss, dfl_loss)
- What mAP50 is and why it matters
- Difference between YOLOv8 model sizes (n/s/m/l/x)

**Output/Result:**
- Model: `runs/detect/steel_defects2/weights/best.pt` (52MB)
- mAP50: **0.708** (70.8%) overall
- Best classes: scratches (0.927), pitted_surface (0.909), patches (0.854)
- Weakest: crazing (0.342), rolled-in_scale (0.418)

**Next up:**
- Day 2: OpenCV basics + data augmentation

---

## [Apr 8, 2026] — Day 0 (Setup)

**What we did:**
- Created CLAUDE.md with project instructions, rules, and resources
- Set up memory tracker (project-sprint.md) with Week 1 day-by-day plan
- Created this logbook
- Activated Python virtual environment

**What you learned:**
- Project structure and sprint plan

**Output/Result:**
- `CLAUDE.md`, `logbook.md`, memory files created
- `venv/` initialized

**Next up:**
- Day 1: Environment setup + install dependencies + run first YOLO model

---
