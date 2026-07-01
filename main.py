
from libs.capture import PiCamera
from libs.pose_estimation import PoseEstimator
from libs.conf import get_conf

def main():
    conf = get_conf()

    camera = PiCamera(conf)
    pose_estimator = PoseEstimator(conf)
    
if __name__ == "__main__":
    main()