import os
import re

# Function to extract network names from the output
def extract_network_names(output):
    networks = re.findall(r'SSID [0-9]+ : (.+)', output)
    return networks

# Scan available Wifi networks
output = os.popen('netsh wlan show networks').read()

# Extract network names
network_names = extract_network_names(output)

# Display network names
print("Available WiFi Networks:")
for name in network_names:
    print(name)
