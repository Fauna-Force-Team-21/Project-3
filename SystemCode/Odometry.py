import time
import math

class Odometry():
    lastTime = time.time()
    deltaTime = 0
    xPos = None
    yPos = None
    lastX = 0
    lastY = 0
    deltaPos = 0
    radAngle = None
    def __init__(self, x, y):
        self.xPos = x * 40 + 20
        self.yPos = y * 40
        self.lastTime = time.time()

    def update(self, vLeft: float, vRight: float, angle: float):
        self.deltaTime = time.time() - self.lastTime
        self.deltaPos = (vRight + vLeft) / 2 * self.deltaTime
        self.radAngle = math.radians(angle)
        self.xPos = self.xPos + (self.deltaPos * math.sin(self.radAngle))
        self.yPos = self.yPos + (self.deltaPos * math.cos(self.radAngle))

        self.lastTime = time.time()

    def update(self, angle: float, robot):
        self.deltaTime = time.time() - self.lastTime
        vx = (robot.drive.getLeftCM() - self.lastX) / self.deltaTime
        vy = (robot.drive.getRightCM() - self.lastY) / self.deltaTime
        self.lastX = robot.drive.getLeftCM()
        self.lastY = robot.drive.getRightCM()
        self.deltaPos = (vx + vy) / 2 * self.deltaTime
        self.radAngle = math.radians(angle)
        self.xPos = self.xPos + (self.deltaPos * math.sin(self.radAngle))
        self.yPos = self.yPos + (self.deltaPos * math.cos(self.radAngle))
        self.lastTime = time.time()

    def getPosition(self):
        return self.xPos, self.yPos
    
    def get2D(self):
        return self.xPos, self.yPos, self.radAngle
    
    def getXPosition(self):
        return self.xPos
    
    def getYPosition(self):
        return self.yPos