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

os.system("python main.py")
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

import cv2
from tensorflow import keras
import numpy as np
import datetime
import csv

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
start=datetime.datetime.now()
error=0

F=open(".\logs\data.csv","a",newline="") #f is the file object
w=csv.writer(F)         # w is the writer object
#w.writerow(["sno.","issue","timestamp","video_refference"]) #header row #only on first time
count=1
rec=[]

# Load your pre-trained image classification model
model = keras.models.load_model("C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\screen\\model1.h5")

# Define the input image size
SIZE = 128

# Open the video file
#video_capture = cv2.VideoCapture("C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\mydrive\\output_2024_02_28_23_59_58.mp4")

video_capture=cv2.VideoCapture(filename)

if not video_capture.isOpened():
    print("Error: Unable to open video file.")
    exit()

# Define categories
categories = ["black", "blurred", "clear", "lines", "partly"]

# Loop through each frame in the video
while True:
    # Read the frame
    ret, frame = video_capture.read()
    
    # Check if the frame was read successfully
    if not ret:
        break
    
    # Preprocess the frame (resize, normalize, etc.)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    im = cv2.resize(img_rgb, (SIZE, SIZE))

    # Normalize the image
    im = im / 255.0

    # Predict the category
    data_arr = np.array([im])
    predicted_category_index = np.argmax(model.predict(data_arr))
    predicted_category = categories[predicted_category_index]
    if predicted_category!="clear" and error==0:
        err_start=datetime.datetime.now()
        error=1
        issue=predicted_category

    if predicted_category=="clear" and error==1:
        err_end=datetime.datetime.now()
        start_lim=int((err_start-start).total_seconds())
        end_lim=int((err_end-start).total_seconds())
        ts = (datetime.datetime.now()).strftime("%Y_%m_%d_%H_%M_%S")
        newname= 'C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\mydrive\\error{}.mp4'.format(ts)
        ffmpeg_extract_subclip(r"C:\Users\Biancaa. R\Downloads\cluster\cluster_qt\mydrive\output_2024_02_28_23_59_58.mp4", start_lim, end_lim, targetname=newname)
        #w.writerow(["sno.","issue","timestamp","video_refference"]) #header row
        w.writerow([count,issue,ts,newname])

        error=0

    print(predicted_category)

# Release the video capture object
F.close()
video_capture.release()









