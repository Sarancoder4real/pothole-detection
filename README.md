# **Pothole Detection using YOLOv8**

This project demonstrates a **pothole detection pipeline** using **YOLOv8** for object detection.  
It processes an input image and outputs detection results in **JSON format**.

---

## **📌 Features**
- ✅ Uses **Ultralytics YOLOv8** for object detection  
- ✅ Accepts an input image (e.g., `road.jpg`)  
- ✅ Outputs a **structured JSON file** with:
  - `frame_id`
  - `timestamp`
  - `detections` (list of detected objects with bounding boxes and confidence scores)
 
---
## 📂 Project Structure
```
pothole/
│── detect.py          # Main detection script
│── yolov8n.pt         # YOLOv8 model weights
│── road.jpg           # Sample input image
│── output.json        # Example output file
│── requirements.txt   # Dependencies
│── README.md          # Project documentation
│── venv/              # Virtual environment (ignored in .gitignore)
```

---
 How to Run

Run detection on an image:
py detect.py road.jpg


 Sample Output (JSON)

{
  "frame_id": 1,
  "timestamp": "2025-09-04T01:30:00",
  "detections": [
    {
      "label": "pothole",
      "confidence": 0.91,
      "bbox": [100, 200, 300, 400]
    }
  ]
}

---

## **✅ Requirements**
Create a virtual environment and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate      
pip install -r requirements.txt



