import time
import math

class Odometry():
    lastTime = time.time()
    deltaTime = 0
    xPos = None
    yPos = None
    rV = 0
    angle = None
    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.lastTime = time.time()

    def update(self, vLeft, vRight, angle):
        self.deltaTime = time.time() - self.lastTime
        self.rV = (vRight + vLeft) / 2
        self.angle = angle
        self.xPos = self.xPos + (self.rV * self.deltaTime * math.cos(angle))
        self.yPos = self.xPos + (self.rV * self.deltaTime * math.sin(angle))

        self.lastTime = time.time()
        

    def returnPosition(self):
        return self.xPos, self.yPos