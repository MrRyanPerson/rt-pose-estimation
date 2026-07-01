import sys
import os
import subprocess

try:
    from picamera2 import Picamera2
    from ai_edge_litert.interpreter import Interpreter
    import cv2
except ImportError:
    if input("Dependencies not installed! Would you like to install? (y/N)") == "y":
        subprocess.run(["sudo", "bash", f"{os.getcwd()}/Scripts/install.sh"])
    else:
        print("Required Dependencies were not installed! Quitting...")
        sys.exit(1)
