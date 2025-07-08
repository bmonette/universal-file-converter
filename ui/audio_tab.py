import customtkinter as ctk
from tkinter import filedialog, messagebox
from audio_converter.converter import convert_files as convert_audio_files, supported_formats
import os
import traceback

# Global state
selected_files = []
selected_format = None
file_display = None

def create_audio_tab(parent):
    """
    Sets up the Audio Converter UI inside the given tab (parent frame).
    """
    global selected_format, file_display

    # Initialize format selection variable
    selected_format = ctk.StringVar(value="MP3")

    # Title
    title_label = ctk.CTkLabel(parent, text="🎵 Audio Converter", font=("Arial", 24, "bold"))
    title_label.pack(pady=20)

    # File picker button
    select_button = ctk.CTkButton(parent, text="📁 Select Audio Files", command=select_audio_files)
    select_button.pack(pady=10)

    # Format dropdown
    format_menu = ctk.CTkOptionMenu(
        parent,
        values=[fmt.upper() for fmt in supported_formats()],
        variable=selected_format
    )
    format_menu.pack(pady=10)

    # Textbox for file list + logs
    file_display = ctk.CTkTextbox(parent, height=100, width=500)
    file_display.pack(pady=10)
    file_display.insert("1.0", "No audio files selected.")
    file_display.configure(state="disabled")

    # Convert button
    convert_button = ctk.CTkButton(parent, text="🔄 Convert", command=handle_audio_conversion)
    convert_button.pack(pady=10)


def select_audio_files():
    """
    File dialog to select audio files.
    """
    global selected_files, file_display

    filetypes = [("Audio Files", "*.mp3 *.wav *.ogg *.flac *.aac *.wma")]
    selected_files = filedialog.askopenfilenames(
        title="Select audio file(s)",
        filetypes=filetypes
    )

    file_display.configure(state="normal")
    file_display.delete("1.0", "end")

    if selected_files:
        for file_path in selected_files:
            file_display.insert("end", file_path + "\n")
    else:
        file_display.insert("1.0", "No audio files selected.")

    file_display.configure(state="disabled")


def handle_audio_conversion():
    """
    Handles conversion when 'Convert' is clicked.
    """
    global selected_files, selected_format, file_display

    if not selected_files:
        messagebox.showwarning("No Files", "Please select audio files to convert.")
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
        success_count = convert_audio_files(
            file_paths=selected_files,
            target_format=target_format,
            output_folder=output_folder,
            log_callback=log_callback
        )
        file_display.insert("end", f"\nDone! {success_count} of {len(set(selected_files))} converted.\n")
    except Exception as e:
        file_display.insert("end", f"\n❌ Unexpected error: {e}\n")
        traceback.print_exc()

    file_display.configure(state="disabled")
