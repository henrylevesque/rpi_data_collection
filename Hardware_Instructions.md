# Project Overview

This project involves setting up a Raspberry Pi Zero 2 W with various sensors and modules, housed in custom 3D printed parts. Below are the details of all the required components, links to purchase them, and instructions for assembling the project.

## Required Components

### Electronics

1. **Raspberry Pi Zero 2 W** $21.39*
   - Description: The main computing unit for the project.

2. **Pi Sugar Battery** $27.99*
   - Description: A battery module to power the Raspberry Pi Zero 2 W.

3. **Raspberry Pi Camera** $14.99*
   - Description: A camera module for capturing images and videos.

4. **GPS Module** $12.99*
   - Description: A GPS module for obtaining location data.

5. **Temperature/Humidity Sensor (DHT22 or DHT11)** $5-10*
   - Description: Measures ambient temperature and humidity. Connects to a GPIO pin on the Raspberry Pi.

6. **Air Quality Sensor (e.g., MQ-135, PMS5003, or similar)** $10-30*
   - Description: Measures air quality parameters such as particulate matter, VOCs, or CO2. Connects via GPIO, UART, or I2C depending on model.

7. **Dupont Wires** $6.98*
   - Description: Wires to connect sensors and modules to the Raspberry Pi Zero 2 W.
   - Optional if you have your own wires, and includes enough wires for multiple devices or modules.
   
  ## Total Cost
   - $84.34*
   *at time of writing


### 3D Printed Parts

**PLA** $23.99*
   - Description: Recommended filament for 3D printing and prototyping. PLA is best for interior use or prototyping because of its low toxicity and UV resistance.

**ASA** $25.99*
   - Description: Recommended filament for final prints or exterior use. ASA has a higher UV resistance for exterior use but does not connect well with PLA parts.


1. **Raspberry Pi Housing**
   - Description: A custom housing for the Raspberry Pi Zero 2 W and Pi Sugar Battery.

2. **Camera Housing**
   - Description: A custom housing for the Raspberry Pi Camera module.

3. **GPS Housing**
   - Description: A custom housing for the GPS module.

**Note:** The most up-to-date 3D printable models for all housings and components can be found at: [https://www.printables.com/@HenryLevesque/collections/1649941](https://www.printables.com/@HenryLevesque/collections/1649941)

## Assembly Instructions

### Step 1: Print the 3D Parts
1. Download the STL files for the Raspberry Pi, Camera, and GPS housings.
2. Use a 3D printer to print the parts.
3. If you do not have access to a 3D printer, you can use a local 3D printing service such as a local makerspace, or an online print service such as Xometry.com or Shapeways.com

### Step 2: Assemble the Electronics
---
#### Wiring Diagrams

**DHT11/DHT22 Temperature & Humidity Sensor**

```
   DHT11/DHT22         Raspberry Pi GPIO
   +-----------+      +------------------+
   |   VCC     +------+ 3.3V or 5V       |
   |   DATA    +------+ GPIO4 (or other) |
   |   GND     +------+ GND              |
   +-----------+      +------------------+
```

**GPS Module (UART)**

```
   GPS Module         Raspberry Pi GPIO
   +--------+         +------------------+
   |   VCC  +---------+ 3.3V or 5V       |
   |   TX   +---------+ RX (GPIO15)      |
   |   RX   +---------+ TX (GPIO14)      |
   |   GND  +---------+ GND              |
   +--------+         +------------------+
```

**Camera Module (Raspberry Pi Camera)**

```
   Camera Ribbon Cable
   +------------------+
   | Connect to CSI   |
   | port on Pi       |
   +------------------+
```

---
If you use a different air quality sensor, refer to its datasheet for wiring. Most connect via UART, I2C, or analog pins (may require ADC).
1. **Raspberry Pi Zero 2 W**
   - Insert the Pi Sugar Battery into the Raspberry Pi Zero 2 W.
   - Place the Raspberry Pi into its 3D printed housing.

2. **Raspberry Pi Camera**
   - Connect the camera module to the Raspberry Pi using the ribbon cable.
   - Place the camera module into its 3D printed housing.

3. **GPS Module**
   - Connect the GPS module to the Raspberry Pi via the GPIO pins.
   - Place the GPS module into its 3D printed housing.

4. **Temperature/Humidity Sensor (DHT22 or DHT11)**
   - Connect the sensor's VCC pin to a 3.3V or 5V pin on the Raspberry Pi (check your sensor's requirements).
   - Connect the GND pin to a ground (GND) pin on the Raspberry Pi.
   - Connect the DATA pin to a free GPIO pin (e.g., GPIO4). Note the pin number for your software configuration.
   - Place the sensor in its housing or mount it securely.

5. **Air Quality Sensor**
   - Refer to your sensor's datasheet for wiring instructions. Most air quality sensors connect via GPIO, UART, or I2C.
   - For UART/I2C sensors, connect the appropriate pins to the Raspberry Pi (e.g., TX/RX for UART, SDA/SCL for I2C).
   - For analog sensors, you may need an ADC (analog-to-digital converter) module.
   - Place the sensor in its housing or mount it securely.

### Step 3: Software Setup
1. Clone this repository to your Raspberry Pi:
    ```sh
    git clone https://github.com/hleve/rpi_data_collection.git
    cd project
    ```
2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the data collection script and ensure all of the modules are working correctly:
    ```sh
    python3 collect_camera_gps.py
    ```

### Step 4: Final Assembly
1. Secure all the housings together using screws or adhesive as needed.
2. Ensure all connections are secure and the modules are properly housed.

## Conclusion

You should now have a fully assembled and functional Raspberry Pi Zero 2 W Data Collection Device with all the required sensors and modules. If you encounter any issues, please post your question in the project discussion section or contact the authors.

Happy data collection!

####
Note: Amazon purchase links have been removed. STL files for 3D printing are available on Printables.com. Please source electronics from your preferred supplier.