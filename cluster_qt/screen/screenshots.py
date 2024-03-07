from PIL import ImageGrab

# Capture the entire screen


# Save the screenshot to a file
i=1
while True:
    screenshot = ImageGrab.grab()
    name= 'C:/Users/Biancaa. R/Downloads/cluster/cluster_qt/images/screenshot{0}.png'.format(str(i))
    screenshot.save(name)

    # Close the screenshot
    i+=1
    screenshot.close()