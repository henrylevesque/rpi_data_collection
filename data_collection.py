import time
import datetime
import pandas as pd
from sensor_control import sensors, sensor_initializers

# data_collection.py

# Set data collection length and calculate the number of loops
data_collection_length = 60  # in seconds
time_interval = 10  # in seconds
num_loops = data_collection_length // time_interval

# Function to collect data from sensors
def collect_data():
    data = {}
    for sensor, status in sensors.items():
        if status == 1:
            # Run the python file for the sensor and get the result
            result = run_sensor_file(sensor)
            data[sensor] = result
        else:
            data[sensor] = None
    return data

# Function to run the python file for a sensor and get the result
def run_sensor_file(sensor):
    filename = f"{sensor}_module.py"
    # Run the python file and get the result
    result = run_python_file(filename)
    return result

# Function to run a python file and get the result
def run_python_file(filename):
    # Assuming the python file returns the result as a string
    # You can modify this function based on your specific requirements
    # Run the python file and get the result
    result = "Result from running the python file"
    return result

# Function to write data to an Excel file
def write_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False, header=True, startrow=1)

# Main function to run on boot
def main():
    # Initialize activated sensors
    for sensor, status in sensors.items():
        if status == 1:
            sensor_initializers[sensor]()

    # Collect data at intervals and write to Excel 
    current_time = datetime.datetime.now().strftime("%m-%d-%Y_%H:%M:%S")
    filename = f"{current_time}_length{data_collection_length}_interval{time_interval}_data.xlsx"
    header = ["Timestamp"] + list(sensors.keys())

    # Collect data from sensors
    data = []
    for _ in range(num_loops):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        row_data = [timestamp]
        sensor_data = collect_data()
        for sensor, value in sensor_data.items():
            if value is not None:
                if isinstance(value, tuple):
                    row_data.extend(list(value))
                else:
                    row_data.append(value)
            else:
                row_data.append(None)
        data.append(row_data)
        time.sleep(time_interval)

    # Write collected data to Excel
    df = pd.DataFrame(data, columns=header)
    df.to_excel(filename, index=False, header=True, startrow=0)

if __name__ == "__main__":
    main()

print("Data collection completed.") # Indicate completion of data collection