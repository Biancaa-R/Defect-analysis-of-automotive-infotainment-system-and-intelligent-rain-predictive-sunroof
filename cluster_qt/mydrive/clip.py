# # Import everything needed to edit video clips 
# from moviepy.editor import *

# # loading video gfg 
# clip = VideoFileClip(r"C:\Users\Biancaa. R\Downloads\cluster\cluster_qt\mydrive\output_2024_02_28_23_59_58.mp4") 

# # getting only first 5 seconds 
# clip = clip.subclip(0, 5) 
	
# # getting only first 5 seconds 
# clip = clip.subclip(0, 10) 

# # cutting out some part from the clip 
# clip = clip.cutout(3, 7) 

# # showing clip 
# clip.ipython_display(width = 360)

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
ffmpeg_extract_subclip(r"C:\Users\Biancaa. R\Downloads\cluster\cluster_qt\mydrive\output_2024_02_28_23_59_58.mp4", 0, 30, targetname="cut.mp4")
