import cv2
import time
import os


folder_path = 'train_videos'
def main():
    try:
        files = os.listdir(folder_path)
        video_extensions = ['.mp4', '.avi', '.mkv']
        video_files = [file for file in files if any(file.lower().endswith(ext) for ext in video_extensions)]

        for video_file in video_files:
            video_path = os.path.join(folder_path, video_file)
            print(f"Processing video: {video_path}")
            cap = cv2.VideoCapture(video_path)

            if not cap.isOpened():
                print("Error: Could not open file.")
                return
            output_folder = 'video_images'
            video_filename = os.path.splitext(os.path.basename(video_file))[0]
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
                print(f"Folder '{output_folder}' created.")

            try:
                print("Press 'q' to quit.")
                count = 0
                frame_counter = 0

                while True:
                    ret, frame = cap.read()

                    if not ret:
                        print("End of video.")
                        break
                    cv2.imshow('Frame', frame)

                    if frame_counter % 30 == 0:
                        filename = os.path.join(output_folder, f'{video_filename}_image_{count}.png')
                        cv2.imwrite(filename, frame)
                        print(f"Saved: {filename}")
                        count += 1
                    frame_counter += 1

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            finally:
                cap.release()
                cv2.destroyAllWindows()


    except FileNotFoundError:
        print(f"The specified folder '{folder_path}' does not exist.")
    except PermissionError:
        print(f"You don't have permission to access the folder '{folder_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()