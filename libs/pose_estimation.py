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
        input_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        input_image = cv2.resize(frame, (192, 192))
        input_image = numpy.expand_dims(input_image, axis=0)
        input_image = input_image.astype(numpy.int8)
        input_image = (input_image - 127.5) / 127.5

        return input_image

    def estimate_pose(self, frame):
        # Get input/output details
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()

        input_index = input_details[0]["index"]

        # Set input tensor
        self.interpreter.set_tensor(input_index, frame)
        self.interpreter.invoke()

        # Get output
        output_data = self.interpreter.get_tensor(output_details[0]["index"])[0]

        keypoints = []

        # Most pose models output [num_keypoints, 3] -> y, x, score
        for kp in output_data:
            y, x, conf = kp

            keypoints.append({
                "x": float(x),
                "y": float(y),
                "confidence": float(conf)
            })

        return keypoints

