import time
import serial
import pandas as pd
# from picamera import PiCamera
from datetime import datetime
import os
import subprocess

# Initialize the camera
# camera = PiCamera()
'''
os.system("sudo pinctrl enable 11")
os.system("sudo pinctrl write 7 1")
os.system("sudo i2cset -y 1 0x70 0x00 0x01")
print("Enabled Camera")
'''




# Setup GPS communication

try:
gps_serial = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)
print("gps port opened successfully")
except serial.SerialException as e:
    print(f"Error opening GPS serial port: {e}")
    gps_serial = None


# Data storage
data = []

# Set intervals (e.g., every 10 seconds)
interval = 5

def get_gps_data():
    """ Read and parse GPS data from the serial port. """
    gps_data = gps_serial.readline().decode('ascii', errors='replace')
    print("gps_data = ", gps_data)
    if gps_data.startswith('$GPGGA'):
        parts = gps_data.split(',')
        if len(parts) > 5:
            # Get latitude and longitude
            lat = parts[2]
            lon = parts[4]
            return lat, lon
    return None, None

def capture_image(image_name):
    """ Capture an image using the PiCamera. """
    # camera.capture(image_name)
    # os.system("sudo libcamera-still -o " + image_name)
    # print("Take picture successfully")
    result = subprocess.run(["libcamera-still", "-o", "imgs/" + image_name], capture_output=True, text=True)
    if result.returncode == 0:
        print("Image captured successfully!")
    else:
        print(f"Failed to capture image: {result.stderr}")


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

        # Store the data
        if latitude and longitude:
            # Capture image
            image_name = f"image_{timestamp}.jpg"
            capture_image(image_name)

            print("ADD :: ", timestamp, " lat = ", latitude, " long = ", longitude, " image = ", image_name)
            data.append([timestamp, latitude, longitude, image_name])

        # Wait for the next interval
        time.sleep(interval)
        
except KeyboardInterrupt:
    print("Data collection stopped.")

finally:
    # Export data to Excel when stopping the script
    export_to_excel()
    print("Data saved to gps_image_data.xlsx.")
