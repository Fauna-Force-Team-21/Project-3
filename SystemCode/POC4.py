import time
import grovepi
import brickpi3
import math



from DistSensor import DistSensor
from DriveTrain import DriveTrain
from Gyroscope import Gyroscope
from Timer import Timer


# set up sys variables
startTime = time.time()
currTime = time.time()
UPDATERATE = 0.05

BP = brickpi3.BrickPi3()

# set up gyroscope
gyro = Gyroscope(5)
gyro.zeroGyro()
gyro.updateGyro()


# distance sensors
leftD1 = DistSensor(3)
leftD2 = DistSensor(4)
rightD = DistSensor(8)

#set up drive motors
rightMotor = BP.PORT_B
leftMotor = BP.PORT_C
drive = DriveTrain(BP, leftMotor, rightMotor, -1, -1)
drive.resetEncoders()


# run program here
try:
    x = float(input("X Position: "))
    y = float(input("Y Position: "))

    time.sleep(1)

    speed = 5
    # turn 180 for the y direction
    mult = 1
    if(y < 0):
        mult = -1
    currDist = drive.getLeftCM()

    drive.setCM(mult * speed,mult * speed)
    while abs(drive.getLeftCM() - currDist) < abs(y):
        time.sleep(UPDATERATE)
    
    drive.setCM(0,0)
    
    if(x > 0):
        angle = 85
    elif(x < 0):
        angle = -85

    while not drive.turnAngle(angle, gyro.getPosition()):
        print("turning")
        gyro.updateGyro()
        time.sleep(UPDATERATE)

    drive.setCM(speed,speed)
    currDist = drive.getLeftCM()

    while abs(drive.getLeftCM() - currDist) < abs(x):
        time.sleep(UPDATERATE)
        
    drive.setCM(0,0)



except IOError as error:
    print(error)
    drive.setCM(0,0)
    drive.resetEncoders()
    BP.reset_all()
except TypeError as error:
    print(error)
    drive.setCM(0,0)
    drive.resetEncoders()
    BP.reset_all()
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
    drive.setCM(0,0)
    drive.resetEncoders()
    BP.reset_all()