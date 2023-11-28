from tkinter import messagebox
from ultralytics import YOLO
import cv2
import math
import sys
from tkinter import *
from datetime import datetime

# Create a Tkinter window for logs
log_window = Tk()
log_window.title("AI Confidence Logs")
log_window.resizable(False, False)

# Create a text widget to display logs
log_text = Text(log_window, height=10, width=50)
log_text.pack()

# Function to export data to a text document
def export_to_text():
    try:
        logs = log_text.get("1.0", END)

        with open('detection_logs.txt', 'w') as file:
            file.write(logs)

        messagebox.showinfo('Export Successful', 'Data exported to detection_logs.txt')

    except Exception as e:
        messagebox.showerror('Error', f"An error occurred during export: {str(e)}")

# Create buttons to export data
export_text_button = Button(log_window, text="Export to Text", command=export_to_text, font=('Arial', 12, 'bold'), bg='white', fg='gray14', padx=10, pady=5, cursor='hand2', relief=FLAT)
export_text_button.pack(side=BOTTOM, fill=BOTH, expand=True)


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

    # Start time for logging
    start_time = datetime.now()

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        if not ret:
            messagebox.showerror('Error', "Can't read frame... Exiting... ")
            break
        
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

                # Log instances with real-world date and time
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_text.insert(END, f'{timestamp}: Class: {classNames[cls]} Confidence: %{conf:.0f}\n')
                
        cv2.imshow('Video Stream', frame)
        log_window.update()

        # Quit key
        if cv2.waitKey(25) & 0xFF == ord(quit_key):
            break

except Exception as e:
    messagebox.showerror('Error', f"An error occurred: {str(e)}")

finally:
    cap.release()
    log_window.destroy()

log_window.mainloop()
