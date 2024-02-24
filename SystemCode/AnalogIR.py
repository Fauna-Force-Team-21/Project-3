import grovepi

class AnalogIR():
    leftPort = None
    rightPort = None

    def __init__(self, portName):
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
        leftVal = grovepi.analogRead(self.leftPort)
        rightVal = grovepi.analogRead(self.rightPort)
        return [leftVal, rightVal]
    
    def getAvg(self):
        return sum(self.getVal()) / 2

    def isNear(self):
        return self.getAvg() > 70