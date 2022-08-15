from camera.color import Color
from camera.frameBuffer import FrameBuffer
import random


class Camera:
    def __init__(self):

        color = []

        for y in range(0, 600):
            for x in range(0, 800):
                color.append(
                    Color(
                        random.random(),
                        random.random(),
                        random.random(),
                        random.random(),
                    )
                )

        self._frameBuffer = FrameBuffer(800, 600, color)

    def getFrameBuffer(self):
        return self._frameBuffer
