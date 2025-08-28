# File Organizer

A simple Python script to automatically organize files in a target directory (by default, the **Downloads** folder) into categorized subfolders such as **Images, Documents, Videos, Audio, Archives, PDFs, etc.**

This project is useful to keep your Downloads or any other folder clean and well-structured.

---

## Features

- Automatically detects file types based on extension.
- Moves files into categorized subfolders (e.g., `.jpg` → **IMAGES**, `.pdf` → **PDF**, `.mp3` → **AUDIO**).
- Removes empty directories after organizing.
- Generates a log file (`file_organizer.log`) to record all actions and errors.
- Easily configurable file extension categories.

---

## Categories and Extensions

Files are sorted into the following categories:

- **HTML** → `.html5`, `.html`, `.htm`, `.xhtml`, `.webp`  
- **IMAGES** → `.jpeg`, `.jpg`, `.tiff`, `.gif`, `.bmp`, `.png`, `.bpg`, `.svg`, `.heif`, `.psd`  
- **VIDEOS** → `.avi`, `.flv`, `.wmv`, `.mov`, `.mp4`, `.webm`, `.vob`, `.mng`, `.qt`, `.mpg`, `.mpeg`, `.3gp`  
- **DOCUMENTS** → `.docx`, `.doc`, `.pdf`, `.rtf`, `.ppt`, `.pptx`, `.xls`, `.xlsx`, `.odt`, etc.  
- **ARCHIVES** → `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.iso`, etc.  
- **AUDIO** → `.mp3`, `.wav`, `.ogg`, `.wma`, `.aac`, etc.  
- **PLAINTEXT** → `.txt`, `.in`, `.out`  
- **PDF** → `.pdf`  
- **PYTHON** → `.py`  
- **XML** → `.xml`  
- **EXE** → `.exe`  
- **SHELL** → `.sh`  
- **SOFTWARES** → `.msi`  

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RasKumar-m/FileOrganizer.git
   cd FileOrganizer
````


3. No external libraries are required beyond the Python standard library.

---

## Usage

1. Run the script:

   ```bash
   python file_organizer.py
   ```

2. By default, it organizes the **Downloads** folder of the current user:

   ```
   C:/Users/<YourUsername>/Downloads  (Windows)
   /home/<YourUsername>/Downloads     (Linux/Mac)
   ```

3. To organize a custom directory, edit the script:

   ```python
   downloads_directory = Path("C:/Users/YourName/Desktop/TestFolder")
   organize_junk(downloads_directory)
   ```

---


---

## Example Output

Before running:

```
Downloads/
  report.pdf
  photo.jpg
  video.mp4
  notes.txt
```

After running:

```
Downloads/
  PDF/
    report.pdf
  IMAGES/
    photo.jpg
  VIDEOS/
    video.mp4
  PLAINTEXT/
    notes.txt
```

---

## Requirements

* Python 3.7+
* Works on **Windows**, **Linux**, and **MacOS**

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

