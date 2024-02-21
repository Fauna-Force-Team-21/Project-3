import grovepi

class DistSensor():

    port = None

    def __init__(self, port):
        self.port = port

    def getDistance(self):
        return grovepi.ultrasonicRead(self.port)