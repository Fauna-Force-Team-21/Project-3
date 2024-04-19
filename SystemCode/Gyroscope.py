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
    # yaw pitch roll angle
    position = [0,0,0]
    angleRatio = 1.192
    offset = [0,0,0]
    pitch = "x"
    roll = "y"
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
        self.position[0] += ((avgVel - self.offset[0]) * self.deltaTime * self.angleRatio)
        
        avgVel = self.aVelocityList[-1][self.pitch]
        self.position[1] += ((avgVel - self.offset[1]) * self.deltaTime * self.angleRatio)

        avgVel = self.aVelocityList[-1][self.roll]
        self.position[2] += ((avgVel - self.offset[2]) * self.deltaTime * self.angleRatio)

        

        # updates acceleration values
        accelVal = self.myIMU.readAccel()
        self.accelList.append(accelVal) 
        if len(self.accelList) > self.NUMSTORED:
            self.accelList.pop(0)
        
        self.lastTime = time.time()
        
    def getRawMag(self):
        return self.myIMU.readMagnet()

    def getMagValue(self):
        return (sum(self.magList)/len(self.magList)) - self.magOffset

    def getYaw(self):
        return self.position[0]
    
    def getAngle(self):
        return {"yaw": self.position[0], "pitch": self.position[1], "roll": self.position[2]}

    def zeroGyro(self):
        timer = Timer(5)
        avgList = []
        avgList2 = []
        avgList3 = []

        avgMag = []
        print("starting zero")
        while(not timer.isTime()):
            avgList.append(self.myIMU.readGyro()[self.yaw])
            avgList2.append(self.myIMU.readGyro()[self.pitch])
            avgList3.append(self.myIMU.readGyro()[self.roll])
            
            listVal = self.myIMU.readMagnet()
            magMag = math.sqrt(listVal["x"]**2 + listVal["y"]**2 + listVal["z"]**2)
            if magMag != 0.0:
                avgMag.append(magMag)
            time.sleep(0.1)
        print("done zero")
        self.offset[0] = sum(avgList) / len(avgList)
        self.offset[1] = sum(avgList2) / len(avgList2)
        self.offset[2] = sum(avgList3) / len(avgList3)

        self.magOffset = sum(avgMag) / len(avgMag)
        print("angle offset is: " + str(self.offset))
        print("gyro offset is: " + str(self.magOffset))

    def getGyroValue(self):
        return {"x": self.aVelocityList[-1]["x"], "y": self.aVelocityList[-1]["y"], "z": self.aVelocityList[-1]["z"]}
    