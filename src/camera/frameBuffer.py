from camera.color import Color


class FrameBuffer:
    def __init__(self, width: int, height: int, _colorBuffer: Color):
        self._width = width
        self._height = height
        self._colorBuffer = _colorBuffer

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def getColorBuffer(self):
        return self._colorBuffer
