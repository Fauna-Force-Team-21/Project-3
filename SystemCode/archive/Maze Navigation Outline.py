import time
from DriveTo import DriveTo
from LeftAlign import LeftAlign
from TurnBy import TurnTo
import grovepi
import brickpi3
import math


from Robot import Robot
from AnalogIR import AnalogIR

robot = None
# run program here
try:
    loopFlag = True
    mapNumber = int(input("Input Map Number: "))
    x = int(input("Offset X: "))
    y = int(input("Offset Y: "))

    robot = Robot(mapNumber, x,y)
    time.sleep(1)

    while loopFlag:
        #print(robot.gyro.getYaw())
        #print(robot.leftD2.getDistance(), robot.rightD.getDistance(), robot.getFrontDistance())
        print(robot.odometry.getXPosition(), robot.odometry.getYPosition())

        DriveTo(robot, 10, 20)
        LeftAlign(robot)

        if robot.leftD1.getDistance() > 25 and robot.rightD.getDistance() > 25 and robot.getFrontDistance() > 25:
            print("is out of maze?")
            DriveTo(robot, 10, 40)
            if robot.leftD1.getDistance() > 25 and robot.rightD.getDistance() > 25 and robot.getFrontDistance() > 25:
                loopFlag = False
                print("out of maze")
        if (robot.irSensor.isNear()):
            print("Turning 180 for IR")
            TurnTo(robot, 180)
        if(robot.getMagValue() > 300):
            print("Turning 180 for magnetic")
            TurnTo(robot, 180)
        if (((robot.leftD1.getDistance() and robot.leftD2.getDistance()) > 25) and robot.rightD.getDistance() < 25):
            continue
        if (((robot.leftD1.getDistance() and robot.leftD2.getDistance()) < 25) and robot.rightD.getDistance() > 25):
            print("Turn Right")
            TurnTo(robot, 90)
        if robot.getFrontDistance() < 20:
            time.sleep(2)
            if (robot.rightD.getDistance() < 25 and robot.leftD1.getDistance() < 25):
                print("Turning 180 for 3 way enclosure")
                TurnTo(robot, 180)
                continue
            if robot.rightD.getDistance() > 25:
                print("Turn Right")
                TurnTo(robot, 90)
            elif robot.rightD.getDistance() < 25: 
                print("Turn Left")
                TurnTo(robot, -90) 

        robot.update()

    # drops cargo
    robot.drive.setCM(0,0)
    robot.cargoHolder.setGateAngle(100)
    time.sleep(2)
    robot.cargoHolder.setGateAngle(0)
    time.sleep(1)
    robot.cargoHolder.stopMotor()
    DriveTo(robot, 10, 10)

    robot.drive.setCM(0,0)

    # printing map
    robot.mapper.printMap()
    robot.mapper.printHazards()
        




except IOError as error:
    print(error)
    robot.drive.setCM(0,0)
    robot.drive.resetEncoders()
    robot.cargoHolder.stopMotor()
    robot.cargoHolder.resetEncoders()
    robot.BP.reset_all()
except TypeError as error:
    print(error)
    robot.drive.setCM(0,0)
    robot.drive.resetEncoders()
    robot.cargoHolder.stopMotor()
    robot.cargoHolder.resetEncoders()
    robot.BP.reset_all()
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
    robot.drive.setCM(0,0)
    robot.drive.resetEncoders()
    robot.cargoHolder.stopMotor()
    robot.cargoHolder.resetEncoders()
    robot.BP.reset_all()