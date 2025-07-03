import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import *

model = YOLO('yolov8s.pt')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print([x, y])

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture('veh2.mp4')

with open("coco.txt", "r") as f:
    class_list = f.read().splitlines()

count = 0
tracker = Tracker()

cy1 = 322
cy2 = 368
offset = 6

while True:
    ret, frame = cap.read()
    if not ret:
        break

    count += 1
    if count % 3 != 0:
        continue

    frame = cv2.resize(frame, (1020, 500))
    results = model.predict(frame)

    boxes = results[0].boxes
    xyxy = boxes.xyxy.cpu().numpy()
    cls = boxes.cls.cpu().numpy()

    list = []
    for i, box in enumerate(xyxy):
        x1, y1, x2, y2 = map(int, box[:4])
        class_id = int(cls[i])
        c = class_list[class_id]
        if 'car' in c:
            list.append([x1, y1, x2, y2])

    bbox_id = tracker.update(list)
    for bbox in bbox_id:
        x3, y3, x4, y4, id = bbox
        cx = (x3 + x4) // 2
        cy = (y3 + y4) // 2
        cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
        cv2.putText(frame, str(id), (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)

    cv2.line(frame, (274, cy1), (814, cy1), (255, 255, 255), 1)
    cv2.line(frame, (177, cy2), (927, cy2), (255, 255, 255), 1)

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()