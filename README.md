Real-Time Object Detection & Motion Tracking using OpenCV
📌 Overview

This project implements real-time object detection and motion tracking using OpenCV in Python.

The system detects moving objects from a live webcam feed and tracks their movement across frames using contour detection and frame differencing techniques.

It demonstrates core computer vision concepts like background subtraction, contour detection, and real-time tracking.

🚀 Features

✅ Real-time motion detection

✅ Object contour detection

✅ Bounding box tracking

✅ Background subtraction

✅ Noise reduction using Gaussian blur

✅ Lightweight and fast processing

🛠️ Tech Stack

Python

OpenCV

NumPy

1️⃣ Clone the Repository
git clone https://github.com/your-username/object-motion-tracking.git
cd object-motion-tracking
2️⃣ Install Dependencies
pip install -r requirements.txt

Or manually:

pip install opencv-python numpy
▶️ How to Run
python motion_tracking.py

Webcam will start

Moving objects will be detected

Bounding boxes will appear around motion areas

Press Q to exit

🧠 How It Works

Webcam captures continuous frames

Frames are converted to grayscale

Gaussian blur reduces noise

Frame differencing detects motion

Thresholding isolates moving regions

Contours are detected

Bounding boxes track objects

📸 Demo

(Add screenshots or demo GIF here)

Example Output:

Green bounding boxes around moving objects

Real-time motion detection

Smooth object tracking

📈 Applications

🛡️ CCTV Surveillance Systems

🚗 Vehicle Detection

🏠 Smart Home Security

🤖 Robotics Vision Systems

🎮 Motion-Based Interaction

🔮 Future Improvements

Object classification using YOLO

Multi-object tracking

Deep learning-based detection

Speed estimation

Alert notification system

📚 Learning Outcomes

Frame differencing techniques

Contour detection logic

Real-time video processing

Noise handling in CV

Motion detection algorithms

👨‍💻 Author

Prashanth
BCA Student | AI & Computer Vision Enthusiast
Building practical vision-based systems
