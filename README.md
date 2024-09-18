## This is very much a work in progress

## Goal
Python-based code for collecting data on Raspberry Pi Zero 2 W from external sensors and writing it to an internal microSD card as an Excel file. The code should start on boot to enable immediate data collection when the Raspberry Pi is turned on.

This device can be used as a modular biometric and environmental data collection device or as a standalone data collection device.

Enclosures for the device will be uploaded on Printables.com with appropriate links.

The emphasis is on making the entire project as user-friendly and accessible as possible.

## Sensors and Modules
- GPS Sensor Module: Provides geotagging data for mapping in GIS applications.
- Camera Module: Collects environmental data and facial data for later use with computer vision analysis.
- Microphone Module: Measures environmental noise levels for noise pollution data collection.
- Thermometer Module: Measures environmental heat levels for heat island data collection.
- Battery Module: Enables wireless operation of the data collection device.

## Directions

To add code to a Raspberry Pi Zero 2 W and run it headlessly, follow these steps:

1. Connect to the Raspberry Pi Zero 2 W via SSH. Use a tool like PuTTY (Windows) or Terminal (Mac/Linux) to establish an SSH connection. Ensure that the Raspberry Pi is connected to the same network as your computer.

2. Once connected, navigate to the desired directory to add your code. For example, you can use the following command to navigate to the home directory:
    ```
    cd ~
    ```

3. Clone the repository using the following command:
    ```
    git clone https://github.com/hleve/rpi_data_collection.git


4. After the cloning process is complete, navigate into the cloned repository directory:
    ```
    cd rpi_data_collection
    ```

6. Install Requirements and Pandas
    ```
    python3 -m venv .venv source .venv/bin/activate python3 -m pip install -r requirements.txt cd rpi_data_collection
  
    sudo apt-get install python3-pandas
    ```
    
9. If you receive the following error while trying to install pandas: dpkg was interrupted, you must manually run sudo dpkg --configure -a to correct the problem.n error when trying to install pandas, run the following code as suggested:
    ```
    sudo dpkg --configure -a
    ```

10. Create a new file for your code using a text editor. For example, you can use the following command to create a Python file named `my_code.py`:
    ```
    nano my_code.py
    ```

11. Write your code in the text editor. For example, you can add the following Python code to `my_code.py`:
    ```python
    cd /home/pi/my_python_projects
    python3 my_script.py
    ```

12. Save and exit the text editor. In nano, you can press `Ctrl + X`, then `Y` to save the changes.

13. Make the file executable by running the following command:
    ```
    chmod +x my_code.py
    ```

14. Test your code by running it. For example, you can use the following command to execute `my_code.py`:
     ```
     python3 my_code.py
     ```

15. If your code requires any dependencies, make sure to install them on the Raspberry Pi using tools like `pip` or `apt`.

16. To run the code headlessly on boot, add it to the Raspberry Pi's startup scripts. One common method is to use the `rc.local` file. Open the file using a text editor:
     ```
     sudo nano /etc/rc.local
     ```

17. Add the following line before the `exit 0` line in the `rc.local` file, replacing `/path/to/my_code.py` with the actual path to your code file:
     ```
     python3 /path/to/my_code.py &
     ```

18. Save and exit the text editor. In nano, you can press `Ctrl + X`, then `Y` to save the changes.

19. Reboot the Raspberry Pi for the changes to take effect:
     ```
     sudo reboot
     ```

After the reboot, your code should run automatically on boot, enabling data collection to begin as soon as the Raspberry Pi is turned on.

## Directions to Run on Boot
Install the necessary libraries:
```
pip install pandas openpyxl
```

Create a systemd service to run the script on boot:
```
sudo nano /etc/systemd/system/data_collection.service
```

Add the following content:
```
[Unit]
Description=Data Collection Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/data_collection.py
WorkingDirectory=/path/to/
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

Enable and start the service:
```
sudo systemctl enable data_collection.service
sudo systemctl start data_collection.service
```

## License
This project is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)

