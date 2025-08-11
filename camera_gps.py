import time
import serial
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

# Setup GPS communication
def initialize_gps():
    try:
        gps_serial = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)
        print("GPS port opened successfully")
        return gps_serial
    except serial.SerialException as e:
        print(f"Error opening GPS serial port: {e}")
        return None

gps_serial = initialize_gps()

# Data storage
data = []

# Function to parse NMEA sentences
def parse_nmea_sentence(nmea_sentence):
    parts = nmea_sentence.split(',')
    if parts[0] == '$GPGGA':
        # Extract latitude and longitude
        latitude = parts[2]
        latitude_direction = parts[3]
        longitude = parts[4]
        longitude_direction = parts[5]
        
        # Convert latitude and longitude to decimal degrees
        latitude = convert_to_decimal_degrees(latitude, latitude_direction)
        longitude = convert_to_decimal_degrees(longitude, longitude_direction)
        
        return latitude, longitude
    return None, None

def convert_to_decimal_degrees(value, direction):
    if not value:
        return None
    degrees = float(value[:2])
    minutes = float(value[2:])
    decimal_degrees = degrees + (minutes / 60)
    if direction in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees

# Function to read GPS data
def read_gps_data(gps_serial):
    if gps_serial:
        try:
            line = gps_serial.readline().decode('ascii', errors='replace')
            latitude, longitude = parse_nmea_sentence(line)
            if latitude and longitude:
                print(f"Latitude: {latitude}, Longitude: {longitude}")
                return latitude, longitude
            else:
                print("Failed to parse GPS data")
                return None, None
        except Exception as e:
            print(f"Error reading GPS data: {e}")
            return None, None
    else:
        print("GPS serial port not initialized")
        return None, None

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

            # Capture GPS data
            latitude, longitude = read_gps_data(gps_serial)

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
