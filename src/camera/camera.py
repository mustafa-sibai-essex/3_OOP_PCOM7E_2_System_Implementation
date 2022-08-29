from camera.color import Color
from camera.frameBuffer import FrameBuffer
import random


class Camera:
    def __init__(self):
        self.__CAMERA_MAX_WIDTH = 120
        self.__CAMERA_MAX_HEIGHT = 40

        # assert random.randint(0, 9) > 1, "Failed to initialize Camera"
        color = []

        for y in range(0, self.__CAMERA_MAX_HEIGHT):
            for x in range(0, self.__CAMERA_MAX_WIDTH):
                color.append(
                    Color(
                        random.random(),
                        random.random(),
                        random.random(),
                        random.random(),
                    )
                )

        self.__frameBuffer = FrameBuffer(
            self.__CAMERA_MAX_WIDTH, self.__CAMERA_MAX_HEIGHT, color
        )

    def getFrameBuffer(self):
        return self.__frameBuffer
