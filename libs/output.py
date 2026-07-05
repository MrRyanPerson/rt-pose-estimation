from libs.libraries import load_dependencies

PiCamera2, Interpreter, cv2, numpy, logger = load_dependencies()

class Output:
    def __init__(self, conf):
        self.conf = conf
        self.output_resolution = conf["OUTPUT_RESOLUTION"]
        logger.info("Output initialized")

    def draw_keypoints(self, frame, keypoints):
        
        frame = cv2.resize(frame, self.conf["OUTPUT_RESOLUTION"], interpolation=cv2.INTER_LINEAR)

        # Code based on this example
        # https://www.geeksforgeeks.org/computer-vision/human-pose-detection-using-movenet-with-tensorflowhub/

        # Define the mapping of keypoints to body parts
        keypoint_names = ['nose', 'left_eye', 'right_eye', 'left_ear', 'right_ear', 'left_shoulder', 'right_shoulder',
                        'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist', 'left_hip', 'right_hip',
                        'left_knee', 'right_knee', 'left_ankle', 'right_ankle']

        # Define the connections between keypoints to draw lines for visualization
        connections = [(0, 1), (0, 2), (1, 3), (2, 4), (0, 5), (0, 6), (5, 7), (7, 9), (6, 8), (8, 10),
                    (5, 6), (5, 11), (6, 12), (11, 12), (11, 13), (13, 15), (12, 14), (14, 16)]
        # Draw lines connecting keypoints
        for connection in connections:
            if keypoints[connection[0], 2] < self.conf["MIN_CONFIDENCE"] or keypoints[connection[1], 2] < self.conf["MIN_CONFIDENCE"]:
                continue
            start_point = (int(keypoints[connection[0], 1] * self.conf["OUTPUT_RESOLUTION"][0]),
                           int(keypoints[connection[0], 0] * self.conf["OUTPUT_RESOLUTION"][1]))
            end_point = (int(keypoints[connection[1], 1] * self.conf["OUTPUT_RESOLUTION"][0]),
                         int(keypoints[connection[1], 0] * self.conf["OUTPUT_RESOLUTION"][1]))
            cv2.line(frame, start_point, end_point, (0, 0, 255), 8)  

        for kp in keypoints:
            if kp[2] < self.conf["MIN_CONFIDENCE"]:
                continue
            x = int(kp[1] * self.conf["OUTPUT_RESOLUTION"][0])
            y = int(kp[0] * self.conf["OUTPUT_RESOLUTION"][1])
            frame = cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

        return frame
