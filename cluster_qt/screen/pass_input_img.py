# import cv2
# from tensorflow import keras
# model=keras.models.load_model("C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\screen\\model1.h5")
# import numpy as np
# SIZE=128
# import os
# # Load your pre-trained image classification model


# # Open the video file
# #video_capture = cv2.VideoCapture('"C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\mydrive\\output_2024_02_28_23_59_58.mp4"')
# categories=["black","blurred","clear","lines","partly"]
# # Loop through each frame in the video
# folder_dir="C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\images"

# for file in os.listdir(folder_dir):
#     if file.endswith("jpg") or file.endswith("png") and file!=None:
#         # Preprocess the frame (resize, normalize, etc.)
#         try:
#             img=cv2.imread(os.path.join(folder_dir,file))
#             if img is not None:
#                 img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#                 im=cv2.resize(img_rgb,(SIZE,SIZE))
#                 data=[]
#                 data.append(im)

#                 data_arr=np.array(data)
#                 data_arr=data_arr/255
#                 print(len(data_arr))
#                 #print(data_arr[0])

#                 value=categories[np.argmax(model.predict(data_arr))]
#                 if value!="clear":
#                     img_path=os.path.join(folder_dir,file)
#                     # Example usage of os.system() with the copy command
#                     destination_folder = '"C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\images\\defective"'

#                     # Construct the copy command
#                     copy_command = f'copy "{img_path}" "{destination_folder}"'

#                     # Execute the copy command using os.system()
#                     os.system(copy_command)

#                     # Release the video capture object
#             else:
#                 break
#         except Exception as e:
#             print(e)


import cv2
from tensorflow import keras
import numpy as np
import os

# Load your pre-trained image classification model
model = keras.models.load_model("C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\screen\\model1.h5")

# Define categories
categories = ["black", "blurred", "clear", "lines", "partly"]

# Define the input image size
SIZE = 128

# Directory containing images
folder_dir = "C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\images"

# Loop through each file in the directory
for file in os.listdir(folder_dir):
    if file.endswith("jpg") or file.endswith("png") and file != None:
        try:
            # Read the image
            img_path = os.path.join(folder_dir, file)
            img = cv2.imread(img_path)

            if img is not None:
                # Convert to RGB and resize
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                im = cv2.resize(img_rgb, (SIZE, SIZE))

                # Normalize the image
                im = im / 255.0

                # Predict the category
                data_arr = np.array([im])
                value = categories[np.argmax(model.predict(data_arr))]

                # Define the destination folder based on the predicted category
                destination_folder = os.path.join(folder_dir, 'defective') if value != "clear" else None

                if destination_folder:
                    # Move the image to the destination folder
                    os.rename(img_path, os.path.join(destination_folder, file))
        except Exception as e:
            print(e)
