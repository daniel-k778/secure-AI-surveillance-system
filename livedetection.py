from tkinter import messagebox
from ultralytics import YOLO
import cv2
import math
import cvzone
import sys


try:
    # Check if command line arguments are provided
    if len(sys.argv) >= 4:
        confidence = float(sys.argv[1])
        rtsp_url = sys.argv[2]
        quit_key = sys.argv[3]
        print(f"Using confidence: {confidence}, RTSP URL: {rtsp_url}, Quit Key: {quit_key}")
    else:
        raise ValueError("Usage: python livedetection.py <confidence> <rtsp_url> <quit_key>")
    
    # YOLO model and video capture setup
    classNames = ['Person']
    model = YOLO('models/best.pt')
    video_path = f'{rtsp_url}'

    cap = cv2.VideoCapture(video_path)

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        if not ret:
            # Show an error message if unable to read a frame
            messagebox.showerror('Error', "Can't read frame... Exiting... ")
            exit()
        
        # YOLO object detection and tracking
        results = model.track(frame, persist=True, stream=True, conf=confidence, verbose=False)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Draw bounding box around detected person
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

                # Display class and confidence on the frame
                conf = (math.ceil((box.conf[0] * 100)) / 100) * 100
                cls = int(box.cls[0])
                cvzone.putTextRect(
                    frame,
                    f'Class: {classNames[cls]} Conf: %{conf:.0f}',
                    (max(0, x1), max(35, y1)),
                    scale=0.4,
                    thickness=1,
                    colorT=(255, 255, 255),
                    colorR=(0, 0, 0),
                    font=cv2.QT_FONT_NORMAL,
                    border=1,
                    colorB=(0, 0, 0)
                )
                
        # Display the frame with bounding boxes
        cv2.imshow('Video Stream', frame)

        # Break the loop if the quit key is pressed
        if cv2.waitKey(25) & 0xFF == ord(quit_key):
            break

except Exception as e:
    messagebox.showerror('Error', f"An error occurred: {str(e)}")