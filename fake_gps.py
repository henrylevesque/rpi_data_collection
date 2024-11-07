import time
import pandas as pd
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

# Data storage
data = []

# Function to export data to Excel
def export_to_excel(data):
    df = pd.DataFrame(data, columns=['timestamp', 'latitude', 'longitude', 'image'])
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    df.to_excel(f'gps_image_data_{timestamp}.xlsx', index=False)
    print(f"Data saved to gps_image_data_{timestamp}.xlsx")

# Function to run the data collection for a specified duration
def run_data_collection(duration_minutes):
    duration_seconds = duration_minutes * 60
    start_time = time.time()
    
    # Create a new directory for images with the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    image_dir = f"images_{timestamp}"
    os.makedirs(image_dir, exist_ok=True)
    
    try:
        while time.time() - start_time < duration_seconds:
            # Get timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Use fixed GPS data
            latitude = 39.1339
            longitude = -84.4950

            # Store the data
            if latitude is not None and longitude is not None:
                # Capture image
                image_name = f"{image_dir}/image_{timestamp}.jpg"
                capture_image(image_name)

                print("ADD :: ", timestamp, " lat = ", latitude, " long = ", longitude, " image = ", image_name)
                data.append([timestamp, latitude, longitude, image_name])

            # Wait for the next interval
            time.sleep(5)

    except KeyboardInterrupt:
        print("Data collection stopped.")

    finally:
        # Export data to Excel when stopping the script
        export_to_excel(data)

# Example usage
if __name__ == "__main__":
    duration_minutes = 5  # Set the duration in minutes here
    run_data_collection(duration_minutes)