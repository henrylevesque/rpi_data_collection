# Open Source Raspberry Pi Based Data Collection
This is an open-source project for Data Collection based on low-cost Raspberry Pi single-board computers, low-cost sensor modules, 3D-printed housings, and Python code to generate human-readable data in the form of spreadsheets, either Excel (.xls) or Comma-Separated Values (.csv) files.

## Goal
Python-based code for collecting data on Raspberry Pi Zero 2 W from external sensors and writing it to an internal microSD card as an Excel file. 
The code can be run through a simple terminal command outlined below.

This device can be used as a modular biometric and environmental data collection device or as a standalone data collection device.

The goal of this project is on making the entire process as user-friendly and accessible as possible.

## Navigation

For first time setup: [Directions for First Time Setup](#directions-for-first-time-setup)

For 3D printable enclosures: [3D Files](./3D%20Files/) or in a collection on [Printables.com](https://www.printables.com/@HenryLevesque/collections/1649941)

## Python File Explanation and Directions
File organization and Directions for how to use specific configurations.

### Python Files Overview

#### camera.py
Collects data using only the camera module. Use this for image/video data collection without GPS.

#### camera_gps.py
Collects data using both the camera and GPS modules. Use this for synchronized image/video and location data collection.

#### temperature_humidity.py
Collects data from a dht11 or dht22 sensor. Use this for collecting digital temperature and humidity.

#### camera_gps_temperature_humidity.py
Collects data using the camera (via libcamera-still), GPS, and temperature/humidity sensors. Use this for full environmental and location data collection.

### How to Run

1. Navigate to the directory:
    ```
    cd rpi_data_collection
    ```
2. Run the desired Python file:
    ```
    python3 camera.py                           # For camera-only data collection
    python3 camera_gps.py                       # For camera + GPS data collection
    python3 temperature_humidity.py             #  For temperature/humidity data collection
    python3 camera_gps_temperature_humidity.py  # For camera + GPS + temperature/humidity data collection
    ```

## Sensors and Modules

### Supported Sensors and Modules
- GPS Module: Provides geotagging data for mapping in GIS applications.
- Camera Module: Collects environmental data and facial data for later use with computer vision analysis.
- Battery Module: PiSugar battery that enables wireless operation of the data collection device.

### Future Sensors and Modules
- Air Quality Sensor: Measures air quality parameters (e.g., particulate matter, VOCs, CO2) for pollution and health studies.
- Microphone Module: Measures environmental noise levels for noise pollution data collection.
- Heartrate Sensor: Measures heart rate to detect stress for biometric data collection.

## Directions for First Time Setup

### 1. Flashing the microSD Card with Raspberry Pi OS

1. Download and install [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on your computer.
2. Insert your microSD card into your computer.
3. Open Raspberry Pi Imager and select "Raspberry Pi OS (32-bit)" as the operating system.
4. Click the gear icon (⚙️) or "Edit settings" before writing the image:
    - Set a hostname (e.g., `rpi-data`)
    - Enable SSH (choose "Enable SSH" and set a password)
    - Set username and password (default: `pi` / `raspberry`)
    - Configure WiFi:
      - Enter your WiFi SSID (network name) and password
      - **Tip:** Institutional WiFi (e.g., university/corporate) often does not work reliably with Raspberry Pi. Instead, use a personal hotspot from your laptop or smartphone. See below for hotspot setup.
    - Set locale, timezone, and keyboard layout if needed
5. Click "Save" and then "Write" to flash the microSD card.
6. Safely eject the microSD card and insert it into your Raspberry Pi Zero.

### 2. Setting Up a Personal Hotspot (Recommended)

#### Smartphone Hotspot
1. On your phone, go to Settings > Network & Internet > Hotspot & tethering (Android) or Settings > Personal Hotspot (iPhone).
2. Turn on the hotspot and set a simple WiFi name (SSID) and password.
3. Enter these credentials in Raspberry Pi Imager when flashing the SD card.

#### Laptop Hotspot (Windows)
1. Go to Settings > Network & Internet > Mobile hotspot.
2. Turn on "Mobile hotspot" and set the network name and password.
3. Enter these credentials in Raspberry Pi Imager when flashing the SD card.

### 3. Powering and Finding Your Raspberry Pi

1. Insert the flashed microSD card into your Raspberry Pi Zero and power it on.
2. Wait 1-2 minutes for it to boot and connect to WiFi.
3. Find the Pi's IP address:
    - Check your hotspot device for connected devices
    - Use a network scanner app (e.g., Fing)
    - If you set a hostname, try: `ping rpi-data.local` from your computer

### 4. Connecting to the Raspberry Pi via SSH

1. Open Terminal:
    - On **Windows 10/11**: Use the built-in Windows Terminal or Command Prompt (no need to install PuTTY unless you prefer it)
    - On **Mac**: Use the built-in Terminal app
    - On **Linux**: Use your system's Terminal
2. Connect using:
    ```
    ssh pi@<raspberrypi_ip_address>
    ```
    - Replace `<raspberrypi_ip_address>` with the actual IP address or hostname
    - Enter the password you set in Raspberry Pi Imager
    - **Note:** PuTTY is an alternative SSH client for Windows, but most users can use Windows Terminal or Command Prompt without installing extra software.

### 5. Cloning the Repository to Your Raspberry Pi

1. Once connected via SSH, update your Pi:
    ```
    sudo apt-get update
    sudo apt-get upgrade
    ```
2. Install git:
    ```
    sudo apt-get install git
    ```
3. Clone the repository:
    ```
    git clone https://github.com/hleve/rpi_data_collection.git
    cd rpi_data_collection
    ```

### 6. (Optional but Recommended) Create and Activate a Python Virtual Environment

1. Install Python 3 and venv if not already installed:
    ```
    sudo apt-get install python3 python3-venv
    ```
2. Create and activate the virtual environment:
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

### 7. Install Required Python Packages

1. Upgrade pip and install requirements:
    ```
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    ```
2. If you see errors about missing system packages (e.g., pandas), install them:
    ```
    sudo apt-get install python3-pandas
    ```
3. The camera scripts use the `libcamera-still` command-line tool (not picamera or picamera2). This is included by default on Raspberry Pi OS Bullseye and later. If you have issues, run:
    ```
    sudo apt-get install libcamera-apps
    ```
4. If you see a dpkg error (e.g., "dpkg was interrupted"), run:
    ```
    sudo dpkg --configure -a
    ```

### 8. Running the Data Collection Code

1. Navigate to the project directory:
    ```
    cd rpi_data_collection
    ```
2. Run the Python file:
    ```
    python3 camera_gps.py
    ```

---
If you need to copy only specific files (not the whole repo), you can use `scp` from your computer:
```sh
scp <local_file_path> pi@<raspberrypi_ip_address>:~/rpi_data_collection/
```
Replace `<local_file_path>` with the path to your file and `<raspberrypi_ip_address>` with your Pi's IP address.

## License
This project is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)