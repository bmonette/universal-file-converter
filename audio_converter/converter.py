from pydub import AudioSegment
import os
import traceback

# Map extensions to pydub-supported formats
SUPPORTED_FORMATS = ["mp3", "wav", "flac", "ogg", "aac", "wma"]

def convert_files(file_paths, target_format, output_folder, log_callback=None):
    """
    Convert audio files to target format using ffmpeg via pydub.
    """
    success_count = 0
    target_format = target_format.lower()
    unique_files = list(set(file_paths))

    if target_format not in SUPPORTED_FORMATS:
        if log_callback:
            log_callback(f"❌ Unsupported format: {target_format}")
        return 0

    for file_path in unique_files:
        try:
            file_ext = os.path.splitext(file_path)[1].lstrip(".").lower()
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            new_filename = f"{file_name}.{target_format}"
            output_path = os.path.join(output_folder, new_filename)

            # Load the audio file
            audio = AudioSegment.from_file(file_path, format=file_ext)
            audio.export(output_path, format=target_format)

            if log_callback:
                log_callback(f"{file_name}.{file_ext} → {new_filename} ✅ Converted Successfully")
            success_count += 1

        except Exception as e:
            if log_callback:
                log_callback(f"{os.path.basename(file_path)} ❌ Failed to Convert! ({e})")
            traceback.print_exc()

    return success_count


def supported_formats():
    return SUPPORTED_FORMATS
