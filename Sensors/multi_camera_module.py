import os
import time

# multi_camera_module.py

# Function to switch to Camera A
def switch_to_camera_a():
	os.system("sudo i2cset -y 1 0x70 0x00 0x01")
	print("Switched to Camera A")

# Function to switch to Camera B
def switch_to_camera_b():
	os.system("sudo i2cset -y 1 0x70 0x00 0x02")
	print("Switched to Camera B")

# Function to enable MIPI data output
def enable_mipi_output():
	os.system("sudo pinctrl enable 11")
	print("MIPI data output enabled")

# Function to select camera
def select_camera(camera):
	if camera == 'A':
		os.system("sudo pinctrl write 7 1")
		switch_to_camera_a()
	elif camera == 'B':
		os.system("sudo pinctrl write 7 0")
		switch_to_camera_b()
	else:
		print("Invalid camera selection")

# Function to take a still image
def take_still_image(camera):
	if camera == 'A':
		os.system("sudo raspistill -o image_a.jpg")
		print("Still image taken from Camera A")
	elif camera == 'B':
		os.system("sudo raspistill -o image_b.jpg")
		print("Still image taken from Camera B")
	else:
		print("Invalid camera selection")

# Main function to demonstrate switching between cameras and taking still images
def main():
	enable_mipi_output()

	select_camera('A')
	take_still_image('A')
	time.sleep(1)  # Wait for 1 second

	select_camera('B')
	take_still_image('B')
	time.sleep(1)  # Wait for 1 second

	print("Images captured successfully!")

if __name__ == "__main__":
	main()
