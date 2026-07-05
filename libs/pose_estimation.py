from libs.libraries import load_dependencies

PiCamera2, Interpreter, cv2, numpy, logger = load_dependencies()

class PoseEstimator:
    def __init__(self, conf):
        self.conf = conf
        self.interpreter = Interpreter(model_path=conf["MODEL_PATH"], num_threads=4)
        self.output_resolution = conf["OUTPUT_RESOLUTION"]
        self.interpreter.allocate_tensors()
        logger.info("Pose Estimator initialized")

    def preprocess(self, frame):

        input_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        input_image = cv2.resize(input_image, (192, 192))
        input_image = numpy.expand_dims(input_image, axis=0)
        match self.conf["QUANTIZATION"]:
            case "int8":
                input_image = input_image.astype(numpy.uint8)
            case "float16":
                input_image = input_image.astype(numpy.float16)
        

        return input_image


    def estimate_pose(self, frame):

        input_image = self.preprocess(frame)

        self.interpreter.set_tensor(self.interpreter.get_input_details()[0]['index'], input_image)
        self.interpreter.invoke()
        keypoints = self.interpreter.get_tensor(self.interpreter.get_output_details()[0]['index'])[0][0]

        return keypoints
    

