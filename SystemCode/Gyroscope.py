from MPU9250 import MPU9250
import math

class Gyroscope():

    NUMSTORED = None
    myIMU = None
    MAGTHRESHOLD = 1000
    currAngle = 0
    angleList = [0]
    magList = [0]
    accelList = [0]

    def __init__(self, NUMSTORED):
        self.myIMU = MPU9250(0x68)
        self.NUMSTORED = NUMSTORED        



    def updateGyro(self):
        # updates magnetic sensor values
        listVal = self.myIMU.readMagnet()
        magMag = math.sqrt(listVal["x"]**2 + listVal["y"]**2 + listVal["z"]**2)
        if magMag != 0.0:
            self.magList.append(magMag) 
            if len(self.magList) > self.NUMSTORED:
                self.magList.pop(0)
        
        # gyro sensor values
        gyroVal = self.myIMU.readGyro()
        self.angleList.append(gyroVal) 
        if len(self.angleList) > self.NUMSTORED:
            self.angleList.pop(0)

        # updates acceleration values
        accelVal = self.myIMU.readAccel()
        self.accelList.append(accelVal) 
        if len(self.accelList) > self.NUMSTORED:
            self.accelList.pop(0)

    def getMagValue(self):
        return sum(self.magList)/len(self.magList)


    def getGyroValue(self):
        return {"x": self.angleList[-1]["x"], "y": self.angleList[-1]["y"], "z": self.angleList[-1]["z"]}