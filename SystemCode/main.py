import time
from DriveLine import DriveLine
from DriveTo import DriveTo
from FrontAlign import FrontAlign
from LeftAlign import LeftAlign
from TurnBy import TurnTo
import grovepi
import brickpi3
import math


from Robot import Robot


robot = None
# run program here
maxDist = 40

try:
    loopFlag = 1
    testing = False
    hasHazard = False

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
        while loopFlag == 1 or loopFlag == 2:
            print("front: " + str(robot.getFrontDistance()) + "\nleft: " + str(robot.leftD1.getDistance()) + "\nright: " + str(robot.rightD.getDistance()))
            print("position: " + str(robot.odometry.get2D()))
            #print("magVal: " + str(robot.gyro.getZMag()))
            print(robot.mapper.getMap())

            if (not hasHazard and robot.irSensor.isNear()):
                print("Turning 180 for IR")
                value = robot.irSensor.getVal()
                dist = robot.irSensor.IRdistance()
                robot.mapper.updateIR(value, robot.odometry.get2D(), dist)
                TurnTo(robot, 180)
                hasHazard = True
            elif(not hasHazard and robot.gyro.getZMag() > 50):
                print("Turning 180 for magnetic")
                value = robot.gyro.getZMag()
                dist = robot.gyro.magneticDistance()
                robot.mapper.updateMag(value, robot.odometry.get2D(), dist)
                TurnTo(robot, 180)
                hasHazard = True
            else:
                DriveLine(robot, 10, 40)
                hasHazard = False
            LeftAlign(robot)

            if robot.leftD1.getDistance() > maxDist * 2 / 3 and robot.rightD.getDistance() > maxDist and robot.getFrontDistance() > maxDist:
                print("is out of maze?")
                if loopFlag == 2:
                    loopFlag = 0
                    print("out of maze")
                    x,y = robot.odometry.getPosition()
                    robot.mapper.addEndBlock(int(x / 40),int(y /40), -2, 0)
                elif loopFlag == 1:
                    loopFlag = 2
                else:
                    loopFlag = 1
            else:
                if robot.getFrontDistance() < 25:
                    FrontAlign(robot)
                    if (robot.rightD.getDistance() < 25 and robot.leftD1.getDistance() < 25):
                        print("Turning 180 for 3 way enclosure")
                        TurnTo(robot, 180)
                    elif robot.rightD.getDistance() > 25:
                        print("Turn Right")
                        TurnTo(robot, 90)
                    elif robot.rightD.getDistance() < 25: 
                        print("Turn Left")
                        TurnTo(robot, -90)
                elif (((robot.leftD1.getDistance() and robot.leftD2.getDistance()) > 25) and robot.rightD.getDistance() < 25):
                    LeftAlign(robot)
                    continue
                elif (((robot.leftD1.getDistance() and robot.leftD2.getDistance()) < 25) and robot.rightD.getDistance() > 25):
                    print("Turn Right")
                    TurnTo(robot, 90)
                loopFlag = 1
            LeftAlign(robot)
            robot.update()


        # drops cargo
        robot.drive.setCM(0,0)
        robot.cargoHolder.setGateAngle(100)
        time.sleep(2)
        robot.cargoHolder.setGateAngle(0)
        robot.colorSensor.flashColor("blue")
        time.sleep(1)
        robot.cargoHolder.stopMotor()
        DriveTo(robot, 10, 10)
        robot.colorSensor.flashColor("blue")
        TurnTo(robot, 180)
        robot.drive.setCM(0,0)

    while testing:
        #print(robot.gyro.getZMag())
        #print(robot.gyro.magneticDistance())
        #print(robot.irSensor.getVal())
        #print(robot.getFrontDistance())
        robot.colorSensor.flashColor("blue")
        robot.update()

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

# printing map
robot.mapper.printMap()
robot.mapper.printHazards()

print("End Program")