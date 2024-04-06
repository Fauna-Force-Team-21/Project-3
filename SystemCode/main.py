import time
from DriveTo import DriveTo
from TurnTo import TurnTo
import grovepi
import brickpi3
import math


from Robot import Robot
from DistSensor import DistSensor
from DriveTrain import DriveTrain
from Gyroscope import Gyroscope
from Timer import Timer




# run program here
try:
    mapNumber = int(input("Input Map Number: "))
    x = int(input("Offset X: "))
    y = int(input("Offset Y: "))

    robot = Robot(mapNumber, x,y)
    time.sleep(1)

    DriveTo(robot, 8, 40)
    TurnTo(robot, 90)

    while True:
        #drive.setCM(10,10)
        print(robot.gyro.getYaw())

        
        robot.update()
        




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