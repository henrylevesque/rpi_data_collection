# gps_module.py

import serial
import time

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
    degrees = float(value[:2])
    minutes = float(value[2:])
    decimal_degrees = degrees + (minutes / 60)
    if direction in ['S', 'W']:
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def read_gps_data():
    # Initialize serial connection (adjust the port and baud rate as needed)
    ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
    time.sleep(2)  # Wait for the serial connection to initialize

    while True:
        try:
            nmea_sentence = ser.readline().decode('ascii', errors='replace')
            latitude, longitude = parse_nmea_sentence(nmea_sentence)
            if latitude and longitude:
                print(f"Latitude: {latitude}, Longitude: {longitude}")
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    read_gps_data()