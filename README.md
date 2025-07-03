# Car Speed Estimation & Counting Using YOLOv8

This project implements a real-time vehicle detection, tracking, and speed estimation system using the YOLOv8 object detection model. It allows you to upload a video or process a recorded file and get a live analysis of vehicle movement, speed (in km/h), and directional flow (up or down). Built with Python, OpenCV, and Streamlit.

---

## Features

- Detects cars using YOLOv8s
- Tracks vehicle movement with custom centroid-based tracker
- Estimates speed based on frame difference across two reference lines
- Counts vehicles moving up and down
- Displays real-time bounding boxes, IDs, and speed
- Outputs a downloadable CSV log of all vehicle detections
- Streamlit interface for interactive usage

---

## Demo Preview

![demo](preview.png) *(Add your own preview if hosted)*

---

## Folder Structure

```
car-speed-estimation-yolov8/
├── app.py                  # Streamlit app interface
├── speed.py                # Video processing and speed calculation logic
├── tracker.py              # Object tracking class
├── coco.txt                # COCO class labels used by YOLO
├── sample_video.mp4        # Demo video file (< 200MB)
├── requirements.txt        # Python dependencies
├── README.md               # This documentation
└── .gitignore              # Ignore unnecessary files
```

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/car-speed-estimation-yolov8.git
cd car-speed-estimation-yolov8
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

---

## How to Run

### Option 1: Local with Streamlit
```bash
streamlit run app.py
```

Upload a video (MP4/AVI/MOV) less than 200MB.

### Option 2: CLI Debugging (No UI)
```bash
python speed.py
```
Make sure `veh2.mp4` is present in the root folder.

---

## Sample Video

Download a sample video from:
[https://archive.org/download/traffic-camera-sample/Traffic%20Camera%20Sample.mp4](https://archive.org/download/traffic-camera-sample/Traffic%20Camera%20Sample.mp4)

Rename it to `sample_video.mp4` and place it in the project directory.

---

## Output CSV File
The CSV includes:
- Vehicle ID
- Direction (Up / Down)
- Speed in km/h

Example:
```
ID,Direction,Speed_kmph
3,Down,43.20
7,Up,37.56
```

---

## Configuration

Edit these variables in `speed.py` if needed:
- `cy1`, `cy2`: vertical line positions in frame (Y-axis)
- `offset`: range margin (default = 6)
- `distance`: real-world distance between the lines (default = 10 meters)

---

## Limitations

- Only detects vehicles labeled as 'car' (can be expanded)
- Detection accuracy depends on YOLO model, video quality, and angle
- Results may vary based on traffic density and camera height

---

## Roadmap

- [ ] Add real-time webcam support
- [ ] Export video with annotated frames
- [ ] Add multi-class support (bus, truck, etc.)
- [ ] Deploy on Streamlit Cloud

---

## License

This project is licensed under the MIT License.

---

## Author

Built by [Eslam Ashraf](https://github.com/Eslam-Ashraf-49).
