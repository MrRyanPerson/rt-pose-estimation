"""Ts is all gpt'd btw"""

import subprocess
import cv2
import numpy as np

# Define frame dimensions (match these in rpicam-vid and numpy)
WIDTH, HEIGHT = 640, 480
FRAME_SIZE = WIDTH * HEIGHT * 3  # 3 bytes per pixel for RGB

# Construct the rpicam command to output raw RGB data to stdout
cmd = [
    'rpicam-vid',
    '-t', '0',               # Run indefinitely
    '--width', str(WIDTH),
    '--height', str(HEIGHT),
    '--inline',              # Force inline headers (useful for streams)
    '--codec', 'yuv420',     # YUV is faster, but let's use raw RGB for easy mapping
    '--codec', 'rgb',        # Request raw RGB frames
    '-o', '-'                # Pipe output to stdout
]

# Start the subprocess
pipe = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=10**7)

print("Starting video stream... Press 'q' to quit.")

try:
    # Read a single frame's worth of bytes from stdout
    raw_image = pipe.stdout.read(FRAME_SIZE)
    
    if len(raw_image) != FRAME_SIZE:
        print("No Image Recieved!")

    # Convert raw bytes into a numpy array
    frame = np.frombuffer(raw_image, dtype=np.uint8).reshape((HEIGHT, WIDTH, 3))
    
    # OpenCV uses BGR, so convert RGB to BGR
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Process frame with OpenCV
    cv2.imshow('rpicam-vid Bridge', frame_bgr)
    cv2.imwrite('test.png', frame)
    
finally:
    # Safely terminate the pipe and window
    pipe.terminate()
    cv2.destroyAllWindows()


