# Pothole Detection using YOLOv8

##  Description
This project detects potholes from road images using the YOLOv8 model and outputs the results in a structured **JSON format**.


##  Features
- Detects potholes in road images.
- Outputs results with:
  - Frame ID
  - Timestamp
  - Detection details (class, confidence, bounding box coordinates)
- Saves results to `output.json`.

---

##  Installation
Clone this repository and install the dependencies:

```bash
git clone https://github.com/Sarancoder4real/pothole-detection.git
cd pothole-detection
pip install -r requirements.txt
