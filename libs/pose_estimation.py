from libs.libraries import load_dependencies

PiCamera2, Interpreter, cv2 = load_dependencies()

class PoseEstimator:
    def __init__(self, conf):
        self.conf = conf
        self.interpreter = Interpreter(model_path=conf["MODEL_PATH"], num_threads=4)
        self.output_resolution = conf["OUTPUT_RESOLUTION"]

    def preprocess(self, frame):
        
        
