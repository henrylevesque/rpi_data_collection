# Project Overview

This project involves setting up a Raspberry Pi Zero 2 W with various sensors and modules, housed in custom 3D printed parts. Below are the details of all the required components, links to purchase them, and instructions for assembling the project.

## Required Components

### Electronics

1. **Raspberry Pi Zero 2 W** $21.39*
   - [Amazon Link](https://amzn.to/4g1tJDt)
   - Description: The main computing unit for the project.

2. **Pi Sugar Battery** $27.99*
   - [Amazon Link](https://amzn.to/3Bfh68Q)
   - Description: A battery module to power the Raspberry Pi Zero 2 W.

3. **Raspberry Pi Camera** $14.99*
   - [Amazon Link](https://amzn.to/3OImMv1)
   - Description: A camera module for capturing images and videos.

4. **GPS Module** $12.99*
   - [Amazon Link](https://amzn.to/3ZJtesd)
   - Description: A GPS module for obtaining location data.

5. **Dupont Wires** $6.98*
   - [Amazon Link](https://amzn.to/41my284)
   - Description: Wires to connect the GPS module to the Raspberry Pi Zero 2 W.
   - Optional if you have your own wires, and includes enough wires for multiple devices or modules.
   
  ## Total Cost
   - $84.34*
   *at time of writing


### 3D Printed Parts

**PLA** $23.99*
   - [Amazon Link](https://amzn.to/41sJKhz)
   - Description: Recommended filament for 3D printing and prototyping. PLA is best for interior use or prototyping because of its low toxicity and UV resistance.

**ASA** $25.99*
   - [Amazon Link](https://amzn.to/3VsVY61)
   - Description: Recommended filament for final prints or exterior use. ASA has a higher UV resistance for exterior use but does not connect well with PLA parts.


1. **Raspberry Pi Housing**
   - [Download STL file](link)
   - Description: A custom housing for the Raspberry Pi Zero 2 W and Pi Sugar Battery.

2. **Camera Housing**
   - [Download STL file](link)
   - Description: A custom housing for the Raspberry Pi Camera module.

3. **GPS Housing**
   - [Download STL file](link)
   - Description: A custom housing for the GPS module.

## Assembly Instructions

### Step 1: Print the 3D Parts
1. Download the STL files for the Raspberry Pi, Camera, and GPS housings.
2. Use a 3D printer to print the parts.
3. If you do not have access to a 3D printer, you can use a local 3D printing service such as a local makerspace, or an online print service such as Xometry.com or Shapeways.com

### Step 2: Assemble the Electronics
1. **Raspberry Pi Zero 2 W**
   - Insert the Pi Sugar Battery into the Raspberry Pi Zero 2 W.
   - Place the Raspberry Pi into its 3D printed housing.

2. **Raspberry Pi Camera**
   - Connect the camera module to the Raspberry Pi using the ribbon cable.
   - Place the camera module into its 3D printed housing.

3. **GPS Module**
   - Connect the GPS module to the Raspberry Pi via the GPIO pins.
   - Place the GPS module into its 3D printed housing.

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
Note: Purchasing links on this page may be affiliate links that help support this project.
