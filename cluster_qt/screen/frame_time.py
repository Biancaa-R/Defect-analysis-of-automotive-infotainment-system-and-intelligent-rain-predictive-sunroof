import cv2

def get_video_frame_time(video_path, frame_number):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = frame_count / fps
    
    frame_time = frame_number / fps
    
    return frame_time, duration

# Example usage:
video_path = "C:\\Users\\Biancaa. R\\Downloads\\cluster\\cluster_qt\\mydrive\\output_2024_02_28_23_59_58.mp4"
frame_number = 100  # Change this to the frame number you're interested in

frame_time, duration = get_video_frame_time(video_path, frame_number)
print(f"Time of frame {frame_number}: {frame_time} seconds")
print(f"Duration of video: {duration} seconds")
