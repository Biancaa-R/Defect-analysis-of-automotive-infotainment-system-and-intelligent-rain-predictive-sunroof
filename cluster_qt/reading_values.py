import serial
import time
from joblib import load
import numpy as np

# Initialize serial port
ser = serial.Serial("COM6", 9600, timeout=1)
time.sleep(0.5)

import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

# Flush input buffer
ser.flushInput()

# Load machine learning models
try:
    loaded_fuel = load(".\\fuel\\linear_regression_model.joblib")
    loaded_rain = load(".\\sun_roof_rain\\model.joblib")
except Exception as e:
    print("Error loading models:", e)
    exit()

while True:
    time.sleep(2)
    line = ser.readline().decode("utf-8").strip()  # Decode bytes to string and strip whitespace

    if line:
        data = line.split()
        print(data)
        
        if len(data) >= 12:  # Ensure all expected data fields are present
            if (data[1]!='inf'):
                resistance = float(data[1])
            xvalue = float(data[3])
            yvalue = float(data[5])
            rain_value = float(data[7])
            temp = float(data[9])
            hum = float(data[11])

            # Perform calculations and predictions
            fuel_level = int(loaded_fuel.predict(np.array([[resistance]])))
            if fuel_level > 100:
                fuel_level = 100
            elif fuel_level < 0:
                fuel_level = 0

            precipitation = loaded_rain.predict(np.array([[hum, temp]]))
            precipitation = round(float(precipitation), 2)

            if yvalue>600:
                print("drive mode")
            if yvalue<300:
                print("reverse mode")
            if xvalue<300:
                print("manual transmission")


            # Print results
            print("Fuel level:", fuel_level)
            print("Precipitation:", precipitation)

            #returing the data:
            ser.write(str(precipitation).encode('utf-8'))
        else:
            print("Incomplete data received:", data)
    else:
        print("No data received")
    
    time.sleep(0.1)  # Add a short delay to avoid busy-waiting
