import os
import shutil


def main() -> bool:
    added_file = False
    image_dir = os.path.join(os.getcwd(), 'images')
    target_dir = os.path.join(
        'C:\\', 'Users', 'jatha', 'OneDrive - NTNU', '6. semester', 'TEP4100 Fluidmekanikk', 'Bilder'
    )

    target_files = [
        filename for filename in os.listdir(target_dir)
        if filename.endswith('.jpg') or filename.endswith('.png')
    ]

    image_files = [
        filename for filename in os.listdir(image_dir)
        if filename.endswith('.jpg') or filename.endswith('.png')
    ]

    for file in image_files:
        if file not in target_files:
            shutil.copy(os.path.join(image_dir, file), os.path.join(target_dir, file))
            added_file = True

    return added_file


if __name__ == "__main__":
    print(f"Added file: {main()}")
