from camera.color import Color


class FrameBuffer:
    def __init__(self, width: int, height: int, colorBuffer: list[Color]):
        self.__width = width
        self.__height = height
        self.__colorBuffer = colorBuffer

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getColorBuffer(self):
        return self.__colorBuffer
