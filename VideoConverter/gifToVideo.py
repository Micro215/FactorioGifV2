from moviepy import editor as edit


def gifConverter(inputPath: str, outputPath: str, heightResize: None | int = None, fps: None | int = None) -> None:
    """Function for convert gif to mp4"""
    clip = edit.VideoFileClip(inputPath)

    if heightResize is not None:
        clip = clip.resize(height=heightResize)

    if fps is not None:
        clip = clip.set_fps(fps)

    clip.write_videofile(outputPath)