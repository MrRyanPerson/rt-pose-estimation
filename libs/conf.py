import os

def get_conf():
    config = {
        "CAMERA_BACKEND": "OpenCV", # Can be PiCamera2 or OpenCV
        "CAMERA_PORT": 0, # index of camera, can be blank if using PiCamera2
        "CAMERA_RESOLUTION": (1280, 720),
        "OUTPUT_RESOLUTION": (640, 480),
        "MODEL_PATH": f"{os.getcwd()}/libs/models/movenet_lightning_float16.tflite", # see models directory for options
        "MIN_CONFIDENCE": 0.3,
    }
    return config