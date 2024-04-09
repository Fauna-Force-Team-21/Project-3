import time
import math

class Odometry():
    lastTime = time.time()
    deltaTime = 0
    xPos = None
    yPos = None
    rV = 0
    angle = None
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y
        self.lastTime = time.time()

    def update(self, vLeft, vRight, angle):
        self.deltaTime = time.time() - self.lastTime
        self.rV = (vRight + vLeft) / 2
        self.angle = math.radians(angle)
        print(angle)
        self.xPos = self.xPos + (self.rV * self.deltaTime * math.sin(angle))
        self.yPos = self.yPos + (self.rV * self.deltaTime * math.cos(angle))

        self.lastTime = time.time()
        

    def getPosition(self):
        return self.xPos, self.yPos
    
    def getXPosition(self):
        return self.xPos
    
    def getYPosition(self):
        return self.yPos