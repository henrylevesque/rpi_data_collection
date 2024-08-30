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

2. Once connected, navigate to the desired directory where you want to add your code. For example, you can use the following command to navigate to the home directory:
    ```
    cd ~
    ```

3. Clone the repository using the following command:
    ```
    git clone https://github.com/your-username/your-repository.git
    ```
    Replace `your-username` with your GitHub username and `your-repository` with the name of your repository.

4. After the cloning process is complete, navigate into the cloned repository directory:
    ```
    cd your-repository
    ```
    Replace `your-repository` with the actual name of your repository.

5. Install any required dependencies mentioned in the repository's documentation before running any code.

6. Create a new file for your code using a text editor. For example, you can use the following command to create a Python file named `my_code.py`:
    ```
    nano my_code.py
    ```

7. Write your code in the text editor. For example, you can add the following Python code to `my_code.py`:
    ```python
    # Your code here
    ```

8. Save and exit the text editor. In nano, you can press `Ctrl + X`, then `Y` to save the changes.

9. Make the file executable by running the following command:
    ```
    chmod +x my_code.py
    ```

10. Test your code by running it. For example, you can use the following command to execute `my_code.py`:
     ```
     python3 my_code.py
     ```

11. If your code requires any dependencies, make sure to install them on the Raspberry Pi using tools like `pip` or `apt`.

12. To run the code headlessly on boot, add it to the Raspberry Pi's startup scripts. One common method is to use the `rc.local` file. Open the file using a text editor:
     ```
     sudo nano /etc/rc.local
     ```

13. Add the following line before the `exit 0` line in the `rc.local` file, replacing `/path/to/my_code.py` with the actual path to your code file:
     ```
     python3 /path/to/my_code.py &
     ```

14. Save and exit the text editor. In nano, you can press `Ctrl + X`, then `Y` to save the changes.

15. Reboot the Raspberry Pi for the changes to take effect:
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

