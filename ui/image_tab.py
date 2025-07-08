import customtkinter as ctk
from tkinter import filedialog, messagebox
from image_converter.converter import convert_images as convert_image_files
import os
import traceback

# Global state for selected files
selected_files = []

# This will be initialized in create_image_tab()
selected_format = None
file_display = None


def create_image_tab(parent):
    """
    Sets up the Image Converter UI inside the given tab (parent frame).
    """
    global selected_format, file_display

    # Initialize format selection variable (must be done after CTk root exists)
    selected_format = ctk.StringVar(value="PNG")

    # Title label
    title_label = ctk.CTkLabel(parent, text="🖼️ Image Converter", font=("Arial", 24, "bold"))
    title_label.pack(pady=20)

    # Select Images Button
    select_button = ctk.CTkButton(parent, text="📁 Select Images", command=select_images)
    select_button.pack(pady=10)

    # Supported output formats
    format_options = ["JPG", "PNG", "WEBP", "BMP", "GIF"]

    # Format dropdown menu
    format_menu = ctk.CTkOptionMenu(
        parent,
        values=format_options,
        variable=selected_format
    )
    format_menu.pack(pady=10)

    # File display box (read-only)
    file_display = ctk.CTkTextbox(parent, height=100, width=500)
    file_display.pack(pady=10)
    file_display.insert("1.0", "No images selected.")
    file_display.configure(state="disabled")

    # Convert Button
    convert_button = ctk.CTkButton(
        parent,
        text="🔄 Convert",
        command=handle_conversion
    )
    convert_button.pack(pady=10)


def select_images():
    """
    Opens a file dialog to select image files and displays them in the textbox.
    """
    global selected_files, file_display

    filetypes = [("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.webp")]
    selected_files = filedialog.askopenfilenames(
        title="Select image(s)",
        filetypes=filetypes
    )

    file_display.configure(state="normal")
    file_display.delete("1.0", "end")

    if selected_files:
        for file_path in selected_files:
            file_display.insert("end", file_path + "\n")
    else:
        file_display.insert("1.0", "No images selected.")

    file_display.configure(state="disabled")


def handle_conversion():
    """
    Handles conversion logic when 'Convert' is clicked.
    """
    global selected_files, selected_format, file_display

    if not selected_files:
        messagebox.showwarning("No Images", "Please select image files to convert.")
        return

    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        return

    target_format = selected_format.get().lower()

    file_display.configure(state="normal")
    file_display.insert("end", f"\n--- Converting to {target_format.upper()} ---\n")

    def log_callback(message):
        file_display.insert("end", message + "\n")
        file_display.see("end")

    try:
        success_count = convert_image_files(
            file_paths=selected_files,
            target_format=target_format,
            output_folder=output_folder,
            log_callback=log_callback
        )
        file_display.insert(
            "end",
            f"\nDone! {success_count} of {len(set(selected_files))} converted.\n"
        )
    except Exception as e:
        file_display.insert("end", f"\n❌ Unexpected error: {e}\n")
        traceback.print_exc()

    file_display.configure(state="disabled")
