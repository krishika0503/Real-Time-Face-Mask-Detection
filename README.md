# Real-Time Face Mask Detection System (Live Camera)

A real-time computer vision project that detects human faces from a live webcam feed and classifies whether a person is **wearing a face mask** or **not wearing a face mask** using Python and OpenCV.

## Author & Internship Details

- **Name:** Krishika  
- **Internship Organization:** Naviotech  
- **Project Type:** Internship Project  
- **Email:** krxshxka@gmail.com  

## Project Overview

The **Real-Time Face Mask Detection System** demonstrates the practical application of **computer vision** and **real-time video processing**.  

The system captures live video from a webcam, detects human faces, and determines whether each detected face is wearing a mask or not.

This project is designed for academic evaluation and provides a clear understanding of real-time object detection using classical machine learning techniques.

## Project Objectives

- Detect human faces from a live camera feed  
- Classify detected faces as **MASK** or **NO MASK**  
- Demonstrate real-time video processing using OpenCV  
- Build a simple, efficient, and explainable system

 ## Technologies Used

- **Python 3**  
- **OpenCV**  
- **NumPy**  

## System Architecture & Working

The system operates in real time using the following steps:

### Face Detection

- Uses a **Haar Cascade Classifier** provided by OpenCV  
- Haar Cascade is a classical machine learning-based object detection technique  
- Detected faces are enclosed within bounding rectangles

 ### Mask Detection Logic

- The system analyzes the **lower half of the detected face**  
- Pixel intensity of the region is examined  
- If the region appears darker (indicating a mask), the face is classified as **MASK**  
- Otherwise, it is classified as **NO MASK**  

### Real-Time Processing

- Webcam feed is processed frame-by-frame  
- Detection and classification occur instantly  
- Results are displayed live on the screen

## How to Run the Project

### Prerequisites

- Python 3 installed  
- Required libraries:
  - OpenCV
  - NumPy  

Install dependencies using:
```bash
pip install opencv-python numpy

📌 Steps to Execute
Clone or download the repository
Ensure the Haar Cascade XML file is present
Run the script:
python live_camera.py
The webcam will open and display real-time detection results 
 
