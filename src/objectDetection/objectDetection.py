from camera.camera import Camera


class ObjectDetection:
    def __init__(self):
        self._camera = Camera()

    def getCamera(self):
        return self._camera
