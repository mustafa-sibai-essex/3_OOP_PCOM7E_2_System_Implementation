from autopilot import Autopilot


class Vehicle:
    def __init__(self):
        self.autopilot = Autopilot()
        print(self.autopilot.objectDetection.getCamera().getFrameBuffer().getWidth())
        print(self.autopilot.objectDetection.getCamera().getFrameBuffer().getHeight())
        print(len(self.autopilot.objectDetection.getCamera().getFrameBuffer().getColorBuffer()))
        print(self.autopilot.objectDetection.getCamera().getFrameBuffer().getColorBuffer()[0])



