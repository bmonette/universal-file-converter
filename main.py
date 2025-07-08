import customtkinter as ctk
from image_converter.converter import convert_images as convert_image_files
from PIL import Image
from tkinter import messagebox
from tkinter import filedialog
import os
import traceback


# Appearance settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Main app window
app = ctk.CTk()
app.iconbitmap("assets/icon.ico")
app.title("Universal File Converter - Image Module")
app.geometry("600x400")
app.resizable(False, False)

# Global variable to store selected files
selected_files = []


# Function to select images
def select_images():
    global selected_files
    filetypes = [("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.webp")]
    selected_files = filedialog.askopenfilenames(
        title="Select image(s)",
        filetypes=filetypes
    )
    if selected_files:
        file_display.configure(state="normal")
        file_display.delete("1.0", "end")  # Clear previous content
        for file_path in selected_files:
            file_display.insert("end", file_path + "\n")
        file_display.configure(state="disabled")
    else:
        file_display.configure(state="normal")
        file_display.delete("1.0", "end")
        file_display.insert("1.0", "No images selected.")
        file_display.configure(state="disabled")


def handle_conversion():
    if not selected_files:
        messagebox.showwarning("No Images", "Please select image files to convert.")
        return

    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        return

    target_format = selected_format.get().lower()

    # Prepare textbox
    file_display.configure(state="normal")
    file_display.insert("end", f"\n--- Converting to {target_format.upper()} ---\n")

    # Log function that updates the textbox
    def log_callback(message):
        file_display.insert("end", message + "\n")
        file_display.see("end")

    # Use the new module logic
    success_count = convert_image_files(
        file_paths=selected_files,
        target_format=target_format,
        output_folder=output_folder,
        log_callback=log_callback
    )

    file_display.insert("end", f"\nDone! {success_count} of {len(set(selected_files))} converted.\n")
    file_display.configure(state="disabled")


# Title
title_label = ctk.CTkLabel(app, text="🖼️ Image Converter", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# Select Images Button
select_button = ctk.CTkButton(app, text="📁 Select Images", command=select_images)
select_button.pack(pady=10)

# Supported output formats
format_options = ["JPG", "PNG", "WEBP", "BMP", "GIF"]
selected_format = ctk.StringVar(value="PNG")  # Default format

# Format dropdown menu
format_menu = ctk.CTkOptionMenu(
    app,
    values=format_options,
    variable=selected_format
)
format_menu.pack(pady=10)

# Textbox to display selected file paths
file_display = ctk.CTkTextbox(app, height=100, width=500)
file_display.pack(pady=10)
file_display.insert("1.0", "No images selected.")
file_display.configure(state="disabled")  # Make it read-only

convert_button = ctk.CTkButton(app, text="🔄 Convert", command=handle_conversion)
convert_button.pack(pady=10)

# Run the app
app.mainloop()
