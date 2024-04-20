import grovepi
import math
class AnalogIR():
    leftPort = None
    rightPort = None

    def __init__(self, portName: int):
        if portName == "A0":
            self.leftPort = 14
            self.rightPort = 15 
        elif portName == "A1":
            self.leftPort = 15
            self.rightPort = 16
        elif portName == "A2":
            self.leftPort = 16
            self.rightPort = 17
        else:
            print("Invalid IR Sensor port")
    
    def getVal(self):
        leftVal = 0
        rightVal = 0
        try:
            leftVal = grovepi.analogRead(self.leftPort)
        except:
            leftVal = 0
        try:
            rightVal = grovepi.analogRead(self.rightPort)
        except:
            rightVal = 0
        
        return [leftVal, rightVal]
    
    def getAvg(self):
        return sum(self.getVal()) / 2

    def isNear(self):
        return self.getAvg() > 70
    def IRdistance(self):
        x = (math.log(183.76) - math.log(self.getAvg())) / 0.022
        return x 