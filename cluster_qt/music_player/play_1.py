import pyaudio
from pydub import AudioSegment

# Assign a mp3 source file to the PyDub Audiosegment
mp3 = AudioSegment.from_mp3("C://Users//Biancaa. R//Downloads//cluster//cluster_qt//music_player//WhatsApp Audio 2024-02-16 at 6.35.02 PM.aac")

# Specify starting and ending offsets from the beginning of the stream
# then apply a fadein and fadeout.  All values are  in millisecond (seconds * 1000).

mp3 = mp3[int(43000):int(58000)].fade_in(2000).fade_out(2000)

# Assign the PyAudio player
player = pyaudio.PyAudio()

# Create the stream from the chosen mp3 file
stream = player.open(format = player.get_format_from_width(mp3.sample_width),
        channels = mp3.channels,
        rate = mp3.frame_rate,
        output = True)

data = mp3.raw_data

# Write audio data to the stream until there's no more data
while data:
    stream.write(data)
    data = None  # Set data to None to exit the loop after writing once

stream.close()
player.terminate()
