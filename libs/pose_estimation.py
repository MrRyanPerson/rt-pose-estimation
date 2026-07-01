from libs.libraries import load_dependencies

PiCamera2, Interpreter, cv2, numpy, logger = load_dependencies()

class PoseEstimator:
    def __init__(self, conf):
        self.conf = conf
        self.interpreter = Interpreter(model_path=conf["MODEL_PATH"], num_threads=4)
        self.output_resolution = conf["OUTPUT_RESOLUTION"]
        logger.info("Pose Estimator initialized")

    def preprocess(self, frame):
        # movenet expects 4d tensor with shape: [1, 192, 192, channels]
        input_image = cv2.resize(frame, (192, 192))
        input_image = numpy.expand_dims(input_image, axis=0)
        input_image = input_image.astype(numpy.int8)
        input_image = (input_image - 127.5) / 127.5

        return input_image

    def estimate_pose(self, frame):
        self.interpreter.set_input_details(0, shape=frame.shape)
        self.interpreter.set_input(frame)
        self.interpreter.invoke()
        outputs = self.interpreter.get_output_details(0)
        # Extract the keypoints
        keypoints = outputs['output_0'].numpy()
        # Return the keypoints
        return keypoints

