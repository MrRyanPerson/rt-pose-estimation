from picamera2 import Picamera2
import cv2
import time
import os

# =========================
# SETTINGS
# =========================
WIDTH = 640
HEIGHT = 480

SAVE_LATEST_FRAME = True          # saves /tmp/latest.jpg
RECORD_VIDEO = False              # set True to record mp4
VIDEO_PATH = "output.mp4"
FPS = 30

# =========================
# INIT CAMERA
# =========================
picam2 = Picamera2()

config = picam2.create_video_configuration(
    main={"format": "BGR888", "size": (WIDTH, HEIGHT)}
)
picam2.configure(config)
picam2.start()

time.sleep(0.2)

# =========================
# VIDEO WRITER (optional)
# =========================
writer = None
if RECORD_VIDEO:
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(VIDEO_PATH, fourcc, FPS, (WIDTH, HEIGHT))

print("Starting headless capture. Press Ctrl+C to stop.")

# =========================
# MAIN LOOP
# =========================
frame_count = 0
start_time = time.time()

try:
    while True:
        frame = picam2.capture_array()

        # frame is already BGR because we used BGR888
        if SAVE_LATEST_FRAME:
            cv2.imwrite("/tmp/latest.jpg", frame)

        if RECORD_VIDEO and writer is not None:
            writer.write(frame)

        frame_count += 1

        # FPS print every 2 seconds
        if frame_count % 60 == 0:
            elapsed = time.time() - start_time
            fps = frame_count / elapsed
            print(f"FPS: {fps:.2f}")

except KeyboardInterrupt:
    print("\nStopping...")

finally:
    picam2.stop()

    if writer is not None:
        writer.release()

    print("Clean exit.")