# Real-Time Face Detection & Counting Using Python and OpenCV

## Overview

A real-time computer vision application developed using Python and OpenCV. The application captures live video from a webcam, detects multiple faces using a pre-trained Haar Cascade classifier, draws bounding boxes around detected faces, and displays the number of detected faces in real time.

## Features

- **Live Webcam Capture:** Processes video directly from the webcam.
- **Face Detection:** Detects faces using a pre-trained Haar Cascade classifier.
- **Multiple Face Detection:** Detects multiple faces within the same video frame.
- **Bounding Boxes:** Draws green rectangles around detected faces.
- **Live Face Counter:** Displays the number of detected faces on the video window.
- **Keyboard Control:** Press `Q` to close the application.

## Technologies Used

- Python
- OpenCV
- Haar Cascade Classifier
- Computer Vision

## Project Structure

```text
real-time-face-detection/
│
├── face_detection.py
├── requirements.txt
├── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd real-time-face-detection
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

Make sure your webcam is connected and accessible.

Press `Q` to exit the application.

## How It Works

The application follows these steps:

1. **Model Loading:** Loads the pre-trained Haar Cascade frontal-face detection classifier.
2. **Video Capture:** Captures continuous frames from the webcam.
3. **Grayscale Conversion:** Converts each frame from BGR to grayscale.
4. **Face Detection:** Processes grayscale frames using `detectMultiScale()`.
5. **Coordinate Extraction:** Retrieves the position and dimensions of each detected face.
6. **Bounding Boxes:** Draws rectangles around detected faces using `cv2.rectangle()`.
7. **Face Counting:** Uses Python's `len()` function to count detected faces.
8. **Text Display:** Displays the live face count using `cv2.putText()`.

## Learning Outcomes

Through this project, I explored:

- Real-time video processing using OpenCV.
- Accessing webcam streams with `VideoCapture()`.
- Image processing and grayscale conversion.
- Understanding and implementing Haar Cascade classifiers.
- Extracting face coordinates using `detectMultiScale()`.
- Drawing bounding boxes on images.
- Displaying dynamic text on video frames.
- Building a continuous computer vision application.

## Future Improvements

- Experiment with different face detection parameters.
- Improve detection under different lighting conditions.
- Explore deep-learning-based face detection models.
- Add face recognition capabilities as a separate feature.

## Author

**Shahan Waheed**

BS Software Engineering Student

GitHub: [Shahan-Wheed728](https://github.com/Shahan-Wheed728)