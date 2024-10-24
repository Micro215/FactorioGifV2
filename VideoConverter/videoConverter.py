import os
import shutil
import sys

from .gifToVideo import gifConverter
from .videoToFrames import splitFrames
from .frameToPixels import frameConverter


INPUTFILEPATH = "temp/temp.mp4"


def convert(filePath: str, height: None | int = None, fps: None | int = None) -> dict:
    os.mkdir("temp")
    os.mkdir("temp/frames")

    # Convert GIF to MP4
    gifConverter(filePath, INPUTFILEPATH, heightResize=height, fps=fps)

    # Split MP4 into frames
    fps = splitFrames(INPUTFILEPATH, "temp/frames")

    # Convert frames to pixels data
    converter = frameConverter("temp/frames")
    data = converter.convert()
    data["fps"] = fps

    # Remove temporary files
    shutil.rmtree("temp")

    return data