from camera.camera import Camera


class ObjectDetection:
    def __init__(self):
        self.__camera = Camera()

    def getCamera(self):
        return self.__camera
