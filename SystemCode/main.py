import time
import grovepi
import brickpi3
import math


from Robot import Robot
from DistSensor import DistSensor
from DriveTrain import DriveTrain
from Gyroscope import Gyroscope
from Timer import Timer


robot = Robot()

# run program here
try:
    time.sleep(1)
    while True:
        #drive.setCM(10,10)
        print(robot.gyro.getYaw())
        robot.gyro.updateGyro()
        time.sleep(robot.UPDATERATE)




except IOError as error:
    print(error)
    robot.drive.setCM(0,0)
    robot.drive.resetEncoders()
    robot.BP.reset_all()
except TypeError as error:
    print(error)
    robot.drive.setCM(0,0)
    robot.drive.resetEncoders()
    robot.BP.reset_all()
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
    robot.drive.setCM(0,0)
    robot.drive.resetEncoders()
    robot.BP.reset_all()