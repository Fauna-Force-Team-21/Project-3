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

#set up drive motors
rightMotor = BP.PORT_B
leftMotor = BP.PORT_C
drive = DriveTrain(BP, leftMotor, rightMotor, -1, -1)
drive.resetEncoders()


# run program here
try:
    while True:
        x = float(input("X Position: ")) * 40
        y = float(input("Y Position: ")) * 40

        time.sleep(1)

        speed = 5
        # turn 180 for the y direction
        mult = 1
        if(y < 0):
            mult = -1
        currDist = drive.getLeftCM()

        drive.setCM(mult * speed,mult * speed)
        while abs(drive.getLeftCM() - currDist) < abs(y):
            print(drive.getLeftCM())
            time.sleep(UPDATERATE)
        
        drive.setCM(0,0)
        
        mult = 1
        if(x < 0):
            mult = -1
        timed = Timer(3)
        drive.setCM(-3, 3)
        while not timed.isTime():
            time.sleep(UPDATERATE)

        drive.setCM(speed * mult,speed * mult)
        currDist = drive.getLeftCM()

        while abs(drive.getLeftCM() - currDist) < abs(x):
            time.sleep(UPDATERATE)
        
        while not drive.turnAngle(0, gyro.getYaw()):
            print("turning")
            gyro.updateGyro()
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