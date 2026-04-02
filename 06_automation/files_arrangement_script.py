import os
import shutil

source_dir = r"C:\Users\Tony\Downloads"

target_dir_img = r"C:\Users\Tony\Downloads\Images Storage"
target_dir_pdf = r"C:\Users\Tony\Downloads\PDF Storage"
target_dir_doc = r"C:\Users\Tony\Downloads\DOC Storage"

# Mapping: destination folder → file extensions
extensions = {
    target_dir_img: (".png", ".jpeg", ".jpg"),
    target_dir_pdf: (".pdf",),
    target_dir_doc: (".doc", ".txt", ".rtf", ".docx")
}

files = os.listdir(source_dir)

for file in files:
    src = os.path.join(source_dir, file)

    # Skip folders
    if not os.path.isfile(src):
        continue

    for target_folder, exts in extensions.items():

        if file.lower().endswith(exts):

            # Create folder if it doesn't exist
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            dst = os.path.join(target_folder, file)

            shutil.move(src, dst)

            print(f"Moved {file} → {target_folder}")

            break  # stop checking other extensions once moved


















