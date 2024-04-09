import time

import grovepi
import brickpi3
import math



from DistSensor import DistSensor
from DriveTrain import DriveTrain
from Gyroscope import Gyroscope
from AnalogIR import AnalogIR
from Manipulator import Manipulator
from Mapper import Mapper
from Odometry import Odometry
from Timer import Timer

class Robot():
    # set up sys variables
    startTime = time.time()
    currTime = time.time()
    UPDATERATE = 0.05

    BP = brickpi3.BrickPi3()
    BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

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

    # set up cargo dropper
    armMotor = BP.PORT_D
    cargoHolder = Manipulator(BP, armMotor, -1)
    cargoHolder.resetEncoders()

    # set up IR sensor
    irSensor = AnalogIR("A2")

    # set up data tracker
    odometry = None
    mapper = None
    

    def __init__(self, mapNum, x, y):
        self.odometry = Odometry(x, y)
        self.mapper = Mapper(10,10,40, mapNum)
        self.mapper.initOrgin(x,y)

    def getFrontDistance(self):
        try:
            return self.BP.get_sensor(self.BP.PORT_1)
        except:
            return 999

    def update(self):
        self.gyro.updateGyro()
        self.odometry.update(self.drive.getLeftVelocity(), self.drive.getRightVelocity(), self.gyro.getYaw())
        self.mapper.update(self.odometry.getXPosition(), self.odometry.getYPosition(), False, False, self.irSensor.getAvg(), self.gyro.getMagValue())
        time.sleep(self.UPDATERATE)