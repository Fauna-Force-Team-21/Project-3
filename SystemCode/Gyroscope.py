from MPU9250 import MPU9250
from Timer import Timer
import math
import time

class Gyroscope():

    NUMSTORED = None
    myIMU = None
    magOffset = 0
    aVelocityList = [0]
    magList = [0]
    accelList = [0]
    lastTime = time.time()
    deltaTime = 0
    position = 0
    angleRatio = 1.192
    offset = 0
    yaw = "z"


    def __init__(self, NUMSTORED):
        self.myIMU = MPU9250(0x68)
        self.NUMSTORED = NUMSTORED        



    def updateGyro(self):
        self.deltaTime = time.time() - self.lastTime

        # updates magnetic sensor values
        listVal = self.myIMU.readMagnet()
        magMag = math.sqrt(listVal["x"]**2 + listVal["y"]**2 + listVal["z"]**2)
        if magMag != 0.0:
            self.magList.append(magMag) 
            if len(self.magList) > self.NUMSTORED:
                self.magList.pop(0)
        
        # angular velocity sensor values
        velocityVal = self.myIMU.readGyro()
        self.aVelocityList.append(velocityVal) 
        if len(self.aVelocityList) > self.NUMSTORED:
            self.aVelocityList.pop(0)

        # position values
        avgVel = self.aVelocityList[-1][self.yaw]
        self.position += ((avgVel - self.offset) * self.deltaTime * self.angleRatio)

        # updates acceleration values
        accelVal = self.myIMU.readAccel()
        self.accelList.append(accelVal) 
        if len(self.accelList) > self.NUMSTORED:
            self.accelList.pop(0)
        
        self.lastTime = time.time()
        

    def getMagValue(self):
        return (sum(self.magList)/len(self.magList)) - self.magOffset

    def getPosition(self):
        return self.position

    def zeroGyro(self):
        timer = Timer(3)
        avgList = []
        avgMag = []
        print("starting zero")
        while(not timer.isTime()):
            avgList.append(self.myIMU.readGyro()[self.yaw])
            listVal = self.myIMU.readMagnet()
            magMag = math.sqrt(listVal["x"]**2 + listVal["y"]**2 + listVal["z"]**2)
            if magMag != 0.0:
                avgMag.append(magMag)
            time.sleep(0.1)
        print("done zero")
        self.offset = sum(avgList) / len(avgList)
        self.magOffset = sum(avgMag) / len(avgMag)
        print("angle offset is: " + str(self.offset))
        print("gyro offset is: " + str(self.magOffset))

    def getGyroValue(self):
        return {"x": self.aVelocityList[-1]["x"], "y": self.aVelocityList[-1]["y"], "z": self.aVelocityList[-1]["z"]}
    