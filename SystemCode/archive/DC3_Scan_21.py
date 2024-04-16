import time
import grovepi
import brickpi3
import math


wheelRad = 8/2
degreeToCM = 1 / 360 * wheelRad * 2 * math.pi
armLength = 19

BP = brickpi3.BrickPi3()
rightMotor = BP.PORT_B
BP.offset_motor_encoder(rightMotor, BP.get_motor_encoder(rightMotor))
pivotMotor = BP.PORT_C
BP.offset_motor_encoder(pivotMotor, BP.get_motor_encoder(pivotMotor))
lightSensor = BP.PORT_1
BP.set_sensor_type(lightSensor, BP.SENSOR_TYPE.NXT_LIGHT_ON)

def getMotorPosition(port):
    return BP.get_motor_encoder(port) * degreeToCM

def getMotorAngle(port):
    return BP.get_motor_encoder(port)

def setMotorSpeed(port, speed):
    BP.set_motor_dps(port, speed / degreeToCM)

def setMotorAngle(port, angle):
    BP.set_motor_position(port, angle)

def setPivotDist(port, xDist):
    print(str(math.acos(xDist/armLength)))
    BP.set_motor_position(port, math.acos(xDist/armLength) * 180 / math.pi)


def getSensorValue(port):
    BP.get_sensor(port)

# run program here
try:
    xSize = int(input("Enter the x size (cm): "))
    ySize = int(input("Enter the y size (cm): "))
    xHalf = int(xSize / 2)

    grid = [[0] * xSize] * ySize

    for i in range(ySize):
        for j in range(xSize):
            setPivotDist(pivotMotor, j - xHalf)
            time.sleep(0.5)
            grid[i][j] = getSensorValue(lightSensor)
    currPos = getMotorPosition(rightMotor)
    setMotorSpeed(rightMotor, 5)
    time.sleep(1/5)
    setMotorSpeed(rightMotor, 0)            
            

        

    




except IOError as error:
    print(error)
    BP.reset_all()
except TypeError as error:
    print(error)
    BP.reset_all()
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
    BP.reset_all()