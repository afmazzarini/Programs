import tkinter as tk
from tkinter import filedialog
import os

def select_folder():
    # Create a hidden root window
    root = tk.Tk()
    root.withdraw() # Prevents the main Tkinter window from appearing
    
    # Open the directory selection dialog
    folder_path = filedialog.askdirectory(
        title="Select a Folder",
        initialdir=os.getcwd() # Optional: sets the initial directory
    )
    
    # Destroy the hidden root window after selection
    root.destroy()

    if folder_path:
        print(f"Selected folder: {folder_path}")
        return folder_path
    else:
        print("Folder selection cancelled.")
        return None

# Example usage:
selected_folder = select_folder()
# You can now use the 'selected_folder' variable in your program