import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def sort_photos(source_dirs, destination):
    """
    Sorts photos and videos from multiple source directories into a selected destination.
    
    Args:
    - source_dirs (list of str): List of source folder paths containing photos and videos.
    - destination (str): Destination folder where sorted files will be moved.

    This function organizes files from the source directories into "Photos" and "Videos"
    subfolders within the destination directory, based on file extensions.
    """
    # Check if source and destination folders are selected
    if not source_dirs or not destination:
        messagebox.showerror("Error", "Select source and destination folders!")
        return

    # Define file type categories for photos and videos
    photo_extensions = {".jpg", ".jpeg", ".png", ".gif", ".tiff", ".bmp", ".heic", ".raw"}
    video_extensions = {".mp4", ".mov", ".avi", ".mkv", ".wmv"}

    # Create subdirectories for photos and videos in the destination folder
    photo_dir = os.path.join(destination, "Photos")
    video_dir = os.path.join(destination, "Videos")

    os.makedirs(photo_dir, exist_ok=True)
    os.makedirs(video_dir, exist_ok=True)

    # Process each source folder and move files to appropriate directories
    for directory in source_dirs:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            # If it's a file, move it to the appropriate subdirectory based on its extension
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1].lower()
                if ext in photo_extensions:
                    shutil.move(file_path, os.path.join(photo_dir, filename))
                elif ext in video_extensions:
                    shutil.move(file_path, os.path.join(video_dir, filename))

    # Show a success message once sorting is done
    messagebox.showinfo("Success", "Photos and videos have been sorted!")


def browse_source_folders():
    """
    Opens a file dialog to allow the user to select multiple source folders.
    
    This function adds the selected folder paths to the `source_dirs` list and updates
    the UI label to reflect the selected directories.
    """
    folders = filedialog.askdirectory()  # Open folder selection dialog
    if folders:
        source_dirs.append(folders)  # Add the selected folder to the list
        source_label.config(text="\n".join(source_dirs))  # Update the UI to show selected folders


def browse_destination_folder():
    """
    Opens a file dialog to allow the user to select the destination folder.
    
    This function updates the `destination_folder` variable with the selected folder path.
    """
    folder_selected = filedialog.askdirectory()  # Open folder selection dialog
    destination_folder.set(folder_selected)  # Update the destination folder path


def start_sorting():
    """
    Starts the sorting process by calling the `sort_photos` function with the selected folders.
    """
    sort_photos(source_dirs, destination_folder.get())  # Call the sorting function


# Create the main Tkinter window
root = tk.Tk()
root.title("Photo & Video Organizer")
root.geometry("500x300")

# Source Folders Section
source_dirs = []  # List to hold selected source folders
tk.Label(root, text="Select Source Folders:").pack(pady=5)
tk.Button(root, text="Add Source Folder", command=browse_source_folders).pack(pady=5)
source_label = tk.Label(root, text="No folders selected", fg="gray")
source_label.pack(pady=5)

# Destination Folder Section
destination_folder = tk.StringVar()  # Variable to store selected destination folder
tk.Label(root, text="Select Destination Folder:").pack(pady=5)
tk.Button(root, text="Choose Destination", command=browse_destination_folder).pack(pady=5)
destination_label = tk.Label(root, textvariable=destination_folder, fg="gray")
destination_label.pack(pady=5)

# Sort Button
tk.Button(root, text="Sort Photos", command=start_sorting, bg="green", fg="white").pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

