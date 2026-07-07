import sys
from libs.libraries import load_dependencies

PiCamera2, Interpreter, cv2, numpy, logger = load_dependencies()
logger.info("Loaded Dependencies")

from libs.capture import PiCamera
from libs.pose_estimation import PoseEstimator
from libs.conf import get_conf
from libs.output import Output

def main():
    try:
        logger.add("logs/app.log", rotation="100 MB")    

        conf = get_conf()

        camera = PiCamera(conf)
        pose_estimator = PoseEstimator(conf)
        output = Output(conf)

        video_writer = cv2.VideoWriter("test.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30.0, conf["OUTPUT_RESOLUTION"])

        video_path = "input.mp4"
        mode = input("Camera/Video mode? (c/v): ").lower()

        while True:
            if mode == "c":
                frame = camera.capture_frame()
            elif mode == "v":
                frame = cv2.imread(video_path)
            
            if frame is None:
                break

            keypoints = pose_estimator.estimate_pose(frame)

            frame = output.draw_keypoints(frame, keypoints)

            video_writer.write(frame)

    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received. Exiting...")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        video_writer.release()
        camera.close()
        logger.info("Application finished")


if __name__ == "__main__":
    main()
