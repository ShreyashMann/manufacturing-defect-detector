import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np

st.set_page_config(page_title="Steel Defect Detector", layout="wide")
st.title("Steel Defect Detector")
st.write("Real-time defect detection on steel manufacturing surfaces using YOLOv8m")

@st.cache_resource
def load_model():
    return YOLO('runs/detect/steel_defects2/weights/best.pt')

model = load_model()

option = st.radio("Choose input:", ["Upload Image", "Webcam"])

if option == "Upload Image":
    uploaded = st.file_uploader("Upload a steel surface image", type=['jpg', 'jpeg', 'png'])
    if uploaded:
        img = Image.open(uploaded)
        img_array = np.array(img)
        results = model(img_array)
        annotated = results[0].plot()
        st.image(annotated, caption='Detections', channels='BGR', use_container_width=True)

        boxes = results[0].boxes
        if len(boxes) > 0:
            st.success(f"Found {len(boxes)} defect(s)")
        else:
            st.info("No defects detected")

elif option == "Webcam":
    st.info("Point your webcam at a metal/steel surface. Click 'Start Camera' to begin.")
    run = st.checkbox("Start Camera")
    FRAME_WINDOW = st.image([])
    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Could not access webcam")
            break
        results = model(frame, verbose=False)
        annotated = results[0].plot()
        FRAME_WINDOW.image(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
    else:
        cap.release()

st.sidebar.markdown("### Model Info")
st.sidebar.write("Model: YOLOv8m")
st.sidebar.write("Dataset: NEU-DET (steel defects)")
st.sidebar.write("mAP50: 70.8%")
st.sidebar.markdown("### Defect Classes")
st.sidebar.write("crazing · inclusion · patches · pitted_surface · rolled-in_scale · scratches")
