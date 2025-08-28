import os
from pathlib import Path
import logging

# Configure logging to record actions in a log file
logging.basicConfig(filename='file_organizer.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Mapping of categories to file extensions
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml", ".webp"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"],
    "SOFTWARES": [".msi"]
}

# Reverse mapping of file extensions → category name
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


def organize_junk(target_directory):
    """
    Organizes files in the given target directory into categorized folders
    based on file extensions defined in DIRECTORIES.
    """

    target_path = Path(target_directory)

    # Iterate through each file in the directory
    for entry in target_path.iterdir():
        if entry.is_dir():  # Skip if it's already a directory
            continue

        file_path = Path(entry)
        file_format = file_path.suffix.lower()  # Get file extension

        # Check if extension belongs to known categories
        if file_format in FILE_FORMATS:
            # Create the category folder if it doesn't exist
            directory_path = target_path / FILE_FORMATS[file_format]
            directory_path.mkdir(exist_ok=True)

            try:
                # Move the file to its category folder
                file_path.rename(directory_path.joinpath(file_path.name))
                logging.info(f'Moved {file_path} to {directory_path}')
            except Exception as e:
                logging.error(f'Failed to move {file_path} to {directory_path}: {e}')

    # Attempt to remove any empty directories after organization
    for dir in target_path.iterdir():
        if dir.is_dir():
            try:
                os.rmdir(dir)  # Removes only if empty
                logging.info(f'Removed empty directory {dir}')
            except OSError:
                # Directory not empty, skip
                pass


if __name__ == "__main__":
    # By default, this script organizes the Downloads folder of the current user
    home_directory = Path.home()
    downloads_directory = home_directory / 'Downloads'  # Change here if needed to add other folders

    # You can change the path here if needed, e.g.:
    # downloads_directory = Path("C:/Users/YourName/Desktop/TestFolder")

    organize_junk(downloads_directory)
