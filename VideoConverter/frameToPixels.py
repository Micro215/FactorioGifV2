from PIL import Image
import os


class frameConverter():
    def __init__(self, imageFolderPath: str) -> None:
        """Initialize frameConverter object with given image folder path"""
        self.imageFolderPath = imageFolderPath
        self.count = len(os.listdir(self.imageFolderPath))

        img = Image.open(f"{self.imageFolderPath}/frame0.jpg")
        self.width, self.height = img.size

    def convertOneFrame(self, frameCount: int) -> tuple:
        """Convert a single frame to a tuple"""
        img = Image.open(f"{self.imageFolderPath}/frame{frameCount}.jpg")
        pixels = img.load()

        result = []

        for x in range(self.width):
            for y in range(self.height):
                r, g, b = pixels[x, y]

                res = int(f"{r:02x}{g:02x}{b:02x}", 16)
                
                result.append(res)

        return tuple(result)

    def convertAllFrames(self) -> tuple:
        """Convert all frames in the folder to a single tuple"""
        result = []

        for i in range(self.count):
            result.append(self.convertOneFrame(i))

        return tuple(result)

    def convert(self) -> dict:
        """Convert all frames to a dictionary"""
        return {
            "count": self.count,
            "width": self.width,
            "height": self.height,
            "fps": 0,
            "frames": self.convertAllFrames()
        }