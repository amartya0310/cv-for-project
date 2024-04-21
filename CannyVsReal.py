import cv2
import numpy as np

# Load the original color video
color_video_path = 'your_color_video.mp4'  # Replace with the path to your color video file
color_cap = cv2.VideoCapture(color_video_path)

# Check if the color video opened successfully
if not color_cap.isOpened():
    print("Error: Failed to open the color video.")
    exit()

# Load the Canny edge detection video
canny_video_path = 'Untitled.mp4'  # Replace with the path to your Canny edge detection video file
canny_cap = cv2.VideoCapture(canny_video_path)

# Check if the Canny edge detection video opened successfully
if not canny_cap.isOpened():
    print("Error: Failed to open the Canny edge detection video.")
    exit()

# Get the videos' frames per second (fps) and size
fps = int(color_cap.get(cv2.CAP_PROP_FPS))
frame_width = int(color_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(color_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a video writer to save the combined video
output_path = '/Users/kunalbhayana/PycharmProjects/ComputerVisionMarch2023/Amartya/2023-07-30 16.30.17.mp4'  # Replace with the desired output video path
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, fps, (2 * frame_width, frame_height))

# Process each frame of the videos and combine them side by side
while color_cap.isOpened() and canny_cap.isOpened():
    ret_color, frame_color = color_cap.read()
    ret_canny, frame_canny = canny_cap.read()

    if not ret_color or not ret_canny:
        break

    # Resize the Canny frame to match the color frame's height (optional)
    frame_canny_resized = cv2.resize(frame_canny, (frame_width, frame_height))

    # Combine the frames horizontally using cv2.hconcat()
    combined_frame = cv2.hconcat([frame_color, frame_canny_resized])

    # Display and save the combined frame
    cv2.imshow('Combined Video', combined_frame)
    out.write(combined_frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and writer objects, and close all windows
color_cap.release()
canny_cap.release()
out.release()
cv2.destroyAllWindows()
