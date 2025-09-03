from ultralytics import YOLO
import json
import datetime
import sys

# Get image path from command-line argument or default
image_path = sys.argv[1] if len(sys.argv) > 1 else "road.jpg"

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Run detection
results = model(image_path)

# Create JSON output
frame_id = 1
timestamp = datetime.datetime.utcnow().isoformat()
detections = []

for r in results:
    for box in r.boxes:
        detections.append({
            "class": "pothole",  # Simulating pothole detection
            "confidence": float(box.conf[0]),
            "bounding_box": {
                "xmin": int(box.xyxy[0][0]),
                "ymin": int(box.xyxy[0][1]),
                "xmax": int(box.xyxy[0][2]),
                "ymax": int(box.xyxy[0][3])
            }
        })

output = {
    "frame_id": frame_id,
    "timestamp": timestamp,
    "detections": detections
}

# Print and save output
print(json.dumps(output, indent=2))
with open("output.json", "w") as f:
    json.dump(output, f, indent=2)
