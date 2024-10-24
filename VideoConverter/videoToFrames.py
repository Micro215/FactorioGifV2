import cv2


def splitFrames(filePath: str, outputFolderPath: str) -> int:
    """Function for splitting video into frames"""
    video = cv2.VideoCapture(filePath)
    fps = video.get(cv2.CAP_PROP_FPS)

    success, image = video.read()
    counter = 0

    while success:
        cv2.imwrite(f"{outputFolderPath}/frame{counter}.jpg", image)
        success, image = video.read()
        counter += 1

    return int(fps)