import os
from ultralytics import YOLO


model = YOLO('models/best.pt')
folder_path = 'video_images'

def main():
    try:
        files = os.listdir(folder_path)
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        image_files = [file for file in files if any(file.lower().endswith(ext) for ext in image_extensions)]

        # Process each image file in the folder
        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            print(f"Processing image: {image_path}")
            image_filename = os.path.splitext(os.path.basename(image_file))[0]
            model.predict(f'{image_path}', save=True, imgsz=1280, conf=0.4, save_txt=True)
            print(f"Saved: infrence_{image_filename}")

    except FileNotFoundError:
         print(f"The specified folder '{folder_path}' does not exist.")
    except PermissionError:
        print(f"You don't have permission to access the folder '{folder_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()