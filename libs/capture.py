from libs.libraries import load_dependencies

PiCamera2, Interpreter, cv2 = load_dependencies()

class PiCamera:
    def __init__(self, conf):
        self.conf = conf
        self.picam2 = PiCamera2()




        

