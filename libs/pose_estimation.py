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
        input_image = input_image.astype(numpy.uint8)

        return input_image


    def estimate_pose(self, frame):

        input_image = self.preprocess(frame)

        self.interpreter.set_tensor(self.interpreter.get_input_details()[0]['index'], input_image)
        self.interpreter.invoke()
        keypoints = self.interpreter.get_tensor(self.interpreter.get_output_details()[0]['index'])[0][0]

        return keypoints
    
    def convert_keypoints(self, keypoints):
        x_res = self.conf["OUTPUT_RESOLUTION"][0]
        y_res = self.conf["OUTPUT_RESOLUTION"][1]

        for kp in keypoints:
            kp[1] = int(kp[1] * x_res)
            kp[0] = int(kp[0] * y_res)


