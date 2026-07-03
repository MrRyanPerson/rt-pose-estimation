import time
from unittest import case
from libs.libraries import load_dependencies

PiCamera2, Interpreter, cv2, numpy, logger = load_dependencies()

class PiCamera:
    def __init__(self, conf):
        self.conf = conf
        match conf["CAMERA_BACKEND"]:
            case "PiCamera2":
                self.picam2 = PiCamera2()
                capture_config = self.picam2.create_still_configuration({"size": self.conf["CAMERA_RESOLUTION"]})
                self.picam2.configure(capture_config)
                self.picam2.start()
                time.sleep(2)  
                logger.info("Raspberry Pi Camera initialized")
            case "OpenCV":
                self.cap = cv2.VideoCapture(conf["CAMERA_PORT"])
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, conf["CAMERA_RESOLUTION"][0])
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, conf["CAMERA_RESOLUTION"][1])
                logger.info("OpenCV Camera initialized")
            

    def capture_frame(self):
        match self.conf["CAMERA_BACKEND"]:
            case "PiCamera2":
                frame = self.picam2.capture_array()
            case "OpenCV":
                ret, frame = self.cap.read()
        return frame






        

