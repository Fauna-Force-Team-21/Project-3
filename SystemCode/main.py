import time
from DriveTo import DriveTo
from LeftAlign import LeftAlign
from TurnBy import TurnTo
import grovepi
import brickpi3
import math


from Robot import Robot


robot = None
# run program here
try:
    loopFlag = True
    testing = True
    if testing == True:
        mapNumber = 0
        x = 0
        y = 0
    else:
        mapNumber = int(input("Input Map Number: "))
        x = int(input("Offset X: "))
        y = int(input("Offset Y: "))

    robot = Robot(mapNumber, x,y)
    time.sleep(1)

    if not testing:
        while loopFlag:
            DriveTo(robot, 10, 20)
            LeftAlign(robot)

            if robot.leftD1.getDistance() > 25 and robot.rightD.getDistance() > 25 and robot.getFrontDistance() > 25:
                print("is out of maze?")
                DriveTo(robot, 10, 40)
                if robot.leftD1.getDistance() > 25 and robot.rightD.getDistance() > 25 and robot.getFrontDistance() > 25:
                    loopFlag = False
                    print("out of maze")
            elif robot.leftD2.getDistance() > 25:
                print("Turn Left")
                TurnTo(robot, -90)
            elif robot.getFrontDistance() < 20:
                print("Turn Right")
                TurnTo(robot, 90)
            
            robot.update()


        # drops cargo
        robot.drive.setCM(0,0)
        robot.cargoHolder.setGateAngle(100)
        time.sleep(2)
        robot.cargoHolder.setGateAngle(0)
        time.sleep(1)
        robot.cargoHolder.stopMotor()
        robot.colorSensor.flashColor("blue")
        DriveTo(robot, 10, 10)
        robot.drive.setCM(0,0)

        # printing map
        robot.mapper.printMap()
        robot.mapper.printHazards()
        
    while testing:
        input = float(input("Go to Angle: "))
        TurnTo(robot, input)



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