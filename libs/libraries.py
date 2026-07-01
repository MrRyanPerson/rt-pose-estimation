import sys
import os
import subprocess

def load_dependencies():
    try:
        from picamera2 import Picamera2
        from ai_edge_litert.interpreter import Interpreter
        import cv2
    except ImportError:
        if input("Dependencies not installed! Install them? (y/N) ") == "y":
            subprocess.run(["sudo", "bash", f"{os.getcwd()}/Scripts/install.sh"], check=True)
            from picamera2 import Picamera2
            from ai_edge_litert.interpreter import Interpreter
            import cv2
        else:
            print("Required dependencies were not installed!")
            sys.exit(1)

    return Picamera2, Interpreter, cv2
