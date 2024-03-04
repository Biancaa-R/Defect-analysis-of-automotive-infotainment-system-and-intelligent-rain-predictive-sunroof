# import cv2
# from tensorflow import keras
# model=keras.models.load_model("C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\screen\\model1.h5")
# import numpy as np
# SIZE=128
# # Load your pre-trained image classification model


# # Open the video file
# video_capture = cv2.VideoCapture('"C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\mydrive\\output_2024_02_28_23_59_58.mp4"')
# categories=["black","blurred","clear","lines","partly"]
# # Loop through each frame in the video
# while True:
#     # Read the frame
#     ret, frame = video_capture.read()
    
#     # Check if the frame was read successfully
#     if not ret:
#         break
    
#     # Preprocess the frame (resize, normalize, etc.)
#     img_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#     im=cv2.resize(img_rgb,(SIZE,SIZE))
#     data=[]
#     data.append(im)

#     data_arr=np.array(data)
#     data_arr=data_arr/255
#     print(len(data_arr))
#     #print(data_arr[0])

#     print(categories[np.argmax(model.predict(data_arr))])
# # Release the video capture object
# video_capture.release()

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
video_capture = cv2.VideoCapture("C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\mydrive\\output_2024_02_28_23_59_58.mp4")

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


