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
        # Get input/output details
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()

        input_index = input_details[0]["index"]

        # Set input tensor
        self.interpreter.set_tensor(input_index, frame)
        self.interpreter.invoke()

        # Get output
        output_data = self.interpreter.get_tensor(output_details[0]["index"])[0]

        output_data = numpy.array(output_data)

        print(output_data.shape)

        return output_data
    
    def draw_keypoints(self, frame, keypoints):

