import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os
import traceback
from ui.image_tab import create_image_tab
from ui.audio_tab import create_audio_tab
# from ui.video_tab import create_video_tab
# from ui.font_tab import create_font_tab
# from ui.spreadsheet_tab import create_spreadsheet_tab
# from ui.document_tab import create_document_tab
# from ui.ebook_tab import create_ebook_tab
# from ui.archive_tab import create_archive_tab


# Appearance settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Create main window
app = ctk.CTk()
app.iconbitmap("assets/icon.ico")
app.title("Universal File Converter")
app.geometry("700x500")
app.resizable(False, False)

# Create tabbed interface
tabview = ctk.CTkTabview(app, width=680, height=460)
tabview.pack(padx=10, pady=10)
tabview.set("Images")  # Sets the default active tab


# Add tabs
image_tab = tabview.add("Images")
audio_tab = tabview.add("Audio")
# video_tab = tabview.add("Video")
# font_tab = tabview.add("Font")
# spreadsheet_tab = tabview.add("Spreadsheet")
# document_tab = tabview.add("Documents")
# ebook_tab = tabview.add("Ebooks")
# archive_tab = tabview.add("Archives")


# Initialize each tab UI
create_image_tab(image_tab)
create_audio_tab(audio_tab)
# create_video_tab(video_tab)
# create_font_tab(font_tab)
# create_spreadsheet_tab(spreadsheet_tab)
# create_document_tab(document_tab)
# create_ebook_tab(ebook_tab)
# create_archive_tab(archive_tab)

# Run the app
app.mainloop()
