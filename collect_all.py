"""
Collects data from camera, GPS, and temperature/humidity sensors on Raspberry Pi.

Usage:
    python3 collect_all.py

Supported temperature/humidity sensors:
    - DHT11: Lower cost, less accurate, smaller range (Temp: 0-50°C, Humidity: 20-90%)
    - DHT22: More accurate, wider range (Temp: -40-80°C, Humidity: 0-100%)
    - Either sensor will work with this code. Set SENSOR = Adafruit_DHT.DHT11 or Adafruit_DHT.DHT22 as needed.

Requirements:
    - Adafruit_DHT (for temperature/humidity)
    - libcamera-still (for camera, command-line tool)
    - gps (for GPS)
    - Ensure hardware is connected and libraries are installed
"""
import time
import time
import Adafruit_DHT
import gps
import subprocess

# Sensor setup
# Change SENSOR to Adafruit_DHT.DHT11 if using DHT11
SENSOR = Adafruit_DHT.DHT22
GPIO_PIN = 4  # Change if your sensor is on a different pin
session = gps.gps(mode=gps.WATCH_ENABLE)

def capture_image(image_path):
    try:
        subprocess.run(["libcamera-still", "-o", image_path, "--width", "1920", "--height", "1080"], check=True)
        print(f"Image saved to {image_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing image: {e}")

print("Starting data collection: camera, GPS, temperature/humidity...")
try:
    while True:
        # Temperature/Humidity
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, GPIO_PIN)
        if humidity is not None and temperature is not None:
            print(f"Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%")
        else:
            print("Failed to retrieve data from temp/humidity sensor")

        # Camera (capture image)
        image_path = f"image_{int(time.time())}.jpg"
        capture_image(image_path)

        # GPS
        report = next(session, None)
        if report and hasattr(report, 'lat') and hasattr(report, 'lon'):
            print(f"GPS: Lat {report.lat}, Lon {report.lon}")
        else:
            print("No GPS data available")

        time.sleep(5)
except KeyboardInterrupt:
    print("Data collection stopped.")
