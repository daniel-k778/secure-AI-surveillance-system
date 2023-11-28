# Overview

This project centers around the development of an object detection application utilizing the YOLOv8 model. The primary aim of this project is to develop a robust and secure surveillance system empowered by AI-based object detection. The system is designed to provide real-time monitoring capabilities, ensuring the identification and tracking of objects within a given environment. The focus is on enhancing security through intelligent detection and authentication mechanisms. This project also features an intuitive interface, configuration settings, and secure access with user authentication.
## Features

* **Object Detection**: Utilizes the swift and precise operational capabilities of the YOLOv8 algorithm for object detection in video streams.
* **Secure Login System**: A well-designed and secure login system that establishes a socket connection with the server, sends encrypted user credentials, and receives authentication results. User passwords are hashed using SHA-256 before being transmitted or stored in the database, enhancing security.
* **GUI Design**: Presents a user-friendly login interface with fields for username and password. Users can also navigate to the account creation view or recover a forgotten password.
* **Configuration Panel**: Users can finely adjust the confidence level for object detection using a slider. The confidence slider allows a dynamic range from 0% to 100%, providing control over the sensitivity of the detection algorithm. The panel also features an entry field for an RTSP URL as well as a drop-down menu for choosing a key to quit the program.
* **Detection Logs**: The Detection Logs feature in this script serves to provide a detailed and timestamped record of object detection instances during the real-time detection process. This feature enhances user visibility and facilitates post-analysis by logging key information for each detected object. Users can export these logs and use them to pin point the exact instance when a specific object was detected.
* **Wireless Compatibility**: The live detection system boasts wireless compatibility, primarily facilitated through the integration of RTSP (Real-Time Streaming Protocol) URL configuration. This feature provides users with several advantages such as remote deployment and real-time monitoring.
* **MySQL Database**: The login system interacts with a MySQL database to check for existing usernames and store new user data securely using SHA-256 encryption. The server utilizes MySQL connection pooling for efficient and scalable database connections.
* **Error Handling**: The system incorporates error handling for various scenarios, including connection errors and database access issues.

## Usage
1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Run the server:

```bash
python server.py
```

3. Run the login GUI:

```bash
python login_gui.py
```

4. Follow the instructions on the login GUI to log in and configure settings.

5. Enter the RTSP URL for ip camera or enter the folder path for a video.

6. Load the live detection stream from the settings GUI by pressing 'LOAD'

7. Perform object detection based on the provided RTSP URL.

8. To ensure the program runs as expected, modify the MySQL host, user, password, and database based on your personal database or create a free one at sql3.freesqldatabase.com. Alongside this, ensure that the subprocess.Popen line in the file `settings_gui.py` contains the correct path for your virtual environment.
## Navigating this repository
### Main Program Files

- `server.py`: Server script for handling user authentication.
- `login_gui.py`: Tkinter-based GUI for user login and account creation.
- `settings_gui.py`: Tkinter-based GUI for configuring object detection settings.
- `livedetection.py`: Script for live object detection using the YOLO model.

### Training Files

- `video_framesave.py`: This script extracts frames from videos in train_videos and saves them as images in the video_images folder. It captures one frame every 30 frames of the video, saving images with filenames based on the video filename and an incremental counter.
- `self_train.py`: This script uses a YOLO model to perform object detection on images in the video_images folder. Detected objects are saved with confidence scores. To use this script paste the images you want YOLO to annotate in the video_images folder. Note that this script is intended to accelerate the training process. It is not recommended to use this script if you have a model trained on a weak dataset. Once the script is finished, look through the annotations and delete any false detections.
- `file_sync.py`: After refining the annotated images, paste them into the data_val/inference_box directory. Alongside, relocate the raw images used in the self_train.py script to the data_val/inference_im directory and the labels created to the data_val/inference_labels directory. This script synchronizes the labels and raw images based on the refined annotations. It removes any labels and raw images which do not correlate to the annotations. After running this script, feel free to delete the annotations and move the labels and raw images to your datasets folder. The script also moves all the false detections to the data_val/not_inference directory. The images in this directory can be self anotated and added to the dataset to further strengthen the model.

## Other

- Find my dataset and Google Collab notebook here: https://drive.google.com/drive/folders/1rQ1QxwT1W-DWCtMU2SG7cg2bSyBjZOMO?usp=sharing
- 
## Acknowledgements

- YOLO model implemented using the Ultralytics library.
- MySQL database used for user authentication.
