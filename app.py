import streamlit as st
import cv2
import tempfile
import pandas as pd
from speed import process_video

st.title("Car Speed Estimation & Counting Using YOLOv8")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    st.video(tfile.name)

    st.info("Processing video...")
    df = process_video(tfile.name)

    st.success("Processing complete")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "vehicle_data.csv", "text/csv")