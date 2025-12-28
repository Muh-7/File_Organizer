import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Python": [".py"],
    "Others": []
}


def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                target_dir = os.path.join(folder_path, folder)
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(target_dir, filename))
                moved = True
                break

        if not moved:
            target_dir = os.path.join(folder_path, "Others")
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(target_dir, filename))


if __name__ == "__main__":
    organize_folder("test_folder")
    print(" Folder organized successfully!")

