# sensor_control.py

# Dictionary to hold sensor names and their activation status
sensors = {
    "GPS": 0,
    "Camera": 0,
    "Microphone": 0,
    "Thermometer": 0,
    "multi_camera": 0 
}

def initialize_gps():
    print("Initializing GPS sensor...")

def initialize_camera():
    print("Initializing Camera module...")

def initialize_microphone():
    print("Initializing Microphone module...")

def initialize_thermometer():
    print("Initializing Thermometer module...")

def initialize_multi_camera():
    print("Initializing Multi Camera module...")

# Dictionary to map sensor names to their initialization functions
sensor_initializers = {
    "GPS": initialize_gps,
    "Camera": initialize_camera,
    "Microphone": initialize_microphone,
    "Thermometer": initialize_thermometer,
    "multi_camera": initialize_multi_camera
}

# Function to activate sensors based on the dictionary
def activate_sensors(sensor_dict):
    for sensor, status in sensor_dict.items():
        if status == 1:
            sensor_initializers[sensor]()
            print(f"{sensor} sensor activated.")
        else:
            print(f"{sensor} sensor deactivated.")

# Example usage
if __name__ == "__main__":
    # Update the sensor status here (0 for deactivated, 1 for activated)
    sensors["GPS"] = 0
    sensors["Camera"] = 0
    sensors["Microphone"] = 0
    sensors["Thermometer"] = 0
    sensors["multi_camera"] = 0

    activate_sensors(sensors)