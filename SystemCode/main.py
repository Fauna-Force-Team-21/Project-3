import time
import grovepi
import brickpi3
import math



from DriveTrain import DriveTrain
from Gyroscope import Gyroscope
from Timer import Timer


# set up sys variables
startTime = time.time()
currTime = time.time()
UPDATERATE = 0.05

BP = brickpi3.BrickPi3()


#set up drive motors
rightMotor = BP.PORT_B
leftMotor = BP.PORT_C
drive = DriveTrain(BP, leftMotor, rightMotor, 1, 1)
drive.resetEncoders()


# run program here
try:
    time.sleep(1)
    while True:
        time.sleep(UPDATERATE)




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