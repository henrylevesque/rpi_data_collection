import time
import serial
import pandas as pd
from picamera import PiCamera
from datetime import datetime

# Initialize the camera
camera = PiCamera()

# Setup GPS communication
gps_serial = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)

# Data storage
data = []

# Set intervals (e.g., every 10 seconds)
interval = 10

def get_gps_data():
    """ Read and parse GPS data from the serial port. """
    gps_data = gps_serial.readline().decode('ascii', errors='replace')
    if gps_data.startswith('$GPGGA'):
        parts = gps_data.split(',')
        if len(parts) > 5:
            # Get latitude and longitude
            lat = float(parts[2])
            lon = float(parts[4])
            return lat, lon
    return None, None

def capture_image(image_name):
    """ Capture an image using the PiCamera. """
    camera.capture(image_name)

def export_to_excel():
    """ Export stored data to an Excel file. """
    df = pd.DataFrame(data, columns=['Timestamp', 'Latitude', 'Longitude', 'Image Name'])
    df.to_excel("gps_image_data.xlsx", index=False)

# Main data collection loop
try:
    while True:
        # Get timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Capture GPS data
        latitude, longitude = get_gps_data()

        # Capture image
        image_name = f"image_{timestamp}.jpg"
        capture_image(image_name)

        # Store the data
        if latitude and longitude:
            data.append([timestamp, latitude, longitude, image_name])

        # Wait for the next interval
        time.sleep(interval)
        
except KeyboardInterrupt:
    print("Data collection stopped.")

finally:
    # Export data to Excel when stopping the script
    export_to_excel()
    print("Data saved to gps_image_data.xlsx.")
