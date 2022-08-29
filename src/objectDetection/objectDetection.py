from queue import Queue
import random
from camera.camera import Camera
from loggingSystem import LoggingSystem


class ObjectDetection:
    """ObjectDetection class is responsible for detecing all objects on the road"""

    def __init__(self):
        """Creates the ObjectDetection class object and sets it up for work"""
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

    def detectObjectsFromImage(self):
        """This function will analize and detect all objects in an image which comes from the camera"""
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
        """Stops detecting objects and cleans up the detected objects and most dangerous objects"""
        self.__detected_objects = {}
        self.__most_dangerous_objects = Queue()

    def getDetectedObjects(self):
        """Returns the detected objects dictionary"""
        return self.__detected_objects

    def getMostDangerousObjects(self):
        """Returns the most dangerous objects queue"""
        return self.__most_dangerous_objects
