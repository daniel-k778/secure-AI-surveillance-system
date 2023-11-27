import os
import shutil

# Synchronize folders based on filenames in folder1
def synchronize_folders(folder1, folder2, folder3, folder4):
    # Extract filenames (without extension) from folder1
    filenames_folder1 = set([os.path.splitext(file)[0] for file in os.listdir(folder1)])

    # Remove files in folder2 that do not have corresponding filenames in folder1
    for file2 in os.listdir(folder2):
        filename2, ext2 = os.path.splitext(file2)
        if filename2 not in filenames_folder1:
            os.remove(os.path.join(folder2, file2))

    # Move files from folder3 to folder4 if their filenames are not in folder1
    for file3 in os.listdir(folder3):
        filename3, ext3 = os.path.splitext(file3)
        if filename3 not in filenames_folder1:
            source_path = os.path.join(folder3, file3)
            destination_path = os.path.join(folder4, file3)
            shutil.move(source_path, destination_path)

if __name__ == "__main__":
    folder1_path = 'data_val/inference_box'
    folder2_path = 'data_val/inference_labels'
    folder3_path = 'data_val/inference_im'
    folder4_path = 'data_val/not_inference'

    try:
        if not os.path.exists(folder4_path):
            os.makedirs(folder4_path)
            print(f"Folder '{folder4_path}' created.")

        # Synchronize the specified folders
        synchronize_folders(folder1_path, folder2_path, folder3_path, folder4_path)
        print("Folders synchronized successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")