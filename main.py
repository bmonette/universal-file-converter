import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os
import traceback

# Tab imports
from ui.image_tab import create_image_tab
from ui.audio_tab import create_audio_tab

# Appearance settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Create main window
app = ctk.CTk()
app.iconbitmap("assets/icon.ico")
app.title("Universal File Converter")
app.geometry("600x400")
app.resizable(False, False)

# Create tabbed interface
tabview = ctk.CTkTabview(app, width=580, height=360)
tabview.pack(padx=10, pady=10)

# Add tabs
image_tab = tabview.add("Images")
audio_tab = tabview.add("Audio")

# Initialize each tab UI
create_image_tab(image_tab)
create_audio_tab(audio_tab)

# Run the app
app.mainloop()
