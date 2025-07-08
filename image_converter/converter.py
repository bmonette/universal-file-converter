from PIL import Image
import os
import traceback

def convert_images(file_paths, target_format, output_folder, log_callback=None):
    """
    Convert a list of image files to the target format and save to output folder.

    :param file_paths: list of image file paths
    :param target_format: string format like 'png', 'jpg', etc.
    :param output_folder: output folder path
    :param log_callback: optional function to log messages (e.g., to GUI)
    :return: number of successful conversions
    """
    success_count = 0
    pillow_format = "JPEG" if target_format.lower() == "jpg" else target_format.upper()
    unique_files = list(set(file_paths))  # Deduplicate

    for file_path in unique_files:
        try:
            with Image.open(file_path) as img:
                base_name = os.path.splitext(os.path.basename(file_path))[0]
                original_ext = os.path.splitext(file_path)[1].lstrip(".").upper()
                new_filename = f"{base_name}.{target_format.lower()}"
                output_path = os.path.join(output_folder, new_filename)

                rgb_img = img.convert("RGB") if pillow_format == "JPEG" else img
                rgb_img.save(output_path, format=pillow_format)

                msg = f"{base_name}.{original_ext.lower()} → {new_filename} ✅ Converted Successfully"
                if log_callback:
                    log_callback(msg)
                success_count += 1

        except Exception as e:
            msg = f"{os.path.basename(file_path)} → {new_filename} ❌ Failed to Convert! ({e})"
            if log_callback:
                log_callback(msg)
            traceback.print_exc()

    return success_count
