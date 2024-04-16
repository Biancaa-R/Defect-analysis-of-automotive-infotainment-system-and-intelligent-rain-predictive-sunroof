#Rpi Interface
import cv2
import time
from picamera2 import Picamera2
import onnxruntime as ort
import numpy as np
categories=["black","blurred","clear","lines","partly"]
picam2= Picamera2()
#picam2.preview_configuration.main.size(1280,720)
#In case of the above command picam tuple is not callable
picam2.preview_configuration.main.format="RGB888"
#picam2.preview_configuration.align()
#picam2.configure("preview")
picam2.start()
fps=0
pos=(130,160)

while True:
    start=time.time()
    im=picam2.capture_array()
    #print im([0,0]) gives data on single pixel
    
    # Change shapes and types to match model
    #input1 = np.zeros([1, 128, 128,3], np.float32)

    # path="C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\screen\\images\\black\\8d8e558b-39f7-4bdb-b72b-2dcc23ad39d1.png"
    # img=cv2.imread(path)
    SIZE=128
    img = np.float32(img)
    img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    im=cv2.resize(img_rgb,(SIZE,SIZE))
    data=[]
    data.append(im)

    data_arr=np.array(data)
    data_arr=data_arr/255
    print(len(data_arr))

    # Start from ORT 1.10, ORT requires explicitly setting the providers parameter if you want to use execution providers
    # other than the default CPU provider (as opposed to the previous behavior of providers getting set/registered by default
    # based on the build flags) when instantiating InferenceSession.
    # Following code assumes NVIDIA GPU is available, you can specify other execution providers or don't include providers parameter
    # to use default CPU provider.
    sess = ort.InferenceSession("model1.onnx")#, providers=["CUDAExecutionProvider"])
    model_inputs = sess.get_inputs()

    for input in model_inputs:
        print(f"Input Name: {input.name}, Shape: {input.shape}")

    # Set first argument of sess.run to None to use all model outputs in default order
    # Input/output names are printed by the CLI and can be set with --rename-inputs and --rename-outputs
    # If using the python API, names are determined from function arg names or TensorSpec names.
    results_ort = sess.run(None, {"x": data_arr})
    print(results_ort)
    print(categories[np.argmax(results_ort)])
    stop=time.time()
    loop_time=stop-start
    fps= 0.9* fps+ 0.1* 1/loop_time
    cv2.putText(im,str(fps),pos,cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,0,0),4)
    cv2.imshow("camera",im)
    if cv2.waitKey(1)==ord("q"):
        picam2.close()
        break
cv2.destroyAllWindows()


