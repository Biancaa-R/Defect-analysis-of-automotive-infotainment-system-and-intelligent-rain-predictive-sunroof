# import module
import os
 
# scan available Wifi networks
os.system('cmd /c "netsh wlan show networks"')
 
# input Wifi name
name_of_router = input('Enter Name/SSID of the Wifi Network you wish to connect to: ')
 
# connect to the given wifi network
os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')
 
print("If you're not yet connected, try connecting to a previously connected SSID again!")