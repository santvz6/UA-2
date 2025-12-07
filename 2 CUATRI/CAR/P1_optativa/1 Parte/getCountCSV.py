from ultralytics import YOLO
import pandas as pd
import os
from datetime import datetime

model = YOLO("yolov8n.pt")
frame_dir = "frames"
results = []

for filename in sorted(os.listdir(frame_dir)):
    if filename.endswith(".jpg"):
        path = os.path.join(frame_dir, filename)
        res = model(path)
        person_count = sum(1 for r in res[0].boxes.cls if r == 0)  # Clase 0 = persona
        timestamp = filename.replace("frame_", "").replace(".jpg", "")
        results.append([timestamp, person_count])

df = pd.DataFrame(results, columns=['timestamp', 'person_count'])
df.to_csv("count.csv", index=False)
