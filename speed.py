import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import *
import time

model = YOLO('yolov8s.pt')

with open("coco.txt", "r") as f:
    class_list = f.read().splitlines()

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    tracker = Tracker()

    cy1 = 322
    cy2 = 368
    offset = 6

    vh_down = {}
    counter = []

    vh_up = {}
    counter1 = []
    vehicle_log = []
    frame_count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % 3 != 0:
            continue

        frame = cv2.resize(frame, (1020, 500))
        results = model.predict(frame)

        boxes = results[0].boxes
        xyxy = boxes.xyxy.cpu().numpy()
        cls = boxes.cls.cpu().numpy()

        detections = []
        for i, box in enumerate(xyxy):
            x1, y1, x2, y2 = map(int, box[:4])
            class_id = int(cls[i])
            if class_list[class_id] == 'car':
                detections.append([x1, y1, x2, y2])

        tracked = tracker.update(detections)
        for x3, y3, x4, y4, vid in tracked:
            cx = (x3 + x4) // 2
            cy = (y3 + y4) // 2

            # DOWN
            if cy1 - offset < cy < cy1 + offset and vid not in vh_down:
                vh_down[vid] = time.time()

            if vid in vh_down and cy2 - offset < cy < cy2 + offset:
                if vid not in counter:
                    counter.append(vid)
                    elapsed = time.time() - vh_down[vid]
                    speed = round((10 / elapsed) * 3.6, 2)
                    vehicle_log.append({"ID": vid, "Direction": "Down", "Speed_kmph": speed})

            # UP
            if cy2 - offset < cy < cy2 + offset and vid not in vh_up:
                vh_up[vid] = time.time()

            if vid in vh_up and cy1 - offset < cy < cy1 + offset:
                if vid not in counter1:
                    counter1.append(vid)
                    elapsed = time.time() - vh_up[vid]
                    speed = round((10 / elapsed) * 3.6, 2)
                    vehicle_log.append({"ID": vid, "Direction": "Up", "Speed_kmph": speed})

    cap.release()
    return pd.DataFrame(vehicle_log)
