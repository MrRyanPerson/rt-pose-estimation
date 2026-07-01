from libs.libraries import load_dependencies

PiCamera2, Interpreter, cv2, numpy, logger = load_dependencies()
logger.info("Loaded Dependencies")

from libs.capture import PiCamera
from libs.pose_estimation import PoseEstimator
from libs.conf import get_conf

def main():
    logger.add("logs/app.log", rotation="100 MB")    

    conf = get_conf()

    camera = PiCamera(conf)
    logger.info("Camera initialized")
    pose_estimator = PoseEstimator(conf)
    logger.info("Pose Estimator initialized")
    
if __name__ == "__main__":
    main()