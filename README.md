# Photo & Video Organizer

This Python application allows users to organize their photos and videos by automatically sorting them into dedicated folders for Photos and Videos. It utilizes the Tkinter library for a simple, easy-to-use graphical interface, making it accessible for both beginners and advanced users.

<img width="496" alt="project_screenshot" src="https://github.com/user-attachments/assets/92d14536-102b-4c14-aea7-7fd1c40814f9" />

## Features
- **Multi-folder support**: Select multiple source folders to sort photos and videos.
- **File type sorting**: Automatically categorizes files into `Photos` and `Videos` based on extensions.
- **GUI Interface**: User-friendly interface built with Tkinter.
- **Customizable destination**: Choose where the organized files should be saved.

## Supported File Extensions
- **Photos**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.tiff`, `.bmp`, `.heic`, `.raw`
- **Videos**: `.mp4`, `.mov`, `.avi`, `.mkv`, `.wmv`

## Installation

### Prerequisites
- Python 3.x
- Tkinter (usually comes pre-installed with Python)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/CarsonL15/photo-video-organizer.git
   
2. Navigate to the project folder:
   ```bash
   cd photo-organizer-gui

3. Set up a virtual environment (optional but recommended):
- On Mac:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
- On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate

4. Install the required dependencies:
   ```bash
   pip install tkinter

5. Run the script
   ```bash
   python photo_organizer_gui.py
