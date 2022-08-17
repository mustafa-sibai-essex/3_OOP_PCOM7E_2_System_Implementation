from camera.color import Color
from camera.frameBuffer import FrameBuffer
import random


class Camera:
    def __init__(self):
        self._CAMERA_MAX_WIDTH = 800
        self._CAMERA_MAX_HEIGHT = 600

        #assert random.randint(0, 9) > 1, "Failed to initialize Camera"
        self.__fillFrameBuffer()

    def __fillFrameBuffer(self):
        color = []

        for y in range(0, self._CAMERA_MAX_HEIGHT):
            for x in range(0, self._CAMERA_MAX_WIDTH):
                color.append(
                    Color(
                        random.random(),
                        random.random(),
                        random.random(),
                        random.random(),
                    )
                )

        self._frameBuffer = FrameBuffer(
            self._CAMERA_MAX_WIDTH, self._CAMERA_MAX_HEIGHT, color
        )

    def getFrameBuffer(self):
        return self._frameBuffer
