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

# run program here
try:
    pid = 0.65
    value = BP.get_sensor(BP.PORT_1)
    time.sleep(1)
    while True:
        #drive.setCM(10,10)
        #print(gyro.getPosition())
        #POC Code
        value = BP.get_sensor(BP.PORT_1)
        d1 = leftD1.getDistance()
        d2 = leftD2.getDistance()
        error = d1-d2
        print(value)
        if error > 20:
            error = 0
        #print(error)
        power = pid * (error)
        drive.setCM(8-power, 8+power)
        if(value < 10):
            if(leftD2.getDistance() > rightD.getDistance()):
                while not drive.turnAngle(-85, gyro.getPosition()):
                    print("turning left")
                    gyro.updateGyro()
                    time.sleep(UPDATERATE)
            elif(leftD2.getDistance() < rightD.getDistance()):
                while not drive.turnAngle(85, gyro.getPosition()):
                    print("turning right")
                    gyro.updateGyro()
                    time.sleep(UPDATERATE)
        #POC end
        gyro.updateGyro()
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
