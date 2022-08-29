from queue import Queue
import random
from camera.camera import Camera
from loggingSystem import LoggingSystem


class ObjectDetection:
    def __init__(self):
        self.__detected_objects = {}
        self.__most_dangerous_objects = Queue()
        self.__possible_object_names = [
            "Car",
            "Pedestrian",
            "Animal",
            "Wall",
            "Truck",
            "Bicycle",
            "Sign",
        ]
        self.__camera = Camera()

    def getCamera(self):
        return self.__camera

    def detectObjectsFromImage(self):

        for i in range(0, 4):
            index = random.randint(0, len(self.__possible_object_names) - 1)
            self.__detected_objects[
                "Object{0}".format(i)
            ] = self.__possible_object_names[index]

        self.__most_dangerous_objects.put(self.__detected_objects["Object3"])
        self.__most_dangerous_objects.put(self.__detected_objects["Object2"])
        self.__most_dangerous_objects.put(self.__detected_objects["Object1"])
        self.__most_dangerous_objects.put(self.__detected_objects["Object0"])

        LoggingSystem.logInfo("Most dangerous objects are as follow: ")

        for i in range(0, 4):
            LoggingSystem.logInfo("{0}".format(self.__most_dangerous_objects.get()))

    def stopObjectDetection(self):
        self.__detected_objects = {}
        self.__most_dangerous_objects = Queue()

    def getDetectedObjects(self):
        return self.__detected_objects

    def getMostDangerousObjects(self):
        return self.__most_dangerous_objects
