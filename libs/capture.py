from libs.libraries import load_dependencies

PiCamera2, Interpreter, cv2, numpy = load_dependencies()

class PiCamera:
    def __init__(self, conf):
        self.conf = conf
        self.picam2 = PiCamera2()
        capture_config = self.picam2.create_still_configuration({"size": self.conf["CAMERA_RESOLUTION"]})
        self.picam2.configure(capture_config)
        self.picam2.start()

    def capture_frame(self):
        frame = self.picam2.capture_array()
        return frame






        

