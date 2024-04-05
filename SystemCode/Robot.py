import time
from Mapper import Mapper
from Odometry import Odometry
import grovepi
import brickpi3
import math



from DistSensor import DistSensor
from DriveTrain import DriveTrain
from Gyroscope import Gyroscope
from AnalogIR import AnalogIR
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

    # set up IR sensor
    irSensor = AnalogIR("A2")

    # set up data tracker
    odometry = Odometry()
    mapper = Mapper(10,10,40)