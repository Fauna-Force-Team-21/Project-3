import time

class Timer:
    startTime = None
    howLong = None

    def __init__(self, howLong):
        self.howLong = howLong
        self.startTime = time.time()
#hi
    def isTime(self):
        currTime = time.time()
        return (currTime - self.startTime) > self.howLong
    
    ####testing testing