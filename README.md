```markdown
# Object Detection Application

## Overview

This repository contains a simple object detection application using YOLO (You Only Look Once) model, implemented in
Python with the help of the Ultralytics library. The application allows users to log in, configure settings, and
perform live object detection using a provided RTSP URL.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

1. Run the server:

```bash
python server.py
```

2. Run the login GUI:

```bash
python login_gui.py
```

3. Follow the instructions on the login GUI to log in and configure settings.

4. Load the live detection stream from the settings GUI.

5. Perform object detection based on the provided RTSP URL.
## Navigating this repository
### Main Program Files

- `server.py`: Server script for handling user authentication.
- `login_gui.py`: Tkinter-based GUI for user login and account creation.
- `settings_gui.py`: Tkinter-based GUI for configuring object detection settings.
- `livedetection.py`: Script for live object detection using the YOLO model.

### Training Files

- `self_train.py`: This script uses a YOLO model to perform object detection on images in the video_images folder. Detected objects are saved with confidence scores, and annotated images are stored with the prefix inference_.
- `file_sync.py`: This script synchronizes files between folder2 and folder3 based on the files present in folder1. It removes files from folder2 without corresponding names in folder1 and moves files from folder3 to folder4 if their names are not in folder1.
- `video_framesave.py`: This script extracts frames from videos in train_videos and saves them as images in video_images. It captures one frame every 30 frames of the video, saving images with filenames based on the video filename and an incremental counter.

## Acknowledgements

- YOLO model implemented using the Ultralytics library.
- MySQL database used for user authentication.

## License

This project is licensed under the [MIT License](LICENSE).
```
