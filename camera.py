# Untested Code

import time
from datetime import datetime
import os
import subprocess

# Check if libcamera-still is available
if subprocess.run(["which", "libcamera-still"], capture_output=True, text=True).returncode != 0:
    raise EnvironmentError("libcamera-still command not found. Please ensure it is installed and configured correctly.")

# Function to capture an image using libcamera
def capture_image(image_path):
    try:
        subprocess.run(["libcamera-still", "-o", image_path, "--width", "1920", "--height", "1080"], check=True)
        print(f"Image saved to {image_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing image: {e}")

# Function to run the image capture for a specified duration and interval
def run_image_capture(duration_minutes, interval_seconds, folder_path):
    duration_seconds = duration_minutes * 60
    start_time = time.time()
    
    # Create the specified folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    try:
        while time.time() - start_time < duration_seconds:
            # Get timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Capture image
            image_name = f"{folder_path}/image_{timestamp}.jpg"
            capture_image(image_name)

            # Wait for the next interval
            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("Image capture stopped.")

# Usage
if __name__ == "__main__":
    duration_minutes = 5  # Set the duration in minutes here
    interval_seconds = 10  # Set the interval in seconds here
    folder_path = "captured_images"  # Set the folder path here
    run_image_capture(duration_minutes, interval_seconds, folder_path)