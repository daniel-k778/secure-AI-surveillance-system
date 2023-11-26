# Overview

This project centers around the development of an object detection application utilizing the YOLOv8 model. The primary aim of this project is to develop a robust and secure surveillance system empowered by AI-based object detection. The system is designed to provide real-time monitoring capabilities, ensuring the identification and tracking of objects within a given environment. The focus is on enhancing security through intelligent detection and authentication mechanisms. This project also features an intuitive interface, configuration settings, and secure access with user authentication.
## Features

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
## Navigating this repository
### Main Program Files

- `server.py`: Server script for handling user authentication.
- `login_gui.py`: Tkinter-based GUI for user login and account creation.
- `settings_gui.py`: Tkinter-based GUI for configuring object detection settings.
- `livedetection.py`: Script for live object detection using the YOLO model.

### Training Files

- `video_framesave.py`: This script extracts frames from videos in train_videos and saves them as images in the video_images folder. It captures one frame every 30 frames of the video, saving images with filenames based on the video filename and an incremental counter.
- `self_train.py`: This script uses a YOLO model to perform object detection on images in the video_images folder. Detected objects are saved with confidence scores. To use this script create a new folder called 'video_images' in the same directory and paste the images you want YOLO to annotate. Note that this script is intended to accelerate the training process. It is not recommended to use this script if you have a model trained on a weak dataset. Once the script is finished, look through the annotations and delete any false detections.
- `file_sync.py`: After refining the annotated images, paste them into the data_val/inference_box directory. Alongside, relocate the raw images used in the self_train.py script to the data_val/inference_im directory and the labels created to the data_val/inference_labels directory. This script synchronizes the labels and raw images based on the refined annotations. It removes any labels and raw images which do not correlate to the annotations. After running this script, feel free to delete the annotations and move the labels and raw images to your datasets folder.

## Acknowledgements

- YOLO model implemented using the Ultralytics library.
- MySQL database used for user authentication.

## License

This project is licensed under the [MIT License](LICENSE).
