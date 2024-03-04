# importing the required packages
import pyautogui
import cv2
import numpy as np
import datetime
import os

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
#codec = cv2.VideoWriter_fourcc(*"XVID")
fourcc = cv2.VideoWriter_fourcc(*'mp4v') #MP4V codec,

# Specify name of Output file
ts = (datetime.datetime.now()).strftime("%Y_%m_%d_%H_%M_%S")
filename= 'C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\mydrive\\output_{}.mp4'.format(ts)

# Specify frames rate. We can choose any 
# value and experiment with it
fps = 10.0


# Creating a VideoWriter object
out = cv2.VideoWriter(filename, fourcc, fps, (resolution))

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 240, 200)

while True:
	# Take screenshot using PyAutoGUIr
	img = pyautogui.screenshot()

	# Convert the screenshot to a numpy array
	frame = np.array(img)

	# Convert it from BGR(Blue, Green, Red) to
	# RGB(Red, Green, Blue)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Write it to the output file
	out.write(frame)
	
	# Optional: Display the recording screen
	cv2.imshow('Live', frame)
	
	# Stop recording when we press 'q'
	if cv2.waitKey(1) == ord('q'):
		break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()




