"""
Collects temperature and humidity data using a DHT22 or DHT11 sensor on Raspberry Pi.

Usage:
    python3 temperature_humidity.py

Supported sensors:
    - DHT11: Lower cost, less accurate, smaller range (Temp: 0-50°C, Humidity: 20-90%)
    - DHT22: More accurate, wider range (Temp: -40-80°C, Humidity: 0-100%)
    - Either sensor will work with this code. Set SENSOR = Adafruit_DHT.DHT11 or Adafruit_DHT.DHT22 as needed.

Make sure to connect the sensor to the correct GPIO pin and install the required library:
    pip install Adafruit_DHT
"""
import time
import Adafruit_DHT


# Sensor type: DHT22 or DHT11
# Change to Adafruit_DHT.DHT11 if using DHT11
SENSOR = Adafruit_DHT.DHT22
# GPIO pin where the sensor is connected
GPIO_PIN = 4  # Change this if your sensor is on a different pin

print("Starting temperature and humidity data collection...")
try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, GPIO_PIN)
        if humidity is not None and temperature is not None:
            print(f"Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%")
        else:
            print("Failed to retrieve data from sensor")
        time.sleep(2)
except KeyboardInterrupt:
    print("Data collection stopped.")
